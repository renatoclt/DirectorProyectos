---
name: "Testing del sistema de agentes"
description: "Convenciones para pruebas estáticas, contratos, baseline y escenarios conductuales."
applyTo: "testing/**/*"
---

# Testing del sistema de agentes

- Las pruebas automáticas deben ser deterministas y no destructivas por defecto.
- No escribas fuera de `testing/reports/` salvo el modo explícito y confirmado de actualización del baseline.
- Distingue validación estructural de evaluación conductual.
- Cada agente debe tener al menos un escenario de regresión.
- Un escenario debe declarar comportamiento esperado, comportamiento prohibido y criterio de aprobación.
- No hagas pasar una prueba relajando el contrato sin justificar y aprobar el cambio.
- Usa identificadores `AGT-###` para defectos del sistema de agentes.
