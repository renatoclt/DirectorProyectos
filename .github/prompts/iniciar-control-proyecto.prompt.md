---
description: "Inicializa el mapa maestro y los registros de control de un proyecto sin sobrescribir información existente."
agent: "Director de Proyectos"
argument-hint: "Indica el nombre y el slug del proyecto."
---

Inicializa el sistema de gobierno del proyecto.

Nombre del proyecto: `${input:projectName:Nombre del proyecto}`
Slug del proyecto: `${input:projectSlug:slug-del-proyecto}`

Reglas:

1. Valida que el slug use únicamente minúsculas, números y guiones.
2. Revisa si existe `projects/${input:projectSlug:slug-del-proyecto}/00-control/`.
3. Si ya existe cualquiera de los archivos de control, no lo sobrescribas. Informa qué existe y qué falta.
4. Lee todas las plantillas de `templates/project-control/`.
5. Invoca al Gestor de Documentación para crear, únicamente si faltan, estos archivos:

```text
projects/${input:projectSlug:slug-del-proyecto}/00-control/PROJECT-STATE.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/REQUIREMENTS.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/DECISIONS.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/TASKS.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/AGENT-ACTIVITY.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/RISKS.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/TRACEABILITY.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/APPROVALS.md
projects/${input:projectSlug:slug-del-proyecto}/00-control/CHANGE-REQUESTS.md
```

6. Sustituye `{{PROJECT_NAME}}`, `{{PROJECT_SLUG}}` y `{{YYYY-MM-DD}}` por valores reales.
7. Inicializa la fase como `INTAKE`, el estado como `ACTIVE` y el alcance como `NO APROBADO`.
8. No inventes requisitos, decisiones, responsables, fechas objetivo ni porcentajes.
9. No modifiques código fuente ni los agentes.
10. Devuelve los archivos creados, los archivos que ya existían y el siguiente paso recomendado.
