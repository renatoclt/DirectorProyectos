# Plan de pruebas del sistema de agentes y Skills

## Objetivo

Detectar cambios accidentales de función, permisos, alcance, visibilidad, delegación, Skills, licencias y comportamiento.

## Suite mínima antes de integrar cambios

1. Ejecutar `python testing/run_tests.py`.
2. Ejecutar `/probar-sistema-agentes mode=smoke`.
3. Ejecutar escenarios del agente o Skill afectados.
4. Revisar diferencias de perfiles, contratos, Skills, referencias y lock.
5. Confirmar que no se ampliaron herramientas sin justificación.
6. Confirmar que licencia y atribución se conservan.
7. Actualizar baselines solo después de aprobación.
8. Repetir la suite estática.

## Criterios de rechazo

- YAML inválido.
- Perfil sin contrato.
- Herramientas desincronizadas.
- Agente visible indebidamente.
- Director sin un agente requerido.
- Skill sin `SKILL.md`, licencia, origen o metadata.
- Nombre de Skill distinto de su carpeta.
- Referencia rota.
- Skill usada por un agente no autorizado.
- Escenario faltante.
- Baseline modificado sin revisión.
- Regresión crítica en aprobación, edición, alcance o evidencia.
