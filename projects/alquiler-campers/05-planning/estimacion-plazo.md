# Estimación preliminar de plazo: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Estimación preliminar de plazo del Planificador de Proyecto, entregada por el Director en su instrucción del 2026-10-26 (contenido transcrito sin cambiar su significado; no hay archivo de origen separado). Complementa el [plan de implementación](implementation-plan.md).  
> **Naturaleza:** **Recomendación / estimación preliminar a confirmar.** No es un compromiso, ni un calendario, ni un presupuesto. **Sin fechas de calendario y sin costos.** El plazo se cuenta **desde H0** (autorización de BUILD), que **no ha ocurrido**.  
> **Aprobación:** NINGUNA. GATE-001 y GATE-002 siguen **PENDING**, el alcance **NO está aprobado** y no existe solicitud PLANNING → BUILD ([APPROVALS](../00-control/APPROVALS.md)). BUILD está prohibido.

**Avisos del Gestor:**
- Los IDs de tarea se transcriben como en la fuente. "TASK-012" en la sección Condiciones es la **TASK-012 [PLAN]** (validación legal); ver ISS-024 y ISS-037 en [RISKS](../00-control/RISKS.md). TASK-042, TASK-043, TASK-033, TASK-041, TASK-053, TASK-060 y TASK-064 son tareas del plan ([TASKS](../00-control/TASKS.md) §2.1).
- **Supuestos que no están aprobados:** la estimación asume B1 a B9 resueltas en H0 y que MFA obligatorio, auditoría mínima en el MVP y precio > 0 están dentro del alcance. Hoy todo eso está **pendiente** ([DECISIONS](../00-control/DECISIONS.md) §3 y §4; PEND-037 a PEND-039). Ver ISS-035.
- La tensión entre "presupuesto y fechas fuera del contrato" [C] y la inclusión de un plazo estimado en la propuesta se registra como pendiente de confirmación del cliente (PEND-041, ISS-034).
- Comprobación aritmética del Gestor (no cambia la fuente): sumando los tamaños S/M/L de las 32 tareas del plan que entran en el cómputo (4 S, 16 M, 12 L; sin P0 ni tareas del cliente) resulta un rango de 42 a 84 semanas-persona, cuyo punto medio es 63, coincidente con el "≈63 sp". Las sumas por fase (22 / 30 / 45), el valor esperado PERT (≈31) y los hitos acumulados también coinciden con las cifras de la fuente.

## 1. Método

- **Tamaños del plan (S/M/L) convertidos a esfuerzo:** S = 0,5–1; M = 1–2; L = 2–4 **semanas-persona** (sp).
- **Esfuerzo total:** ≈ **63 sp**, **sin P0 ni tareas del cliente**.
- **Plazo:** lo define la **ruta crítica**, no la suma del esfuerzo (el trabajo se solapa entre frentes).
- **Tres puntos:** (O + 4·P + Pe) / 6, con O = optimista, P = probable y Pe = pesimista.
- **Sin base histórica** (R-PL-007). Los tamaños S/M/L son orden relativo. **Revisar tras H1.**

## 2. Supuestos de equipo

| Rol | Dedicación asumida |
|---|---|
| BE (backend) | 2 a tiempo completo |
| FE (frontend) | 1 a tiempo completo |
| DAT (datos) | 1 en P1 y luego 0,5 |
| DO (DevOps) | 0,5 |
| QA | 0,5 desde P1 y 1 desde P2 |
| SEC, RT, TL, DIR | Puntuales |

- **Con un solo BE** el total sube **+25 a 40 %** (≈ **38 a 42 semanas probables**).

### Otros supuestos

- B1 a B9 resueltas **en H0**.
- MFA obligatorio, auditoría mínima en el MVP y precio > 0 **dentro del alcance** (TASK-042 y TASK-043).
- El cliente responde cada entrega en **≤ 3 días hábiles**.

## 3. Duración por fase (semanas, desde H0)

| Fase | Optimista (O) | Probable (P) | Pesimista (Pe) | Nota |
|---|---:|---:|---:|---|
| P0 | 2 | 3 | 4+ | **Fuera del reloj** (previa a H0) |
| P1 Fundaciones | 3 | 4 | 6 | |
| P2 Núcleo de reserva y pago | 7 | 9 | 12 | |
| P3 Post-reserva, panel y web | 4 | 6 | 9 | Incremento |
| P4 QUALITY | 4 | 6 | 9 | Incremento |
| P5 OPERATIONS y DOCUMENTATION | 2 | 3 | 6 | Incremento |
| P6 DELIVERY | 2 | 2 | 3 | |
| **Total P1 a P6** | **22** | **30** | **45** | |

- **Valor esperado (PERT):** ≈ **31 semanas**.
- **Confianza del 80 %:** ≈ **36 semanas**.

## 4. Recomendación para la propuesta

- **Rango recomendado: 28 a 36 semanas desde H0** (probable 30 a 31).
- **No publicar 22 ni 45** (los extremos optimista y pesimista).
- **Contingencia de 15 a 20 % (≈ 5 a 6 semanas)** ya incluida en el extremo alto.
- Es una recomendación. Su uso en la propuesta comercial depende de la confirmación del cliente (PEND-041).

## 5. Hitos relativos (semanas desde H0)

| Semana | Hito | Rango (O – Pe) |
|---|---|---|
| S0 | H0 (autorización de BUILD) | — |
| S4 | H1 (esqueleto, CI y esquema con exclusión probada) | 3 – 6 |
| S8 | Revisión intermedia | 7 – 11 |
| S13 | H2 (reserva y pago extremo a extremo en sandbox) | 10 – 18 |
| S19 | H3 (MVP funcional completo) | 14 – 27 |
| S25 | H4 (calidad y seguridad aprobadas) | 18 – 36 |
| S28 | H5 (operable) | 20 – 42 |
| S30 | H6 (auditoría y cierre) | 22 – 45 |

**Control:** revisar la estimación en **H1 (S4)** y en **H2**.

## 6. Límites aproximados de las decisiones si llegan tarde

Último momento aproximado antes de que cada decisión retrase la ruta crítica:

| Decisión | Límite aprox. | Tarea afectada |
|---|---|---|
| B1 (pasarela y titularidad) | ~S6 | Adaptador real de TASK-033 |
| B6 (MFA obligatorio del admin) | ~S8 | TASK-042 (hay valor por defecto) |
| B2, B8, B9 (hosting y región, RPO/RTO, dominio y titularidad de cuentas) | ~S10 | TASK-060 |
| B3, B5 (política de cancelación, acceso y cancelación con segundo factor) | ~S14 | Cierre de TASK-041 |
| B4, B7 (validación legal, retención de datos) | Antes de TASK-053 (~S20) | TASK-053 |

**Aclaración del Director:** el plazo asume B1 a B9 **resueltas en H0**. Los límites S6 a S20 son el último momento antes de que cada decisión retrase la ruta crítica; **no son un plan alternativo**.

## 7. Condiciones

- Feedback del cliente en **≤ 3 días hábiles**.
- Validación legal (TASK-012 [PLAN]) **antes de P5**.
- Contenidos y fotos reales (TASK-064) **antes de P5**. Si no, se usan imágenes de ejemplo (R-PL-009).
- Titularidad de cuentas resuelta.
- Alta de la pasarela y hosting con **PostgreSQL y worker persistente** (R-PL-010).
- **Autorizaciones específicas** de staging y de despliegue.

## 8. No incluye

- Tiempos de terceros: pasarela, DNS, dominio de correo, asesoría legal.
- Aprobaciones legales y **esperas de decisión** (se suman **1:1** al plazo).
- P0.
- Fase 2.
- Ampliaciones.
- Cambios sin solicitud de cambio.
- Producción con tráfico real.

## 9. Riesgos de plazo

| ID | Riesgo (ver [RISKS](../00-control/RISKS.md) §5) |
|---|---|
| R-PL-001 | Decisiones B1-B9 llegan tarde y paran el núcleo de pago |
| R-PL-002 | Cambio de alcance (MFA, auditoría, precio > 0) sin CR |
| R-PL-003 | Sesión de pago con caducidad mayor que el hold (R-ARQ-02) |
| R-PL-004 | Carrera hold, expiración y webhook produce doble reserva o cobro sin servicio (SEG-003) |
| R-PL-005 | Política de cancelación indefinida cambia el cálculo (ISS-002) |
| R-PL-006 | Validación legal tardía retrasa producción |
| R-PL-007 | Estimaciones S/M/L sin base histórica |
| **R-PL-012 [PLAN]** (nuevo) | **Cierre de las 7 Altas de seguridad (SEG-001 a SEG-007) más SEG-010 en P4** |

> Nota del Gestor: R-PL-012 es un ID nuevo registrado en [RISKS](../00-control/RISKS.md) §5. El plan original llegaba hasta R-PL-011.

## 10. Qué falta para pasar a fecha calendario

- Fecha de autorización de BUILD y cierre de B1 a B9.
- Dedicación real y calendario del equipo.
- Fecha objetivo y estacionalidad del cliente.
- Proveedor de pasarela y plazo de alta.
- Hosting.
- Asesoría legal y su plazo.
- Calendario de feedback y entrega de fotos y textos.
- Stack final (TASK-014).
- Flota y volumen (PEND-021).
- Protocolo de CWV (PEND-014).

Registrado como PEND-042 en [DECISIONS](../00-control/DECISIONS.md).

---

## Registro documental (Gestor de Documentación)

- **Estado:** BORRADOR. **Fecha de persistencia:** 2026-10-26. Sin fechas de calendario ni costos.
- **Fuente:** instrucción del Director del 2026-10-26, que transcribe la estimación preliminar del Planificador. El Planificador no modificó archivos ([ACT-010](../00-control/AGENT-ACTIVITY.md)).
- **Tarea:** [TASK-018](../00-control/TASKS.md) (IN_REVIEW).
- **Decisión relacionada:** DEC-033 (propuesta, pendiente de confirmación del cliente) y PEND-041, PEND-042 en [DECISIONS](../00-control/DECISIONS.md).
- **Riesgo nuevo:** R-PL-012 [PLAN].
- **Inconsistencias registradas:** ISS-034 a ISS-037 en [RISKS](../00-control/RISKS.md).
- **Propuesta comercial relacionada:** `12-propuesta/` (propiedad del Redactor de Propuestas; el Gestor no la ha leído ni modificado). Ver [ACT-011](../00-control/AGENT-ACTIVITY.md).

## Enlaces relativos

[Plan de implementación](implementation-plan.md) · [Estado del proyecto](../00-control/PROJECT-STATE.md) · [Decisiones](../00-control/DECISIONS.md) · [Riesgos e impedimentos](../00-control/RISKS.md) · [Tareas](../00-control/TASKS.md) · [Aprobaciones](../00-control/APPROVALS.md) · [Trazabilidad](../00-control/TRACEABILITY.md) · [Revisión de seguridad](../08-security/security-review.md) · [Arquitectura de solución](../04-architecture/solution-architecture.md)
