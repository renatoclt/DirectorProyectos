---
name: "probar-sistema-agentes"
description: "Ejecuta pruebas estáticas y, opcionalmente, escenarios conductuales del equipo de agentes."
agent: "Ingeniero de Testing de Agentes"
argument-hint: "mode=static|smoke|full o agent=Nombre del agente"
---

Valida el sistema de agentes con el modo `${input:testMode:static}`.

Procedimiento:

1. Lee `testing/README.md`, `governance/tool-policies.json` y los contratos aplicables.
2. Ejecuta `python testing/run_tests.py` sin opciones de escritura.
3. Si el modo es `static`, termina después del reporte automático.
4. Si el modo es `smoke`, ejecuta escenarios con la etiqueta `smoke`.
5. Si el modo es `full`, ejecuta todos los escenarios de `testing/scenarios/`.
6. Si el modo comienza con `agent:`, ejecuta únicamente escenarios del agente indicado.
7. Para cada escenario conductual, invoca el agente señalado con el prompt exacto del escenario y evalúa la respuesta con su rúbrica.
8. No modifiques archivos y no ejecutes `--update-baseline`.

Entrega una matriz con escenario, resultado, evidencia, desviación y severidad. Usa hallazgos `AGT-###`.
