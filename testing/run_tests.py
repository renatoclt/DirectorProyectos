#!/usr/bin/env python3
"""Validación no destructiva del sistema de agentes de VS Code."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

try:
    import yaml
    import jsonschema
except ImportError:
    print("ERROR: faltan dependencias. Ejecuta: python -m pip install -r testing/requirements.txt")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / ".github" / "agents"
CONTRACTS_DIR = ROOT / "governance" / "contracts"
PROMPTS_DIR = ROOT / ".github" / "prompts"
INSTRUCTIONS_DIR = ROOT / ".github" / "instructions"
SCENARIOS_DIR = ROOT / "testing" / "scenarios"
BASELINE_PATH = ROOT / "testing" / "baselines" / "agent-manifest.json"
TOOL_POLICY_PATH = ROOT / "governance" / "tool-policies.json"
SYSTEM_VERSION_PATH = ROOT / "VERSION"

@dataclass
class Finding:
    severity: str
    code: str
    message: str
    path: str = ""

findings: list[Finding] = []
checks = 0

def ok(condition: bool, code: str, message: str, path: Path | None = None, severity: str = "ERROR") -> None:
    global checks
    checks += 1
    if not condition:
        findings.append(Finding(severity, code, message, str(path.relative_to(ROOT)) if path else ""))


def frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    ok(text.startswith("---"), "FMT-001", "El archivo no inicia con frontmatter YAML.", path)
    try:
        _, raw, body = text.split("---", 2)
    except ValueError:
        findings.append(Finding("ERROR", "FMT-002", "Frontmatter incompleto.", str(path.relative_to(ROOT))))
        return {}, text
    try:
        data = yaml.safe_load(raw) or {}
    except Exception as exc:
        findings.append(Finding("ERROR", "FMT-003", f"YAML inválido: {exc}", str(path.relative_to(ROOT))))
        return {}, body
    ok(isinstance(data, dict), "FMT-004", "El frontmatter debe ser un objeto.", path)
    return data, body


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        findings.append(Finding("ERROR", "JSON-001", f"JSON inválido: {exc}", str(path.relative_to(ROOT))))
        return {}


def discover_agents() -> dict[str, dict[str, Any]]:
    agents: dict[str, dict[str, Any]] = {}
    for path in sorted(AGENTS_DIR.glob("*.agent.md")):
        meta, body = frontmatter(path)
        slug = path.name.removesuffix(".agent.md")
        agents[slug] = {"path": path, "meta": meta, "body": body}
    return agents


def validate_agents(agents: dict[str, dict[str, Any]]) -> None:
    ok(len(agents) == 21, "AGENT-001", f"Se esperaban 21 agentes y se encontraron {len(agents)}.", AGENTS_DIR)
    names: list[str] = []
    for slug, item in agents.items():
        path, meta, body = item["path"], item["meta"], item["body"]
        for field in ("name", "description", "target", "user-invocable", "disable-model-invocation", "tools"):
            ok(field in meta, "AGENT-002", f"Falta el campo obligatorio {field}.", path)
        name = meta.get("name", "")
        names.append(name)
        ok(meta.get("target") == "vscode", "AGENT-003", "target debe ser vscode.", path)
        ok(isinstance(meta.get("tools"), list), "AGENT-004", "tools debe ser una lista explícita.", path)
        ok(meta.get("disable-model-invocation") is False, "AGENT-005", "El agente debe permitir invocación controlada como subagente.", path)
        expected_visibility = name == "Director de Proyectos"
        ok(meta.get("user-invocable") is expected_visibility, "AGENT-006", "Solo Director de Proyectos debe ser visible.", path)
        contract_ref = f"../../governance/contracts/{slug}.contract.json"
        ok(contract_ref in body, "AGENT-007", "El perfil no referencia su contrato.", path)
    ok(len(names) == len(set(names)), "AGENT-008", "Hay nombres de agentes duplicados.", AGENTS_DIR)

    director = agents.get("director-proyectos", {})
    dmeta = director.get("meta", {})
    expected_workers = sorted(n for n in names if n != "Director de Proyectos")
    ok(sorted(dmeta.get("agents", [])) == expected_workers, "AGENT-009", "La lista de subagentes del Director no coincide con el catálogo.", director.get("path"))
    ok("agent" in dmeta.get("tools", []), "AGENT-010", "El Director necesita la herramienta agent.", director.get("path"))

    tester = agents.get("testing-agentes", {})
    tmeta = tester.get("meta", {})
    expected_testable = sorted(n for n in names if n != "Ingeniero de Testing de Agentes")
    ok(sorted(tmeta.get("agents", [])) == expected_testable, "AGENT-011", "El agente de testing no puede invocar exactamente a los agentes esperados.", tester.get("path"))


def validate_contracts(agents: dict[str, dict[str, Any]]) -> None:
    schema_path = CONTRACTS_DIR / "agent-contract.schema.json"
    schema = load_json(schema_path)
    required = [
        "contract_version", "agent_id", "agent_name", "purpose", "allowed_phases",
        "allowed_tools", "allowed_actions", "forbidden_actions", "allowed_paths",
        "forbidden_paths", "required_inputs", "required_outputs", "completion_criteria",
        "escalation_rules", "test_scenarios"
    ]
    contract_paths = sorted(CONTRACTS_DIR.glob("*.contract.json"))
    ok(len(contract_paths) == len(agents), "CONTRACT-001", "Debe existir un contrato por agente.", CONTRACTS_DIR)
    for slug, item in agents.items():
        path = CONTRACTS_DIR / f"{slug}.contract.json"
        ok(path.exists(), "CONTRACT-002", "Falta contrato del agente.", path)
        if not path.exists():
            continue
        contract = load_json(path)
        try:
            jsonschema.validate(instance=contract, schema=schema)
        except jsonschema.ValidationError as exc:
            findings.append(Finding("ERROR", "CONTRACT-008", f"No cumple el esquema: {exc.message}", str(path.relative_to(ROOT))))
        for field in required:
            ok(field in contract, "CONTRACT-003", f"Falta {field} en el contrato.", path)
        ok(contract.get("agent_id") == slug, "CONTRACT-004", "agent_id no coincide con el archivo.", path)
        ok(contract.get("agent_name") == item["meta"].get("name"), "CONTRACT-005", "agent_name no coincide con el perfil.", path)
        ok(contract.get("allowed_tools") == item["meta"].get("tools"), "CONTRACT-006", "allowed_tools no coincide con tools del perfil.", path)
        for field in ("allowed_actions", "forbidden_actions", "required_inputs", "required_outputs", "completion_criteria", "escalation_rules", "test_scenarios"):
            ok(isinstance(contract.get(field), list) and len(contract.get(field, [])) > 0, "CONTRACT-007", f"{field} debe ser una lista no vacía.", path)


def validate_tool_policy(agents: dict[str, dict[str, Any]]) -> None:
    policy = load_json(TOOL_POLICY_PATH)
    visible = sorted(name for item in agents.values() if item["meta"].get("user-invocable") for name in [item["meta"].get("name")])
    ok(visible == sorted(policy.get("visible_agents", [])), "TOOLS-001", "La visibilidad no coincide con la política.", TOOL_POLICY_PATH)
    groups = ["coordinators", "read_only_agents", "test_execution_read_only_agents", "implementation_agents", "documentation_agents"]
    expected: dict[str, list[str]] = {}
    for group in groups:
        expected.update(policy.get(group, {}))
    actual = {item["meta"].get("name"): item["meta"].get("tools") for item in agents.values()}
    ok(set(expected) == set(actual), "TOOLS-002", "La política no cubre exactamente todos los agentes.", TOOL_POLICY_PATH)
    for name, tools in expected.items():
        ok(actual.get(name) == tools, "TOOLS-003", f"Herramientas desincronizadas para {name}.", TOOL_POLICY_PATH)
    for name in ["QA Engineer", "Revisor de Seguridad", "Auditor de Trazabilidad", "Auditor de Entrega"]:
        ok("edit" not in actual.get(name, []), "TOOLS-004", f"{name} no debe tener edit.", TOOL_POLICY_PATH)


def validate_prompts(agents: dict[str, dict[str, Any]]) -> None:
    names = {item["meta"].get("name") for item in agents.values()}
    prompts = list(PROMPTS_DIR.glob("*.prompt.md"))
    ok(len(prompts) >= 7, "PROMPT-001", "Faltan prompt files esperados.", PROMPTS_DIR)
    by_name = {}
    for path in prompts:
        meta, _ = frontmatter(path)
        prompt_name = meta.get("name", path.name.removesuffix(".prompt.md"))
        by_name[prompt_name] = meta
        ok(meta.get("agent") in names, "PROMPT-002", f"El prompt referencia un agente inexistente: {meta.get('agent')}", path)
    ok(by_name.get("auditar-trazabilidad", {}).get("agent") == "Auditor de Trazabilidad" or (PROMPTS_DIR / "auditar-trazabilidad.prompt.md").exists(), "PROMPT-003", "La auditoría debe usar el Auditor de Trazabilidad.", PROMPTS_DIR / "auditar-trazabilidad.prompt.md")
    # Existing file may omit name and derive it from filename.
    aud_meta, _ = frontmatter(PROMPTS_DIR / "auditar-trazabilidad.prompt.md")
    ok(aud_meta.get("agent") == "Auditor de Trazabilidad", "PROMPT-004", "auditar-trazabilidad usa el agente incorrecto.", PROMPTS_DIR / "auditar-trazabilidad.prompt.md")
    test_meta, _ = frontmatter(PROMPTS_DIR / "probar-sistema-agentes.prompt.md")
    ok(test_meta.get("agent") == "Ingeniero de Testing de Agentes", "PROMPT-005", "probar-sistema-agentes usa el agente incorrecto.", PROMPTS_DIR / "probar-sistema-agentes.prompt.md")


def validate_instructions() -> None:
    required = {
        "project-governance.instructions.md": "**",
        "agent-maintenance.instructions.md": ".github/agents/**/*.agent.md",
        "testing.instructions.md": "testing/**/*",
    }
    for filename, apply_to in required.items():
        path = INSTRUCTIONS_DIR / filename
        ok(path.exists(), "INSTR-001", "Falta instruction file.", path)
        if path.exists():
            meta, _ = frontmatter(path)
            ok(meta.get("applyTo") == apply_to, "INSTR-002", f"applyTo debe ser {apply_to}.", path)
            ok(bool(meta.get("description")), "INSTR-003", "Falta description.", path)


def validate_scenarios(agents: dict[str, dict[str, Any]]) -> None:
    names = {item["meta"].get("name") for item in agents.values()}
    ids: dict[str, Path] = {}
    for path in sorted(SCENARIOS_DIR.rglob("*.json")):
        scenario = load_json(path)
        sid = scenario.get("id")
        ok(bool(sid), "SCEN-001", "Escenario sin id.", path)
        if sid:
            ok(sid not in ids, "SCEN-002", f"ID de escenario duplicado: {sid}.", path)
            ids[sid] = path
        ok(scenario.get("agent") in names, "SCEN-003", "Escenario referencia agente inexistente.", path)
        for field in ("prompt", "expected_sections", "required_behaviors", "forbidden_behaviors", "pass_criteria", "tags"):
            ok(field in scenario and bool(scenario.get(field)), "SCEN-004", f"Falta o está vacío {field}.", path)
    ok(len(ids) >= 24, "SCEN-005", f"Se esperaban al menos 24 escenarios y existen {len(ids)}.", SCENARIOS_DIR)
    for slug in agents:
        contract = load_json(CONTRACTS_DIR / f"{slug}.contract.json")
        for sid in contract.get("test_scenarios", []):
            ok(sid in ids, "SCEN-006", f"El contrato referencia un escenario inexistente: {sid}.", CONTRACTS_DIR / f"{slug}.contract.json")


def validate_relative_links() -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw in pattern.findall(text):
            target = raw.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "~", "${")):
                continue
            if "<" in target or ">" in target or "*" in target:
                continue
            resolved = (path.parent / target).resolve()
            ok(resolved.exists(), "LINK-001", f"Enlace relativo roto: {raw}", path)


def validate_required_files() -> None:
    required = [
        "README.md", "MAPA-DEL-SISTEMA.md", "AGENT-CATALOG.md", "VERSION",
        "governance/tool-policies.json", "governance/phase-gates.json",
        "testing/README.md", "testing/manual/PLAN-DE-PRUEBAS.md",
        "aprendizaje/README.md", ".github/workflows/validate-agent-system.yml",
        ".vscode/tasks.json",
    ]
    for rel in required:
        ok((ROOT / rel).exists(), "FILE-001", "Falta archivo requerido.", ROOT / rel)
    learning_docs = list((ROOT / "aprendizaje").glob("*.md"))
    ok(len(learning_docs) >= 10, "FILE-002", "La carpeta aprendizaje debe contener al menos 10 documentos.", ROOT / "aprendizaje")


def current_manifest(agents: dict[str, dict[str, Any]]) -> dict[str, Any]:
    version = SYSTEM_VERSION_PATH.read_text(encoding="utf-8").strip() if SYSTEM_VERSION_PATH.exists() else "unknown"
    entries: dict[str, Any] = {}
    for slug, item in sorted(agents.items()):
        contract_path = CONTRACTS_DIR / f"{slug}.contract.json"
        entries[slug] = {
            "name": item["meta"].get("name"),
            "tools": item["meta"].get("tools"),
            "user_invocable": item["meta"].get("user-invocable"),
            "disable_model_invocation": item["meta"].get("disable-model-invocation"),
            "profile_sha256": sha256(item["path"]),
            "contract_sha256": sha256(contract_path) if contract_path.exists() else None,
        }
    return {"baseline_version": "1.0.0", "system_version": version, "agents": entries}


def validate_baseline(agents: dict[str, dict[str, Any]]) -> None:
    ok(BASELINE_PATH.exists(), "BASE-001", "Falta baseline de agentes.", BASELINE_PATH)
    if not BASELINE_PATH.exists():
        return
    expected = load_json(BASELINE_PATH)
    actual = current_manifest(agents)
    ok(expected == actual, "BASE-002", "Los perfiles o contratos cambiaron respecto al baseline. Revisa el cambio antes de actualizarlo.", BASELINE_PATH)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--update-baseline", action="store_true", help="Actualiza el baseline después de una revisión humana.")
    parser.add_argument("--confirm-update-baseline", action="store_true", help="Confirmación obligatoria para escribir el baseline.")
    parser.add_argument("--json-report", type=Path, help="Guarda un reporte JSON en la ruta indicada.")
    args = parser.parse_args()

    agents = discover_agents()
    validate_agents(agents)
    validate_contracts(agents)
    validate_tool_policy(agents)
    validate_prompts(agents)
    validate_instructions()
    validate_scenarios(agents)
    validate_relative_links()
    validate_required_files()

    if args.update_baseline:
        if not args.confirm_update_baseline:
            findings.append(Finding("ERROR", "BASE-003", "Para actualizar el baseline también debes usar --confirm-update-baseline."))
        elif any(f.severity == "ERROR" for f in findings):
            findings.append(Finding("ERROR", "BASE-004", "No se actualiza el baseline porque existen errores estructurales."))
        else:
            BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
            BASELINE_PATH.write_text(json.dumps(current_manifest(agents), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Baseline actualizado: {BASELINE_PATH.relative_to(ROOT)}")
    else:
        validate_baseline(agents)

    errors = [f for f in findings if f.severity == "ERROR"]
    warnings = [f for f in findings if f.severity == "WARNING"]
    print(f"\nValidaciones ejecutadas: {checks}")
    print(f"Errores: {len(errors)} | Advertencias: {len(warnings)}")
    for f in findings:
        location = f" [{f.path}]" if f.path else ""
        print(f"{f.severity} {f.code}{location}: {f.message}")

    if args.json_report:
        out = args.json_report if args.json_report.is_absolute() else ROOT / args.json_report
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"checks": checks, "findings": [asdict(f) for f in findings]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if errors:
        print("\nRESULTADO: RECHAZADO")
        return 1
    print("\nRESULTADO: APROBADO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
