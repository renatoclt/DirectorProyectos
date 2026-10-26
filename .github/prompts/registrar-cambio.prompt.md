---
description: "Registra y analiza una solicitud de cambio sin implementarla antes de su aprobación."
agent: "Director de Proyectos"
argument-hint: "Indica el proyecto y describe el cambio solicitado."
---

Registra una solicitud de cambio para el proyecto `${input:projectSlug:slug-del-proyecto}`.

Cambio solicitado:

`${input:changeDescription:Describe el cambio solicitado}`

Procedimiento obligatorio:

1. Lee `PROJECT-STATE.md`, `REQUIREMENTS.md`, `DECISIONS.md`, `TASKS.md`, `RISKS.md`, `APPROVALS.md` y `CHANGE-REQUESTS.md`.
2. Asigna el siguiente identificador `CR-###` disponible.
3. Clasifica la solicitud como corrección, ampliación, reducción, sustitución o cambio técnico.
4. Determina qué requisitos, historias, tareas, pruebas, decisiones, riesgos, seguridad, datos, operación y documentación podrían verse afectados.
5. Invoca únicamente a los especialistas necesarios para analizar el impacto. No autorices implementación.
6. Distingue claramente impacto confirmado, estimación preliminar, incertidumbre y decisiones necesarias.
7. Invoca al Gestor de Documentación para registrar la solicitud con estado:
   - `APPROVED` solo si el usuario la aprobó explícitamente en este mismo mensaje;
   - `WAITING_FOR_APPROVAL` en cualquier otro caso.
8. Actualiza `PROJECT-STATE.md` únicamente para reflejar que existe una solicitud abierta o aprobada.
9. No cambies el alcance aprobado, requisitos, tareas de construcción ni arquitectura hasta que exista aprobación registrada.

Entrega:

## Solicitud registrada
## Motivo y clasificación
## Impacto estimado
## Elementos afectados
## Riesgos
## Recomendación del equipo
## Decisión requerida
## Trabajo que permanece detenido hasta la aprobación
