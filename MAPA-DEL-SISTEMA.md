# Mapa del sistema

## Arquitectura

```text
USUARIO / CLIENTE
       |
       v
DIRECTOR DE PROYECTOS
       |
       +-- Descubrimiento: Analista, Product, UX, Arquitectura
       +-- Planificación: Planificador, Delivery, Tech Lead
       +-- Construcción: Generalista o Backend/Frontend/Móvil/Datos/DevOps
       +-- Calidad: QA, Seguridad
       +-- Control: Auditor de Trazabilidad, Auditor de Entrega
       +-- Documentación: Gestor, Redactor Técnico

CONTROL EXTERNO
       +-- Contratos JSON
       +-- Política de herramientas
       +-- Puertas de fase
       +-- Pruebas automáticas
       +-- Escenarios conductuales
       +-- Baseline
       +-- Aprobaciones humanas
```

## Fuentes de verdad

| Tema | Archivo o carpeta |
|---|---|
| Reglas globales | `.github/copilot-instructions.md` |
| Perfiles | `.github/agents/` |
| Procedimientos `/` | `.github/prompts/` |
| Reglas dirigidas | `.github/instructions/` |
| Contratos | `governance/contracts/` |
| Herramientas esperadas | `governance/tool-policies.json` |
| Fases | `governance/phase-gates.json` |
| Testing | `testing/` |
| Explicaciones | `aprendizaje/` |
| Control por proyecto | `projects/<slug>/00-control/` |

## Regla de lectura rápida

Para saber dónde estás en un proyecto, abre `PROJECT-STATE.md`. Para saber por qué existe una pieza del sistema, abre `aprendizaje/`. Para saber si una modificación rompió agentes, ejecuta `python testing/run_tests.py`.
