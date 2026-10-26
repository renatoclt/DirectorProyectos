# 5. Testing y regresión

## Dos QA diferentes

- **QA Engineer:** prueba el producto del cliente.
- **Ingeniero de Testing de Agentes:** prueba los perfiles, contratos y conducta del equipo de IA.

## Pruebas automáticas

`python testing/run_tests.py` valida archivos, YAML, contratos, herramientas, visibilidad, referencias, escenarios y baseline.

## Baseline

Guarda huellas de perfiles y contratos. Si alguien cambia un agente, la prueba falla hasta que el cambio sea revisado y el baseline se actualice explícitamente.

## Pruebas conductuales

Los modelos no responden siempre con las mismas palabras. Por eso cada escenario evalúa:

- secciones esperadas;
- comportamientos obligatorios;
- comportamientos prohibidos;
- criterio de aprobación.

No se compara texto literal; se comprueba la función.

## Por qué la suite conductual se ejecuta directamente

Los subagentes anidados están deshabilitados por defecto. Si el Director invocara al agente de testing como subagente, este no debería volver a delegar. El prompt `/probar-sistema-agentes` lo activa directamente como agente principal y mantiene la arquitectura sin recursión.
