# 8. Cómo modificar un agente sin romperlo

1. Define el motivo del cambio.
2. Edita `.github/agents/<agente>.agent.md`.
3. Actualiza `governance/contracts/<agente>.contract.json`.
4. Revisa `governance/tool-policies.json` si cambian herramientas.
5. Añade o modifica escenarios.
6. Ejecuta `python testing/run_tests.py`.
7. Ejecuta `/probar-sistema-agentes mode=agent:<nombre>`.
8. Revisa diferencias y hallazgos.
9. Con aprobación humana, actualiza baseline.
10. Repite las pruebas.

Nunca actualices el baseline primero: eso solo escondería que algo cambió.
