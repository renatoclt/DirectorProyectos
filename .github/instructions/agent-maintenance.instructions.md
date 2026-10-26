---
name: "Mantenimiento seguro de agentes"
description: "Se aplica al crear o modificar perfiles de agentes; exige contrato, pruebas y baseline revisado."
applyTo: ".github/agents/**/*.agent.md"
---

# Mantenimiento seguro de agentes

Toda modificación de un perfil debe conservar estas capas:

1. Perfil `.agent.md` con rol e instrucciones.
2. Contrato correspondiente en `governance/contracts/<slug>.contract.json`.
3. Política de herramientas en `governance/tool-policies.json`.
4. Escenarios relacionados en `testing/scenarios/`.
5. Pruebas automáticas ejecutadas con `python testing/run_tests.py`.
6. Baseline actualizado solo después de revisión humana explícita.

No elimines restricciones para hacer pasar una tarea. Aplica mínimo privilegio. Si cambias nombre, herramientas, visibilidad, rutas, entradas, salidas o prohibiciones, actualiza el contrato y las pruebas en la misma modificación.
