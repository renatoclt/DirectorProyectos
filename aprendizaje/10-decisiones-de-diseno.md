# 10. Decisiones de diseño

## Solo un agente visible

Reduce ruido y mantiene una sola conversación con el cliente.

## Auditor de Trazabilidad separado

El Director coordina el mapa y no debe ser juez único de su propia coordinación.

## Testing de Agentes separado de QA

El producto y el sistema que lo construye tienen riesgos distintos. Mezclarlos ocultaría regresiones del equipo de agentes.

## Contratos JSON

Permiten validación automática y evitan depender solo de lenguaje natural.

## Prompt files para procedimientos

Inicializar control, consultar estado y auditar son acciones repetibles. Un prompt file evita reescribir el procedimiento.

## Baseline con actualización explícita

Detecta cambios accidentales y obliga a revisar cambios intencionales.
