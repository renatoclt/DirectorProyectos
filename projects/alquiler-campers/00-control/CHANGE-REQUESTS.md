# Solicitudes de cambio: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) (reporte del Planificador sobre la opción B), instrucción del usuario del 2026-10-26 trasladada al Gestor, [REQUIREMENTS](REQUIREMENTS.md), [estimacion-plazo.md](../05-planning/estimacion-plazo.md); plantilla `templates/project-control/CHANGE-REQUESTS.md`; [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) (escalaciones).

Una solicitud no modifica el alcance hasta quedar `APPROVED` y estar vinculada a requisitos y tareas actualizados.

## Estados

`DRAFT`, `UNDER_ANALYSIS`, `WAITING_FOR_APPROVAL`, `APPROVED`, `REJECTED`, `IMPLEMENTED`, `CANCELLED`.

## 1. Solicitudes activas

| ID | Fecha | Solicitante | Tipo | Descripción | Motivo | Impacto preliminar | Estado | Decisión requerida | Evidencia |
|---|---|---|---|---|---|---|---|---|---|
| CR-001 | 2026-10-26 | Usuario (instrucción al Director de Proyectos) | Alcance, plazo y precio | **Sustituir el MVP completo por una entrega inicial acotada (opción B) con plazo objetivo de 1 semana y valor de 400 USD; pago en línea, disponibilidad automática, panel, cuentas y la seguridad asociada pasan a la fase siguiente** | El usuario eligió la opción B, un plazo objetivo de 1 semana y el valor de 400 USD [C]. Hay margen de negociación en la propuesta (sin cifra) | Ver §2. Cubre 3 RNF, cubre parcialmente 8 RF, 6 RNF y RN-026, y no cubre 18 RF, RN-003, RN-010 y 4 RNF. Desvía RN-001 y RNF-010 (confirmados [C]) | **WAITING_FOR_APPROVAL** (solicitado por el usuario; **pendiente de aprobación formal del cliente**, PEND-044). No aprobada: no modifica el alcance | Aprobación o rechazo del cliente de España, vía Director. Moneda e IVA (PEND-043) | [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md); instrucción del usuario 2026-10-26; DEC-034 [OPB] |

**Aclaración sobre los plazos (ISS-040):** el **MVP completo** (28 a 36 semanas desde H0, [estimacion-plazo.md](../05-planning/estimacion-plazo.md), DEC-033) **sigue vigente como fase siguiente**. El plazo objetivo de **1 semana** corresponde a la **entrega inicial acotada** (opción B). Son **alcances distintos**: los dos plazos no se comparan ni se suman sin precisar qué incluye cada uno. CR-001 no sustituye ni anula DEC-033.

**Por qué el alcance sigue sin aprobación:** CR-001 está en `WAITING_FOR_APPROVAL`; GATE-001 y GATE-002 siguen PENDING y no hay solicitud PLANNING → BUILD ([APPROVALS](APPROVALS.md)). Las diferencias de alcance entre el Analista y el Product Manager siguen en [RISKS](RISKS.md) §2 (ISS-004 a ISS-011) y [DECISIONS](DECISIONS.md) (DEC-029).

**Aviso del Product Manager (fuente):** si los extras (RF-005) se necesitaran en la salida inicial, "movería RF-005 al MVP y ampliaría el alcance, por lo que sería una solicitud de cambio" (P-009). CR-001 es la primera solicitud registrada. Los cambios de alcance que exige seguridad para el MVP completo (MFA, auditoría mínima, VAL-020, segundo factor; R-PL-002, ISS-029) **siguen sin CR** (el Gestor no recibió instrucción).

## 2. Análisis de impacto

### CR-001 (análisis preliminar del Gestor, a partir del reporte del Planificador; BORRADOR)

| Cambio | Requisitos | Arquitectura y datos | Seguridad | Tareas | Pruebas | Operación | Documentación | Riesgos | Recomendación |
|---|---|---|---|---|---|---|---|---|---|
| CR-001 | **Cubiertos:** RNF-001 (objetivo, sin garantía), RNF-002, RNF-003. **Parciales:** RF-001, RF-006, RF-010, RF-015, RF-016, RF-017, RF-018, RF-026, RN-026, RNF-004, RNF-005, RNF-006, RNF-008, RNF-013, RNF-014. **No cubiertos:** RF-002 a RF-005, RF-007 a RF-009, RF-011 a RF-013, RF-019 a RF-025, RF-032, RN-003, RN-010, RNF-007, RNF-009, RNF-010, RNF-011. **Sin clasificar por el Planificador:** RF-014, RF-027 a RF-031 (Fase 2/ampliaciones) y RNF-012 (ISS-042). **Desviación:** RN-001 y RNF-010 | Sitio estático con función para el formulario, sin base de datos propia (el formulario por servicio de correo o función serverless, sin almacenamiento propio). **El Planificador no revisó 04-architecture**: la compatibilidad con ADR-001/ADR-002 queda por verificar (PEND-047, R-007 [OPB], ISS-044) | SEG-001 a SEG-007 y SEG-010 se **difieren a la fase del pago y del panel** (dependen de código + email, webhook, concurrencia, reembolsos, MFA, auditoría). **Siguen aplicando** la seguridad del formulario (antispam, validación, cabeceras) y el **RGPD** (datos del conductor, aceptación de privacidad, fecha y versión en el correo). SEG-010 está marcado "validar legal"; no se resuelve (ISS-043) | T1 a T10 [OPB] (50–70 h; "núcleo B" ~38–42 h) en [TASKS](TASKS.md). Las 38 tareas del plan (TASK-010 [PLAN] a TASK-071) del MVP completo no se modifican | T8 [OPB]: QA de móvil, formulario, enlaces y rendimiento. Sin auditoría de accesibilidad AA ni garantía de Core Web Vitals. No hay plan de pruebas CP/CA para B | Hosting, dominio y correo de terceros y sus costos los asume el cliente. Sin mantenimiento posterior. Una sola ronda de cambios | [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) (creado). Quedan por revisar si proceden: [REQUIREMENTS](REQUIREMENTS.md), [TRACEABILITY](TRACEABILITY.md) (actualizada con el alcance B), `12-propuesta/` (fuera del contrato del Gestor, ISS-045) | R-001 a R-008 [OPB] (ver [RISKS](RISKS.md) §6). R-006 [OPB]: sin margen, cualquier retraso rompe la semana. R-007 [OPB]: rehacer la parte pública al migrar. ISS-038 a ISS-045 | El Gestor no elige. Del Planificador: comprometer en 1 semana la **entrega a revisión** y la publicación en D8–D10; alternativas: B completa en 1,5–2,5 semanas o 2 personas |

**Desviación de requisitos confirmados [C]:** RN-001 ("flota y sedes son datos configurables desde el panel") y RNF-010 ("flota, sedes, tarifas y políticas editables sin cambios de código") son [C] del cliente. En la opción B flota y sedes se gestionan por **contenido editado por el proveedor** (archivos de datos) y el panel pasa a la fase siguiente. Si el cliente debe editar solo, hace falta un CMS ligero (+1–2 días) o pasa a la fase siguiente (PEND-045). No se cambia el texto de RN-001 ni de RNF-010; la desviación es a confirmar (PEND-044, ISS-039).

**Plazos de alcances distintos:** 28 a 36 semanas = MVP completo desde H0 (fase siguiente, vigente). 1 semana = entrega inicial acotada B (entrega a revisión; publicación D7–D10 según DNS y aprobación). Condiciones del plazo de 1 semana (todas necesarias): dedicación del 100 % o 1 persona más apoyo parcial de 15–20 h; contenido del cliente el D1; acceso a DNS y hosting el D1–D2; feedback en ≤ 1 día hábil; hosting estático con función para el formulario.

**Pasa a la fase siguiente:** pago en línea, disponibilidad automática, panel de administración, cuentas, reembolsos, MFA y auditoría, y la seguridad asociada.

**Precio:** el valor de 400 USD lo fijó el usuario [C]; moneda de facturación e IVA pendientes (PEND-043). La aritmética y la estrategia de negociación son **INTERNAS** ([estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) §7) y no se copian aquí ni a documentos del cliente.

### Plantilla general

| Cambio | Requisitos | Arquitectura y datos | Seguridad | Tareas | Pruebas | Operación | Documentación | Riesgos | Recomendación |
|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — |

## 3. Historial de decisiones

| Cambio | Decisión | Decisor | Fecha | Condiciones | Elementos actualizados |
|---|---|---|---|---|---|
| CR-001 | **Ninguna.** Solicitada por el usuario; pendiente de aprobación formal del cliente (WAITING_FOR_APPROVAL). La elección de la opción B, el plazo de 1 semana y los 400 USD son [C] del usuario (DEC-034 [OPB]) y no constituyen aprobación del CR | — | 2026-10-26 | Moneda e IVA (PEND-043); aceptación del cliente de España (PEND-044) | [DECISIONS](DECISIONS.md), [TASKS](TASKS.md), [RISKS](RISKS.md), [TRACEABILITY](TRACEABILITY.md), [AGENT-ACTIVITY](AGENT-ACTIVITY.md), [PROJECT-STATE](PROJECT-STATE.md) (todos en BORRADOR; el alcance no cambia hasta que CR-001 sea APPROVED) |

## Enlaces

[Estado del proyecto](PROJECT-STATE.md) · [Aprobaciones](APPROVALS.md) · [Decisiones](DECISIONS.md) · [Requisitos](REQUIREMENTS.md) · [Riesgos](RISKS.md) · [Trazabilidad](TRACEABILITY.md) · [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) · [estimacion-plazo.md](../05-planning/estimacion-plazo.md)
