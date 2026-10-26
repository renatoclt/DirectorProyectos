# 4. Restricciones técnicas

## Mínimo privilegio

La propiedad `tools` limita las herramientas visibles para cada agente:

- analistas y auditores: lectura y búsqueda;
- implementadores: lectura, edición y terminal;
- QA y Seguridad: lectura y terminal, sin edición;
- Director: delegación, lectura, preguntas y tareas;
- Testing de Agentes: delegación, lectura y terminal, sin edición.

## Límite real

Una terminal puede modificar archivos aunque el agente no tenga la herramienta `edit`. Por eso las herramientas no son una seguridad absoluta. Se combinan con contrato, instrucciones, comandos no destructivos y revisión de evidencia.

## Visibilidad

Solo el Director tiene `user-invocable: true`. Los demás permanecen ocultos pero disponibles para delegación controlada.
