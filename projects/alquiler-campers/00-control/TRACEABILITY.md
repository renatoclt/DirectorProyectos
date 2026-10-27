# Matriz de trazabilidad: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** [REQUIREMENTS](REQUIREMENTS.md), [DECISIONS](DECISIONS.md), [requirements.md](../01-discovery/requirements.md), [mvp-and-backlog.md](../02-product/mvp-and-backlog.md), [ux-specification.md](../03-ux/ux-specification.md) (matriz pantalla → requisito), [solution-architecture.md](../04-architecture/solution-architecture.md) (matriz de trazabilidad y ADR), [security-review.md](../08-security/security-review.md) (hallazgos SEG), [implementation-plan.md](../05-planning/implementation-plan.md) (tareas y cierres) y [estimacion-plazo.md](../05-planning/estimacion-plazo.md) (solo mencionada, §10) y [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) (opción B, §3 y §11). Las relaciones se toman de las trazas explícitas de las fuentes.

La trazabilidad debe permitir responder qué se pidió, qué se decidió, qué se construyó, cómo se probó y qué evidencia existe.

**Estado general:** fase de descubrimiento en borrador, con borradores de diseño UX/UI y arquitectura (sin aprobar; GATE-002 PENDING). No hay implementación, pruebas, defectos ni revisión de seguridad. En todas las filas de §1 y §2, las columnas "Implementación", "Pruebas", "Defectos", "Seguridad" y "Evidencia final" valen `—` por esa razón, no por omisión. "Documentación" apunta a los dos documentos fuente originales. **Los vínculos con pantallas (UX) y con ADR (arquitectura) no se mezclan en las tablas de §1 y §2:** están en §6 y §7, tal como los entregan las matrices de los reportes (estado PROPUESTO). Las tareas de implementación no existen (ver [TASKS](TASKS.md)).

## 1. Cobertura de requisitos

Estado de todos los requisitos: **PROPUESTO**. Las decisiones listadas son **PROPUESTAS**, no aprobadas.

| Requisito | Estado | Historia o regla | Diseño o decisión | Tareas | Implementación | Pruebas | Defectos | Seguridad | Documentación | Evidencia final |
|---|---|---|---|---|---|---|---|---|---|---|
| RF-001 | PROPUESTO | HU-001; RNF-013 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-002 | PROPUESTO | HU-002 | DEC-012 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-003 | PROPUESTO | HU-002, HU-003; RN-003 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-004 | PROPUESTO | HU-004; RN-010 | DEC-004 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-005 | PROPUESTO | HU-025; RN-012 | DEC-018 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-006 | PROPUESTO | HU-005; RN-026 | DEC-010, DEC-011 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-007 | PROPUESTO | HU-006; RN-016 | DEC-027 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-008 | PROPUESTO | HU-007; RN-023 | DEC-001, DEC-003 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-009 | PROPUESTO | HU-007; RN-023 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-010 | PROPUESTO | HU-010; RN-018, RN-027 | DEC-007, DEC-023 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-011 | PROPUESTO | HU-011; RN-025 | DEC-005 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-012 | PROPUESTO | HU-011, HU-032; RN-025 | DEC-005, DEC-006 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-013 | PROPUESTO | HU-012; RN-014 | DEC-024, DEC-025 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-014 | PROPUESTO | HU-027 | DEC-020 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-015 | PROPUESTO | HU-013, HU-026 | DEC-019 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-016 | PROPUESTO | HU-014 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-017 | PROPUESTO | HU-014; RN-026 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-018 | PROPUESTO | HU-015; RNF-002 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-019 | PROPUESTO | HU-017 | DEC-014 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-020 | PROPUESTO | HU-018; RN-001 | DEC-028 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-021 | PROPUESTO | HU-019; RN-001 | DEC-012, DEC-028 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-022 | PROPUESTO | HU-020, HU-025; RN-010 | DEC-018 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-023 | PROPUESTO | HU-021; RN-021 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-024 | PROPUESTO | HU-022; RN-003 | DEC-015 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-025 | PROPUESTO | HU-023; RN-022 | — | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-026 | PROPUESTO | HU-024, HU-035 | DEC-022 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-027 | PROPUESTO | HU-029 | DEC-021 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-028 | PROPUESTO | HU-028 | DEC-015 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-029 | PROPUESTO | HU-033 | DEC-016 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-030 | PROPUESTO | HU-034 | DEC-017 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-031 | PROPUESTO | HU-030, HU-031 | DEC-002, DEC-003, DEC-004, DEC-007, DEC-008, DEC-009, DEC-010 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |
| RF-032 | PROPUESTO | HU-009; RN-015 | DEC-027 | — | — | — | — | — | requirements.md; mvp-and-backlog.md | — |

## 2. Cobertura de requisitos no funcionales

Validación, resultado y evidencia no existen. Las medidas son las de la fuente. Las marcadas "pendiente" no tienen valor.

| Requisito | Medida esperada | Diseño | Tareas | Validación | Resultado | Evidencia | Estado |
|---|---|---|---|---|---|---|---|
| RNF-001 | LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 en móvil (protocolo pendiente, PEND-014). CA-014 | — | — | — | — | — | PROPUESTO |
| RNF-002 | Páginas indexables, sin garantía de posicionamiento. CA-028 | — | — | — | — | — | PROPUESTO |
| RNF-003 | Utilizable en móvil, tableta y ordenador. CA-030 | — | — | — | — | — | PROPUESTO |
| RNF-004 | Flujo corto con progreso y errores comprensibles. Métrica [R] sin valor. CA-030 | — | — | — | — | — | PROPUESTO |
| RNF-005 | Objetivo WCAG 2.1 AA (alcance pendiente, PEND-014). CA-030 | — | — | — | — | — | PROPUESTO |
| RNF-006 | Sin almacenar datos de tarjeta. CA-031, CA-021 | — | — | — | — | — | PROPUESTO |
| RNF-007 | Sin doble reserva. CA-003 | — | — | — | — | — | PROPUESTO |
| RNF-008 | Datos mínimos y retención definida. CA-010, CA-018 | — | — | — | — | — | PROPUESTO |
| RNF-009 | Eventos de pago y cambios de estado registrados. CA-024, CA-004, CA-032 | — | — | — | — | — | PROPUESTO |
| RNF-010 | Configuración sin cambios de código. CA-011 | — | — | — | — | — | PROPUESTO |
| RNF-011 | Pendiente (PEND-015) | — | — | — | — | — | PROPUESTO |
| RNF-012 | Pendiente (PEND-015, PEND-021) | — | — | — | — | — | PROPUESTO |
| RNF-013 | Imágenes de ejemplo sustituibles sin desarrollo. CA-011 | — | — | — | — | — | PROPUESTO |
| RNF-014 | Entregabilidad de correo. CA-019 | — | — | — | — | — | PROPUESTO |

## 3. Cambios y su impacto

| Solicitud | Requisitos afectados | Decisiones | Tareas | Pruebas | Documentación | Estado |
|---|---|---|---|---|---|---|
| CR-001 | Cubiertos, parciales y no cubiertos por la opción B: ver [§11](#11-alcance-de-la-opción-b-cr-001-rf-rnf-y-rn). Desviación de RN-001 y RNF-010 | DEC-034 [OPB], PEND-043 a PEND-047 | T1 a T10 [OPB] (BACKLOG), TASK-026 [OPB] (IN_REVIEW) | Solo T8 [OPB] (QA de la entrega B); sin pruebas ejecutadas | [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md), [CHANGE-REQUESTS](CHANGE-REQUESTS.md) | WAITING_FOR_APPROVAL |

## 4. Resumen verificable

Conteos tomados de [REQUIREMENTS](REQUIREMENTS.md), [DECISIONS](DECISIONS.md), [RISKS](RISKS.md) y [TASKS](TASKS.md) a fecha 2026-10-26.

| Métrica | Cantidad | Observación |
|---|---:|---|
| Requisitos funcionales registrados (PROPUESTO) | 32 | RF-001 a RF-032 |
| Requisitos no funcionales registrados (PROPUESTO) | 14 | RNF-001 a RNF-014 |
| Reglas de negocio registradas (PROPUESTO) | 27 | RN-001 a RN-027 |
| Historias de usuario registradas | 36 | HU-001 a HU-036 (24 MVP, 12 Fase 2) |
| Criterios de aceptación del Product Manager | 34 | CA-001 a CA-034, con ISS-001 sin resolver |
| Criterios de aceptación del Analista | 14 | CA-001 a CA-014, mismos IDs, distinto contenido en 2 casos |
| Requisitos aprobados | 0 | Sin alcance aprobado |
| Requisitos con tareas | 0 | Sin planificación |
| Requisitos implementados | 0 | BUILD no solicitado |
| Requisitos validados | 0 | — |
| Tareas terminadas con evidencia | 1 | TASK-003 (documentación) |
| Defectos abiertos | 0 | No hay QA |
| Hallazgos de seguridad abiertos | 17 | SEG-001 a SEG-017, todos OPEN, de una **revisión de diseño sin pruebas ejecutadas**. No hay revisión de implementación. Esto no indica que el sistema sea seguro |
| Decisiones propuestas | 32 | DEC-001 a DEC-032, ninguna aprobada |
| Decisiones de arquitectura propuestas | 12 | ADR-001 a ADR-012, ninguna aprobada |
| Impedimentos abiertos | 45 | ISS-001 a ISS-045 (ISS-015 a ISS-023 numeración confirmada por el Director; ISS-024 a ISS-045 nuevas, sin revisar; ISS-038 a ISS-045 de la opción B) |
| Pendientes de confirmación abiertos | 47 | PEND-001 a PEND-047 (PEND-025 a PEND-036 confirmados; PEND-037 a PEND-047 nuevos, numerados por el Gestor; PEND-043 a PEND-047 [OPB]) |
| Decisiones propuestas (propuesta comercial y plazo) | 1 | DEC-033, pendiente de confirmación del cliente (PEND-041). Se suma a DEC-001 a DEC-032 (33 en total, ninguna aprobada) |
| Decisiones propuestas (opción B) | 1 | DEC-034 [OPB], elección del usuario, pendiente de aprobación del cliente (CR-001, PEND-044). Total DEC-001 a DEC-034: 34, ninguna aprobada |
| Solicitudes de cambio | 1 | CR-001, WAITING_FOR_APPROVAL (ninguna aprobada) |
| Tareas de la opción B en BACKLOG | 10 | T1 a T10 [OPB] ([TASKS](TASKS.md) §2.2). Más TASK-026 [OPB] en IN_REVIEW. Ninguna en DONE |
| Riesgos de la opción B | 8 | R-001 a R-008 [OPB], todos OPEN ([RISKS](RISKS.md) §6) |
| Decisiones bloqueantes de BUILD según el plan | 9 | B1 a B9, todas pendientes ([DECISIONS](DECISIONS.md) §4) |
| Tareas del plan en BACKLOG | 38 | TASK-010 [PLAN] a TASK-071 (sin asignar, sin autorización, [TASKS](TASKS.md) §2.1) |
| Riesgos del plan registrados | 12 | R-PL-001 a R-PL-012, todos OPEN (R-PL-012 añadido con la estimación de plazo) |
| Pantallas diseñadas (borrador) | 21 | P01 a P21 en [ux-specification.md](../03-ux/ux-specification.md). P21 no es una pantalla: es un campo de configuración |
| Riesgos de experiencia y técnicos registrados | 22 | R-UX-01 a R-UX-10 y R-ARQ-01 a R-ARQ-12, todos OPEN y sin evaluar |

## 5. Elementos huérfanos

| Tipo | ID | Problema | Acción necesaria |
|---|---|---|---|
| Requisito | RF-001 a RF-032, RNF-001 a RNF-014 | Sin tareas ni pruebas | Esperado en DISCOVERY. Resolver en PLANNING |
| Criterio | CA-033 | La fuente lo marca "decisión del Director" y no traza a un RF o RN | Confirmar su origen (DEC-012) |
| Historia | HU-030, HU-031, HU-036 | Origen "Decisión del Director" sin un RF de origen. RF-031 cubre las dos primeras como ampliación (ISS-004) | Decidir (DEC-002, DEC-007, DEC-013) |
| Criterio | CA-001 a CA-014 | Mismo ID con contenido distinto entre fuentes | Reconciliar (ISS-001, DEC-030) |
| Riesgo | R-001 a R-010 | IDs duplicados entre AN y PM | Calificador [AN]/[PM] provisional (ISS-003, DEC-031) |
| Requisito | RF-012, RF-013, RF-015, RF-026 | Resumen del PM difiere del AN en alcance o prioridad | Ver ISS-002, ISS-007, ISS-008, ISS-010 |
| Requisito | RF-023, RN-017, RN-020, RN-024 | No aparecen citados en la matriz de trazabilidad del Arquitecto (RF-023 sí está cubierto por UX, P15) | Confirmar cobertura (ISS-020) |
| Criterio | CA-001 a CA-014 | UX y arquitectura los citan sin indicar de cuál versión (AN o PM) | Reconciliar (ISS-001, ISS-023, DEC-030) |
| Requisito | RF-001 a RF-032, RNF-001 a RNF-014 | Hay tareas del plan en BACKLOG, pero **sin autorización**: ningún requisito tiene tarea asignada ni aprobada | Esperado. Requiere alcance aprobado, GATE-002 y PLANNING → BUILD |
| Tarea | TASK-010 [PLAN], TASK-011 [PLAN], TASK-012 [PLAN] | El ID colisiona con tareas ya registradas (TASK-010, TASK-011, TASK-012). TASK-012 [PLAN] duplica TASK-006 según el plan | Decisión del Director (ISS-024) |
| Tarea | TASK-062, TASK-065, TASK-071 | El plan no les asigna RF, CA ni SEG propios | Aceptable por su tipo (manual, índice, auditoría). Confirmar |
| Hallazgo | SEG-004 a SEG-007, SEG-009 a SEG-013, SEG-016 | El Revisor no los vincula a un ADR concreto (solo a RF, RN, DEC o a la arquitectura en general; SEG-006 cita "ADR RF-019" sin número) | Confirmar cobertura arquitectónica de cada control |
| Hallazgo | SEG-014 | Sin RF, RN, ADR ni DEC asociados (cadena de suministro, CI) | Confirmar origen del requisito |
| Decisión | B1 a B9 | Prefijo B- fuera del catálogo de identificadores (ISS-013) | Decisión del Director (DEC-032, ISS-031) |

## 6. Pantallas (UX) → requisitos, historias y criterios

Fuente: [ux-specification.md](../03-ux/ux-specification.md) §14, transcrita sin cambios. Estado: BORRADOR. P21 no es una pantalla (campo de configuración del correo de aviso, ubicación [P], PEND-027). Los CA se citan como en la fuente (ver ISS-023).

| Pantalla | RF | HU | CA |
|---|---|---|---|
| P01 Inicio | RF-002, 018 | HU-001, 002, 015 | CA-028 |
| P02 Catálogo / P03 Ficha | RF-001, 003 | HU-001, 003 | CA-016 |
| P04 Resultados | RF-002, 003 | HU-002, 003 | CA-001, 009, 015 |
| P05 Resumen | RF-004 | HU-004 | CA-017, 034 |
| P06 Datos conductor | RF-006 | HU-005 | CA-010, 018 |
| P07 Pago | RF-007, 008, 009 | HU-006, 007 | CA-003, 006, 031 |
| P08 Estado y confirmación | RF-010, 032 | HU-008, 009, 010 | CA-004, 005, 007, 019 |
| P09 Consulta | RF-011, 012 | HU-011 | CA-013, 020 |
| P10 Cancelación | RF-013 | HU-012 | CA-008 |
| P11 Contacto | RF-015 | HU-013 | CA-029 |
| P12 Legales / P13 Cookies | RF-016, 017 | HU-014 | CA-026, 027 |
| P14 Acceso admin | RF-019 | HU-017 | CA-021 |
| P15 Reservas admin | RF-023 | HU-021 | CA-022, 032 |
| P16 Flota / P17 Sedes | RF-020, 021 | HU-018, 019 | CA-011, 033 |
| P18 Tarifas | RF-022 | HU-020 | CA-012, 034 |
| P19 Bloqueos | RF-024 | HU-022 | CA-023, 002 |
| P20 Pagos y reembolsos | RF-025 | HU-023 | CA-024 |
| P21 Aviso admin | RF-026 | HU-024 | CA-025 |
| Transversal | RNF-001 a 005 | HU-015, 016 | CA-014, 030 |

El UX también cita RNF-013 (panel de flota, rendimiento visual) y VAL-001 a VAL-022 en el texto de las pantallas. RF-005, RF-014 y RF-027 a RF-031 están fuera del MVP del PM y el UX solo los menciona como notas de Fase 2 (§13).

## 7. Arquitectura (ADR y módulos) → RF, RNF y RN

Fuente: [solution-architecture.md](../04-architecture/solution-architecture.md) "Trazabilidad con RF, RNF y RN", transcrita sin cambios. Estado: BORRADOR (los ADR son PROPUESTA, ver [DECISIONS](DECISIONS.md) §2).

| Elemento | Cubierto por |
|---|---|
| RF-001, RF-018, RNF-001, RNF-002 | ADR-010, SEO técnico, módulo Catálogo |
| RF-002, RF-003, RF-007, RF-024, RF-032, RN-003, RN-016, RNF-007 | ADR-003, módulo Disponibilidad |
| RF-004, RF-022, RN-007 a RN-010 | Módulo Tarifas, instantánea de precio |
| RF-006, RN-026, RNF-008 | Políticas, `consent`, privacidad |
| RF-008, RF-009, RN-013 (MVP), RN-022, RN-023, RNF-006, RNF-009 | ADR-004 a ADR-006 |
| RF-013, RF-025, RN-014, RN-019 | ADR-008, `refund` |
| RN-015 | ADR-007 |
| RF-010, RF-026, RN-018, RN-027, RNF-014 | ADR-009 (justificante en el MVP, factura en Fase 2) |
| RF-011, RF-012, RN-025 | ADR-011 |
| RF-019 a RF-021, RN-001, RNF-010, RNF-013 | Módulo Admin, almacén de imágenes |
| RF-015 (contacto), RF-016, RF-017 | Contacto, legales y cookies |
| RN-021, RN-002, RN-005, RN-006 | Estados, modelo de reserva, `Europe/Madrid` |
| RNF-003 a RNF-005 | Frontend responsive y accesible. Validación con QA |
| RNF-011, RNF-012 | **Sin cifras (PEND-015)**. Recomendaciones de copia y escalado |

### 7.1 Vista inversa ADR → elementos (derivada de la tabla anterior y de los textos de los ADR)

| ADR | Elementos que cita la fuente |
|---|---|
| ADR-001 | Sin fila propia en la matriz (estilo general del sistema) |
| ADR-002 | Sin fila propia en la matriz (base de datos transaccional) |
| ADR-003 | RF-002, RF-003, RF-007, RF-024, RF-032, RN-003, RN-016, RNF-007. El texto del ADR cita además RN-004 |
| ADR-004 | RF-008, RF-009, RN-013 (MVP), RN-022, RN-023, RNF-006, RNF-009 (junto con ADR-005 y ADR-006). Cita PEND-012 |
| ADR-005 | Igual que ADR-004. Cita RNF-006 |
| ADR-006 | Igual que ADR-004. Cita RNF-009 |
| ADR-007 | RN-015. El texto del ADR cita CA-007 |
| ADR-008 | RF-013, RF-025, RN-014, RN-019. Cita ISS-002, DEC-025 y PEND-010 |
| ADR-009 | RF-010, RF-026, RN-018, RN-027, RNF-014 |
| ADR-010 | RF-001, RF-018, RNF-001, RNF-002 |
| ADR-011 | RF-011, RF-012, RN-025. La sección de autenticación de la fuente cita además CA-013 |
| ADR-012 | Sin fila propia en la matriz. Cubre las divergencias ISS-004 a ISS-011 con puntos de extensión (cuentas, depósito + saldo, extras, otras sedes, roles, multi-idioma, auditoría RF-029). Ver ISS-020 |

## 8. Seguridad (hallazgos SEG) → ADR, RF, RN y requisitos

Fuente: [security-review.md](../08-security/security-review.md) (columna "Ubicación") y [RISKS](RISKS.md) §4. Las referencias son las que cita el Revisor en su columna "Ubicación" o en el texto del hallazgo; la columna "Relación" de RISKS §4 añade vínculos del Gestor a registros del proyecto. Estado de los hallazgos: **OPEN**. Revisión de diseño, ninguna prueba ejecutada.

| Hallazgo | Sev. | ADR / diseño | RF, HU, RN, RNF, VAL, DEC citados | Tareas del plan que lo cierran (según el plan) |
|---|---|---|---|---|
| SEG-001 | Alta | ADR-011 | RN-025, DEC-005, HU-012 (CA-013 en la verificación) | TASK-041 |
| SEG-002 | Alta | ADR-005, ADR-006 | RN-023, VAL-018 (CA-004 en la verificación) | TASK-033 |
| SEG-003 | Alta | ADR-003, ADR-007, R-ARQ-02, R-ARQ-03 | (CA-002, CA-003, CA-007 en la verificación) | TASK-034 |
| SEG-004 | Alta | — | RF-007, RN-016, VAL-016, RN-018 | TASK-035 |
| SEG-005 | Alta | — | RF-013, RF-025, DEC-024, HU-023, VAL-020 (ISS-002, DEC-025) | TASK-041, TASK-043 |
| SEG-006 | Alta | — | RF-019, HU-017, DEC-014 | TASK-042 |
| SEG-007 | Alta | — | DEC-016, RF-029, RNF-009 | TASK-043 |
| SEG-008 | Media | ADR-010 | — | TASK-023 (base) |
| SEG-009 | Media | — | RF-020, VAL-022, RNF-013 | TASK-043 |
| SEG-010 | Alta (validar legal) | — | RN-026, RNF-008, PEND-010 (VAL-011) | TASK-053 con B4 y B7 |
| SEG-011 | Media | — | (RGPD, observabilidad) | TASK-023 |
| SEG-012 | Media | — | (secretos, entornos, despliegue) | TASK-020, TASK-022, TASK-021 |
| SEG-013 | Media | — | RNF-011 | TASK-060, TASK-061 |
| SEG-014 | Media | — | (despliegue, CI) | TASK-020, TASK-063 |
| SEG-015 | Media | ADR-009 | VAL-009, RN-018 | TASK-040 |
| SEG-016 | Media | — | RF-017, RF-015 | TASK-045 |
| SEG-017 | Baja | ADR-004 | RF-019 | TASK-042 |

Las tareas de la última columna son las que el plan cita al cerrar cada SEG (TASK-023, 033, 034, 035, 040, 041, 042, 043, 045, 053, 060 a 063); en los casos de SEG-012 y SEG-014 se infieren de la descripción de las tareas de repo, CI y esquema. Ver ISS-026 sobre el momento de cierre.

## 9. Tareas del plan → RF, CA y SEG

Fuente: [implementation-plan.md](../05-planning/implementation-plan.md) "Desglose de trabajo" (columna "Cierre") y [TASKS](TASKS.md) §2.1. Estado de todas: BACKLOG, sin autorización. Los CA se citan como en el plan (ver ISS-023). Las tareas de P0, de documentación, de operación y de auditoría sin RF/CA/SEG propios no figuran.

| Tarea (plan) | RF / pantallas | CA | SEG |
|---|---|---|---|
| TASK-021 | — (esquema de datos, ADR-003) | CA-002 | (SEG-007, SEG-012 en la descripción) |
| TASK-022 | — | — | SEG-012 |
| TASK-023 | — | — | SEG-008, SEG-011 |
| TASK-030 | RF-004, RF-022 (precio y temporadas) | CA-012, CA-017, CA-034 | — |
| TASK-031 | RF-002, RF-003 (disponibilidad y búsqueda) | CA-001, CA-002, CA-009, CA-015 | — |
| TASK-032 | RF-006, RF-007 (reserva, hold, consentimientos, conductor) | CA-003, CA-010, CA-018, CA-033 | — |
| TASK-033 | RF-008, RF-009 (pago, webhook) | CA-004, CA-006, CA-031, CA-032 | SEG-002 |
| TASK-034 | RF-032 (pago tardío, expiración) | CA-005, CA-007 | SEG-003 |
| TASK-035 | RF-007 (antiabuso) | — | SEG-004 |
| TASK-036 | P01 a P06 | CA-015 a CA-018 | — |
| TASK-037 | P07, P08 | CA-004, CA-006 | — |
| TASK-040 | RF-010, RF-026 (correo) | CA-019, CA-025 | SEG-015 |
| TASK-041 | RF-011, RF-013 (consulta, cancelación) | CA-008, CA-013, CA-020 | SEG-001, SEG-005 |
| TASK-042 | RF-019 (auth del panel) | CA-021 | SEG-006, SEG-017 |
| TASK-043 | RF-020 a RF-025 (API admin) | CA-011, CA-022, CA-023, CA-024 | SEG-007, SEG-009 |
| TASK-044 | P14 a P20 | CA-011, CA-021 a CA-024 | — |
| TASK-045 | P09, P10, P11, P12, P13 | CA-013, CA-020, CA-026 a CA-029 | SEG-016 |
| TASK-046 | RF-015, RF-017 | CA-029 | — |
| TASK-050 | — | CA-001 a CA-034 | — |
| TASK-051 | — | CA-002, CA-003 (plan de validación) | (SEG-002, SEG-003 en la descripción) |
| TASK-052 | — | CA-014, CA-028, CA-030 | — |
| TASK-053 | — | — | SEG-001 a SEG-017 |
| TASK-060, TASK-061 | — | — | (SEG-012, SEG-013; B1, B2, B8, B9) |
| TASK-063 | — | — | (SEG-014 en el plan de CI) |

Los RF y pantallas de esta tabla los asigna el Gestor a partir de la descripción de cada tarea y de la matriz pantalla → requisito del UX (§6); el plan solo cita CA y SEG. Los valores entre paréntesis son inferencias de esa descripción, no citas literales del plan. Ver ISS-020 y ISS-023.

## 10. Documentos complementarios (sin cambios en los vínculos)

Estos documentos se mencionan para que no queden fuera de la trazabilidad. **No se modifica ningún vínculo de las secciones 1 a 9.**

| Documento | Relación | Estado |
|---|---|---|
| [estimacion-plazo.md](../05-planning/estimacion-plazo.md) | Estimación preliminar de plazo (≈63 sp; rango recomendado 28 a 36 semanas desde H0). Se apoya en las tareas, hitos (H0 a H6) y riesgos del plan ([§9](#9-tareas-del-plan--rf-ca-y-seg)) y en R-PL-012. Ver TASK-018, DEC-033, PEND-041 | BORRADOR. Estimación a confirmar |
| [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) | Estimación de la entrega inicial acotada (opción B): T1 a T10 [OPB], R-001 a R-008 [OPB], cobertura de requisitos ([§11](#11-alcance-de-la-opción-b-cr-001-rf-rnf-y-rn)). Su sección 7 es INTERNA. Ver CR-001, DEC-034 [OPB], TASK-026 [OPB] | BORRADOR. Estimación a confirmar. CR-001 WAITING_FOR_APPROVAL |
| `12-propuesta/` (propuesta comercial y mockups) | Entregable añadido por DEC-033. Creado por el Redactor de Propuestas fuera del contrato del Gestor. **El Gestor no la ha leído ni vinculado a RF, HU, CA, ADR ni SEG**; su coherencia con el expediente está sin verificar (ISS-036). Ver TASK-019 | Estado no declarado al Gestor. Sin aprobación |

## 11. Alcance de la opción B (CR-001): RF, RNF y RN

Fuente: [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) §6 (clasificación del Planificador; el Gestor no la contrastó con el texto completo de cada requisito). **CR-001 está en `WAITING_FOR_APPROVAL`: esta tabla no modifica el alcance ni el estado de ningún requisito (siguen PROPUESTO).** Las tablas de §1 y §2 no se alteran. Las tareas citadas son T1 a T10 [OPB] ([TASKS](TASKS.md) §2.2), en BACKLOG; la relación con tareas la deduce el Gestor de la descripción de cada tarea. Implementación, pruebas y evidencia final: `—`.

| Requisito | Cobertura en la opción B | Alcance en B (según el Planificador) | Tareas [OPB] | Observación |
|---|---|---|---|---|
| RNF-001 | **Cubre** (objetivo, sin garantía) | Rendimiento como objetivo | T3, T8 | Sin garantía de Core Web Vitals reales |
| RNF-002 | **Cubre** | SEO técnico | T4 | Sin garantía de posicionamiento (R-005 [OPB]) |
| RNF-003 | **Cubre** | Responsive | T3, T8 | — |
| RF-001 | Parcial | Catálogo sin gestión en panel | T2 | Desvía RN-001 y RNF-010 |
| RF-006 | Parcial | Solicitud, sin resumen ni pago | T6 | — |
| RF-010 | Parcial | Aviso por correo, sin justificante | T6 | — |
| RF-015 | Parcial | Contacto; el FAQ ya estaba en Fase 2 | T2 | — |
| RF-016 | Parcial | Legales como borrador | T5 | "Borrador a validar" (PEND-010, R-002 [OPB]) |
| RF-017 | Parcial | Banner informativo, sin categorías | T5 | Sin analítica |
| RF-018 | Parcial | SEO base | T4 | — |
| RF-026 | Parcial | Aviso por solicitud, no por reserva ni cancelación | T6 | — |
| RN-026 | Parcial | Fecha y versión solo en el correo | T6 | — |
| RNF-004, RNF-005, RNF-006, RNF-008, RNF-013, RNF-014 | Parcial | Accesibilidad solo básica, sin auditoría AA | T3, T5, T6, T7, T8 | El Planificador no detalla cada RNF |
| RF-002 a RF-005 | **No cubre** | Búsqueda, disponibilidad, precio y extras | — | Fase siguiente |
| RF-007 a RF-009 | **No cubre** | Bloqueo y pago | — | Fase siguiente |
| RF-011 a RF-013 | **No cubre** | Consulta, código y cancelación | — | Fase siguiente |
| RF-019 a RF-025 | **No cubre** | Panel | — | Fase siguiente |
| RF-032 | **No cubre** | Expiración de reservas | — | Fase siguiente |
| RN-003, RN-010 | **No cubre** | Sin solapes y precio calculado en servidor | — | Fase siguiente |
| RNF-007, RNF-009, RNF-010, RNF-011 | **No cubre** | — | — | RNF-010: desviación |
| RN-001, RNF-010 | **Desviación [C]** | Flota y sedes por contenido editado por el proveedor, sin panel | T2, T10 | Requiere aprobación del cliente (PEND-044, PEND-045; ISS-039) |
| RF-014, RF-027 a RF-031, RNF-012 | **Sin clasificar** | No clasificados por el Planificador | — | ISS-042 |

Seguridad: SEG-001 a SEG-007 y SEG-010 se difieren a la fase del pago y del panel; siguen aplicando la seguridad del formulario (antispam, validación, cabeceras) y el RGPD (ISS-043). **No hay hallazgos de seguridad nuevos de la opción B**: ninguno de los 17 SEG se modifica.

## Enlaces

[Estado del proyecto](PROJECT-STATE.md) · [Requisitos](REQUIREMENTS.md) · [Decisiones](DECISIONS.md) · [Tareas](TASKS.md) · [Riesgos e impedimentos](RISKS.md) · [Cambios](CHANGE-REQUESTS.md) · [requirements.md](../01-discovery/requirements.md) · [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) · [ux-specification.md](../03-ux/ux-specification.md) · [solution-architecture.md](../04-architecture/solution-architecture.md) · [security-review.md](../08-security/security-review.md) · [implementation-plan.md](../05-planning/implementation-plan.md) · [estimacion-plazo.md](../05-planning/estimacion-plazo.md) · [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md)