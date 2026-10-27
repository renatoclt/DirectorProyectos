# Testing del sistema de agentes y Skills

Esta carpeta prueba **el equipo de agentes y sus capacidades reutilizables**, no el producto que construyan.

## Cinco niveles

1. **Estructura:** YAML, archivos, nombres, visibilidad y referencias.
2. **Contratos:** perfil, contrato y política de herramientas deben coincidir.
3. **Skills:** nombre, descripción, referencias, licencia, origen, lock y agentes autorizados.
4. **Baseline:** detecta cambios en perfiles, contratos, Skills, referencias, licencias o lock.
5. **Conducta:** escenarios que evalúan si agentes y Skills conservan su función.

## Baselines

```text
testing/baselines/
├── agent-manifest.json
└── skill-manifest.json
```

El baseline de Skills incluye hashes de todos los archivos dentro de cada Skill y del lock. Un cambio produce `SKILLBASE-002` hasta que se revise y apruebe.

## Ejecutar en Windows

```powershell
python -m pip install -r testing/requirements.txt
python testing/run_tests.py
```

También puedes usar:

```powershell
./testing/run-tests.ps1
```

En VS Code: `Ctrl+Shift+P` → `Tasks: Run Task` → `Validar sistema de agentes`.

## Ejecutar escenarios conductuales

Con Session Target **Local**, ejecuta directamente:

```text
/probar-sistema-agentes mode=smoke
```

El prompt activa al Ingeniero de Testing de Agentes como agente principal. Esto permite que invoque a los agentes evaluados sin habilitar subagentes anidados.

Modos disponibles: `static`, `smoke`, `full` y `agent:<nombre>`.

Los escenarios con etiqueta `design-skill` comprueban creación, autocontrol, revisión independiente y auditoría visual.

## Actualizar baselines

Los baselines no se actualizan para ocultar una prueba fallida. Después de revisar y aprobar un cambio intencional:

```powershell
python testing/run_tests.py --update-baseline --confirm-update-baseline
python testing/run_tests.py
```

El comando actualiza ambos manifests. El Ingeniero de Testing de Agentes tiene prohibido ejecutarlo; la decisión debe ser humana.

## Códigos relevantes de Skills

- `SKILL-*`: estructura y metadata.
- `SKILLLOCK-*`: origen, licencia y agentes autorizados.
- `SKILLBASE-001`: falta baseline.
- `SKILLBASE-002`: cambió una Skill, referencia, licencia o lock.
- `LINK-001`: referencia local rota.

## Prueba de mutación recomendada

En una copia temporal:

1. cambia una línea de `SKILL.md`;
2. elimina una referencia;
3. ejecuta pruebas;
4. verifica `SKILLBASE-002` y `LINK-001`;
5. revierte cambios;
6. no actualices el baseline.

## Limitación importante

Las pruebas automáticas validan estructura y coherencia. Las pruebas conductuales usan modelos generativos y pueden variar; por eso se evalúan mediante rúbricas, comportamientos obligatorios y comportamientos prohibidos.

## Pruebas de propuesta y mockup

La versión 5 añade escenarios para verificar:

- propuesta ejecutiva concisa;
- referencia visible a adjuntos;
- presentación sin credenciales inventadas;
- plazo preliminar con supuestos;
- disponibilidad confirmada o marcada como pendiente;
- paquete documental separado;
- mockup conceptual sin integraciones reales;
- escritura limitada del Prototipador UX.

Escenarios principales:

- `DIR-005`
- `PLAN-002`
- `DOC-002`
- `PROTO-001`

## Sistema de color

La v6 valida `color-system`, sus referencias, script de contraste, agentes autorizados, A07, escenarios conductuales y baseline de Skills. Un cambio no aprobado debe producir `SKILLBASE-002`.
