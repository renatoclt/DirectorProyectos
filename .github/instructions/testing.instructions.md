---
name: "Testing del sistema de agentes y Skills"
description: "Convenciones para pruebas estáticas, contratos, Skills, licencias, baseline y escenarios conductuales."
applyTo: "testing/**/*"
---

# Testing del sistema

- Las pruebas automáticas deben ser deterministas y no destructivas por defecto.
- No escribas fuera de `testing/reports/` salvo el modo explícito y confirmado de actualización de baselines.
- Distingue validación estructural de evaluación conductual.
- Cada agente debe tener al menos un escenario de regresión.
- Las Skills deben validar nombre, descripción, referencias, licencia, origen, lock y agentes autorizados.
- Un escenario debe declarar comportamiento esperado, comportamiento prohibido y criterio de aprobación.
- No hagas pasar una prueba relajando el contrato o la Skill sin justificar y aprobar el cambio.
- Usa identificadores `AGT-###` para defectos del sistema.
- `BASE-002` protege agentes y contratos; `SKILLBASE-002` protege Skills, referencias, licencias y lock.
