---
description: "Reglas para utilizar color-system, frontend-design y frontend-design-review sin ampliar alcance ni permisos."
applyTo: "**/*.{html,css,scss,sass,less,js,jsx,ts,tsx,vue,svelte}"
---

# Skills de diseño frontend

Cuando una tarea aprobada requiera decidir colores, tokens o contraste, considerar `color-system` antes del diseño visual completo.
Cuando una tarea aprobada cree o rediseñe una interfaz, considerar `frontend-design` usando la dirección cromática aprobada o recomendada.
Cuando una tarea revise una interfaz, PR, componente o flujo, considerar `frontend-design-review`.

Reglas obligatorias:

- El brief, los requisitos, la marca confirmada, el sistema de diseño y el contrato del agente prevalecen.
- Una Skill no concede herramientas, rutas ni autorización adicionales.
- No utilizar Skills frontend para backend, datos, infraestructura o lógica sin interfaz.
- No inventar funcionalidades para completar una composición.
- `color-system` genera tres alternativas y recomienda una; no presenta la recomendación como marca aprobada.
- `frontend-design` no debe sustituir silenciosamente la paleta aprobada o recomendada.
- En QA o Auditoría, revisar sin modificar código ni rediseñar.
- Registrar la Skill aplicada en el reporte del agente cuando haya influido materialmente en el resultado.
