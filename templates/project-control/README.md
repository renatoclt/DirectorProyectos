# Plantillas de control y trazabilidad del proyecto

Estas plantillas complementan el equipo empresarial de agentes. No reemplazan los agentes existentes: agregan el mapa operativo que permite saber qué se pidió, qué se aprobó, qué hizo cada agente, qué evidencia existe y cuál es el siguiente paso.

## Objetivo

El sistema debe permitir responder en cualquier momento:

- ¿Cuál es el objetivo del proyecto?
- ¿En qué fase se encuentra?
- ¿Qué alcance está aprobado?
- ¿Qué está fuera de alcance?
- ¿Qué tareas están activas, bloqueadas o terminadas?
- ¿Qué hizo cada agente?
- ¿Qué decisiones tomó el usuario?
- ¿Qué requisitos ya fueron implementados y probados?
- ¿Qué riesgos o cambios siguen abiertos?
- ¿Qué acción corresponde ejecutar después?

## Inicialización

Al iniciar un proyecto, copia las nueve plantillas a:

```text
projects/<slug>/00-control/
```

Sustituye:

- `{{PROJECT_NAME}}` por el nombre legible del proyecto;
- `{{PROJECT_SLUG}}` por el identificador de carpeta;
- `{{YYYY-MM-DD}}` por la fecha de inicialización.

La forma recomendada es usar:

```text
/iniciar-control-proyecto
```

El comando debe crear solamente los archivos faltantes y nunca sobrescribir información existente.

## Archivos de control

| Archivo | Uso principal |
|---|---|
| `PROJECT-STATE.md` | Panel ejecutivo: fase, alcance, equipo, bloqueos, decisiones y siguiente paso |
| `REQUIREMENTS.md` | Requisitos funcionales, no funcionales, reglas, historias y criterios |
| `DECISIONS.md` | Decisiones generales y de arquitectura, incluidas las sustituidas |
| `TASKS.md` | Trabajo activo, backlog, bloqueos, responsables, límites y evidencias |
| `AGENT-ACTIVITY.md` | Registro cronológico de la actividad de cada agente |
| `RISKS.md` | Riesgos, impedimentos, mitigaciones y aceptaciones |
| `TRACEABILITY.md` | Relación entre requisitos, decisiones, tareas, implementación, pruebas y evidencia |
| `APPROVALS.md` | Puertas de fase, aprobaciones, condiciones y revocaciones |
| `CHANGE-REQUESTS.md` | Solicitudes que podrían modificar el alcance y su análisis de impacto |

`PROJECT-STATE.md` es el punto de entrada, pero no reemplaza a los registros detallados. Debe actualizarse después de ellos.

## Comandos disponibles

En una sesión Local de VS Code:

```text
/iniciar-control-proyecto
/estado-proyecto
/registrar-cambio
/cerrar-fase
/auditar-trazabilidad
```

### `/iniciar-control-proyecto`

Crea la carpeta `projects/<slug>/00-control/` y los nueve registros a partir de estas plantillas.

### `/estado-proyecto`

Lee el control sin modificarlo y muestra:

- fase y estado;
- alcance;
- progreso mediante conteos verificables;
- equipo activo;
- tareas y bloqueos;
- decisiones pendientes;
- riesgos;
- inconsistencias;
- siguiente paso recomendado.

### `/registrar-cambio`

Crea una solicitud `CR-###`, analiza su impacto y la deja pendiente de aprobación, salvo que el usuario la apruebe explícitamente en el mismo mensaje. No implementa el cambio.

### `/cerrar-fase`

Evalúa una transición de fase. No sustituye la aprobación humana y no debe avanzar si falta evidencia o una condición obligatoria.

### `/auditar-trazabilidad`

Detecta elementos huérfanos, contradicciones, estados sin evidencia, referencias rotas y fases avanzadas sin aprobación.

## Orden recomendado

1. Inicializar el control.
2. Registrar la idea, objetivo y actores.
3. Realizar descubrimiento y registrar requisitos.
4. Registrar decisiones y alcance.
5. Crear tareas relacionadas con requisitos, defectos, riesgos o cambios.
6. Consultar el estado después de cada bloque importante.
7. Registrar variaciones del alcance como `CR-###`.
8. Evaluar la puerta antes de cambiar de fase.
9. Auditar la trazabilidad antes de aprobar una fase o entregar.

## Fases

```text
INTAKE
DISCOVERY
DESIGN
PLANNING
BUILD
QUALITY
OPERATIONS
DOCUMENTATION
DELIVERY
CLOSED
PAUSED
CANCELLED
```

No se debe pasar de `PLANNING` a `BUILD` sin aprobación humana explícita en `APPROVALS.md`.

## Identificadores

```text
RF-001   Requisito funcional
RNF-001  Requisito no funcional
RN-001   Regla de negocio
HU-001   Historia de usuario
CA-001   Criterio de aceptación
TASK-001 Tarea
DEC-001  Decisión general
ADR-001  Decisión de arquitectura
R-001    Riesgo
ISS-001  Impedimento
CP-001   Caso de prueba
DEF-001  Defecto
SEG-001  Hallazgo de seguridad
CR-001   Solicitud de cambio
GATE-001 Aprobación o puerta
```

No reutilices identificadores.

## Reporte mínimo de un agente

Cada agente debe devolver:

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

```text
COMPLETADO
COMPLETADO_CON_PENDIENTES
BLOQUEADO
NO_INICIADO
CANCELADO
```

## Orden de actualización

Después de un paquete de trabajo:

1. `AGENT-ACTIVITY.md`;
2. `TASKS.md`;
3. `TRACEABILITY.md`;
4. `RISKS.md`;
5. `DECISIONS.md`;
6. `CHANGE-REQUESTS.md`;
7. `APPROVALS.md`;
8. `PROJECT-STATE.md` al final.

## Consulta rápida

Para recuperar el contexto de un proyecto, usa:

```text
/estado-proyecto
```

O solicita al Director:

```text
Lee projects/<slug>/00-control/ y dime el objetivo, fase, alcance aprobado,
trabajo terminado con evidencia, trabajo en curso, bloqueos, decisiones que
necesitan mi participación, riesgos, agentes activos y siguiente acción.
No modifiques archivos.
```

## Reglas de seguridad operativa

- No inventar avance, fechas, responsables o evidencias.
- No implementar una recomendación como si fuera requisito.
- No ampliar el alcance sin una solicitud de cambio aprobada.
- No marcar tareas `DONE` sin evidencia.
- No ocultar contradicciones.
- No interpretar silencio como aprobación.
- No desplegar, publicar, hacer `commit` o `push` sin autorización específica.
- No usar todos los agentes si el proyecto no los necesita.


## Auditoría independiente

Usa `/auditar-trazabilidad` para ejecutar el Auditor de Trazabilidad. Este agente detecta huecos y contradicciones, pero no modifica los registros.
