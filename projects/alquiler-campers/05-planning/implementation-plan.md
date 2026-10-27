# Plan de implementación del MVP: web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Reporte del agente Planificador de Proyecto, persistido por el Gestor de Documentación sin cambiar su significado.  
> **Aprobación:** NINGUNA. El plan **no autoriza BUILD ni despliegues**. GATE-001 y GATE-002 siguen **PENDING**, el alcance **NO está aprobado** y no existe solicitud PLANNING → BUILD ([APPROVALS](../00-control/APPROVALS.md)). **Sin fechas.**

**Avisos del Gestor sobre identificadores (ver ISS-024 en [RISKS](../00-control/RISKS.md)):**
- El plan numera sus tareas desde TASK-010 porque dice que existen TASK-001 a TASK-009. Cuando el plan se recibió, el Gestor ya había registrado otras tareas como TASK-010 (especificación UX), TASK-011 (arquitectura) y TASK-012 (revisión de inconsistencias). **No se reutilizan IDs.**
- En los registros de `00-control/`, las tareas del plan que colisionan se identifican como **TASK-010 [PLAN]**, **TASK-011 [PLAN]** y **TASK-012 [PLAN]**. Las demás tareas del plan (TASK-013 y siguientes) conservan su ID tal cual en [TASKS](../00-control/TASKS.md). Los IDs de este documento son los **originales del plan**.
- Las tareas del Gestor para los reportes de seguridad y plan usan TASK-015 y TASK-016, que el plan no utiliza.
- B1 a B9 y R-PL-001 a R-PL-011 se conservan con el ID del plan. "B-P12" (TASK-052) y "PEND-012/P-012" (Plan de validación) se transcriben tal cual: ver ISS-031.
- El plan declara que no pudo leer `RISKS` ni `requirements` completos; su estado de lectura figura en el encabezado del reporte.

# Plan de implementación del MVP: web de alquiler de campers (España)

- **Agente:** Planificador de Proyecto. **Contrato:** `planificador-proyecto.contract.json` (solo lectura, fase PLANNING).
- **Conflicto devuelto al Director:** el proyecto está en INTAKE con GATE-001 PENDING. El alcance **NO está aprobado**, GATE-002 está PENDING y PLANNING→BUILD no se ha solicitado. Este plan es un **BORRADOR**. No autoriza BUILD ni despliegues, y el planificador no lo aprueba.
- **Archivos modificados:** ninguno. **Pruebas ejecutadas:** ninguna.
- **Leído:** `PROJECT-STATE`, `DECISIONS` (parcial), `TASKS`, `RISKS` (no accesible por tamaño; sin lectura), `requirements` (no accesible por tamaño; consultado vía backlog), `mvp-and-backlog`, y los borradores de UX, Arquitectura y Seguridad.
- **Resultado:** COMPLETADO_CON_PENDIENTES.
- **Leyenda:** **[C]** Confirmado, **[S]** Supuesto, **[R]** Recomendación, **[P]** Pendiente.
- **Tamaños S/M/L:** esfuerzo relativo. No son calendario, costo ni dimensión de equipo.
- **Identificadores:** TASK-001 a TASK-009 ya existen, así que uso TASK-010 en adelante. Uso `R-PL-xxx` para los riesgos porque `R-001` ya colisiona (ISS-003).

## Base del plan

- **[C]** Web de campers en España con reserva, pago seguro y panel de flota y sedes. Sin migración ni integraciones. Presupuesto y fechas están fuera de contrato.
- **[S]** MVP del PM (DEC-029), sin aprobar:
  - pago total y fianza informativa;
  - acceso con código+email;
  - un solo admin;
  - misma sede, ES/EUR;
  - extras y FAQ en F2.
- **[R]** Arquitectura:
  - monolito modular con worker;
  - PostgreSQL con exclusión por rango (ADR-001 a ADR-012);
  - `PaymentProvider` con pago alojado;
  - SSR/ISR;
  - correo mediante outbox.
- **[R]** Seguridad: SEG-001 a SEG-017. **Siete Altas** (001 a 007) más SEG-010 (RGPD) se cierran antes de BUILD o de producción.
- **[R]** Cambios de alcance que el Director debe decidir (Seguridad los exige):
  - MFA obligatorio;
  - auditoría mínima en el MVP (hoy RF-029 está en F2);
  - precio > 0 (VAL-020);
  - segundo factor para cancelar.
- **[P]** Repo y stack aún no existen. Las fronteras de archivos de abajo son lógicas **[R]**.

## Estrategia de ejecución

1. **Puertas primero.** No hay código sin alcance aprobado, GATE-002 y aprobación humana PLANNING→BUILD.
2. **Núcleo transaccional primero.** Datos → disponibilidad/precio → reserva+hold → pago/webhook → expiración y pago tardío. Es lo más caro de corregir y lo que más riesgo concentra.
3. **Mocks y sandbox.** La pasarela, el correo y el anti-bot se desarrollan contra interfaz y mock. El adaptador real se activa al decidir proveedor.
4. **Seguridad desde el diseño.** Los controles SEG se convierten en criterios de cierre de cada tarea. Revisión final obligatoria antes de producción.
5. **Despliegue fuera del plan de código.** Staging y producción necesitan autorización específica y adicional.
6. **Equipo mínimo [R].** Sin cifras.

   | Rol | Responsabilidad |
   |---|---|
   | DIR | Coordina y es el único portavoz ante el cliente |
   | TL | Stack, ADR y revisión |
   | BE | Backend |
   | FE | Frontend |
   | DAT | Datos; absorbible por BE si el volumen lo permite |
   | DO | DevOps |
   | QA | Calidad |
   | SEC | Seguridad, independiente |
   | RT | Redactor Técnico |
   | GD | Gestor de Documentación |
   | AUD | Auditor de Trazabilidad y Auditor de Entrega |

   **No se activan:** Mobile (no hay app), Desarrollador genérico, Delivery Manager (lo cubre DIR), ni Analista, PM, UX y Arquitecto en BUILD (solo consulta puntual). **Sin agente:** decisiones del cliente, validación legal, contratación de pasarela, dominio y hosting, fotos y textos finales, y la aprobación de puertas.
7. **Fronteras [R]** (un archivo, un dueño):

   | Frente | Ruta lógica |
   |---|---|
   | BE | `server/modules/{catalog,pricing,availability,reservations,payments,policies,notifications,admin}`, `server/worker` |
   | FE | `web/public`, `web/admin` |
   | DAT | `db/migrations`, `db/seed` |
   | DO | `infra/`, `.github/workflows` |
   | QA | `tests/` |
   | RT | `docs/` |

   **Contratos compartidos:** las interfaces del API las fija TL y las edita solo BE. FE consume contrato o mock.

## Fases

| Fase | Contenido | Puerta de salida (humana) |
|---|---|---|
| P0 Preparación (DESIGN/PLANNING) | Reconciliar ISS, decisiones bloqueantes, aprobar alcance y plan | GATE-002 y PLANNING→BUILD |
| P1 Fundaciones (BUILD) | Repo, CI, modelo de datos, esqueleto, tokens UI | Esquema y CI verdes; SEG-012 y SEG-014 base |
| P2 Núcleo de reserva y pago | Precio, disponibilidad, hold, pago, webhook, worker | Concurrencia y pago en verde con sandbox |
| P3 Post-reserva, panel y web | Correo, consulta, cancelación, panel, auditoría, SEO, legales | Funcionalidad completa del MVP, sin las 7 Altas abiertas |
| P4 QUALITY | QA integral, revisión de seguridad final, correcciones | Revisión SEC aprobada y 0 Altas abiertas |
| P5 OPERATIONS y DOCUMENTATION | Entornos, copias, restauración, runbook, manual, datos reales | Autorización explícita de despliegue |
| P6 DELIVERY | Auditoría, go/no-go | Aprobación del cliente |

## Hitos

Sin fechas.

| Hito | Contenido |
|---|---|
| H0 | Alcance, plan y decisiones bloqueantes aprobados; BUILD autorizado |
| H1 | Esqueleto, CI y esquema con exclusión probada |
| H2 | Reserva y pago extremo a extremo (sandbox) sin doble reserva |
| H3 | MVP funcional completo |
| H4 | Calidad y seguridad aprobadas |
| H5 | Operable: copias restauradas, runbook y manual |
| H6 | Auditoría y cierre |

## Desglose de trabajo

Estado de todas: BACKLOG, sin asignar. El responsable es una propuesta.

**Entradas comunes:** alcance aprobado, UX, arquitectura, SEG y los CA citados. La columna "Cierre" es el DoD específico y exige evidencia verificable. **Dependencias:** TL = TASK-014; ARR = arranque (H0).

> Nota del Gestor: en esta tabla los IDs son los del plan. En [TASKS](../00-control/TASKS.md), TASK-010, 011 y 012 del plan figuran como TASK-010 [PLAN], TASK-011 [PLAN] y TASK-012 [PLAN]. Las dependencias de la forma "010, 011, 012" se refieren a las del plan. TASK-004, 006, 007, 008 y 009 son las del registro ya existente.

| ID | Objetivo → salida | Resp. | T | Dep. | Cierre (evidencia) |
|---|---|---|---|---|---|
| TASK-010 | Paquete de decisiones bloqueantes → registro en DECISIONS | DIR | S | TASK-004, 007, 008 | Las 9 decisiones B1-B9 respondidas por escrito |
| TASK-011 | Formalizar UX, arquitectura y seguridad en `03-ux`, `04-architecture`, `08-security` | GD | S | GATE-002 | Archivos persistidos y revisados por DIR |
| TASK-012 | Validación legal (= TASK-006) → informe de la asesoría | Cliente | M | — | Informe sobre RGPD, cookies, IVA, desistimiento y SCA |
| TASK-013 | Aprobación del plan y solicitud PLANNING→BUILD | DIR/Humano | S | 010, 011, 014 | Aprobación registrada en APPROVALS |
| TASK-014 | Stack, convenciones, ADR finales y contratos de API | TL | S | GATE-002 | ADR-001 a 012 aprobados o modificados |
| TASK-020 | Repo, ramas protegidas, CI (lint, test, SCA, secretos, SAST, presupuesto Lighthouse), entorno local | DO | M | ARR, 014 | CI verde en repo vacío; escaneo de secretos activo |
| TASK-021 | Esquema y migraciones: `occupancy` con exclusión, reserva, pago, `payment_event`, `consent`, `policy_version`, auditoría, outbox, roles de BD de mínimo privilegio | DAT | L | ARR, 014 | Migraciones con marcha atrás; pruebas de exclusión (CA-002) |
| TASK-022 | Semillas de ejemplo "por validar", sin datos reales | DAT | S | 021 | Datos sintéticos; sin PII (SEG-012) |
| TASK-023 | Esqueleto BE: config por entorno, errores, idempotencia, logs con redacción, cabeceras (CSP, HSTS) | BE | M | 014, 021 | SEG-008 base y SEG-011 verificados con pruebas |
| TASK-024 | Sistema de componentes FE con tokens de marca provisionales y accesibilidad base | FE | M | ARR, UX | Storybook o equivalente; axe sin críticos |
| TASK-030 | Precio y temporadas en servidor, mínimo de noches, instantánea | BE | M | 021, 023 | CA-012, 017, 034 con pruebas unitarias |
| TASK-031 | Disponibilidad y búsqueda | BE | M | 021, 023 | CA-001, 002, 009, 015 |
| TASK-032 | Reserva pendiente, hold, consentimientos versionados, conductor, edad mínima | BE | M | 030, 031 | CA-003, 010, 018, 033; concurrencia OK |
| TASK-033 | `PaymentProvider`, adaptador mock y adaptador sandbox, webhook firmado, máquina de estados, idempotencia | BE | L | 032 | CA-004, 006, 031, 032; SEG-002 en pruebas |
| TASK-034 | Worker: expiración de holds, pago tardío, conciliación, alineación hold y sesión de pago | BE | L | 033 | CA-005, 007; SEG-003 con prueba de carrera |
| TASK-035 | Antiabuso: límites de holds, anti-bot, verificación de email, alertas | BE | M | 032 | SEG-004 con prueba de abuso en staging |
| TASK-036 | FE de inicio, catálogo, ficha, resultados, resumen y datos (P01-P06) | FE | M | 024, 030-032 o mock | CA-015 a 018; sin saltos de layout |
| TASK-037 | FE de pago, estado y variantes (P07, P08) con temporizador accesible | FE | M | 036, 033 mock | CA-004, 006; aviso 2.2.1 |
| TASK-040 | Outbox, plantillas (confirmación, justificante, avisos de admin) | BE | M | 033 | CA-019, 025; SEG-015 |
| TASK-041 | Consulta código+email, cancelación, política versionada y reembolso | BE | L | 033, 034, B3, B5 | CA-008, 013, 020; SEG-001 y SEG-005 con pruebas |
| TASK-042 | Auth del panel con MFA, sesión, recuperación, CSRF y deny-by-default | BE | L | 023, B6 | CA-021; SEG-006 y SEG-017 con pruebas |
| TASK-043 | API admin (flota, sedes, tarifas, bloqueos, reservas, pagos), auditoría mínima, subida segura de imágenes | BE | L | 042, 030, 031, 041 | CA-011, 022-024; SEG-007 y SEG-009 |
| TASK-044 | FE del panel P14-P20 | FE | L | 043 | CA-011, 021-024 |
| TASK-045 | FE de consulta, cancelación, contacto, legales y cookies; SEO técnico y CWV | FE | L | 041, 024 | CA-013, 020, 026-029; SEG-016 |
| TASK-046 | Contacto con antispam y registro de consentimiento de cookies | BE | S | 023 | CA-029; sin cookies no técnicas previas |
| TASK-050 | Plan de pruebas CP con trazabilidad CA a CP | QA | M | 011 | Matriz CA-001 a 034 cubierta |
| TASK-051 | Pruebas de concurrencia y de pago automatizadas en CI | QA | L | 033, 034 | N peticiones, solo una gana; casos de webhook |
| TASK-052 | E2E, accesibilidad, SEO y CWV | QA | L | 044, 045, B-P12 | CA-014, 028, 030 con protocolo acordado |
| TASK-053 | Revisión de seguridad final de implementación (SEG-001 a 017, DAST) | SEC | L | 051, 052 | Informe sin Altas abiertas; veredicto SEC |
| TASK-054 | Corrección de defectos DEF y retests | BE/FE | M | 051-053 | DEF cerrados con evidencia |
| TASK-060 | Entornos de staging y producción, secretos, observabilidad, copias cifradas | DO | L | B1, B2, B8, B9, autorización | Entorno aprovisionado con `noindex` en staging |
| TASK-061 | Prueba de restauración completa y verificación de RPO/RTO | DO/QA | M | 060 | Acta de restauración |
| TASK-062 | Manual de administración y runbook operativo | RT | M | 044, 051 | Revisado por QA; cubre pago sin reserva, reembolso fallido, correo no entregado, código perdido |
| TASK-063 | Pipeline de despliegue con aprobación manual y despliegue autorizado | DO | S | 053, 060, autorización | Despliegue verificado, solo con autorización específica |
| TASK-064 | Cliente: datos reales, fotos, textos legales validados | Cliente | M | 012 | Imágenes de ejemplo sustituidas (R-008 [PM]) |
| TASK-065 | Índice documental y change-log | RT/GD | S | P5 | Archivos persistidos |
| TASK-070 | Auditoría de trazabilidad (RF→HU→CA→TASK→CP→SEG) | AUD | M | 054 | Informe sin huecos críticos |
| TASK-071 | Auditoría de entrega y go/no-go | AUD | M | 063, 070 | Informe con veredicto |

## Orden de implementación

1. **P0:** 010, 011, 012, 014, 013 (012 corre en paralelo y el resto hasta H0).
2. **P1:** 020, 021, 024 en paralelo. Después 022, 023.
3. **P2:** 030 y 031, luego 032, luego 033, luego 034. 035 y 036 corren en paralelo a 033. 037 sigue a 036.
4. **P3:** 040, 041, 042 y 046. Después 043, luego 044, y 045 en paralelo. 050 puede arrancar en P1.
5. **P4:** 051, 052, 053 y 054.
6. **P5:** 060, 061, 062, 064, 063, 065.
7. **P6:** 070 y 071.

## Dependencias críticas

- **Ruta crítica:** aprobación de alcance y GATE-002 → decisiones B1-B9 → TASK-014 → TASK-021 → 031/030 → 032 → 033 (adaptador real) → 034 → 041 → 051 → 053 → 061 + legal final + 064 → autorización de despliegue → 063.
- **Fuera de la ruta crítica:**
  - FE y panel (036, 037, 044, 045);
  - correo (040);
  - SEO;
  - documentación.
- **Decisiones bloqueantes de BUILD** (B1-B9). El cliente las eligió como puerta de inicio de BUILD:
  - B1 pasarela (PEND-012) y titularidad de la cuenta (PEND-011);
  - B2 hosting y región (UE, **[R]**);
  - B3 política de cancelación: valores, momento (ISS-002, DEC-025) y comisiones (PEND-009);
  - B4 validación legal (PEND-010). Contradicción abierta: el PM la trata como bloqueo de producción, no de planificación. **[R]** Para la puerta de BUILD basta con la asesoría contratada, el alcance legal definido y el inventario de datos. Los textos finales se necesitan antes de producción.
  - B5 acceso y cancelación con segundo factor, o enlace mágico (SEG-001);
  - B6 MFA obligatorio del admin (SEG-006);
  - B7 retención de datos (SEG-010);
  - B8 RPO/RTO (PEND-015);
  - B9 dominio y titularidad de cuentas (pasarela, dominio, correo, hosting).
- **Decisiones del Director que acompañan a B1-B9** (cambio de alcance frente al PM):
  - resolver ISS-004 a ISS-011, incluido el pago total;
  - auditoría mínima en el MVP;
  - VAL-020 con precio > 0;
  - priorización de P-004, P-007 y P-009.
- **Sí pueden empezar con dependencias abiertas** (mock, sandbox o aislamiento):

  | Tarea | Abierto | Cómo |
  |---|---|---|
  | 020, 021, 022 | B2 | Sin aprovisionar; el esquema usa PostgreSQL estándar |
  | 023, 024, 030, 031, 032 | marca, B3 | Tokens configurables; reglas parametrizadas |
  | 033 | B1 | `PaymentProvider` con mock y sandbox |
  | 034, 035 | B1 | Contra mock; el anti-bot se decide aparte |
  | 036, 037, 045, 046 | marca, textos | Textos legales como marcadores |
  | 040 | B9 | Proveedor simulado |
  | 042, 043, 044 | B6 | MFA implementado por defecto como obligatorio |

- **No pueden empezar o cerrar sin su decisión:**
  - Adaptador real de 033: B1.
  - Cierre de 041: B3 y B5.
  - 060 y 063: B2, B8, B9 y autorización.
  - 053 con SEG-010: B4 y B7.
  - Cierre de 031 y 030: PEND-013 (noche o día), con `date` como valor por defecto.

## Riesgos

| ID | Riesgo | P | I | Mitigación |
|---|---|---|---|---|
| R-PL-001 | Decisiones B1-B9 llegan tarde y paran el núcleo de pago | Alta | Alta | Paquete único TASK-010; mock; seguimiento en DECISIONS |
| R-PL-002 | Cambio de alcance (MFA, auditoría, precio > 0) sin CR | Media | Alta | DIR lo registra como CR antes de H0 |
| R-PL-003 | Sesión de pago con caducidad mayor que el hold (R-ARQ-02) | Media | Alta | PoC con el sandbox elegido en TASK-033 |
| R-PL-004 | Carrera hold, expiración y webhook produce doble reserva o cobro sin servicio (SEG-003) | Media | Alta | Exclusión en BD; pruebas de concurrencia en CI |
| R-PL-005 | Política de cancelación indefinida cambia el cálculo (ISS-002) | Alta | Media | Políticas versionadas (ADR-008); cierre de 041 condicionado a B3 |
| R-PL-006 | Validación legal tardía retrasa producción | Alta | Alta | Contratar asesoría pronto; textos como marcadores |
| R-PL-007 | Estimaciones S/M/L sin base histórica | Alta | Media | Usar solo como orden relativo; revisar tras H1 |
| R-PL-008 | Contratos de API cambian y rompen FE y BE | Media | Media | TL fija contratos; FE usa mock hasta que BE publique |
| R-PL-009 | Cliente no entrega datos reales y fotos | Media | Media | TASK-064 con dueño; imágenes de ejemplo sustituibles |
| R-PL-010 | Hosting sin PostgreSQL con exclusión o worker persistente | Baja | Alta | B2 antes de 060; criterios de hosting en TASK-014 |
| R-PL-011 | Sobrediseño en puntos de extensión (ADR-012) | Media | Baja | Solo estructura mínima |

## Definición de preparado

Una tarea puede empezar cuando cumple todo esto:

- Alcance y puerta aprobados.
- Dependencias cerradas, o mock acordado y documentado.
- Archivos propios asignados sin solapes con otro agente.
- CA y SEG aplicables identificados.
- Datos de prueba y sandbox disponibles.

## Definición de terminado

Una tarea se cierra cuando cumple todo esto:

- Cumple los CA y SEG de su fila.
- Tiene pruebas ejecutadas con evidencia.
- Pasa CI (lint, SCA, SAST, secretos).
- Tiene revisión de TL.
- No introduce secretos ni PII en repo y logs.
- Actualiza la trazabilidad.

**Del MVP completo:** CA-001 a 034 trazados, 0 Altas abiertas, revisión SEC aprobada, restauración probada, manual y runbook entregados. Nada se declara terminado sin evidencia.

## Plan de validación

Todo está propuesto y nada se ha ejecutado.

- **Unitarias:** precio y temporadas, reembolsos, máquina de estados.
- **Concurrencia:** N peticiones por el mismo vehículo y rango (CA-002, 003); carrera hold-expiración-webhook.
- **Pago:** firma inválida, replay, duplicado, desorden, importe o moneda distintos, pago tardío, contrato con el sandbox.
- **E2E:** R1 a R5.
- **Accesibilidad y CWV:** WCAG 2.1 AA y CWV móvil (CA-014, 030), con protocolo de PEND-012/P-012 acordado antes de P4.
- **SEO:** sitemap, canonical, JSON-LD y `noindex` donde corresponda.
- **Seguridad:** enumeración, fuerza bruta, XSS, CSRF, cabeceras, caché CDN, imágenes manipuladas, SCA.
- **Operación:** envío real en staging con SPF, DKIM y DMARC; restauración de copia.

## Controles de seguridad y operación aplicables

- **Acceso del cliente (SEG-001):** código CSPRNG, errores uniformes, límites, `no-store` y segundo factor para cancelar.
- **Pago (SEG-002, 003, 005):** firma sobre el cuerpo crudo, importe y moneda contra la BD, reembolso con tope e idempotencia.
- **Antiabuso y panel (SEG-004, 006, 007):** límites y anti-bot; MFA obligatorio; auditoría mínima.
- **Web (SEG-008, 009):** CSP, HSTS, CSRF; formatos de imagen cerrados y reprocesado.
- **Datos (SEG-010, 011):** retención, supresión, consentimientos versionados, logs sin PII.
- **Entornos (SEG-012):** gestor de secretos, sin datos reales fuera de producción, BD de mínimo privilegio, TLS.
- **Operación (SEG-013, 014):** copias cifradas con restauración probada; lockfile, SCA y ramas protegidas.
- **Despliegue:** sin ejecutarlo sin autorización específica y adicional.
- **Operación mínima:** runbook, alertas de webhook y conciliación, y `/health`.

## Entregables por fase

- **P0:** decisiones B1-B9, plan aprobado, UX y arquitectura persistidos.
- **P1:** repo, CI, esquema y migraciones.
- **P2:** módulos de precio, disponibilidad, reserva, pago y worker, con pruebas.
- **P3:** correo, consulta y cancelación, panel, web pública con SEO y legales.
- **P4:** `test-report.md` y `security-review.md`, con defectos cerrados.
- **P5:** `deployment-runbook.md`, manual admin, acta de restauración, índice documental.
- **P6:** `delivery-audit.md`.

## Decisiones pendientes

- **Bloquean BUILD:** B1-B9 y las del Director (resolución de ISS-004 a 011, auditoría mínima, precio > 0, prioridades P-004, P-007, P-009).
- **No bloquean BUILD:**
  - marca, nombre y tono tú/usted;
  - duración del hold (15 min es solo propuesta);
  - fianza (importe y texto);
  - edad mínima y antelación;
  - noche frente a día (ver arriba);
  - recuperación de contraseña del admin;
  - dónde se configura el correo de aviso;
  - qué pasa al desactivar con reservas futuras (DEC-028);
  - protocolo de CWV y alcance de accesibilidad (antes de P4);
  - metas de métricas;
  - sede única o múltiple y SEO por sede.
- **Del Director:** reconciliar CA-001 a 014 (ISS-001), confirmar TASK-004 y activar UX y Seguridad (TASK-009).

## Siguiente acción recomendada

El Director revisa este borrador y lanza TASK-010 para pedir B1-B9 al cliente. El plan solo se vuelve vinculante si el Director y el cliente lo aprueban de forma explícita. Hasta entonces, no se inicia BUILD ni se despliega.

---

## Registro documental (Gestor de Documentación)

- **Estado:** BORRADOR. **Fecha de persistencia:** 2026-10-26. **Sin fechas de calendario** (el plan no las incluye; los tamaños S/M/L son esfuerzo relativo).
- **Fuente:** reporte del Planificador de Proyecto entregado por el Director. El archivo de origen no traía línea de metadatos del agente.
- **Tareas del plan:** registradas en [TASKS](../00-control/TASKS.md) §2 con estado BACKLOG y las dependencias del plan. Colisiones de ID: ver ISS-024.
- **Decisiones bloqueantes B1 a B9 y del Director:** [DECISIONS](../00-control/DECISIONS.md) §4.
- **Riesgos del plan:** R-PL-001 a R-PL-011 en [RISKS](../00-control/RISKS.md) §5.
- **Trazabilidad:** tareas → RF/CA/SEG en [TRACEABILITY](../00-control/TRACEABILITY.md) §9.
- **Actividad y tarea:** [ACT-008](../00-control/AGENT-ACTIVITY.md), [TASK-016](../00-control/TASKS.md).
- **Solicitud PLANNING → BUILD:** no existe ([APPROVALS](../00-control/APPROVALS.md) §2).
- **Inconsistencias nuevas detectadas al persistir:** ISS-024 a ISS-033 en [RISKS](../00-control/RISKS.md).

## Enlaces relativos

[Estado del proyecto](../00-control/PROJECT-STATE.md) · [Decisiones](../00-control/DECISIONS.md) · [Riesgos e impedimentos](../00-control/RISKS.md) · [Trazabilidad](../00-control/TRACEABILITY.md) · [Tareas](../00-control/TASKS.md) · [Aprobaciones](../00-control/APPROVALS.md) · [requirements.md](../01-discovery/requirements.md) · [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) · [Especificación UX/UI](../03-ux/ux-specification.md) · [Arquitectura de solución](../04-architecture/solution-architecture.md) · [Revisión de seguridad](../08-security/security-review.md)
