---
description: "Detecta requisitos, tareas, pruebas, decisiones o entregables huérfanos y estados sin evidencia."
agent: "Auditor de Trazabilidad"
argument-hint: "Indica el slug del proyecto."
---

Audita la trazabilidad del proyecto `${input:projectSlug:slug-del-proyecto}` sin modificar archivos.

Lee todo `projects/${input:projectSlug:slug-del-proyecto}/00-control/` y los documentos enlazados.

Comprueba como mínimo:

1. Requisitos sin fuente o estado.
2. Requisitos aprobados sin criterios de aceptación.
3. Requisitos del MVP sin tareas.
4. Tareas sin requisito, defecto, riesgo o solicitud de cambio relacionada.
5. Tareas `DONE` sin evidencia.
6. Decisiones aplicadas sin registro.
7. Solicitudes de cambio implementadas sin aprobación.
8. Pruebas sin requisito asociado o sin resultado.
9. Requisitos implementados sin pruebas cuando deban tenerlas.
10. Defectos cerrados sin evidencia de revalidación.
11. Riesgos sin responsable o tratamiento.
12. Hallazgos de seguridad sin disposición.
13. Fases avanzadas sin puerta aprobada.
14. Contradicciones entre `PROJECT-STATE.md` y los registros detallados.
15. Actividad de agentes no reflejada en tareas o trazabilidad.
16. Referencias a archivos inexistentes.
17. Documentos desactualizados según su última fecha registrada.

Asigna hallazgos `TRA-001`, `TRA-002`, etc.

Entrega:

## Resultado general

Usa uno:

- `TRAZABILIDAD_COMPLETA`;
- `TRAZABILIDAD_PARCIAL`;
- `TRAZABILIDAD_INSUFICIENTE`.

## Hallazgos críticos
## Elementos huérfanos
## Estados sin evidencia
## Contradicciones
## Referencias rotas
## Correcciones recomendadas
## Orden sugerido de regularización

No corrijas los registros durante esta auditoría.
