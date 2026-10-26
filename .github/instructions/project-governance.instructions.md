---
name: "Gobierno y trazabilidad"
description: "Reglas de gobierno, trazabilidad, control de alcance y actualización del mapa maestro de cada proyecto."
applyTo: "**"
---

# Gobierno y trazabilidad del proyecto

Estas reglas se aplican cuando el repositorio utiliza el equipo de agentes y existe un proyecto administrado dentro de `projects/<slug>/`. Para tareas no relacionadas con un proyecto administrado, no crees registros artificiales.

## Fuente única de verdad

Cada proyecto controlado debe tener esta carpeta:

```text
projects/<slug>/00-control/
```

Y estos archivos:

```text
PROJECT-STATE.md
REQUIREMENTS.md
DECISIONS.md
TASKS.md
AGENT-ACTIVITY.md
RISKS.md
TRACEABILITY.md
APPROVALS.md
CHANGE-REQUESTS.md
```

`PROJECT-STATE.md` es el panel ejecutivo. Los demás documentos contienen el detalle verificable.

Antes de iniciar una actividad:

1. Identifica el proyecto y su `slug`.
2. Lee `PROJECT-STATE.md`, `TASKS.md`, `DECISIONS.md` y `APPROVALS.md`.
3. Lee los demás registros que sean relevantes para la tarea.
4. Verifica que la actividad esté vinculada a un requisito, tarea, defecto, riesgo, decisión o solicitud de cambio.
5. Si falta el control del proyecto, no inventes su estado: informa que debe inicializarse.

## Escritura controlada

El Director de Proyectos coordina las actualizaciones y delega su persistencia al Gestor de Documentación.

Los especialistas deben devolver un reporte autosuficiente, pero no cambiar directamente los archivos de `00-control/` salvo asignación explícita. El Gestor de Documentación debe registrar el resultado sin alterar su significado.

Después de cada paquete de trabajo terminado, actualiza de manera coherente:

1. `AGENT-ACTIVITY.md` con la actividad realizada.
2. `TASKS.md` con el estado y la evidencia de la tarea.
3. `TRACEABILITY.md` si cambió la cobertura de un requisito.
4. `RISKS.md` si apareció, cambió o se cerró un riesgo o impedimento.
5. `DECISIONS.md` si se tomó o propuso una decisión.
6. `CHANGE-REQUESTS.md` si se pidió modificar el alcance aprobado.
7. `APPROVALS.md` si hubo una decisión humana sobre una puerta de fase.
8. `PROJECT-STATE.md` como último paso, reflejando el estado consolidado.

No dejes `PROJECT-STATE.md` contradiciendo los registros detallados.

## Identificadores obligatorios

Usa identificadores estables y no los reutilices:

- Requisito funcional: `RF-001`.
- Requisito no funcional: `RNF-001`.
- Regla de negocio: `RN-001`.
- Historia de usuario: `HU-001`.
- Criterio de aceptación: `CA-001`.
- Tarea: `TASK-001`.
- Decisión general: `DEC-001`.
- Decisión de arquitectura: `ADR-001`.
- Riesgo: `R-001`.
- Impedimento o problema activo: `ISS-001`.
- Caso de prueba: `CP-001`.
- Defecto: `DEF-001`.
- Hallazgo de seguridad: `SEG-001`.
- Solicitud de cambio: `CR-001`.
- Aprobación o puerta: `GATE-001`.

## Control de alcance

Ningún agente puede iniciar una actividad que no se relacione con uno de estos elementos:

- requisito aprobado;
- tarea autorizada;
- defecto confirmado;
- riesgo o impedimento que requiera tratamiento;
- decisión solicitada;
- solicitud de cambio aprobada;
- instrucción explícita del usuario.

Una idea adicional no es alcance aprobado. Regístrala como recomendación o `CR-###` y espera decisión.

## Estados permitidos

### Requisitos

`PROPUESTO`, `CONFIRMADO`, `APROBADO`, `RECHAZADO`, `SUSTITUIDO`.

### Tareas

`BACKLOG`, `READY`, `IN_PROGRESS`, `BLOCKED`, `IN_REVIEW`, `DONE`, `CANCELLED`.

### Riesgos

`OPEN`, `MITIGATING`, `ACCEPTED`, `CLOSED`.

### Solicitudes de cambio

`DRAFT`, `UNDER_ANALYSIS`, `WAITING_FOR_APPROVAL`, `APPROVED`, `REJECTED`, `IMPLEMENTED`, `CANCELLED`.

### Fases

`INTAKE`, `DISCOVERY`, `DESIGN`, `PLANNING`, `BUILD`, `QUALITY`, `OPERATIONS`, `DOCUMENTATION`, `DELIVERY`, `CLOSED`, `PAUSED`, `CANCELLED`.

## Puertas de aprobación

- No pases de `PLANNING` a `BUILD` sin aprobación humana explícita registrada en `APPROVALS.md`.
- No realices despliegues, publicaciones, commits, pushes ni cambios externos sin una autorización específica.
- No pases a `DELIVERY` con defectos críticos abiertos, evidencia de pruebas insuficiente o revisiones obligatorias pendientes.
- No interpretes el silencio como aprobación.
- Una aprobación condicionada debe conservar sus condiciones y responsables.

## Evidencia

No marques una tarea como `DONE` sin evidencia verificable, por ejemplo:

- rutas de archivos modificados;
- identificador de commit, cuando exista y esté autorizado;
- comando de prueba y resultado;
- enlace a documento;
- salida de compilación;
- captura o registro de validación;
- decisión registrada.

No inventes porcentajes de avance. Usa conteos verificables o explica el método de cálculo.

## Conflictos y desactualización

Cuando dos documentos se contradigan:

1. No elijas silenciosamente una versión.
2. Marca la inconsistencia.
3. Identifica la fuente más reciente y su evidencia.
4. Solicita decisión cuando el conflicto afecte alcance, seguridad, costo, calendario o comportamiento.
5. Registra la resolución en `DECISIONS.md`.

## Reporte mínimo de cada agente

Cada especialista debe devolver:

```text
Agente:
Objetivo:
Elementos relacionados:
Tareas realizadas:
Archivos consultados:
Archivos modificados:
Comandos o pruebas ejecutadas:
Evidencia:
Decisiones propuestas o tomadas:
Riesgos o bloqueos:
Resultado:
Siguiente acción recomendada:
```

Resultados permitidos:

`COMPLETADO`, `COMPLETADO_CON_PENDIENTES`, `BLOQUEADO`, `NO_INICIADO`, `CANCELADO`.


## Auditoría independiente

El Auditor de Trazabilidad revisa vínculos y evidencias sin modificar registros. El Auditor de Entrega evalúa si el producto está listo. No combines ambos veredictos.
