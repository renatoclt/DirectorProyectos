# Tablero de tareas: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Reportes del Analista, del Product Manager, del Diseñador UX/UI, del Arquitecto de Soluciones, del Revisor de Seguridad y del Planificador (plan y estimación de plazo, incluida la opción B) ("Siguiente acción recomendada", "Escalaciones" y desglose de trabajo); instrucciones del Director.

## Estados

`BACKLOG`, `READY`, `IN_PROGRESS`, `BLOCKED`, `IN_REVIEW`, `DONE`, `CANCELLED`.

Una tarea solo puede marcarse `DONE` con evidencia verificable.

**Alcance de este tablero:** en "Trabajo activo" y "Trabajo terminado" solo hay tareas de documentación, diseño y gobierno. Las tareas de implementación, calidad, operaciones y entrega del plan figuran **únicamente en el backlog (§2.1) como BACKLOG, sin asignar y sin autorización**: no existe alcance aprobado, GATE-002 está PENDING y no hay puerta PLANNING → BUILD solicitada. Ninguna puede iniciarse.

**Convención de IDs del plan (ISS-024):** el plan numera sus tareas desde TASK-010. Sus TASK-010, TASK-011 y TASK-012 colisionan con tareas ya registradas por el Gestor y se identifican con el calificador **[PLAN]** (TASK-010 [PLAN], TASK-011 [PLAN], TASK-012 [PLAN]). No se reutilizan IDs. El resto de IDs del plan (TASK-013 en adelante) se conservan sin calificador porque no colisionan. Los IDs TASK-015 a TASK-019 y TASK-025 los asigna el Gestor y el plan no los usa. **Opción B (2026-10-26):** TASK-026 [OPB] lo asigna el Gestor; T1 a T10 conservan los IDs del reporte del Planificador con el calificador **[OPB]** (§2.2). No hay colisión con ningún ID del plan.

## 1. Trabajo activo

| ID | Descripción | Relación | Fase | Prioridad | Responsable | Estado | Dependencias | Archivos o límites | Evidencia | Actualizado |
|---|---|---|---|---|---|---|---|---|---|---|
| TASK-001 | Análisis de negocio: requisitos, reglas, validaciones y preguntas | RF-001 a RF-032, RNF-001 a RNF-014, RN-001 a RN-027 | DISCOVERY (borrador) | — | Analista de Negocio | IN_REVIEW | GATE-001 PENDING | Solo lectura | [requirements.md](../01-discovery/requirements.md) | 2026-10-26 |
| TASK-002 | Definición de MVP, backlog, historias y criterios | HU-001 a HU-036, CA-001 a CA-034 | DISCOVERY/DESIGN (borrador) | — | Product Manager | IN_REVIEW | TASK-001 | Solo lectura | [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) | 2026-10-26 |
| TASK-010 | Especificación UX/UI del MVP (recorridos, pantallas P01 a P21, estados, accesibilidad, propuesta de marca no aprobada) | RF-001 a RF-026 y RF-032, RNF-001 a RNF-005, RNF-013, HU-001 a HU-024, CA-001 a CA-034, ISS-002 | DESIGN (borrador). GATE-002 PENDING y alcance no aprobado: conflicto de contrato devuelto al Director (ACT-004) | — | Diseñador UX/UI | IN_REVIEW | TASK-002; GATE-002 PENDING | Solo lectura (el agente no modificó archivos) | [ux-specification.md](../03-ux/ux-specification.md) | 2026-10-26 |
| TASK-011 | Arquitectura de solución del MVP (ADR-001 a ADR-012, modelo de datos, integraciones, seguridad, despliegue) | RF-001 a RF-032, RNF-001 a RNF-014, RN-001 a RN-027, DEC-029, ISS-002 | DESIGN (borrador). GATE-002 PENDING y alcance no aprobado | — | Arquitecto de Soluciones | IN_REVIEW | TASK-002; GATE-002 PENDING | Solo lectura (el agente no modificó archivos) | [solution-architecture.md](../04-architecture/solution-architecture.md) | 2026-10-26 |
| TASK-015 | Revisión de seguridad **de diseño** (SEG-001 a SEG-017). Estática y documental: no se ejecutó ninguna prueba | ADR-001 a ADR-012, RF-001 a RF-032, SEG-001 a SEG-017 | DESIGN (borrador). GATE-002 PENDING | — | Revisor de Seguridad | IN_REVIEW | TASK-011; GATE-002 PENDING | Solo lectura (el agente no modificó archivos) | [security-review.md](../08-security/security-review.md) | 2026-10-26 |
| TASK-016 | Plan de implementación del MVP (fases, hitos, desglose, riesgos). Sin fechas | RF-001 a RF-032, CA-001 a CA-034, ADR-001 a ADR-012, SEG-001 a SEG-017, B1 a B9 | PLANNING (borrador). Alcance NO aprobado, GATE-002 PENDING y PLANNING → BUILD no solicitada: conflicto devuelto al Director | — | Planificador de Proyecto | IN_REVIEW | TASK-010, TASK-011, TASK-015; GATE-002 PENDING | Solo lectura (el agente no modificó archivos) | [implementation-plan.md](../05-planning/implementation-plan.md) | 2026-10-26 |
| TASK-018 | Estimación preliminar de plazo (Recomendación / a confirmar): ≈63 sp, 28 a 36 semanas desde H0, sin fechas ni costos | TASK-016, H0 a H6, B1 a B9, R-PL-007, R-PL-012, DEC-033, PEND-041, PEND-042 | PLANNING (borrador). Alcance NO aprobado, GATE-002 PENDING; el plazo se cuenta desde H0, que no ha ocurrido | — | Planificador de Proyecto | IN_REVIEW | TASK-016; B1 a B9 (supuestas resueltas en H0); GATE-002 PENDING | Solo lectura (el agente no modificó archivos) | [estimacion-plazo.md](../05-planning/estimacion-plazo.md) | 2026-10-26 |
| TASK-019 | Propuesta comercial del proyecto (README, propuesta-comercial, analisis-consolidado, perfil-empresa, checklist-calidad-propuesta y 13 archivos en `mockups/`), solicitada por el Director por instrucción explícita del usuario | DEC-033, PEND-041, ISS-034, ISS-036, TASK-018 | Propuesta comercial. Alcance NO aprobado | — | Redactor de Propuestas (ejecutado por un agente general bajo su perfil) | IN_REVIEW | TASK-018; confirmación del cliente (PEND-041) | `projects/alquiler-campers/12-propuesta/` (propiedad del Redactor de Propuestas; **fuera del contrato del Gestor**) | [12-propuesta](../12-propuesta/) (18 archivos según el Director; **no verificados por el Gestor**) | 2026-10-26 |
| TASK-026 [OPB] | Revisar la **propuesta actualizada para la opción B** (`12-propuesta/`, actualizada por un agente general bajo el perfil del Redactor de Propuestas por instrucción del usuario; ACT-014) frente a CR-001, DEC-034 [OPB], [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) y al expediente. Verificar que no copie la sección 7 (INTERNA) y que distinga el plazo de 1 semana (opción B) del de 28 a 36 semanas (MVP completo) | CR-001, DEC-034 [OPB], PEND-043, PEND-044, ISS-038 a ISS-040, ISS-045, TASK-019 | Propuesta comercial. Alcance NO aprobado; CR-001 WAITING_FOR_APPROVAL | — | Director de Proyectos (la propuesta es del Redactor de Propuestas) | IN_REVIEW | CR-001 pendiente de aprobación del cliente (PEND-044); TASK-019 | `12-propuesta/` queda **fuera del contrato del Gestor**; el Gestor no la lee ni la modifica | [12-propuesta](../12-propuesta/) (no verificada por el Gestor); [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) | 2026-10-26 |

## 2. Backlog

Tareas derivadas de los pasos recomendados por las fuentes. Ninguna ha sido asignada ni autorizada. El responsable es una **propuesta**.

| ID | Descripción | Relación | Prioridad | Condición para iniciar | Responsable propuesto |
|---|---|---|---|---|---|
| TASK-004 | Confirmar la equivalencia de la lista ISS-001 a ISS-014 y de DEC-001 a DEC-032 con la lista aprobada anteriormente | ISS-001 a ISS-014, DEC-001 a DEC-032 | — | Ninguna | Director de Proyectos |
| TASK-005 | Trasladar al cliente las preguntas Q1 a Q7 del Analista | PEND-001 a PEND-007 | — | Decisión del Director | Director de Proyectos |
| TASK-006 | Solicitar la validación legal de los puntos listados por el Analista | PEND-010 (P-005) | — | Decisión del Director | Director de Proyectos |
| TASK-007 | Reconciliar CA-001 a CA-014 del Analista con los del Product Manager | ISS-001, DEC-030 | — | Ninguna | Director de Proyectos |
| TASK-008 | Resolver las discrepancias de alcance entre Analista y Product Manager | ISS-004 a ISS-011, DEC-029 | — | Respuestas del cliente | Director de Proyectos |
| TASK-009 | Decidir la activación de UX/UI y Seguridad | Carpetas `03-ux/` y `08-security/` vacías | — | Cierre de DISCOVERY según el Director | Director de Proyectos |
| TASK-012 | Revisar y resolver las inconsistencias nuevas entre UX, arquitectura, PM y Analista, sin elegir versión hasta la decisión del Director | ISS-015 a ISS-023 | — | Decisión del Director | Director de Proyectos |
| TASK-017 | Revisar y resolver las inconsistencias nuevas entre seguridad, plan y las demás fuentes (ISS-024 a ISS-033), sin elegir versión hasta la decisión del Director | ISS-024 a ISS-033, PEND-037 a PEND-040 | — | Decisión del Director | Director de Proyectos |
| TASK-025 | Revisar ISS-034 a ISS-037, revisar el contenido de `12-propuesta/` frente al expediente y confirmar con el cliente el uso del plazo estimado (PEND-041), sin elegir versión hasta la decisión del Director | ISS-034 a ISS-037, DEC-033, PEND-041, PEND-042 | — | Decisión del Director | Director de Proyectos |

> Nota del Gestor sobre TASK-009: el Diseñador UX/UI, el Arquitecto de Soluciones y el Revisor de Seguridad ya entregaron borradores (TASK-010, TASK-011, TASK-015) con GATE-002 PENDING. El Gestor no modifica el estado de TASK-009 ni de ninguna puerta. `05-planning/` y `08-security/` contienen cada una un borrador.

### 2.1 Backlog del plan de implementación [PLAN]

Fuente: [implementation-plan.md](../05-planning/implementation-plan.md) ("Desglose de trabajo"). **Estado de todas: BACKLOG, sin asignar y sin autorización.** El responsable es una propuesta del plan. Tamaños S/M/L: esfuerzo relativo, no calendario. **Las dependencias son las del plan**, con IDs del plan (las de forma "TASK-010 [PLAN]" son las del plan, no las de §1). "ARR" = arranque (H0: alcance, plan y decisiones B1-B9 aprobados y BUILD autorizado, que **no ha ocurrido**). TL = TASK-014. Todas requieren además la entrada común del plan: alcance aprobado, UX, arquitectura, SEG y los CA citados. La columna "Relación" la compone el Gestor con los RF, CA, SEG, ADR, B y PEND que el plan menciona en la descripción, el cierre o las fases (no es una columna del plan). La columna "Cierre" es el criterio de cierre específico del plan y exige evidencia verificable.

| ID | Fase del plan | Descripción (objetivo → salida) | Relación | Resp. propuesto | T | Dependencias (plan) | Cierre (evidencia) |
|---|---|---|---|---|---|---|---|
| TASK-010 [PLAN] | P0 | Paquete de decisiones bloqueantes → registro en DECISIONS | B1 a B9, ISS-004 a ISS-011 | DIR | S | TASK-004, TASK-007, TASK-008 | Las 9 decisiones B1-B9 respondidas por escrito |
| TASK-011 [PLAN] | P0 | Formalizar UX, arquitectura y seguridad en `03-ux`, `04-architecture`, `08-security` | ISS-025 | GD | S | GATE-002 | Archivos persistidos y revisados por DIR |
| TASK-012 [PLAN] | P0 | Validación legal (= TASK-006 según el plan) → informe de la asesoría | PEND-010, B4, SEG-010 | Cliente | M | — | Informe sobre RGPD, cookies, IVA, desistimiento y SCA |
| TASK-013 | P0 | Aprobación del plan y solicitud PLANNING → BUILD | APPROVALS | DIR/Humano | S | TASK-010 [PLAN], TASK-011 [PLAN], TASK-014 | Aprobación registrada en APPROVALS |
| TASK-014 | P0 | Stack, convenciones, ADR finales y contratos de API | ADR-001 a ADR-012 | TL | S | GATE-002 | ADR-001 a 012 aprobados o modificados |
| TASK-020 | P1 | Repo, ramas protegidas, CI (lint, test, SCA, secretos, SAST, presupuesto Lighthouse), entorno local | SEG-012, SEG-014 | DO | M | ARR, TASK-014 | CI verde en repo vacío; escaneo de secretos activo |
| TASK-021 | P1 | Esquema y migraciones: `occupancy` con exclusión, reserva, pago, `payment_event`, `consent`, `policy_version`, auditoría, outbox, roles de BD de mínimo privilegio | ADR-003, CA-002, SEG-007, SEG-012 | DAT | L | ARR, TASK-014 | Migraciones con marcha atrás; pruebas de exclusión (CA-002) |
| TASK-022 | P1 | Semillas de ejemplo "por validar", sin datos reales | SEG-012 | DAT | S | TASK-021 | Datos sintéticos; sin PII (SEG-012) |
| TASK-023 | P1 | Esqueleto BE: config por entorno, errores, idempotencia, logs con redacción, cabeceras (CSP, HSTS) | SEG-008, SEG-011 | BE | M | TASK-014, TASK-021 | SEG-008 base y SEG-011 verificados con pruebas |
| TASK-024 | P1 | Sistema de componentes FE con tokens de marca provisionales y accesibilidad base | UX, RNF-005 | FE | M | ARR, UX | Storybook o equivalente; axe sin críticos |
| TASK-030 | P2 | Precio y temporadas en servidor, mínimo de noches, instantánea | RF-004, RF-022, CA-012, CA-017, CA-034 | BE | M | TASK-021, TASK-023 | CA-012, 017, 034 con pruebas unitarias |
| TASK-031 | P2 | Disponibilidad y búsqueda | RF-002, RF-003, CA-001, CA-002, CA-009, CA-015 | BE | M | TASK-021, TASK-023 | CA-001, 002, 009, 015 |
| TASK-032 | P2 | Reserva pendiente, hold, consentimientos versionados, conductor, edad mínima | RF-006, RF-007, CA-003, CA-010, CA-018, CA-033 | BE | M | TASK-030, TASK-031 | CA-003, 010, 018, 033; concurrencia OK |
| TASK-033 | P2 | `PaymentProvider`, adaptador mock y adaptador sandbox, webhook firmado, máquina de estados, idempotencia | RF-008, RF-009, CA-004, CA-006, CA-031, CA-032, SEG-002 | BE | L | TASK-032 | CA-004, 006, 031, 032; SEG-002 en pruebas |
| TASK-034 | P2 | Worker: expiración de holds, pago tardío, conciliación, alineación hold y sesión de pago | RF-032, CA-005, CA-007, SEG-003 | BE | L | TASK-033 | CA-005, 007; SEG-003 con prueba de carrera |
| TASK-035 | P2 | Antiabuso: límites de holds, anti-bot, verificación de email, alertas | SEG-004 | BE | M | TASK-032 | SEG-004 con prueba de abuso en staging |
| TASK-036 | P2 | FE de inicio, catálogo, ficha, resultados, resumen y datos (P01-P06) | CA-015 a CA-018 | FE | M | TASK-024, TASK-030 a TASK-032 o mock | CA-015 a 018; sin saltos de layout |
| TASK-037 | P2 | FE de pago, estado y variantes (P07, P08) con temporizador accesible | CA-004, CA-006 | FE | M | TASK-036, TASK-033 (mock) | CA-004, 006; aviso 2.2.1 |
| TASK-040 | P3 | Outbox, plantillas (confirmación, justificante, avisos de admin) | CA-019, CA-025, SEG-015 | BE | M | TASK-033 | CA-019, 025; SEG-015 |
| TASK-041 | P3 | Consulta código+email, cancelación, política versionada y reembolso | RF-011, RF-013, CA-008, CA-013, CA-020, SEG-001, SEG-005 | BE | L | TASK-033, TASK-034, B3, B5 | CA-008, 013, 020; SEG-001 y SEG-005 con pruebas |
| TASK-042 | P3 | Auth del panel con MFA, sesión, recuperación, CSRF y deny-by-default | RF-019, CA-021, SEG-006, SEG-017 | BE | L | TASK-023, B6 | CA-021; SEG-006 y SEG-017 con pruebas |
| TASK-043 | P3 | API admin (flota, sedes, tarifas, bloqueos, reservas, pagos), auditoría mínima, subida segura de imágenes | RF-020 a RF-025, CA-011, CA-022 a CA-024, SEG-007, SEG-009 | BE | L | TASK-042, TASK-030, TASK-031, TASK-041 | CA-011, 022-024; SEG-007 y SEG-009 |
| TASK-044 | P3 | FE del panel P14-P20 | CA-011, CA-021 a CA-024 | FE | L | TASK-043 | CA-011, 021-024 |
| TASK-045 | P3 | FE de consulta, cancelación, contacto, legales y cookies; SEO técnico y CWV | CA-013, CA-020, CA-026 a CA-029, SEG-016 | FE | L | TASK-041, TASK-024 | CA-013, 020, 026-029; SEG-016 |
| TASK-046 | P3 | Contacto con antispam y registro de consentimiento de cookies | RF-015, RF-017, CA-029 | BE | S | TASK-023 | CA-029; sin cookies no técnicas previas |
| TASK-050 | P4 (puede arrancar en P1) | Plan de pruebas CP con trazabilidad CA a CP | CA-001 a CA-034 | QA | M | TASK-011 [PLAN] | Matriz CA-001 a 034 cubierta |
| TASK-051 | P4 | Pruebas de concurrencia y de pago automatizadas en CI | CA-002, CA-003, SEG-002, SEG-003 | QA | L | TASK-033, TASK-034 | N peticiones, solo una gana; casos de webhook |
| TASK-052 | P4 | E2E, accesibilidad, SEO y CWV | CA-014, CA-028, CA-030 | QA | L | TASK-044, TASK-045, "B-P12" (ID del plan; ver ISS-031) | CA-014, 028, 030 con protocolo acordado |
| TASK-053 | P4 | Revisión de seguridad final de implementación (SEG-001 a SEG-017, DAST) | SEG-001 a SEG-017 | SEC | L | TASK-051, TASK-052 | Informe sin Altas abiertas; veredicto SEC |
| TASK-054 | P4 | Corrección de defectos DEF y retests | DEF | BE/FE | M | TASK-051 a TASK-053 | DEF cerrados con evidencia |
| TASK-060 | P5 | Entornos de staging y producción, secretos, observabilidad, copias cifradas | B1, B2, B8, B9, SEG-012, SEG-013 | DO | L | B1, B2, B8, B9, autorización | Entorno aprovisionado con `noindex` en staging |
| TASK-061 | P5 | Prueba de restauración completa y verificación de RPO/RTO | SEG-013, B8 | DO/QA | M | TASK-060 | Acta de restauración |
| TASK-062 | P5 | Manual de administración y runbook operativo | — | RT | M | TASK-044, TASK-051 | Revisado por QA; cubre pago sin reserva, reembolso fallido, correo no entregado, código perdido |
| TASK-063 | P5 | Pipeline de despliegue con aprobación manual y despliegue autorizado | SEG-014 | DO | S | TASK-053, TASK-060, autorización | Despliegue verificado, solo con autorización específica |
| TASK-064 | P5 | Cliente: datos reales, fotos, textos legales validados | PEND-020, R-008 [PM] | Cliente | M | TASK-012 [PLAN] | Imágenes de ejemplo sustituidas (R-008 [PM]) |
| TASK-065 | P5 | Índice documental y change-log | — | RT/GD | S | P5 | Archivos persistidos |
| TASK-070 | P6 | Auditoría de trazabilidad (RF→HU→CA→TASK→CP→SEG) | [TRACEABILITY](TRACEABILITY.md) | AUD | M | TASK-054 | Informe sin huecos críticos |
| TASK-071 | P6 | Auditoría de entrega y go/no-go | — | AUD | M | TASK-063, TASK-070 | Informe con veredicto |

**Orden de implementación del plan (sin fechas):** P0: TASK-010 [PLAN], TASK-011 [PLAN], TASK-012 [PLAN] (en paralelo), TASK-014, TASK-013. P1: TASK-020, 021, 024 en paralelo; después TASK-022, 023. P2: TASK-030 y 031; luego 032, 033, 034; TASK-035 y 036 en paralelo a 033; TASK-037 tras 036. P3: TASK-040, 041, 042 y 046; después 043, luego 044; TASK-045 en paralelo; TASK-050 puede arrancar en P1. P4: TASK-051 a 054. P5: TASK-060, 061, 062, 064, 063, 065. P6: TASK-070 y 071.

**Ruta crítica (plan):** aprobación de alcance y GATE-002 → decisiones B1-B9 → TASK-014 → TASK-021 → TASK-031/030 → TASK-032 → TASK-033 (adaptador real) → TASK-034 → TASK-041 → TASK-051 → TASK-053 → TASK-061 + validación legal final + TASK-064 → autorización de despliegue → TASK-063. Detalle de lo que puede empezar con dependencias abiertas y de lo que no: ver [implementation-plan.md](../05-planning/implementation-plan.md) "Dependencias críticas" e ISS-027.

### 2.2 Backlog de la entrega inicial acotada (opción B) [OPB]

Fuente: [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) §2 (Planificador, BORRADOR). Los IDs T1 a T10 son los del reporte y llevan el calificador **[OPB]**. **Todas en BACKLOG, sin asignar y sin autorización:** CR-001 está en `WAITING_FOR_APPROVAL`, no existe alcance aprobado, GATE-002 está PENDING y no hay solicitud PLANNING → BUILD. **Ninguna está en DONE.** Horas de 1 persona full-stack (supuesto [S]); tamaños relativos, no un calendario comprometido. Total 50–70 h (valor probable 60 h); "núcleo B" ~38–42 h.

| ID | Descripción | Relación | Prioridad | h (mín–máx) | Dependencias | Responsable propuesto |
|---|---|---|---|---|---|---|
| T1 [OPB] | Arranque, repo, hosting estático, despliegue, base de mockups | CR-001, RNF-002, RNF-003 | — | 4–5 | — | Full-stack (propuesta) |
| T2 [OPB] | Inicio, catálogo, fichas, tarifas, condiciones y contacto (datos en archivo) | RF-001 (parcial), RF-015 (parcial), RN-001 y RNF-010 (desviación) | — | 14–18 | T1 [OPB], contenido del cliente (D1) | Full-stack (propuesta) |
| T3 [OPB] | Responsive, accesibilidad básica, imágenes optimizadas | RNF-001, RNF-003, RNF-004 y RNF-005 (parciales), RNF-013 (parcial) | — | 5–7 | T2 [OPB] | Full-stack (propuesta) |
| T4 [OPB] | SEO base: metadatos, sitemap, robots, datos estructurados, URLs limpias | RF-018 (parcial), RNF-002 | — | 3–4 | T2 [OPB] | Full-stack (propuesta) |
| T5 [OPB] | Legales (borrador desde plantilla) y aviso de cookies | RF-016 (parcial), RF-017 (parcial), RNF-008 (parcial), PEND-010, R-002 [OPB] | — | 4–6 | Datos legales de la empresa | Full-stack (propuesta) |
| T6 [OPB] | Formulario de solicitud: fechas, camper, conductor, privacidad; antispam; correo; fecha y versión de la aceptación en el correo | RF-006 (parcial), RF-010 (parcial), RF-026 (parcial), RN-026 (parcial), RNF-014 (parcial) | — | 8–12 | T1 [OPB], correo de destino | Full-stack (propuesta) |
| T7 [OPB] | Dominio, HTTPS, SPF/DKIM/DMARC | RNF-014 (parcial), R-003 [OPB] | — | 2–3 (+ espera de DNS) | Acceso a DNS | Full-stack (propuesta) |
| T8 [OPB] | QA: móvil, formulario, enlaces, rendimiento | RNF-001, RNF-003, RNF-006 (parcial) | — | 4–6 | T3 a T7 [OPB] | Full-stack (propuesta) |
| T9 [OPB] | Una ronda de ajustes del cliente | CR-001 | — | 3–5 | T8 [OPB], feedback del cliente | Full-stack (propuesta) |
| T10 [OPB] | Publicación y guía de edición de contenido | CR-001, PEND-045 | — | 3–4 | T9 [OPB], aprobación del cliente | Full-stack (propuesta) |

**Ruta crítica (opción B):** contenido del cliente (D1) → T2 → T6, junto con acceso DNS → T7 → T8 → feedback del cliente → T9 → T10. **Condición para iniciar cualquiera (propuesta del Gestor, no del Planificador):** CR-001 APPROVED y autorización explícita del Director; hoy ninguna se cumple. La relación con RF/RNF es la que el Gestor deduce de la descripción de cada tarea y de la cobertura del reporte (§6); el Planificador no la dio por tarea.

## 3. Tareas bloqueadas

| ID | Bloqueo | Impacto | Responsable de desbloquear | Próxima revisión |
|---|---|---|---|---|
| — | Ninguna registrada | — | — | — |

## 4. Trabajo terminado

| ID | Descripción | Relación | Responsable | Fecha | Evidencia | Validado por |
|---|---|---|---|---|---|---|
| TASK-003 | Persistir el expediente inicial y los nueve registros de control como BORRADOR | Gobierno del proyecto | Gestor de Documentación | 2026-10-26 | Los 12 archivos listados en [ACT-003](AGENT-ACTIVITY.md) existen en `projects/alquiler-campers/`. Ver [PROJECT-STATE](PROJECT-STATE.md) §10 | Pendiente de validación del Director |

## 5. Reglas de asignación

- Cada tarea debe relacionarse con al menos un requisito, defecto, riesgo, decisión o solicitud de cambio.
- Define límites de archivos o módulos cuando varios implementadores trabajen en paralelo.
- No asignes el mismo archivo a varios agentes sin una coordinación explícita.
- Registra dependencias antes de iniciar tareas paralelas.

## Enlaces

[Estado del proyecto](PROJECT-STATE.md) · [Actividad de agentes](AGENT-ACTIVITY.md) · [Riesgos](RISKS.md) · [Decisiones](DECISIONS.md) · [Solicitudes de cambio](CHANGE-REQUESTS.md) · [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md)
