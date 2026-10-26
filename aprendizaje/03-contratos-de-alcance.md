# 3. Contratos de alcance

## Por qué no basta el prompt

El cuerpo del agente puede editarse accidentalmente o interpretarse de forma amplia. El contrato externo declara de forma estructurada:

- propósito;
- fases permitidas;
- herramientas;
- acciones permitidas y prohibidas;
- rutas permitidas y prohibidas;
- entradas y salidas;
- criterios de finalización;
- reglas de escalamiento;
- escenarios de prueba.

Los contratos están en `governance/contracts/*.contract.json` porque JSON es legible por personas y por pruebas automáticas sin ambigüedad.

## Ejemplo

QA puede ejecutar pruebas, pero no editar código. Esa regla aparece en su contrato, su perfil y las pruebas. Si una capa cambia y las otras no, la suite falla.
