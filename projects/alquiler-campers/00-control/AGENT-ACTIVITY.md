# Registro de actividad de agentes: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Reportes del Analista de Negocio, del Product Manager, del Diseñador UX/UI, del Arquitecto de Soluciones, del Revisor de Seguridad y del Planificador (incluidas la estimación de plazo y la estimación de la opción B) entregados por el Director; instrucciones del Director y del usuario al Gestor.

Este registro es cronológico y acumulativo. No borres entradas anteriores; añade correcciones como entradas nuevas.

**Limitación:** las fuentes no indican la hora de cada actividad. Se registra solo la fecha 2026-10-26 indicada por el Director para el expediente. El orden de las entradas es el orden lógico de producción de los documentos (el Product Manager se basa en el análisis previo).

## Resumen por agente

| Agente | Última actividad | Tarea relacionada | Resultado | Próxima acción |
|---|---|---|---|---|
| Analista de Negocio | 2026-10-26 | TASK-001 | COMPLETADO_CON_PENDIENTES | Atender PEND-001 a PEND-007 y validación legal (vía Director) |
| Product Manager | 2026-10-26 | TASK-002 | No declarado en la fuente | Resolver P-004, P-007 y P-009 (vía Director) |
| Diseñador UX/UI | 2026-10-26 | TASK-010 | COMPLETADO_CON_PENDIENTES (BORRADOR; conflicto de contrato devuelto al Director) | Decidir PEND-033 y las de marca (vía Director) |
| Arquitecto de Soluciones | 2026-10-26 | TASK-011 | COMPLETADO_CON_PENDIENTES (BORRADOR; sin conflicto de contrato declarado) | Decisiones del cliente listadas en [DECISIONS](DECISIONS.md) (vía Director) |
| Revisor de Seguridad | 2026-10-26 | TASK-015 | COMPLETADO_CON_PENDIENTES (BORRADOR; revisión de diseño, ninguna prueba ejecutada; sin conflicto de contrato) | Decisiones PEND-035, 037, 038, 039 y B1 a B9 (vía Director) |
| Planificador de Proyecto | 2026-10-26 | TASK-016, TASK-018, T1 a T10 [OPB] | COMPLETADO_CON_PENDIENTES (BORRADOR sin fechas; conflicto de fase devuelto al Director; estimación de plazo preliminar a confirmar; estimación de la opción B a confirmar, ACT-013) | El Director lanza TASK-010 [PLAN] (B1 a B9); decide la variante de la opción B (PEND-046) |
| Redactor de Propuestas (ejecutado por un agente general bajo su perfil) | 2026-10-26 | TASK-019, TASK-026 [OPB] | No declarado por el Gestor (reporte no recibido por el Gestor). Actualizó `12-propuesta/` para la opción B (ACT-014) | Revisión del Director y confirmación del cliente (PEND-041, PEND-044) |
| Gestor de Documentación | 2026-10-26 | TASK-003, TASK-010, TASK-011, TASK-015, TASK-016, TASK-018, TASK-019, TASK-026 [OPB] | COMPLETADO_CON_PENDIENTES (ACT-015) | Esperar decisiones del Director |
| Director de Proyectos | 2026-10-26 | Coordinación | No registrado por el Gestor | Ver [PROJECT-STATE](PROJECT-STATE.md) §12 |

## Actividad cronológica

### ACT-001 — Análisis de negocio

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Analista de Negocio
- **Objetivo:** Convertir la idea del cliente y sus respuestas en requisitos, reglas, validaciones, criterios de aceptación y preguntas abiertas.
- **Elementos relacionados:** RF-001 a RF-032, RNF-001 a RNF-014, RN-001 a RN-027, CA-001 a CA-014, R-001 a R-013, VAL-001 a VAL-022, Q1 a Q7. Escenario AN-001.
- **Tareas realizadas:** Análisis del contexto recibido. Revisión de reglas corporativas, contrato y plantilla. Comprobación de que `projects/` no contenía documentación previa.
- **Archivos consultados:** `.github/copilot-instructions.md`, `governance/contracts/analista-negocio.contract.json`, `testing/scenarios/analista-negocio/an-001-no-inventar.json`, extractos de `templates/agent-report.md` y `.github/instructions/project-governance.instructions.md`, listado de `projects/`.
- **Archivos modificados:** Ninguno (según la fuente).
- **Comandos o pruebas ejecutadas:** Ninguna.
- **Evidencia:** [requirements.md](../01-discovery/requirements.md).
- **Decisiones propuestas o tomadas:** Ninguna tomada. Recomendaciones [R] y supuestos [S] sujetos a confirmación (ver [DECISIONS](DECISIONS.md)).
- **Riesgos o bloqueos:** R-001 a R-013 del Analista (ver [RISKS](RISKS.md)). Tensión entre "completa y robusta" y la separación MVP/F2/AMP.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada (según la fuente):** El Director traslada al cliente las 7 preguntas y solicita validación legal. Con las respuestas, consolida DISCOVERY y evalúa activar Product Manager. Después decide Seguridad y UX/UI. No iniciar desarrollo sin aprobación explícita del alcance.

### ACT-002 — Definición de MVP y backlog

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Product Manager
- **Objetivo:** Definir visión, MVP, priorización MoSCoW, historias de usuario, criterios de aceptación, dependencias, métricas, segunda fase y riesgos de producto.
- **Elementos relacionados:** HU-001 a HU-036, CA-001 a CA-034, R-001 a R-010 (producto), P-001 a P-016, y los RF/RN/RNF del análisis.
- **Tareas realizadas:** Lectura del contrato y las reglas corporativas. Definición del MVP como ciclo buscar → precio → reservar → pagar → confirmar → administrar. Formulación de CA-001 a CA-034.
- **Archivos consultados:** Contrato y reglas corporativas (según la fuente).
- **Archivos modificados:** Ninguno (según la fuente).
- **Comandos o pruebas ejecutadas:** Ninguna declarada.
- **Evidencia:** [mvp-and-backlog.md](../02-product/mvp-and-backlog.md).
- **Decisiones propuestas o tomadas:** Ninguna tomada. Las decisiones de producto del Director (pago total, fianza informativa, código+email, etc.) son [R] y el cliente no las ha confirmado.
- **Riesgos o bloqueos:** R-001 a R-010 del Product Manager. Reconciliación pendiente de CA-001 a CA-014 con el análisis. Contradicción P-007 sobre RF-031.
- **Resultado:** No declarado en la fuente (el reporte no incluye una línea de resultado). Declara que no aprueba el alcance y que el MVP es viable, pero no puede salir a producción sin P-001, P-005 y P-014.
- **Siguiente acción recomendada (según la fuente):** El Director resuelve las escalaciones P-004, P-007 y P-009 y reconcilia los CA con el análisis original.

### ACT-003 — Persistencia del expediente e inicialización del control

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Gestor de Documentación
- **Objetivo:** Persistir como BORRADOR el resumen del cliente, los dos reportes de especialistas y los nueve registros de control.
- **Elementos relacionados:** Gobierno del proyecto; ISS-001 a ISS-014; DEC-001 a DEC-032; PEND-001 a PEND-024; GATE-001 y GATE-002.
- **Tareas realizadas:** Lectura de las dos fuentes, del contrato y de las plantillas de control. Creación de [client-brief.md](../00-intake/client-brief.md), [requirements.md](../01-discovery/requirements.md), [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) y los nueve archivos de `00-control/`. Comparación de ambas fuentes para registrar discrepancias.
- **Archivos consultados:** Los dos archivos de origen indicados por el Director; `governance/contracts/gestor-documentacion.contract.json`; `.github/copilot-instructions.md`; plantillas de `templates/project-control/`.
- **Archivos modificados:** Solo archivos nuevos dentro de `projects/alquiler-campers/`.
- **Comandos o pruebas ejecutadas:** No aplica.
- **Evidencia:** Archivos presentes en `projects/alquiler-campers/`. Ver [TASKS](TASKS.md) TASK-003.
- **Decisiones propuestas o tomadas:** Ninguna tomada. Se registran 32 propuestas (DEC-001 a DEC-032) como PROPUESTA.
- **Riesgos o bloqueos:** La lista de 14 discrepancias y la numeración DEC-001 a DEC-032 no estaban disponibles en el contexto del Gestor y se reconstruyeron desde las dos fuentes (ver sección "Observaciones del Gestor" de [DECISIONS](DECISIONS.md)). El texto literal del mensaje inicial del cliente no fue suministrado.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada:** El Director confirma que la reconstrucción de ISS y DEC equivale a la lista aprobada, confirma el ID de GATE-002, y decide la secuencia de puertas.

### ACT-004 — Especificación UX/UI del MVP

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Diseñador UX/UI
- **Objetivo:** Diseñar la experiencia del MVP de la web de alquiler de campers (España) según la propuesta del PM (DEC-029).
- **Elementos relacionados:** RF-001 a RF-026 y RF-032, RNF-001 a RNF-005 y RNF-013, HU-001 a HU-024, CA-001 a CA-034, DEC-001 a DEC-032, PEND-001 a PEND-024, ISS-002. Escenario UX-001.
- **Tareas realizadas:** Diseño de recorridos R1 a R5, mapa del sitio, pantallas P01 a P21 con wireframes, estados de interfaz, formularios, responsive, accesibilidad, microcopy, propuesta de marca (no aprobada), rendimiento visual, matriz pantalla → requisito y riesgos de experiencia.
- **Archivos consultados:** PROJECT-STATE, DECISIONS, requirements, mvp-and-backlog, `ux-ui-designer.contract.json`, `copilot-instructions.md`, plantilla de reporte y escenario UX-001 (según la fuente).
- **Archivos modificados:** Ninguno (según la fuente).
- **Comandos o pruebas ejecutadas:** Ninguna (según la fuente). No hay usuarios, analítica ni pruebas de usabilidad.
- **Evidencia:** [ux-specification.md](../03-ux/ux-specification.md) (BORRADOR).
- **Decisiones propuestas o tomadas:** Ninguna tomada. No elige entre las dos lecturas de ISS-002. La propuesta de marca ("Ruta Camper", paleta y tipografía) no está aprobada. Pendientes en PEND-025 a PEND-033 y PEND-012, PEND-013, PEND-017 a PEND-019, PEND-023 (ver [DECISIONS](DECISIONS.md)).
- **Riesgos o bloqueos:** **Conflicto de contrato devuelto al Director:** el contrato limita el trabajo a la fase DESIGN y al "alcance aprobado"; GATE-002 está PENDING y el alcance no está aprobado. Riesgos de experiencia R-UX-01 a R-UX-10 (ver [RISKS](RISKS.md)).
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada (según la fuente):** El Director decide la pregunta 1 (activar DESIGN pese a GATE-002) y las de marca. Con el alcance aprobado, el diseño se formaliza en `03-ux/ux-specification.md`.

### ACT-005 — Arquitectura de solución del MVP

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Arquitecto de Soluciones
- **Objetivo:** Proponer una arquitectura proporcional al MVP del PM, con puntos de extensión para Fase 2.
- **Elementos relacionados:** ADR-001 a ADR-012, RF-001 a RF-032, RNF-001 a RNF-014, RN-001 a RN-027, DEC-001 a DEC-032, PEND-001 a PEND-024, R-ARQ-01 a R-ARQ-12. Escenario ARQ-001.
- **Tareas realizadas:** Alternativas, arquitectura recomendada (monolito modular con worker), flujo de datos, contratos conceptuales, modelo de datos conceptual, autenticación, seguridad y privacidad, integraciones (comparación de pasarelas sin imponer), observabilidad, escalabilidad, estrategia de despliegue, SEO técnico, ADR-001 a ADR-012, trazabilidad, pruebas recomendadas, riesgos técnicos y supuestos.
- **Archivos consultados:** `PROJECT-STATE.md`, `DECISIONS.md`, `requirements.md`, `mvp-and-backlog.md`, `arquitecto-soluciones.contract.json`, `copilot-instructions.md` (según la fuente).
- **Archivos modificados:** Ninguno (según la fuente).
- **Comandos o pruebas ejecutadas:** Ninguna (según la fuente). Las pruebas recomendadas no se han ejecutado.
- **Evidencia:** [solution-architecture.md](../04-architecture/solution-architecture.md) (BORRADOR).
- **Decisiones propuestas o tomadas:** Ninguna tomada. ADR-001 a ADR-012 son Recomendaciones registradas como PROPUESTA (ver [DECISIONS](DECISIONS.md) §2). Ninguna tecnología se declara obligatoria.
- **Riesgos o bloqueos:** R-ARQ-01 a R-ARQ-12 (ver [RISKS](RISKS.md)). El reporte declara que no hay restricción incompatible ni riesgo crítico que impida diseñar, y que la integración no confirmada es la pasarela (ADR-004). No declara conflicto de contrato (ver ISS-016 en [RISKS](RISKS.md)).
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada (según la fuente):** El Director traslada al cliente las decisiones listadas, confirma DEC-029 con la excepción de CA-008, activa Seguridad y UX/UI (TASK-009) antes de PLANNING y reconcilia CA-001 a CA-014 (ISS-001). Ninguna decisión está aprobada: no iniciar BUILD ni desplegar sin autorización expresa del cliente.

### ACT-006 — Persistencia de UX y arquitectura y actualización del control

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Gestor de Documentación
- **Objetivo:** Persistir como BORRADOR los reportes del Diseñador UX/UI y del Arquitecto de Soluciones y actualizar los registros de control.
- **Elementos relacionados:** ACT-004, ACT-005, TASK-010, TASK-011, ADR-001 a ADR-012, R-UX-01 a R-UX-10, R-ARQ-01 a R-ARQ-12, ISS-015 a ISS-023, PEND-025 a PEND-036, GATE-002.
- **Tareas realizadas:** Lectura completa de ambos reportes y de los registros de control. Creación de `03-ux/ux-specification.md` y `04-architecture/solution-architecture.md`. Actualización de AGENT-ACTIVITY, TASKS, DECISIONS, RISKS, TRACEABILITY y PROJECT-STATE. Comparación de UX, arquitectura, PM y Analista para registrar inconsistencias nuevas sin elegir versión.
- **Archivos consultados:** Los dos reportes de origen indicados por el Director, `governance/contracts/gestor-documentacion.contract.json` y los registros existentes de `00-control/`.
- **Archivos modificados:** Solo dentro de `projects/alquiler-campers/` (ver la lista exacta en el reporte del Gestor al Director).
- **Comandos o pruebas ejecutadas:** No aplica.
- **Evidencia:** [ux-specification.md](../03-ux/ux-specification.md), [solution-architecture.md](../04-architecture/solution-architecture.md).
- **Decisiones propuestas o tomadas:** Ninguna. ADR-001 a ADR-012 y PEND-025 a PEND-036 se registran como pendientes.
- **Riesgos o bloqueos:** Los IDs R-UX-01 a R-UX-10 y PEND-025 a PEND-036 son asignados por el Gestor (no vienen numerados así en las fuentes). Inconsistencias nuevas: ISS-015 a ISS-023.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada:** El Director revisa las inconsistencias nuevas (ISS-015 a ISS-023), decide PEND-033 y las demás pendientes, y confirma la numeración provisional.

### ACT-007 — Revisión de seguridad del diseño

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Revisor de Seguridad (independiente, no correctivo)
- **Objetivo:** Revisar la seguridad del diseño del MVP de alquiler de campers (revisión estática y documental).
- **Elementos relacionados:** SEG-001 a SEG-017, ADR-001 a ADR-012, DEC-001 a DEC-032, RF/RN/RNF/CA citados, PEND-010, PEND-011, PEND-012, PEND-015.
- **Tareas realizadas:** Modelado básico de amenazas (STRIDE) con guía OWASP ASVS y Top 10 sobre los flujos de reserva, pago, consulta y panel. Identificación de 17 hallazgos, controles obligatorios para BUILD y limitaciones.
- **Archivos consultados:** `DECISIONS.md` (completo); `requirements.md` y `mvp-and-backlog.md` (parcial, no leídos enteros); borrador de arquitectura (archivo temporal, completo) (según la fuente).
- **Archivos modificados:** Ninguno (según la fuente).
- **Comandos o pruebas ejecutadas:** **Ninguna.** No hay código, entorno ni analizadores aplicables. Las verificaciones propuestas no están ejecutadas.
- **Evidencia:** [security-review.md](../08-security/security-review.md) (BORRADOR).
- **Decisiones propuestas o tomadas:** Ninguna tomada. Ninguna aceptación de riesgo solicitada ni concedida. Escala al Director: segundo factor para cancelar y MFA obligatorio (SEG-001, SEG-006), auditoría mínima en el MVP (SEG-007) y VAL-020 con precio > 0 (SEG-005). Ver PEND-035, PEND-037, PEND-038, PEND-039.
- **Riesgos o bloqueos:** SEG-001 a SEG-017, todos OPEN ([RISKS](RISKS.md) §4). Sin conflicto de contrato declarado. Veredicto del Revisor: "APROBADO CON CONDICIONES" para continuar el diseño y pasar a PLANNING; **no** para BUILD ni producción (ver ISS-025: no es una aprobación del proyecto).
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada (según la fuente):** El Director decide las cuatro escalaciones. La revisión de implementación queda para QUALITY.

### ACT-008 — Plan de implementación del MVP

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Planificador de Proyecto
- **Objetivo:** Planificar la implementación del MVP: estrategia, fases, hitos, desglose de trabajo, dependencias, riesgos, definiciones de preparado y terminado, y plan de validación.
- **Elementos relacionados:** TASK-010 a TASK-071 del plan, B1 a B9, R-PL-001 a R-PL-011, SEG-001 a SEG-017, ADR-001 a ADR-012, CA-001 a CA-034, ISS-002, ISS-004 a ISS-011.
- **Tareas realizadas:** Definición de 7 fases (P0 a P6), 7 hitos (H0 a H6) y 38 tareas del plan (según el desglose), con dependencias, tamaños relativos y criterios de cierre. Sin fechas.
- **Archivos consultados:** `PROJECT-STATE`, `DECISIONS` (parcial), `TASKS`, `mvp-and-backlog` y los borradores de UX, arquitectura y seguridad. `RISKS` y `requirements` no se leyeron completos (según la fuente).
- **Archivos modificados:** Ninguno (según la fuente).
- **Comandos o pruebas ejecutadas:** Ninguna (según la fuente). El plan de validación es una propuesta.
- **Evidencia:** [implementation-plan.md](../05-planning/implementation-plan.md) (BORRADOR).
- **Decisiones propuestas o tomadas:** Ninguna tomada. El plan no se aprueba a sí mismo. Pide al Director B1 a B9 y decisiones de alcance (resolver ISS-004 a ISS-011, auditoría mínima, VAL-020 con precio > 0, prioridades P-004, P-007, P-009).
- **Riesgos o bloqueos:** **Conflicto devuelto al Director:** proyecto en INTAKE con GATE-001 PENDING, alcance no aprobado, GATE-002 PENDING y PLANNING → BUILD no solicitada. El plan no autoriza BUILD ni despliegues. R-PL-001 a R-PL-011 ([RISKS](RISKS.md) §5). Inconsistencias: ISS-024 a ISS-033.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada (según la fuente):** El Director revisa el borrador y lanza TASK-010 [PLAN] para pedir B1 a B9 al cliente. El plan solo es vinculante si el Director y el cliente lo aprueban de forma explícita.

### ACT-009 — Persistencia de seguridad y plan, y actualización del control

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Gestor de Documentación
- **Objetivo:** Persistir como BORRADOR los reportes del Revisor de Seguridad y del Planificador y actualizar los registros de control.
- **Elementos relacionados:** ACT-007, ACT-008, TASK-015, TASK-016, TASK-010 [PLAN] a TASK-071, B1 a B9, SEG-001 a SEG-017, R-PL-001 a R-PL-011, ISS-024 a ISS-033, PEND-037 a PEND-040, GATE-002.
- **Tareas realizadas:** Registro de las decisiones del Director de esta sesión: (a) confirma las numeraciones R-UX-xx, PEND-025 a PEND-036 e ISS-015 a ISS-023; (b) PEND-033: el diseño continúa como BORRADOR con GATE-002 PENDING y ningún artefacto se considera aprobado; (c) las erratas del Arquitecto se mantienen con la nota del Gestor. Lectura completa de ambos reportes y de los registros de control. Creación de `08-security/security-review.md` y `05-planning/implementation-plan.md`. Actualización de AGENT-ACTIVITY, TASKS, DECISIONS, RISKS, TRACEABILITY, APPROVALS (solo nota) y PROJECT-STATE. Resolución de la colisión de IDs de tareas con el calificador [PLAN], sin reutilizar IDs.
- **Archivos consultados:** Los dos reportes de origen indicados por el Director, `governance/contracts/gestor-documentacion.contract.json`, `templates/project-control/README.md` (catálogo de identificadores) y los registros existentes de `00-control/`.
- **Archivos modificados:** Solo dentro de `projects/alquiler-campers/` (lista exacta en el reporte del Gestor al Director).
- **Comandos o pruebas ejecutadas:** No aplica.
- **Evidencia:** [security-review.md](../08-security/security-review.md), [implementation-plan.md](../05-planning/implementation-plan.md).
- **Decisiones propuestas o tomadas:** Ninguna. B1 a B9 y PEND-037 a PEND-040 se registran como pendientes. El Gestor no registra ninguna solicitud ni aprobación de PLANNING → BUILD.
- **Riesgos o bloqueos:** IDs asignados por el Gestor: TASK-015, TASK-016, TASK-017, PEND-037 a PEND-040 e ISS-024 a ISS-033 (por confirmar por el Director). Inconsistencias nuevas: ISS-024 a ISS-033.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada:** El Director revisa ISS-024 a ISS-033 (TASK-017), decide cómo tratar la numeración de tareas del plan y lanza TASK-010 [PLAN] cuando corresponda.

### ACT-010 — Estimación preliminar de plazo

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Planificador de Proyecto
- **Objetivo:** Estimar de forma preliminar el plazo del MVP (Recomendación / estimación a confirmar), sin fechas de calendario ni costos, contado desde H0 (autorización de BUILD).
- **Elementos relacionados:** TASK-016 (plan), H0 a H6, B1 a B9, R-PL-001 a R-PL-007, R-PL-012, R-PL-009, R-PL-010, TASK-012 [PLAN], TASK-064, PEND-014, PEND-021.
- **Tareas realizadas:** Conversión de tamaños S/M/L a semanas-persona (≈63 sp sin P0 ni tareas del cliente), estimación de tres puntos por fase, rango recomendado de 28 a 36 semanas desde H0 (probable 30 a 31), hitos relativos, límites de decisiones, condiciones, exclusiones y datos que faltan para pasar a fecha calendario.
- **Archivos consultados:** No indicados en la fuente recibida por el Gestor (la instrucción del Director transcribe el resultado).
- **Archivos modificados:** Ninguno (según la instrucción del Director).
- **Comandos o pruebas ejecutadas:** Ninguna declarada.
- **Evidencia:** [estimacion-plazo.md](../05-planning/estimacion-plazo.md) (BORRADOR).
- **Decisiones propuestas o tomadas:** Ninguna tomada. Recomienda comunicar el rango 28 a 36 semanas y no publicar 22 ni 45. Ver DEC-033, PEND-041 y PEND-042.
- **Riesgos o bloqueos:** Riesgo nuevo R-PL-012 [PLAN]. El plazo asume B1 a B9 resueltas en H0 y MFA, auditoría mínima y precio > 0 dentro del alcance; ninguna de esas decisiones está aprobada (ISS-035). Tensión con "presupuesto y fechas fuera del contrato" (ISS-034).
- **Resultado:** No declarado por el agente en la fuente recibida.
- **Siguiente acción recomendada (según la fuente):** Revisar la estimación en H1 (S4) y en H2. Usar el rango 28 a 36 semanas en la propuesta, sujeto a confirmación del cliente.

### ACT-011 — Propuesta comercial (Redactor de Propuestas)

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Redactor de Propuestas, **ejecutado por un agente general bajo su perfil** (no por un agente dedicado), según la instrucción del Director.
- **Objetivo:** Elaborar la propuesta comercial del proyecto. El Director solicitó este trabajo **por instrucción explícita del usuario**.
- **Elementos relacionados:** `projects/alquiler-campers/12-propuesta/`, DEC-033, PEND-041, ISS-034, ISS-036, TASK-019.
- **Tareas realizadas (según el Director):** Creó `projects/alquiler-campers/12-propuesta/` con **18 archivos**: README, propuesta-comercial, analisis-consolidado, perfil-empresa, checklist-calidad-propuesta y `mockups/` con 10 pantallas HTML, `index.html`, `_base.css` y README.
- **Archivos consultados:** No conocidos por el Gestor.
- **Archivos modificados:** Creó `12-propuesta/` (18 archivos). **El Gestor no los ha leído, verificado ni modificado**: la ruta está prohibida a su contrato. La lista y el número de archivos son los que indica el Director.
- **Comandos o pruebas ejecutadas:** Ninguna declarada al Gestor.
- **Evidencia:** carpeta [12-propuesta](../12-propuesta/) (estado documental no declarado al Gestor; se registra como BORRADOR en este expediente, sin aprobación).
- **Decisiones propuestas o tomadas:** Ninguna tomada. Ver DEC-033 (propuesta comercial como entregable, plazo como rango 28 a 36 semanas desde H0) y PEND-041.
- **Riesgos o bloqueos:** El contenido no está revisado por el Gestor frente al expediente (ISS-036). Tensión con "presupuesto y fechas fuera del contrato" (ISS-034).
- **Resultado:** No declarado en la información recibida por el Gestor.
- **Siguiente acción recomendada:** El Director revisa la propuesta frente al expediente y obtiene la confirmación del cliente (PEND-041) antes de comunicar plazos.

### ACT-012 — Persistencia de la estimación de plazo y actualización del control

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Gestor de Documentación
- **Objetivo:** Persistir como BORRADOR la estimación preliminar de plazo, registrar la propuesta comercial creada por el Redactor de Propuestas y actualizar los registros de control.
- **Elementos relacionados:** ACT-010, ACT-011, TASK-018, TASK-019, TASK-025, DEC-033, PEND-041, PEND-042, R-PL-012, ISS-034 a ISS-037.
- **Tareas realizadas:** Creación de `05-planning/estimacion-plazo.md` desde la instrucción del Director. Comprobación aritmética de las cifras (el Gestor no halló discrepancias). Actualización de AGENT-ACTIVITY, TASKS, DECISIONS, RISKS, TRACEABILITY y PROJECT-STATE. **No se leyó ni se escribió en `12-propuesta/`** (ruta prohibida a su contrato).
- **Archivos consultados:** `governance/contracts/gestor-documentacion.contract.json` (rutas permitidas y prohibidas) y los registros existentes de `00-control/`.
- **Archivos modificados:** Solo dentro de `projects/alquiler-campers/`, fuera de `12-propuesta/` (lista exacta en el reporte del Gestor al Director).
- **Comandos o pruebas ejecutadas:** No aplica.
- **Evidencia:** [estimacion-plazo.md](../05-planning/estimacion-plazo.md).
- **Decisiones propuestas o tomadas:** Ninguna. DEC-033 se registra como PROPUESTA y PEND-041, PEND-042 como pendientes.
- **Riesgos o bloqueos:** IDs asignados por el Gestor: TASK-018, TASK-019, TASK-025, ACT-010 a ACT-012, DEC-033, PEND-041, PEND-042, ISS-034 a ISS-037 (por confirmar). No hay archivo de origen separado para la estimación: la fuente es la instrucción del Director.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada:** El Director revisa ISS-034 a ISS-037, confirma el uso del plazo con el cliente (PEND-041) y revisa el contenido de `12-propuesta/`.

### ACT-013 — Estimación de la opción B (entrega inicial acotada)

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Planificador de Proyecto
- **Objetivo:** Evaluar y estimar la Opción B (entrega inicial acotada) como Recomendación / estimación a confirmar, sin fechas de calendario ni costos propios.
- **Elementos relacionados:** T1 a T10 [OPB], R-001 a R-008 [OPB], D1 a D7 (días relativos), RN-001, RNF-010, estimacion-plazo.md, PEND-025.
- **Tareas realizadas:** Veredicto (la B completa, 50–70 h, no cabe en 1 semana con holgura; un "núcleo B" de ~38–42 h cabe solo para entrega a revisión, con riesgo alto y 5 condiciones; alternativa: B completa en 1,5–2,5 semanas o 2 personas), desglose T1 a T10 y ruta crítica, dependencias del cliente, riesgos, exclusiones, hitos D1 a D7, cobertura de RF, RNF y RN, desviación de RN-001 y RNF-010, y sección de alcance y precio (400 USD, fijado por el usuario) con aritmética y criterio de negociación.
- **Archivos consultados:** Según el propio reporte: el catálogo de requisitos, el MVP y backlog (alcance y MoSCoW), `estimacion-plazo.md` y el README de mockups. **No revisó** en detalle `ux-specification`, `implementation-plan` ni la arquitectura.
- **Archivos modificados:** Ninguno (según la instrucción del Director).
- **Comandos o pruebas ejecutadas:** Ninguna declarada.
- **Evidencia:** [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) (BORRADOR). Su §7 es INTERNA.
- **Decisiones propuestas o tomadas:** Ninguna tomada por el agente. Pendientes para el Director: variante (PEND-046), quién edita el contenido (PEND-045), USD o EUR e impuestos (PEND-043), confirmar la desviación y abrir el CR (CR-001, PEND-044), compatibilidad de la pila (PEND-047). Recomendación interna: ante negociación, ceder alcance y no calidad; no ceder plazo sin ceder alcance (DEC-034 [OPB], nota).
- **Riesgos o bloqueos:** R-001 a R-008 [OPB]. Inconsistencias ISS-038 a ISS-045.
- **Resultado:** No declarado por el agente en la fuente recibida.
- **Siguiente acción recomendada (según la fuente):** El Director decide entre el núcleo en 1 semana, la B completa en unas 2 semanas o 2 personas; confirma quién edita el contenido, la moneda y el IVA; confirma la desviación de RN-001 y RNF-010 y abre el CR.

### ACT-014 — Actualización de la propuesta comercial para la opción B (Redactor de Propuestas)

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Redactor de Propuestas, **ejecutado por un agente general bajo su perfil** (no por un agente dedicado), por **instrucción explícita del usuario** trasladada por el Director.
- **Objetivo:** Actualizar `12-propuesta/` para la opción B.
- **Elementos relacionados:** `projects/alquiler-campers/12-propuesta/`, CR-001, DEC-034 [OPB], TASK-019, TASK-026 [OPB], ISS-040, ISS-045.
- **Tareas realizadas (según el Director):** Actualizó `12-propuesta/` para la opción B. El Gestor no recibió la lista de archivos modificados ni su contenido.
- **Archivos consultados:** No conocidos por el Gestor.
- **Archivos modificados:** `12-propuesta/` (archivos exactos no declarados al Gestor). **El Gestor no los ha leído, verificado ni modificado**: la ruta está prohibida a su contrato.
- **Comandos o pruebas ejecutadas:** Ninguna declarada al Gestor.
- **Evidencia:** carpeta [12-propuesta](../12-propuesta/) (estado documental no declarado al Gestor; se registra como BORRADOR en este expediente, sin aprobación).
- **Decisiones propuestas o tomadas:** Ninguna tomada. Ver DEC-034 [OPB], CR-001.
- **Riesgos o bloqueos:** El contenido no está revisado por el Gestor frente al expediente (ISS-045). Riesgo de copiar la sección 7 INTERNA de la estimación de la opción B o de mezclar los plazos de 1 semana y de 28 a 36 semanas (ISS-040).
- **Resultado:** No declarado en la información recibida por el Gestor.
- **Siguiente acción recomendada:** El Director revisa la propuesta frente al expediente (TASK-026 [OPB]) y obtiene la aprobación formal del cliente a CR-001 (PEND-044).

### ACT-015 — Persistencia de la estimación de la opción B y actualización del control

- **Fecha:** 2026-10-26 (hora no registrada)
- **Agente:** Gestor de Documentación
- **Objetivo:** Persistir como BORRADOR la estimación de la opción B, registrar CR-001 y actualizar los registros de control.
- **Elementos relacionados:** ACT-013, ACT-014, CR-001, DEC-034 [OPB], PEND-043 a PEND-047 [OPB], TASK-026 [OPB], T1 a T10 [OPB], R-001 a R-008 [OPB], ISS-038 a ISS-045.
- **Tareas realizadas:** Creación de `05-planning/estimacion-opcion-b.md` desde el reporte del Planificador (leído completo; §7 marcada INTERNA). Comprobación aritmética de horas (50–70 h) y de las cifras de §7 (sin discrepancias aritméticas). Registro de CR-001 con análisis de impacto. Actualización de DECISIONS, TASKS, RISKS, TRACEABILITY, APPROVALS (solo nota), CHANGE-REQUESTS, AGENT-ACTIVITY y PROJECT-STATE. **No se leyó ni se escribió en `12-propuesta/`** (ruta prohibida a su contrato). No se registró ninguna aprobación.
- **Archivos consultados:** Los registros existentes de `00-control/`, `05-planning/estimacion-plazo.md` (cabecera) y el reporte del Planificador (archivo temporal de la herramienta).
- **Archivos modificados:** Solo dentro de `projects/alquiler-campers/`, fuera de `12-propuesta/` (lista exacta en el reporte del Gestor al Director).
- **Comandos o pruebas ejecutadas:** No aplica.
- **Evidencia:** [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md), [CHANGE-REQUESTS](CHANGE-REQUESTS.md).
- **Decisiones propuestas o tomadas:** Ninguna. DEC-034 [OPB] se registra como PROPUESTA (elección del usuario [C]); PEND-043 a PEND-047 [OPB] como pendientes. IDs asignados por el Gestor: ACT-013 a ACT-015, CR-001, DEC-034, PEND-043 a PEND-047, TASK-026, ISS-038 a ISS-045 (por confirmar). T1 a T10 y R-001 a R-008 conservan los IDs del reporte con el calificador [OPB].
- **Riesgos o bloqueos:** ISS-038 a ISS-045.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Siguiente acción recomendada:** El Director revisa ISS-038 a ISS-045, decide la variante de la opción B (PEND-046), trata CR-001 con el cliente (PEND-044) y revisa `12-propuesta/` (TASK-026 [OPB]).

---

## Plantilla para una nueva entrada

### ACT-XXX — Título breve

- **Fecha:** YYYY-MM-DD HH:MM zona horaria
- **Agente:**
- **Objetivo:**
- **Elementos relacionados:**
- **Tareas realizadas:**
- **Archivos consultados:**
- **Archivos modificados:**
- **Comandos o pruebas ejecutadas:**
- **Evidencia:**
- **Decisiones propuestas o tomadas:**
- **Riesgos o bloqueos:**
- **Resultado:** COMPLETADO | COMPLETADO_CON_PENDIENTES | BLOQUEADO | NO_INICIADO | CANCELADO
- **Siguiente acción recomendada:**

## Enlaces

[Estado del proyecto](PROJECT-STATE.md) · [Tareas](TASKS.md) · [Riesgos](RISKS.md) · [Decisiones](DECISIONS.md) · [Solicitudes de cambio](CHANGE-REQUESTS.md) · [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md)
