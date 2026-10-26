# 2. Agentes, prompts e instructions

## Agent

Responde a **quién hace el trabajo**. Tiene rol, herramientas y un contrato. Ejemplo: QA Engineer.

## Prompt file

Responde a **qué procedimiento se ejecuta ahora**. Se invoca con `/`. Ejemplo: `/auditar-trazabilidad`.

## Instructions

Responde a **qué reglas se aplican de manera transversal**. Ejemplo: ningún agente marca una tarea DONE sin evidencia.

## Por qué se combinan

Un agente sin instrucciones globales puede perder reglas comunes. Un prompt sin agente no define independencia ni permisos. Una instruction no ejecuta un procedimiento. Cada pieza resuelve un problema distinto.
