---
description: "Muestra el panel ejecutivo verificable de un proyecto, sus bloqueos y la siguiente acción."
agent: "Director de Proyectos"
argument-hint: "Indica el slug del proyecto."
---

Genera el estado ejecutivo del proyecto `${input:projectSlug:slug-del-proyecto}`.

Lee todos los archivos disponibles en:

```text
projects/${input:projectSlug:slug-del-proyecto}/00-control/
```

No modifiques archivos durante esta consulta.

Presenta exactamente estas secciones:

## Estado ejecutivo

- Proyecto.
- Fase actual.
- Estado general.
- Puerta de aprobación actual.
- Alcance aprobado: sí, no o condicionado.
- Última actualización verificable.

## Objetivo y resultado esperado

Resume únicamente información registrada.

## Alcance

- Incluido.
- Fuera de alcance.
- Solicitudes de cambio abiertas.

## Progreso verificable

Usa conteos, no porcentajes inventados:

- requisitos por estado;
- tareas por estado;
- pruebas ejecutadas y pendientes;
- defectos abiertos por severidad;
- hallazgos de seguridad abiertos;
- documentos o entregables pendientes.

## Equipo

- agentes activos;
- última actividad de cada uno;
- agentes todavía no utilizados que sean relevantes.

## Trabajo actual

- tareas en progreso;
- tareas bloqueadas;
- dependencias pendientes.

## Decisiones del usuario pendientes

Incluye identificador, pregunta concreta e impacto de no decidir.

## Riesgos principales

Máximo cinco, ordenados por impacto y probabilidad registrados.

## Inconsistencias o información desactualizada

Indica documentos contradictorios, referencias rotas, tareas sin evidencia o registros sin actualización.

## Siguiente paso recomendado

Proporciona una única acción principal y explica por qué.

## Acción requerida del usuario

Indica claramente `NINGUNA` cuando no se necesite una decisión.
