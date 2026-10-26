# Plan de pruebas del sistema de agentes

## Objetivo

Detectar cambios accidentales de función, permisos, alcance, visibilidad, delegación y comportamiento.

## Suite mínima antes de integrar cambios

1. Ejecutar `python testing/run_tests.py`.
2. Ejecutar `/probar-sistema-agentes mode=smoke`.
3. Ejecutar los escenarios del agente modificado.
4. Revisar diferencias del perfil y contrato.
5. Confirmar que no se ampliaron herramientas sin justificación.
6. Actualizar baseline solo después de aprobación.
7. Repetir la suite estática.

## Criterios de rechazo

- YAML inválido.
- Perfil sin contrato.
- Herramientas desincronizadas.
- Agente visible indebidamente.
- Director sin un agente requerido.
- Escenario faltante.
- Baseline modificado sin revisión.
- Regresión crítica en aprobación, edición, alcance o evidencia.
