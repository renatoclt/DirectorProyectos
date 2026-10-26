# Gobierno del sistema de agentes

Esta carpeta contiene controles externos a los prompts de los agentes.

## Por qué existe

Un prompt puede desviarse o cambiar accidentalmente. Por eso cada agente tiene tres capas:

1. **Contrato de alcance** en `contracts/*.contract.json`.
2. **Restricción técnica** mediante `tools`, visibilidad y rutas permitidas.
3. **Pruebas de regresión** en `testing/`.

Los contratos son la fuente legible y verificable de lo que el agente puede hacer. `tool-policies.json` mantiene las herramientas esperadas y `phase-gates.json` formaliza las transiciones que requieren evidencia o aprobación humana.

## Regla de mantenimiento

Cuando cambie un agente:

1. actualiza su `.agent.md`;
2. actualiza su contrato;
3. añade o modifica escenarios de prueba;
4. ejecuta `python testing/run_tests.py`;
5. revisa el cambio;
6. actualiza el baseline únicamente con aprobación humana explícita;
7. vuelve a ejecutar las pruebas.
