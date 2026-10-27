# Estado maestro: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Última actualización:** 2026-10-26  
> **Fuente:** Instrucciones del Director de Proyectos, reportes del Analista de Negocio, del Product Manager, del Diseñador UX/UI, del Arquitecto de Soluciones, del Revisor de Seguridad y del Planificador (incluida la estimación de la opción B), y el resto de registros de `00-control/`. Este panel resume y no sustituye a los registros detallados.

## 1. Identificación

| Campo | Valor |
|---|---|
| Proyecto | Web de alquiler de campers (España). Nombre provisional: el cliente no indicó un nombre comercial en el material recibido |
| Slug | `alquiler-campers` |
| Estado general | ACTIVE |
| Fase actual | INTAKE (GATE-001 PENDING). Análisis de DISCOVERY, producto, diseño UX/UI, arquitectura, revisión de seguridad de diseño y plan de implementación realizados como **borradores sin aprobación** (ver [APPROVALS](APPROVALS.md) §3). Por decisión del Director (PEND-033), el diseño continúa como BORRADOR con GATE-002 PENDING |
| Puerta actual | GATE-001 PENDING. GATE-002 (DISCOVERY → DESIGN) PENDING. PLANNING → BUILD **no solicitada**. BUILD prohibido |
| Alcance aprobado | **NO** |
| Responsable de coordinación | Director de Proyectos |

## 2. Objetivo

- **[C]** Web para alquiler de campers en España con reservas en línea (fechas, disponibilidad, gestión de alquileres por el usuario) y pasarela de pago segura, con atención a experiencia de usuario, velocidad y SEO.
- **[C]** Flota y sedes configurables desde un panel.

Fuente: [client-brief.md](../00-intake/client-brief.md), [requirements.md](../01-discovery/requirements.md) §1.

## 3. Resultado esperado

- **[C]** Canal propio en línea para reservar y pagar, con gestión desde panel y base SEO técnica, sin garantía de posicionamiento.
- **[R]** Reducir la gestión manual de disponibilidad y cobros y evitar dobles reservas.
- **[P]** Metas cuantitativas de negocio no definidas.

## 4. Alcance aprobado

**No existe alcance aprobado.** El MVP y el backlog del Product Manager son una **propuesta en BORRADOR** ([mvp-and-backlog.md](../02-product/mvp-and-backlog.md)). No se autoriza ningún desarrollo.

### Incluido

- Nada está aprobado. Propuesta en borrador: ver el MVP en [mvp-and-backlog.md](../02-product/mvp-and-backlog.md). Hay diferencias con el Analista (ISS-004 a ISS-011 en [RISKS](RISKS.md)).

### Fuera de alcance

- **[C]** Migración de datos e integración con sistemas existentes.
- **[C]** Presupuesto y fechas (fuera del contrato).
- Las exclusiones marcadas [R] por el Analista y el Product Manager no están confirmadas.

## 5. Equipo activo

| Agente | Responsabilidad actual | Última actividad | Estado |
|---|---|---|---|
| Director de Proyectos | Coordinar y consolidar. Es el único portavoz ante el cliente | 2026-10-26 | ACTIVE |
| Analista de Negocio | Requisitos y preguntas (entregado) | 2026-10-26 | COMPLETADO_CON_PENDIENTES |
| Product Manager | MVP y backlog (entregado) | 2026-10-26 | Entregado. Sin resultado declarado en la fuente |
| Gestor de Documentación | Persistir el expediente | 2026-10-26 | COMPLETADO_CON_PENDIENTES |
| Diseñador UX/UI | Especificación UX (entregada como BORRADOR, con conflicto de contrato devuelto al Director) | 2026-10-26 | COMPLETADO_CON_PENDIENTES |
| Arquitecto de Soluciones | Arquitectura de solución (entregada como BORRADOR) | 2026-10-26 | COMPLETADO_CON_PENDIENTES |
| Revisor de Seguridad | Revisión de seguridad de diseño (BORRADOR; ninguna prueba ejecutada) | 2026-10-26 | COMPLETADO_CON_PENDIENTES |
| Planificador de Proyecto | Plan de implementación (BORRADOR, sin fechas; conflicto de fase devuelto al Director), estimación preliminar de plazo (a confirmar) y estimación de la opción B (BORRADOR, a confirmar; ACT-013) | 2026-10-26 | COMPLETADO_CON_PENDIENTES |
| Redactor de Propuestas | Propuesta comercial en `12-propuesta/`, ejecutada por un agente general bajo su perfil por instrucción explícita del usuario; actualizada para la opción B (ACT-014). Contenido no verificado por el Gestor | 2026-10-26 | No declarado al Gestor |

UX/UI, Arquitectura, Seguridad y Planificación entregaron borradores con GATE-002 PENDING (ver ISS-016 e ISS-025). El plan no activa agentes de BUILD: no hay BUILD autorizado. `05-planning/`, `08-security/`, `04-architecture/` y `03-ux/` contienen un borrador cada una.

## 6. Trabajo en curso

| Tarea | Descripción | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-001 | Análisis de negocio | Analista de Negocio | IN_REVIEW | [requirements.md](../01-discovery/requirements.md) |
| TASK-002 | MVP, backlog, historias y criterios | Product Manager | IN_REVIEW | [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) |
| TASK-010 | Especificación UX/UI del MVP | Diseñador UX/UI | IN_REVIEW | [ux-specification.md](../03-ux/ux-specification.md) |
| TASK-011 | Arquitectura de solución del MVP | Arquitecto de Soluciones | IN_REVIEW | [solution-architecture.md](../04-architecture/solution-architecture.md) |
| TASK-015 | Revisión de seguridad de diseño (SEG-001 a SEG-017) | Revisor de Seguridad | IN_REVIEW | [security-review.md](../08-security/security-review.md) |
| TASK-016 | Plan de implementación del MVP (sin fechas) | Planificador de Proyecto | IN_REVIEW | [implementation-plan.md](../05-planning/implementation-plan.md) |
| TASK-018 | Estimación preliminar de plazo (28 a 36 semanas desde H0, a confirmar) | Planificador de Proyecto | IN_REVIEW | [estimacion-plazo.md](../05-planning/estimacion-plazo.md) |
| TASK-019 | Propuesta comercial (18 archivos según el Director) | Redactor de Propuestas (agente general bajo su perfil) | IN_REVIEW | [12-propuesta](../12-propuesta/) (no verificada por el Gestor) |
| TASK-026 [OPB] | Revisar la propuesta actualizada para la opción B frente a CR-001 y al expediente | Director de Proyectos | IN_REVIEW | [12-propuesta](../12-propuesta/) (no verificada por el Gestor); [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) |

Backlog (TASK-004 a TASK-009, TASK-012, TASK-017 y TASK-025) en [TASKS](TASKS.md) §2. **Opción B:** T1 a T10 [OPB] en BACKLOG, sin asignar y sin autorización ([TASKS](TASKS.md) §2.2); ninguna en DONE. Las 38 tareas del plan (TASK-010 [PLAN] a TASK-071) están en BACKLOG, sin asignar y **sin autorización** ([TASKS](TASKS.md) §2.1). TASK-010 [PLAN], TASK-011 [PLAN] y TASK-012 [PLAN] usan el calificador por colisión de IDs (ISS-024).

## 7. Bloqueos e impedimentos

45 impedimentos abiertos, ISS-001 a ISS-045. ISS-001 a ISS-014 son discrepancias entre el Analista y el Product Manager. ISS-015 a ISS-023 (numeración confirmada por el Director) son inconsistencias entre UX, arquitectura, PM y Analista. ISS-024 a ISS-045 son inconsistencias nuevas (seguridad, plan, estimación de plazo, propuesta comercial y opción B), registradas sin elegir versión y sin revisar por el Director. Detalle en [RISKS](RISKS.md) §2.

| ID | Descripción | Impacto | Responsable | Próxima acción |
|---|---|---|---|---|
| ISS-001 | CA-001 a CA-014 no reconciliados entre AN y PM | Trazabilidad HU → CA ambigua | Director de Proyectos | TASK-007 |
| ISS-002 | Política de cancelación: al reservar (AN, recomendación del Director) o al cancelar (PM, CA-008) | Cálculo del reembolso | Director de Proyectos | DEC-025, validación legal |
| ISS-003 a ISS-014 | Ver [RISKS](RISKS.md) §2 | Alcance, prioridades e identificadores | Director de Proyectos | TASK-008 |
| ISS-015 a ISS-023 | Ver [RISKS](RISKS.md) §2. Resumen: ISS-002 propagado a UX y arquitectura (ISS-015); conflicto de contrato declarado solo por UX (ISS-016); acceso admin con MFA y recuperación (ISS-017); reenvío de correos y código (ISS-018); pago alojado/embebido y bloqueo vs sesión de pago (ISS-019); cobertura de la matriz del Arquitecto (ISS-020); precio "desde" y correo de aviso frente a caché y modelo de datos (ISS-021); fechas y zona horaria (ISS-022); IDs de CA ambiguos (ISS-023) | Alcance de UX y arquitectura, trazabilidad | Director de Proyectos | TASK-012 |
| ISS-024 a ISS-033 | Ver [RISKS](RISKS.md) §2. Resumen: colisión de IDs de tareas del plan con TASK-010 a TASK-012 (ISS-024); puertas y veredicto del Revisor frente a GATE-002 (ISS-025); momento de cierre de SEG-001 a SEG-007 y SEG-010 (ISS-026); alcance de B1 a B9 como bloqueantes (ISS-027); validación legal con cuatro lecturas (ISS-028); cambios de alcance que exige seguridad (MFA, auditoría mínima, VAL-020, segundo factor) (ISS-029); controles que alteran flujos de UX/PM (ISS-030); IDs mal citados "B-P12" y "PEND-012/P-012" (ISS-031); dos revisiones con el nombre `security-review.md` (ISS-032); lecturas parciales y riesgos duplicados (ISS-033) | Alcance, puerta de BUILD y trazabilidad | Director de Proyectos | TASK-017 |
| ISS-034 a ISS-037 | Ver [RISKS](RISKS.md) §2. Resumen: "presupuesto y fechas fuera del contrato" frente al plazo estimado solicitado (ISS-034); el rango de plazo depende de B1 a B9 y de cambios de alcance no aprobados (ISS-035); propuesta comercial ejecutada bajo perfil y no revisada por el Gestor (ISS-036); "TASK-012" citada sin calificador (ISS-037) | Contenido de la propuesta comercial y fiabilidad del plazo | Director de Proyectos | TASK-025 |
| ISS-038 a ISS-045 | Ver [RISKS](RISKS.md) §2. Resumen (opción B y CR-001): 400 USD y plazo de 1 semana frente a "presupuesto y fechas fuera del contrato" y a un cliente en España, con moneda e IVA pendientes (ISS-038); la opción B sin panel desvía RN-001 y RNF-010 confirmados (ISS-039); 28–36 semanas y 1 semana corresponden a alcances distintos (ISS-040); la B completa (50–70 h) no cabe en 1 semana con holgura y el reporte tiene ambigüedades internas (ISS-041); RF-014, RF-027 a RF-031 y RNF-012 sin clasificar (ISS-042); seguridad y RGPD en B (ISS-043); pila sin verificar frente a 04-architecture (ISS-044); propuesta actualizada bajo perfil y no revisada por el Gestor (ISS-045) | Alcance, plazo, precio y propuesta de la opción B | Director de Proyectos | TASK-026 [OPB], CR-001 |

## 8. Decisiones pendientes del usuario

Ninguna decisión está aprobada. Hay 34 propuestas (DEC-001 a DEC-034; DEC-033 = propuesta comercial y rango de plazo, pendiente de confirmación del cliente; DEC-034 [OPB] = opción B, plazo objetivo de 1 semana y 400 USD, elección del usuario pendiente de aprobación del cliente), 12 propuestas de arquitectura (ADR-001 a ADR-012), 47 pendientes (PEND-001 a PEND-047) y 9 decisiones bloqueantes de BUILD según el plan (B1 a B9). Detalle en [DECISIONS](DECISIONS.md). Las fuentes no definen fechas requeridas.

| ID | Pregunta o decisión | Impacto | Fecha requerida |
|---|---|---|---|
| GATE-001 | Autorizar inicio de DISCOVERY | Fase y legitimidad del análisis ya realizado | No definida |
| GATE-002 | DISCOVERY → DESIGN | Paso a diseño | No definida |
| PEND-001 a PEND-007 | Preguntas Q1 a Q7 del Analista | Cobro, fianza, acceso, factura, conductor, sedes y panel | No definida |
| PEND-010 | Validación legal (P-005) | Bloquea la salida a producción, no la planificación (PM) | No definida |
| PEND-008, PEND-011 | Política de cancelación (P-001) y titularidad de pasarela, dominio y correo (P-014) | Bloquean la salida a producción, no la planificación (PM) | No definida |
| DEC-001 a DEC-032 | Propuestas pendientes de aprobación del cliente | Alcance y reglas | No definida |
| ADR-001 a ADR-012 | Propuestas de arquitectura pendientes de aprobación | Diseño técnico. Ninguna tecnología es obligatoria | No definida |
| PEND-025 a PEND-033 | Pendientes de UX/UI: marca, recuperación de contraseña del admin, correo de aviso, sedes y SEO, precio "desde", fichas desactivadas, ampliación del bloqueo, pantalla de inicio del panel y activación formal de DESIGN (PEND-033, Director) | Diseño | No definida |
| PEND-034 a PEND-036 | Pendientes de arquitectura: hosting y región, acceso del cliente (código + email o enlace mágico) y MFA del admin, retención de datos | Diseño técnico y privacidad | No definida |
| PEND-037 a PEND-040 | Seguridad y plan: segundo factor para cancelar (SEG-001), auditoría mínima en el MVP (SEG-007), VAL-020 con precio > 0 (SEG-005), y resolución de ISS-004 a ISS-011 con prioridades P-004, P-007 y P-009 | Cambios de alcance frente al PM (R-PL-002) | No definida |
| B1 a B9 | Decisiones bloqueantes de BUILD según el plan: pasarela y titularidad, hosting y región, política de cancelación, validación legal, acceso y cancelación con segundo factor, MFA del admin, retención de datos, RPO/RTO, dominio y titularidad de cuentas (ver ISS-027) | Puerta de BUILD | No definida |
| DEC-033, PEND-041 | Incluir en la propuesta comercial un plazo estimado (28 a 36 semanas desde H0, preliminar a confirmar) pese a que "presupuesto y fechas" figuran fuera del contrato (ISS-034) | Contenido de la propuesta comercial | No definida |
| PEND-042 | Datos para pasar la estimación a fecha de calendario | Plazo | No definida |
| CR-001, DEC-034 [OPB], PEND-043 a PEND-047 | Opción B (entrega inicial acotada, plazo objetivo de 1 semana, 400 USD [C] del usuario): aprobación del cliente de España a prescindir temporalmente de pago y panel (PEND-044); moneda USD/EUR e IVA (PEND-043); edición de contenido por el cliente o el proveedor (PEND-045); variante: núcleo, B completa o 2 personas (PEND-046); pila compatible con 04-architecture (PEND-047) | Alcance, plazo y precio de la entrega inicial | No definida |

## 9. Riesgos principales

Los niveles no están evaluados en las fuentes. Registro completo, con IDs calificados [AN] y [PM] por la colisión ISS-003, en [RISKS](RISKS.md).

| ID | Riesgo | Nivel | Estado | Tratamiento |
|---|---|---|---|---|
| R-001 [AN] / R-002 [PM] | Requisitos legales y textos sin validar | — | OPEN | Asesoría legal (PEND-010) |
| R-002 [AN] / R-001 [PM] | Política de pago, cancelación y precios sin definir | — | OPEN | Decidir Q1 y validar valores |
| R-003 [AN] | Doble reserva por concurrencia | — | OPEN | RN-003, RN-016, RNF-007 |
| R-007 [AN] | "Completa" y "robusto" sin acotar | — | OPEN | MVP/F2/AMP y gestión de cambios |
| R-ARQ-01 [ARQ] | Pasarela no elegida, o con particularidades que obliguen a rediseñar el pago | — | OPEN | ADR-004. Prueba de concepto con el sandbox al elegir |
| R-ARQ-02 [ARQ] / R-UX-05 [UX] | Sesión de pago con caducidad mayor que el bloqueo de 15 min. El bloqueo vence mientras el cliente autentica el pago | — | OPEN | Alinear hold y sesión. Avisos del temporizador (ISS-019) |
| R-ARQ-04 [ARQ] / R-UX-01 [UX] | Política de cancelación indefinida (ISS-002) y su efecto en P05, P10 y ADR-008 | — | OPEN | ADR-008 admite ambas. Decisión tras validación legal (ISS-015) |
| R-UX-10 [UX] | Marca provisional: cambiarla tarde implica rehacer componentes | — | OPEN | PEND-025 |
| SEG-001 a SEG-007 (7 Altas) | Acceso por código + email con cancelación y reembolso (001), webhook (002), concurrencia (003), abuso de negocio (004), importes y reembolsos (005), autenticación del panel (006), auditoría aplazada a Fase 2 (007). **Hallazgos de una revisión de diseño; ninguna prueba ejecutada** | Alta (según el Revisor) | OPEN | Controles obligatorios antes de BUILD según el Revisor; ver ISS-026 |
| SEG-010 | RGPD sin cerrar (retención, supresión, contratos, transferencias) | Alta, validar legal | OPEN | Asesoría legal (PEND-010, B4, B7) |
| R-PL-001 [PLAN] / R-PL-006 [PLAN] | Decisiones B1-B9 tardías. Validación legal tardía | Alta (según el plan) | OPEN | Paquete único TASK-010 [PLAN]. Asesoría pronto |
| R-PL-012 [PLAN] | Cierre de las 7 Altas de seguridad (SEG-001 a SEG-007) más SEG-010 en P4 (riesgo de plazo) | — | OPEN | Revisar la estimación en H1 (S4) y H2 |
| R-001 [OPB] a R-008 [OPB] | Riesgos de la entrega inicial acotada (opción B): contenidos tardíos (Alta/Alto), legales sin validar, entregabilidad del correo, solicitudes perdidas sin base de datos, SEO sin garantías, **sin margen: cualquier retraso rompe la semana (R-006, Alta/Alto)**, rehacer la parte pública al migrar, estacionalidad | Según el Planificador: ver [RISKS](RISKS.md) §6 | OPEN | Mitigaciones del Planificador en [RISKS](RISKS.md) §6 |

Registro completo, incluidos R-UX-01 a R-UX-10, R-ARQ-01 a R-ARQ-12, SEG-001 a SEG-017 (17 hallazgos, todos OPEN, esto no indica que el sistema sea seguro) y R-PL-001 a R-PL-011, en [RISKS](RISKS.md). Los riesgos [UX] y [ARQ] no están evaluados (Prob., Impacto y Nivel en `—`); la evaluación del plan (P e I) está en [RISKS](RISKS.md) §5.

## 10. Entregables y evidencia reciente

| Fecha | Entregable o evidencia | Relación | Estado |
|---|---|---|---|
| 2026-10-26 | [client-brief.md](../00-intake/client-brief.md) | INTAKE | BORRADOR |
| 2026-10-26 | [requirements.md](../01-discovery/requirements.md) | DISCOVERY | BORRADOR |
| 2026-10-26 | [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) | Producto | BORRADOR |
| 2026-10-26 | [ux-specification.md](../03-ux/ux-specification.md) | Diseño UX/UI (GATE-002 PENDING) | BORRADOR |
| 2026-10-26 | [solution-architecture.md](../04-architecture/solution-architecture.md) | Arquitectura (GATE-002 PENDING) | BORRADOR |
| 2026-10-26 | [security-review.md](../08-security/security-review.md) | Revisión de seguridad de diseño, sin pruebas ejecutadas (GATE-002 PENDING) | BORRADOR |
| 2026-10-26 | [implementation-plan.md](../05-planning/implementation-plan.md) | Plan de implementación sin fechas. No autoriza BUILD | BORRADOR |
| 2026-10-26 | [estimacion-plazo.md](../05-planning/estimacion-plazo.md) | Estimación preliminar de plazo, desde H0, sin fechas ni costos. A confirmar | BORRADOR |
| 2026-10-26 | [12-propuesta](../12-propuesta/) | Propuesta comercial y mockups (18 archivos según el Director; actualizada para la opción B por un agente general bajo el perfil del Redactor de Propuestas, ACT-014). Creada fuera del contrato del Gestor, **no verificada por el Gestor** | Estado no declarado al Gestor. Sin aprobación |
| 2026-10-26 | [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) | Estimación de la entrega inicial acotada (opción B): veredicto, T1 a T10 [OPB], riesgos, hitos, cobertura de requisitos. **Su §7 (alcance y precio) es INTERNA: no copiar a documentos del cliente** | BORRADOR. Estimación a confirmar |
| 2026-10-26 | [CR-001](CHANGE-REQUESTS.md) | Solicitud de cambio: sustituir el MVP completo por la entrega inicial acotada (opción B) | WAITING_FOR_APPROVAL |
| 2026-10-26 | Nueve registros en `00-control/`: este archivo, [REQUIREMENTS](REQUIREMENTS.md), [DECISIONS](DECISIONS.md), [TASKS](TASKS.md), [AGENT-ACTIVITY](AGENT-ACTIVITY.md), [RISKS](RISKS.md), [TRACEABILITY](TRACEABILITY.md), [APPROVALS](APPROVALS.md) y [CHANGE-REQUESTS](CHANGE-REQUESTS.md). Actualizados 2026-10-26: PROJECT-STATE, DECISIONS, TASKS, AGENT-ACTIVITY, RISKS, TRACEABILITY, CHANGE-REQUESTS y APPROVALS (solo nota §2) | Gobierno del proyecto | BORRADOR |

Las carpetas `03-ux/`, `04-architecture/`, `05-planning/` y `08-security/` contienen cada una al menos un borrador (`05-planning/`: plan, estimación de plazo y estimación de la opción B). `12-propuesta/` no es gestionada por el Gestor.

## 11. Solicitudes de cambio abiertas

| ID | Resumen | Estado | Decisión requerida |
|---|---|---|---|
| CR-001 | Sustituir el MVP completo por una entrega inicial acotada (opción B) con plazo objetivo de 1 semana y valor de 400 USD; pago en línea, disponibilidad automática, panel, cuentas y la seguridad asociada pasan a la fase siguiente. Desvía RN-001 y RNF-010 (confirmados). El MVP completo (28 a 36 semanas) sigue vigente como fase siguiente | WAITING_FOR_APPROVAL (solicitado por el usuario; pendiente de aprobación formal del cliente) | Aprobación o rechazo del cliente de España, vía Director (PEND-044); moneda e IVA (PEND-043). Ver [CHANGE-REQUESTS](CHANGE-REQUESTS.md) y [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) |

Los cambios de alcance que exige seguridad para el MVP completo (MFA obligatorio, auditoría mínima, precio > 0, segundo factor para cancelar; R-PL-002) **siguen sin CR**: el Gestor no recibió instrucción. Ver PEND-037 a PEND-039.

## 12. Siguiente paso recomendado

Según las fuentes, correspondería al Director:

1. Confirmar que ISS-001 a ISS-014 y DEC-001 a DEC-032 equivalen a la lista que aprobó (TASK-004), y el ID de GATE-002.
2. Decidir cómo regularizar GATE-001 y decidir la puerta GATE-002.
3. Trasladar al cliente las preguntas Q1 a Q7 (PEND-001 a PEND-007) y solicitar la validación legal (PEND-010).
4. Reconciliar los CA y resolver las discrepancias de alcance (TASK-007, TASK-008).
5. Decidir la activación de Seguridad en BUILD y el alcance de TASK-009. UX/UI, Arquitectura, Seguridad y Planificación ya entregaron borradores.
6. Revisar las inconsistencias nuevas ISS-015 a ISS-023 (TASK-012) e ISS-024 a ISS-033 (TASK-017). PEND-033 resuelta por el Director: el diseño continúa como BORRADOR con GATE-002 PENDING.
7. Trasladar al cliente las decisiones de diseño, arquitectura, seguridad y plan: PEND-025 a PEND-040, B1 a B9 y las ADR-001 a ADR-012 propuestas (el plan propone lanzar TASK-010 [PLAN] como paquete único). Ninguna se considera aceptada.
8. Decidir si los cambios de alcance de seguridad (MFA obligatorio, auditoría mínima, precio > 0, segundo factor para cancelar) se tramitan como solicitud de cambio (R-PL-002). No hay solicitud PLANNING → BUILD: BUILD sigue prohibido.
9. Revisar `12-propuesta/` frente al expediente, confirmar con el cliente que se incluya el plazo estimado (28 a 36 semanas desde H0, preliminar a confirmar; DEC-033, PEND-041) y revisar ISS-034 a ISS-037 (TASK-025). La fase sigue en BORRADOR sin aprobar.
10. **Opción B (CR-001, 2026-10-26):** decidir con el cliente de España si acepta prescindir temporalmente de pago y panel (PEND-044) y la moneda e IVA (PEND-043); decidir la variante (núcleo en 1 semana, B completa o 2 personas, PEND-046) y quién edita el contenido (PEND-045); verificar la pila frente a 04-architecture (PEND-047); revisar la propuesta actualizada de `12-propuesta/` (TASK-026 [OPB]) y ISS-038 a ISS-045. Recomendación interna: ante negociación, ceder alcance y no calidad, y no ceder plazo sin ceder alcance ([DECISIONS](DECISIONS.md) DEC-034 [OPB]). Ninguna T1 a T10 [OPB] puede iniciarse sin CR-001 aprobada y autorización del Director.

## 13. Acción requerida del usuario

Aprobar o rechazar GATE-001. Responder a las preguntas Q1 a Q7 cuando el Director se las traslade. Ninguna propuesta se considera aceptada por silencio.

## 14. Enlaces de control

- [Requisitos](REQUIREMENTS.md)
- [Decisiones](DECISIONS.md)
- [Tareas](TASKS.md)
- [Actividad de agentes](AGENT-ACTIVITY.md)
- [Riesgos](RISKS.md)
- [Trazabilidad](TRACEABILITY.md)
- [Aprobaciones](APPROVALS.md)
- [Solicitudes de cambio](CHANGE-REQUESTS.md)

## 15. Documentos del expediente

- [Resumen del cliente (INTAKE)](../00-intake/client-brief.md)
- [Requisitos del Analista (DISCOVERY)](../01-discovery/requirements.md)
- [MVP y backlog del Product Manager](../02-product/mvp-and-backlog.md)
- [Especificación UX/UI (BORRADOR)](../03-ux/ux-specification.md)
- [Arquitectura de solución (BORRADOR)](../04-architecture/solution-architecture.md)
- [Revisión de seguridad de diseño (BORRADOR)](../08-security/security-review.md)
- [Plan de implementación (BORRADOR)](../05-planning/implementation-plan.md)
- [Estimación preliminar de plazo (BORRADOR, a confirmar)](../05-planning/estimacion-plazo.md)
- [Estimación de la opción B, entrega inicial acotada (BORRADOR, a confirmar; §7 INTERNA)](../05-planning/estimacion-opcion-b.md)
- [Solicitud de cambio CR-001 (WAITING_FOR_APPROVAL)](CHANGE-REQUESTS.md)
- [Propuesta comercial (`12-propuesta/`, no gestionada ni verificada por el Gestor)](../12-propuesta/)
