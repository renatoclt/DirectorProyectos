---
description: "Verifica una puerta de calidad y registra el avance de fase solamente con evidencia y aprobación."
agent: "Director de Proyectos"
argument-hint: "Indica el slug, la fase actual y la fase objetivo."
---

Evalúa el cierre de fase del proyecto `${input:projectSlug:slug-del-proyecto}`.

Fase actual declarada: `${input:currentPhase:fase-actual}`
Fase objetivo: `${input:targetPhase:fase-objetivo}`

Lee todos los archivos de `projects/${input:projectSlug:slug-del-proyecto}/00-control/` y los entregables enlazados.

## Criterios mínimos por transición

### INTAKE a DISCOVERY

- objetivo inicial registrado;
- usuarios o actores preliminares;
- supuestos diferenciados de hechos;
- preguntas principales identificadas.

### DISCOVERY a DESIGN

- requisitos y reglas registrados;
- alcance preliminar distinguido de ampliaciones;
- pendientes materiales visibles;
- contradicciones resueltas o aceptadas explícitamente.

### DESIGN a PLANNING

- MVP definido;
- experiencia o flujo principal definido cuando corresponda;
- arquitectura propuesta;
- datos, seguridad e integraciones evaluados cuando sean aplicables;
- decisiones técnicas pendientes visibles.

### PLANNING a BUILD

- alcance aprobado;
- tareas y dependencias definidas;
- responsables o agentes propuestos;
- criterios de aceptación trazables;
- riesgos principales con tratamiento;
- aprobación humana explícita registrada.

### BUILD a QUALITY

- tareas de construcción relevantes terminadas con evidencia;
- compilación o validación técnica ejecutada cuando corresponda;
- cambios fuera de alcance inexistentes o regularizados;
- trazabilidad actualizada.

### QUALITY a OPERATIONS, DOCUMENTATION o DELIVERY

- pruebas ejecutadas con evidencia;
- defectos críticos y altos resueltos o aceptados explícitamente;
- revisión de seguridad completada cuando sea obligatoria;
- riesgos residuales visibles;
- documentación u operación pendientes claramente separadas.

### DELIVERY a CLOSED

- auditoría final disponible;
- entregables identificados;
- condiciones de entrega cerradas o aceptadas;
- aprobaciones finales registradas;
- pendientes residuales con propietario.

## Reglas

1. No marques una condición como cumplida sin evidencia enlazada.
2. No avances automáticamente si falta una condición obligatoria.
3. No interpretes este prompt como aprobación humana.
4. Solo registra aprobación si el usuario la expresa de forma inequívoca en el mensaje actual.
5. Si la transición es válida y está aprobada, invoca al Gestor de Documentación para actualizar `APPROVALS.md` y luego `PROJECT-STATE.md`.
6. Si no es válida, no cambies la fase.

Entrega:

## Veredicto

Usa uno:

- `LISTO_PARA_APROBACION`;
- `APROBADO_Y_REGISTRADO`;
- `NO_LISTO`;
- `BLOQUEADO`.

## Lista de control
## Evidencias
## Faltantes
## Riesgos de avanzar
## Decisión requerida
## Siguiente acción
