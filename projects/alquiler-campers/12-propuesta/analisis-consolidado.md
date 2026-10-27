# Análisis consolidado — Web de alquiler de campers (España)

| Campo | Valor |
|---|---|
| Proyecto | Web de alquiler de campers (España) (`alquiler-campers`) |
| Estado del documento | BORRADOR |
| Fecha | 2026-10-26 |
| Fase del proyecto | INTAKE con GATE-001 PENDING. Análisis, diseño, arquitectura, revisión de seguridad de diseño y plan realizados como **borradores sin aprobación**; GATE-002 (DISCOVERY → DESIGN) PENDING; PLANNING → BUILD no solicitada; alcance **no aprobado** (según [PROJECT-STATE.md](../00-control/PROJECT-STATE.md), sección 1) |
| Oferta principal | **Opción B: entrega inicial acotada** (1 semana para entrega a revisión; 400 USD; solicitud de cambio **CR-001**, WAITING_FOR_APPROVAL, registrada en el control). El MVP completo (secciones 2 a 11) queda como **fase siguiente**, sin precio. Véase la sección «Opción B» |
| Propósito | Reunir en un solo archivo todo el análisis que respalda la [propuesta comercial](propuesta-comercial.md) |

> Este documento **consolida**; no redefine. Cada sección resume una fuente del expediente, conserva sus identificadores y cita su ubicación mediante enlaces relativos. Nada de lo que aquí figura está aprobado. Donde las fuentes se contradicen, se señala la contradicción y **no se elige una versión en silencio**: se usa la versión del Product Manager solo como **propuesta pendiente de aprobación** (DEC-029) y se deja la decisión al cliente.

**Leyenda de estado:** Confirmado · Supuesto · Recomendación · Pendiente. En los requisitos, el estado indicado es el **estado principal** (el primero que declara la fuente); cuando la fuente combina varios marcadores, el detalle se menciona en el texto.

## Resumen e índice

**Resumen (actualizado para la opción B).** La oferta principal es una **entrega inicial acotada** (sitio público con solicitud de reserva por correo), con objetivo de 1 semana para la entrega a revisión y un valor de 400 USD fijado por el usuario. Cubre pocos requisitos del MVP completo y desvía dos requisitos confirmados (RN-001 y RNF-010). El análisis del **MVP completo** (secciones 1 a 11) **se conserva íntegro** y pasa a ser la **fase siguiente**, con plazo preliminar de 28 a 36 semanas y sin precio.

| Parte | Contenido | Estado |
|---|---|---|
| [Opción B: entrega inicial acotada](#opción-b-entrega-inicial-acotada-oferta-principal) | Alcance, cobertura de requisitos, estimación D1–D7, riesgos, relación con el MVP completo y CR-001, desviación de RN-001 y RNF-010 | Recomendación (pendiente de CR-001) |
| [0 · Fuentes y estado](#0-fuentes-y-estado) a [11 · Resumen por estado](#11-resumen-por-estado) | Análisis del MVP completo (fase siguiente): brief, requisitos, MVP, UX, arquitectura, seguridad, plan y plazo, riesgos, decisiones y trazabilidad | BORRADOR (sin aprobación) |

## Opción B: entrega inicial acotada (oferta principal)

> **Estado: Recomendación, pendiente de CR-001.** Fuente: evaluación y estimación de la opción B del Planificador de Proyecto, transcrita de [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md) (persistida por el Director; se excluye su sección interna de precio). Es una estimación a confirmar, **no un compromiso ni un calendario**: no incluye fechas ni costos propios. El objetivo de 1 semana, la elección de la opción B y el valor de 400 USD son **Confirmado por el usuario** (instrucción explícita). **No se ha convertido ninguna moneda**; moneda de facturación e IVA están Pendientes.

El Planificador declara que leyó el catálogo de requisitos, el MVP y backlog y la estimación del MVP completo; **no revisó en detalle** `ux-specification`, `implementation-plan` ni la arquitectura, y la coherencia de la pila con [solution-architecture.md](../04-architecture/solution-architecture.md) queda **por verificar**.

### B.1 Veredicto de viabilidad

| Aspecto | Resultado | Estado |
|---|---|---|
| Capacidad frente al alcance | Con **1 persona de desarrollo completo**, la opción B completa **no cabe en 1 semana con holgura**; su plazo realista con 1 persona es de **1,5 a 2,5 semanas** desde el inicio, contando la latencia del cliente | Recomendación |
| Lo que sí cabe en 1 semana | Un **núcleo B**, sin holgura y con **riesgo alto**, para **entrega a revisión** (dirección de pruebas); la publicación en el dominio del cliente ocurre en D7–D10 según DNS y aprobación | Recomendación |
| Opción recomendada | Comprometer en 1 semana la **entrega a revisión** y la publicación en D8–D10; otra salida es usar 2 personas (unos 5 a 6 días hábiles) | Recomendación |
| Recortes que hacen caber el núcleo | Máximo 3 o 4 campers de ejemplo; tarifas y condiciones en una sola página; legales desde plantilla y aviso de cookies informativo sin analítica; formulario por servicio de correo o función serverless sin base de datos propia; datos estructurados solo de organización y vehículo básico; **una sola ronda** de cambios | Recomendación |
| Condiciones necesarias (todas) | 1 persona al 100 % (o con apoyo parcial de contenido y calidad); contenido del cliente completo el D1; acceso a dominio/DNS y hosting el D1–D2 (o dirección provisional); feedback en un día hábil como máximo; hosting estático con función para el formulario | Supuesto / Pendiente |

### B.2 Alcance

**Incluido (propuesta):** sitio público adaptable a móvil y rápido (inicio, catálogo y fichas con contenido y fotos de ejemplo sustituibles); tarifas orientativas y condiciones; contacto; páginas legales y de cookies como **borrador a validar** con la asesoría del cliente; SEO técnico base (metadatos, mapa del sitio, robots, datos estructurados, direcciones limpias); **formulario de solicitud de reserva** (fechas, camper, datos del conductor, aceptación de la privacidad con fecha y versión en el correo) que avisa por correo a la empresa para su confirmación manual; guía breve de edición de contenido; una ronda de ajustes.

**No incluido:** pago en línea; disponibilidad automática en tiempo real; panel de administración; cuentas y acceso del cliente a sus reservas; reembolsos; MFA y auditoría (pasan a la fase siguiente); hosting, dominio y correo de terceros y sus costes; asesoría legal; mantenimiento posterior; garantía de posicionamiento y de Core Web Vitals reales; otras rondas de cambios; extras, preguntas frecuentes y varios idiomas; formato de factura, moneda e impuestos (pendientes).

**Supuesto a confirmar:** «contenido editable por el equipo» significa que lo edita el proveedor mediante archivos de datos. Si el cliente debe editar solo, hace falta un gestor de contenidos ligero (+1 a 2 días) o pasa a la fase siguiente.

### B.3 Cobertura de requisitos de la entrega inicial

| Cobertura | Requisitos | Observaciones |
|---|---|---|
| **Cubierto** | RNF-002 (SEO técnico), RNF-003 (responsive), RNF-001 (rendimiento) | RNF-001 como **objetivo, sin garantía** de resultados reales |
| **Parcial** | RF-001 | Catálogo sin gestión en panel |
| | RF-006 | Solicitud de reserva; sin resumen de precio ni pago |
| | RF-010 | Aviso por correo; sin justificante de pago |
| | RF-015 | Contacto; las preguntas frecuentes ya estaban en la segunda fase |
| | RF-016 | Páginas legales como borrador a validar |
| | RF-017 | Aviso de cookies informativo, sin categorías de consentimiento |
| | RF-018 | SEO base |
| | RF-026 | Aviso por solicitud, no por reserva ni cancelación |
| | RN-026 | Fecha y versión de la aceptación solo en el correo |
| | RNF-004, RNF-005, RNF-006, RNF-008, RNF-013, RNF-014 | Parciales; la accesibilidad es solo básica, sin auditoría de nivel AA; RNF-013 (contenido sustituible) lo sustituye el proveedor, no el cliente sin desarrollo |
| **No cubierto** | RF-002 a RF-005 | Búsqueda, disponibilidad, precio y extras |
| | RF-007 a RF-009 | Bloqueo temporal y pago |
| | RF-011 a RF-013 | Consulta, código de acceso y cancelación |
| | RF-019 a RF-025 | Panel de administración |
| | RF-032 | Expiración de reservas |
| | RN-003, RN-010 | Sin reservas ni precio calculado en servidor |
| | RNF-007, RNF-009, RNF-010, RNF-011 | Integridad y concurrencia, trazabilidad de pagos, configurabilidad sin cambios de código y copias/recuperación |

### B.4 Desviación de RN-001 y RNF-010 (a confirmar con el cliente)

El cliente confirmó que **la flota y las sedes sean configurables desde un panel** (RN-001, RNF-010; ver secciones 1 y 2 de este análisis). En la entrega inicial **no hay panel**: la flota y las sedes pasan a **contenido editado por el proveedor**; el panel pasa a la fase siguiente. Es un **cambio de alcance** que sustituye temporalmente el MVP completo por la entrega inicial acotada. Se registra como **CR-001** (estado WAITING_FOR_APPROVAL según el Director). **No se asume aceptado.** Ningún elemento de la sección 2 se renumera ni se retira: RN-001 y RNF-010 siguen Confirmados en el brief.

### B.5 Estimación D1–D7 (relativa al arranque)

| Día | Hito | Entregable | Dependencia del cliente |
|---|---|---|---|
| D1 | Arranque | Contenido y accesos recibidos | Datos de campers, fotos o aceptar las de ejemplo; datos legales, contacto, correo de destino y marca |
| D2 | Esqueleto | Sitio en la dirección de revisión, con inicio y una ficha | Acceso a DNS y hosting (D1–D2) o permiso de dirección provisional; textos de condiciones o aceptar un borrador genérico |
| D3 | Catálogo | Catálogo, fichas y contacto completos | — |
| D4 | Formulario | Formulario de extremo a extremo, legales en borrador y SEO | Correo de destino |
| D5 | Entrega a revisión | Pruebas de calidad y entrega a revisión del cliente | — |
| D6 | Ajustes | Una ronda de cambios | Feedback en un día hábil como máximo (D5 → D6) |
| D7 | Publicación | En el dominio del cliente, solo si el DNS y la aprobación llegaron; si no, D8 o después | Aprobación final (D6–D7) |

**Ruta crítica:** contenido del cliente (D1) → páginas y datos → formulario, junto con el acceso al DNS → registros del dominio de correo → pruebas de calidad → feedback del cliente → ajustes → publicación.

**Tareas del núcleo** (sin cifras de esfuerzo en este documento): T1 arranque, repositorio, hosting estático, despliegue y base de mockups; T2 inicio, catálogo, fichas, tarifas, condiciones y contacto (datos en archivo); T3 responsive, accesibilidad básica e imágenes optimizadas; T4 SEO base; T5 legales en borrador y aviso de cookies; T6 formulario de solicitud (antispam, correo, fecha y versión de la aceptación); T7 dominio, HTTPS y registros SPF/DKIM/DMARC (más la espera del DNS); T8 pruebas de calidad (móvil, formulario, enlaces, rendimiento); T9 una ronda de ajustes; T10 publicación y guía de edición de contenido. Dependencias: T2 depende de T1 y del contenido; T3, T4 y T6 de T2; T5 de los datos de la empresa; T6 también del correo de destino; T7 del acceso al DNS; T8 de T3 a T7; T9 de T8 y del cliente; T10 de T9.

### B.6 Riesgos de la opción B

Numeración del Planificador (colisiona con otros riesgos del expediente; se distingue con **[OPB]** y el Director debe asignar identificadores definitivos al registrarlos en RISKS).

| ID | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R-001 [OPB] | Contenidos y fotos tardíos o de baja calidad | Alta | Alto | Contenido de ejemplo marcado; fecha límite el D1 |
| R-002 [OPB] | Textos legales y de cookies sin validar | Media | Alto | Publicar como borrador; asesoría legal del cliente fuera de alcance |
| R-003 [OPB] | Entregabilidad del correo (spam, DNS tardío) | Media | Alto | SPF/DKIM/DMARC; copia en el servicio de correo; prueba con la cuenta real |
| R-004 [OPB] | Solicitudes perdidas al no haber base de datos | Baja | Alto | Registro del proveedor de correo y copia a un segundo buzón |
| R-005 [OPB] | SEO sin garantías de posicionamiento | Alta | Medio | Prometer solo lo técnico, no posiciones |
| R-006 [OPB] | Sin margen: cualquier retraso rompe la semana (la entrega se mueve 1:1) | Alta | Alto | Núcleo recortado; ampliar el plazo o el equipo |
| R-007 [OPB] | Rehacer parte de la web pública al migrar al MVP completo | Media | Medio | Elegir una pila compatible con 04-architecture (por verificar) |
| R-008 [OPB] | Estacionalidad: la web debe estar publicada antes de la temporada alta | Media | Medio | Confirmar con el cliente su temporada |

### B.7 Relación con el MVP completo y con CR-001

- **CR-001** (WAITING_FOR_APPROVAL) sustituye el MVP completo por la entrega inicial acotada como oferta principal y está registrada en [CHANGE-REQUESTS.md](../00-control/CHANGE-REQUESTS.md) (pendiente de aprobación formal del cliente, PEND-044). No modifica el alcance mientras no sea APPROVED. Aclara que 28–36 semanas (MVP completo, DEC-033) y 1 semana (entrega inicial) son **alcances distintos** y no se suman ni se comparan (ISS-040). El control del expediente deja sin clasificar RF-014, RF-027 a RF-031 y RNF-012 (ISS-042); esta propuesta tampoco les asigna cobertura.
- El **MVP completo** (secciones 2 a 11) es la **fase siguiente**: pago seguro, disponibilidad en tiempo real, panel, seguridad (MFA, auditoría mínima, segundo paso para cancelar, precio mayor que cero) y operación. Plazo preliminar **28 a 36 semanas** desde la autorización de su construcción; **sin precio**, a cotizar aparte tras confirmar las decisiones B1 a B9. La estimación 28–36 sigue aplicando al MVP completo y **no se reestimó** considerando lo que la entrega inicial pudiera reutilizar (Pendiente: confirmar con el Planificador).
- Los hallazgos de seguridad SEG-001 a SEG-017 son de la revisión **de diseño** del MVP completo; para la entrega inicial no existe una revisión de seguridad propia ni se ejecutó ninguna prueba.
- Los mockups de la entrega inicial (01, 03 y 10 en versión `-entrega-inicial`, 11, 12 y 13) y los de la fase siguiente (01 a 10) se distinguen con insignia en [mockups/index.html](mockups/index.html); los estados alternativos están en [mockups/14-estados.html](mockups/14-estados.html).

### B.8 Decisiones y dudas pendientes de la opción B

| # | Tema | Estado |
|---|---|---|
| 1 | Elegir entre el núcleo en 1 semana (entrega a revisión), la opción B completa en más tiempo, o 2 personas (PEND-046) | Pendiente (el usuario confirmó 1 semana; la propuesta lo califica como entrega a revisión) |
| 2 | Quién edita el contenido: el proveedor o el cliente (PEND-045) | Pendiente |
| 3 | Moneda de facturación e impuestos (PEND-043; la cifra se fijó en USD y no se convierte) | Pendiente |
| 4 | Aprobación formal del cliente de la desviación de RN-001 y RNF-010 y de CR-001 (PEND-044) | Pendiente |
| 5 | Compatibilidad de la pila con 04-architecture (PEND-047; ADR-001 y ADR-002 proponen un monolito modular con PostgreSQL) | Pendiente |
| 6 | Tensión con el brief («presupuesto y fechas no entran en el contrato») frente a un valor y un plazo ofertados (ISS-038) | Pendiente |

## 0. Fuentes y estado

| Sección | Fuente en el expediente | Estado de la fuente | Fecha de la fuente |
|---|---|---|---|
| Brief | [client-brief.md](../00-intake/client-brief.md) | BORRADOR | 2026-10-26 |
| Requisitos | [requirements.md](../01-discovery/requirements.md) | BORRADOR | 2026-10-26 |
| MVP y backlog | [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) | BORRADOR | 2026-10-26 |
| UX | [ux-specification.md](../03-ux/ux-specification.md) | BORRADOR | 2026-10-26 |
| Arquitectura | [solution-architecture.md](../04-architecture/solution-architecture.md) | BORRADOR | 2026-10-26 |
| Seguridad (revisión de diseño; no se ejecutó ninguna prueba) | [security-review.md](../08-security/security-review.md) | BORRADOR | 2026-10-26 |
| Plan de implementación | [implementation-plan.md](../05-planning/implementation-plan.md) | BORRADOR | 2026-10-26 |
| Estimación de plazo | [estimacion-plazo.md](../05-planning/estimacion-plazo.md) (persistida por el Director después de la elaboración de la versión 0.1; el contenido se transcribió tal como lo entregó el Director). `implementation-plan.md` declara «sin fechas» y no contiene semanas | BORRADOR (Recomendación a confirmar) | 2026-10-26 |
| Control: estado | [PROJECT-STATE.md](../00-control/PROJECT-STATE.md) | BORRADOR | 2026-10-26 |
| Control: decisiones | [DECISIONS.md](../00-control/DECISIONS.md) | BORRADOR | 2026-10-26 |
| Control: riesgos e impedimentos | [RISKS.md](../00-control/RISKS.md) | BORRADOR | 2026-10-26 |
| Control: trazabilidad | [TRACEABILITY.md](../00-control/TRACEABILITY.md) | BORRADOR. Auditoría de trazabilidad: TRAZABILIDAD_PARCIAL (informada por el Director; el informe no está en el expediente leído) | 2026-10-26 |
| Control: aprobaciones | [APPROVALS.md](../00-control/APPROVALS.md) | GATE-001 y GATE-002 PENDING | 2026-10-26 |
| Control: tareas | [TASKS.md](../00-control/TASKS.md) | BORRADOR | 2026-10-26 |
| Control: solicitudes de cambio | [CHANGE-REQUESTS.md](../00-control/CHANGE-REQUESTS.md) | **CR-001** (opción B) registrada: WAITING_FOR_APPROVAL | 2026-10-26 |
| Estimación de la opción B | [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md). Su sección 7 es **interna** y no se transcribe. Véase la sección «Opción B» | BORRADOR (Recomendación a confirmar) | 2026-10-26 |

**Nota de fuente:** los encabezados de `requirements.md` y `mvp-and-backlog.md` citan archivos temporales de origen del reporte del agente; no se reproducen aquí. El contenido consolidado proviene de los propios documentos del expediente.

## 1. Resumen del brief

Fuente: [client-brief.md](../00-intake/client-brief.md). El mensaje inicial se recibió como un resumen del Director, no como texto literal (limitación documental declarada por la fuente).

| Tema | Contenido | Estado |
|---|---|---|
| Idea original del cliente | Una web de alquiler de campers con reservas, pasarela de pago segura y atención a la experiencia de usuario (UX), la velocidad y el SEO | Confirmado |
| Respuestas literales del cliente a las 7 preguntas de la propuesta inicial | 1: «esta en españa» · 2: «que sea configurable» · 3: «pon tu las reglas» · 4: «lo que creas conveniente» · 5: «crealo» · 6: «no y ponlo que no abra migracion» · 7: «no entra en el contrato» (no se conservan los textos de las preguntas; la relación de cada respuesta con un tema es una interpretación del Gestor, pendiente de confirmar) | Confirmado (las respuestas) · Pendiente (su relación con cada pregunta) |
| Problema u oportunidad | Negocio de alquiler de campers en España que necesita reservar en línea, cobrar con seguridad y gestionar alquileres sin intermediación manual | Supuesto |
| Usuarios y actores | Cliente particular (visitante), administrador de la empresa (al menos un rol), pasarela de pago, servicio de correo transaccional y asesoría legal/fiscal; operador de sede en Fase 2 | Supuesto |
| Objetivo del proyecto | Canal propio en línea para reservar y pagar, gestión desde panel y base SEO técnica sin garantía de posicionamiento; reducir la gestión manual y evitar dobles reservas. Metas cuantitativas: no definidas | Confirmado (canal propio, SEO técnico sin garantía) · Recomendación (reducir gestión manual) |
| Restricciones conocidas | Negocio en España; flota y sedes configurables desde un panel; sin migración ni integración con sistemas existentes; presupuesto y fechas fuera del contrato | Confirmado |
| Supuestos de partida | Español, euros, zona horaria Europe/Madrid, cliente particular, pago con tarjeta, una sola empresa, una reserva = un vehículo, recogida y devolución en la misma sede | Supuesto |
| Delegación del cliente | Las reglas y decisiones resultantes de «pon tu las reglas», «lo que creas conveniente» y «crealo» son **Recomendación**: el cliente delegó pero no las ha confirmado | Recomendación |

**Contraste señalado por la fuente:** la propuesta inicial presentada al cliente y el MVP del Product Manager no coinciden en todo (la propuesta inicial incluía consulta y cancelación por el cliente y panel básico en el MVP, y listaba «extras y seguros» y «facturación automática» como ampliaciones; el Product Manager sitúa los extras y la factura automática en Fase 2). Véanse ISS-004 e ISS-006 (sección 9.4).

## 2. Requisitos

Fuente: [requirements.md](../01-discovery/requirements.md) (Analista de Negocio, **COMPLETADO_CON_PENDIENTES**). Todos los requisitos figuran como **PROPUESTO** en [TRACEABILITY.md](../00-control/TRACEABILITY.md) §1 y §2; ninguno está aprobado. «Destino» indica la prioridad del Analista (MVP, F2 = segunda fase, AMP = ampliación) y, tras la flecha, el destino en la propuesta del Product Manager cuando difiere (DEC-029).

### 2.1 Requisitos funcionales

| ID | Requisito | Destino | Estado | Fuente |
|---|---|---|---|---|
| RF-001 | Catálogo de campers con ficha (descripción, plazas, equipamiento, fotos, precio orientativo). Fotos de ejemplo hasta que existan reales. Necesidad confirmada; contenido de ficha Recomendación; fotos reales Pendiente | MVP | Confirmado | [requirements.md](../01-discovery/requirements.md) §6 |
| RF-002 | Búsqueda por fechas de recogida y devolución y por sede (cuando hay varias) | MVP | Confirmado | requirements.md §6 |
| RF-003 | Disponibilidad por vehículo y fechas, validada en servidor | MVP | Confirmado | requirements.md §6 |
| RF-004 | Cálculo y desglose de precio (tarifa por noche, temporadas, extras, impuestos, fianza informativa) antes de pagar | MVP | Recomendación | requirements.md §6 |
| RF-005 | Selección de extras opcionales configurables | MVP → F2 (PM, ISS-006) | Recomendación | requirements.md §6; mvp-and-backlog.md P-009 |
| RF-006 | Flujo de reserva: datos del conductor principal, resumen, aceptación de condiciones y pago | MVP | Recomendación | requirements.md §6 |
| RF-007 | Bloqueo temporal de fechas durante el pago | MVP | Recomendación | requirements.md §6 |
| RF-008 | Pago en línea mediante pasarela segura. Necesidad confirmada; proveedor Pendiente; con tarjeta Supuesto | MVP | Confirmado | requirements.md §6 |
| RF-009 | Autenticación reforzada del pago (3-D Secure/SCA) gestionada por la pasarela. Validar PSD2 | MVP | Recomendación | requirements.md §6 |
| RF-010 | Confirmación en pantalla y correos transaccionales (RN-018). En el MVP del PM: confirmación con justificante; los demás tipos sin asignar (ISS-009) | MVP | Recomendación | requirements.md §6 |
| RF-011 | Gestión de la reserva por el cliente: consultar estado, detalle y justificante | MVP | Confirmado | requirements.md §6 |
| RF-012 | Acceso a la reserva mediante cuenta de cliente **o** código de reserva + email. PM: solo código + email en el MVP; cuentas en F2 (ISS-008) | MVP | Supuesto | requirements.md §6 |
| RF-013 | Cancelación por el cliente con cálculo automático de reembolso según política | MVP | Recomendación | requirements.md §6 |
| RF-014 | Modificación de fechas, vehículo o extras por el cliente | F2 | Recomendación | requirements.md §6 |
| RF-015 | Formulario de contacto y página de preguntas frecuentes. PM: contacto en MVP; FAQ en F2 (ISS-007) | MVP | Recomendación | requirements.md §6 |
| RF-016 | Páginas legales: aviso legal, privacidad, cookies, condiciones de alquiler. Contenido a validar con asesoría | MVP | Recomendación | requirements.md §6 |
| RF-017 | Banner de consentimiento de cookies con categorías. Validar LSSI-CE | MVP | Recomendación | requirements.md §6 |
| RF-018 | Datos y páginas indexables para SEO: URLs limpias, metadatos, sitemap, datos estructurados, páginas por vehículo y sede | MVP | Confirmado | requirements.md §6 |
| RF-019 | Panel de administración con acceso autenticado por rol | MVP | Supuesto | requirements.md §6 |
| RF-020 | Gestión de flota: alta, edición, desactivación, fotos, equipamiento, plazas, fianza, sede base | MVP | Confirmado | requirements.md §6 |
| RF-021 | Gestión de sedes: alta, edición, desactivación, horarios y contacto | MVP | Confirmado | requirements.md §6 |
| RF-022 | Gestión de tarifas, temporadas, mínimos de noches y extras. Configurable confirmado; detalle Recomendación. PM: la parte de extras pasa a F2 | MVP | Confirmado | requirements.md §6 |
| RF-023 | Gestión de reservas: listar, filtrar, ver detalle, cancelar y anotar | MVP | Recomendación | requirements.md §6 |
| RF-024 | Bloqueo manual de fechas de un vehículo (mantenimiento, uso propio) | MVP | Recomendación | requirements.md §6 |
| RF-025 | Gestión de pagos: ver transacciones y emitir reembolsos totales o parciales | MVP | Recomendación | requirements.md §6 |
| RF-026 | Aviso interno al administrador por nueva reserva o cancelación. PM: aviso mínimo (incluye pago tardío sin disponibilidad); centro de avisos completo en F2 (ISS-010) | MVP | Recomendación | requirements.md §6 |
| RF-027 | Edición de plantillas de correo y de textos de políticas con versionado | F2 | Recomendación | requirements.md §6 |
| RF-028 | Creación manual de reservas (por teléfono o mostrador) | F2 | Recomendación | requirements.md §6 |
| RF-029 | Informes básicos (reservas, ocupación, ingresos) y registro de auditoría de cambios en el panel. Seguridad recomienda una auditoría mínima en el MVP (SEG-007, ISS-029) | F2 | Recomendación | requirements.md §6 |
| RF-030 | Roles adicionales (operador de sede) | F2 | Recomendación | requirements.md §6 |
| RF-031 | Preautorización de fianza en línea, saldo diferido con recordatorios, factura automática, otros medios de pago, multi-idioma, cupones, reseñas, subida de documentos del conductor, contrato digital con firma, sincronización con canales externos. Solo si el cliente lo decide. PM: depósito + saldo y factura automática en F2 (ISS-004) | AMP | Pendiente | requirements.md §6 |
| RF-032 | Expiración automática de reservas impagadas y liberación de fechas (RN-015) | MVP | Recomendación | requirements.md §6 |

### 2.2 Requisitos no funcionales

| ID | Requisito | Estado | Fuente |
|---|---|---|---|
| RNF-001 | Rendimiento: meta recomendada de Core Web Vitals «buenos» en móvil (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1); imágenes optimizadas y carga diferida. Necesidad de velocidad confirmada; métricas Recomendación | Confirmado | [requirements.md](../01-discovery/requirements.md) §12 |
| RNF-002 | SEO técnico: HTML indexable, URLs limpias, metadatos, sitemap, datos estructurados, versión móvil. No se garantiza posicionamiento | Confirmado | requirements.md §12 |
| RNF-003 | Responsive, mobile-first y compatibilidad con navegadores modernos | Recomendación | requirements.md §12 |
| RNF-004 | Usabilidad: flujo corto y claro, con progreso y mensajes de error comprensibles. «Excelente UX» confirmada; métrica Recomendación | Confirmado | requirements.md §12 |
| RNF-005 | Accesibilidad: objetivo WCAG 2.1 AA, a validar si es obligatoria | Recomendación | requirements.md §12 |
| RNF-006 | Seguridad: HTTPS, sin almacenar datos de tarjeta, control de acceso por rol, contraseñas protegidas, protección contra vulnerabilidades habituales, límites de intentos. «Pago seguro» confirmado; medidas Recomendación | Confirmado | requirements.md §12 |
| RNF-007 | Integridad y concurrencia: operaciones de reserva y pago transaccionales, sin doble reserva | Recomendación | requirements.md §12 |
| RNF-008 | Privacidad por diseño: minimización, retención definida (validar legal) | Recomendación | requirements.md §12 |
| RNF-009 | Trazabilidad: registro de eventos de pago y cambios de estado | Recomendación | requirements.md §12 |
| RNF-010 | Configurabilidad: flota, sedes, tarifas y políticas editables sin cambios de código | Confirmado | requirements.md §12 |
| RNF-011 | Disponibilidad y copias de seguridad: objetivos y plazos de recuperación (no se inventan porcentajes) | Pendiente | requirements.md §12 |
| RNF-012 | Escalabilidad: dimensionar según tráfico y reservas esperadas (no informados) | Pendiente | requirements.md §12 |
| RNF-013 | Contenido sustituible: las imágenes de ejemplo deben poder reemplazarse sin desarrollo | Recomendación | requirements.md §12 |
| RNF-014 | Fiabilidad de correo: entregabilidad configurada correctamente | Recomendación | requirements.md §12 |

### 2.3 Reglas de negocio y validaciones

Todas **PROPUESTO**. Los valores numéricos (tramos de cancelación, porcentajes, minutos de bloqueo, edad mínima, etc.) no están fijados; los citados como ejemplo son Recomendación o Pendiente.

| ID | Regla | Estado | Fuente |
|---|---|---|---|
| RN-001 | Flota y sedes son datos configurables desde el panel; no se fijan cifras en el sistema | Confirmado | [requirements.md](../01-discovery/requirements.md) §7 |
| RN-002 | Una reserva = 1 vehículo + rango de fechas + sede de recogida y de devolución | Supuesto | requirements.md §7 |
| RN-003 | Un vehículo no puede tener dos reservas confirmadas o bloqueadas solapadas, ni solaparse con un bloqueo manual (derivada de «robusto») | Recomendación | requirements.md §7 |
| RN-004 | El alquiler se calcula por noches; se admite tiempo de preparación entre reservas, configurable (valor Pendiente) | Recomendación | requirements.md §7 |
| RN-005 | Moneda euros, idioma español, zona horaria Europe/Madrid | Supuesto | requirements.md §7 |
| RN-006 | Recogida y devolución en distinta sede: no se asume (pregunta Q6) | Pendiente | requirements.md §7 |
| RN-007 | Precio por noche por vehículo, variable por temporada; temporadas = rangos de fechas configurables sin solapes | Recomendación | requirements.md §7 |
| RN-008 | Mínimo de noches configurable por temporada (valores del cliente, Pendiente) | Recomendación | requirements.md §7 |
| RN-009 | Antelación mínima y duración máxima de reserva configurables (valores Pendiente) | Recomendación | requirements.md §7 |
| RN-010 | El precio se calcula siempre en servidor y se congela al crear la reserva; cambios posteriores de tarifa no afectan a reservas existentes | Recomendación | requirements.md §7 |
| RN-011 | Se muestra precio final con impuestos y desglose (alquiler, extras, fianza). IVA a validar con asesoría | Recomendación | requirements.md §7 |
| RN-012 | Extras: precio fijo por reserva o por noche, con stock opcional; precios definidos por la empresa | Recomendación | requirements.md §7 |
| RN-013 | Pago: opción recomendada por el Analista, depósito (% a definir) + saldo hasta fecha límite; alternativa más simple, pago total al reservar. **PM/DEC-001: pago total en el MVP** (ISS-005). Decisión Q1 | Recomendación | requirements.md §7 |
| RN-014 | Cancelación por el cliente: reembolso escalonado por antelación (tramos y porcentajes Pendiente); el reembolso se calcula según la política vigente al reservar (Analista). ISS-002 | Recomendación | requirements.md §7 |
| RN-015 | Reservas impagadas: una reserva en Pendiente de pago expira al terminar el bloqueo y libera las fechas; un pago tardío se confirma solo si las fechas siguen libres, si no se reembolsa y se avisa | Recomendación | requirements.md §7 |
| RN-016 | Bloqueo temporal durante el pago de duración configurable; se propone 15 minutos como valor inicial no confirmado | Recomendación | requirements.md §7 |
| RN-017 | Fianza: importe configurable por vehículo, mostrado antes de pagar; en el MVP se gestiona en la entrega (no se cobra en la web). Decisión Q2 | Recomendación | requirements.md §7 |
| RN-018 | Correos transaccionales mínimos: reserva iniciada con enlace de pago si procede, pago recibido y reserva confirmada, pago fallido, reserva expirada, cancelación y reembolso, recordatorio previo a la recogida, aviso interno al administrador | Recomendación | requirements.md §7 |
| RN-019 | Cancelación por la empresa (avería, imposibilidad): reembolso total o alternativa de vehículo, con aviso inmediato | Recomendación | requirements.md §7 |
| RN-020 | No presentación y devolución tardía: condiciones y penalizaciones a definir en las condiciones de alquiler | Pendiente | requirements.md §7 |
| RN-021 | Estados de reserva: Pendiente de pago (bloqueada) → Confirmada → En curso → Completada; salidas: Expirada, Cancelada por cliente, Cancelada por empresa, No presentada | Recomendación | requirements.md §7 |
| RN-022 | Estados de pago: Pendiente, Pagado, Parcialmente pagado (solo con depósito), Fallido, Reembolsado parcialmente, Reembolsado totalmente; disputa/contracargo en Fase 2 | Recomendación | requirements.md §7 |
| RN-023 | Una reserva solo pasa a Confirmada cuando el servidor recibe la confirmación del pago desde la pasarela; la redirección del navegador no basta | Recomendación | requirements.md §7 |
| RN-024 | Conductor: edad mínima, antigüedad y tipo de permiso, conductores adicionales y verificación de documentos; no se fija ningún valor (Q5 y validación legal) | Pendiente | requirements.md §7 |
| RN-025 | Acceso: el cliente solo ve sus reservas; el acceso por código requiere un segundo dato (email) y el código no debe ser adivinable | Recomendación | requirements.md §7 |
| RN-026 | Datos personales y consentimientos: solo datos necesarios, con registro de fecha y versión aceptada; marketing opcional, aparte y no premarcado (validar RGPD/LOPDGDD) | Recomendación | requirements.md §7 |
| RN-027 | Facturación: se emite justificante de pago al cobrar; la factura formal se define con asesoría (Q4) | Pendiente | requirements.md §7 |

**Validaciones (VAL-001 a VAL-022).** El prefijo VAL es local del reporte del Analista y no está en el catálogo corporativo (ISS-013, DEC-032). Todas son Recomendación: fechas reales y en Europe/Madrid (VAL-001); recogida no anterior a hoy más la antelación mínima (VAL-002); devolución posterior a la recogida (VAL-003); duración entre mínimo de noches y máximo (VAL-004); sin solape con reservas ni bloqueos (VAL-005); horas dentro del horario de la sede (VAL-006); disponibilidad revalidada en servidor al buscar, resumir, iniciar el pago y confirmar (VAL-007); nombre, correo, teléfono, edad mínima, documento (solo si se decide), ocupantes, aceptaciones, extras y antispam (VAL-008 a VAL-016); importe calculado por el servidor, notificaciones de la pasarela verificadas e idempotentes y reintentos solo mientras dure el bloqueo (VAL-017 a VAL-019); en el panel, temporadas sin solape, precios ≥ 0 (la seguridad recomienda > 0, SEG-005), mínimo de noches ≥ 1, no eliminar sedes o vehículos con reservas futuras, y validación de imágenes (VAL-020 a VAL-022).

**Puntos para validación legal** (no es asesoramiento jurídico ni requisito confirmado): protección de datos (RGPD/LOPDGDD), cookies y servicios de la sociedad de la información (LSSI-CE), consumidores (información precontractual, condiciones generales, precio final con impuestos, desistimiento), IVA, pagos (PSD2/SCA), facturación, y otros (seguro, accesibilidad web si aplica, licencias de la actividad).

### 2.4 Criterios de aceptación: versión del Analista de Negocio (CA-001 a CA-014)

Fuente: [requirements.md](../01-discovery/requirements.md) §13. Son Recomendación y se validarán con el cliente antes de usarse como base de prueba. **Los mismos identificadores tienen otro contenido en la versión del Product Manager (sección 3.3): la reconciliación está pendiente (ISS-001, DEC-030, TASK-007).**

| ID | Criterio (versión del Analista) | Traza | Estado |
|---|---|---|---|
| CA-001 | Dado un rango con un camper libre, cuando el cliente busca, entonces lo ve disponible con precio total desglosado | RF-002, RF-003, RF-004 | Recomendación |
| CA-002 | Dado un camper reservado o bloqueado en parte del rango, cuando busca, entonces no aparece disponible | RN-003, VAL-005 | Recomendación |
| CA-003 | Dados dos clientes que reservan a la vez el mismo camper y fechas, solo uno obtiene el bloqueo y el otro recibe aviso | RN-003, RN-016, RNF-007 | Recomendación |
| CA-004 | Dado un pago correcto, la reserva pasa a Confirmada solo tras la notificación de la pasarela y se envían los correos | RN-023, RN-018 | Recomendación |
| CA-005 | Dado un pago no completado, la reserva expira al terminar el bloqueo y las fechas quedan libres | RN-015, RN-016 | Recomendación |
| CA-006 | Dado un pago fallido o autenticación rechazada, no se confirma y se permite reintento mientras dure el bloqueo | RF-008, RF-009, VAL-019 | Recomendación |
| CA-007 | Dado un pago tras expirar la reserva, se confirma si las fechas siguen libres; si no, se reembolsa y se avisa | RN-015 | Recomendación |
| CA-008 | Dada una cancelación del cliente, el reembolso corresponde al tramo de la política vigente **al reservar** | RF-013, RN-014 | Recomendación |
| CA-009 | Dadas fechas inválidas (pasadas, devolución anterior, bajo el mínimo de noches), el sistema las rechaza con mensaje claro | VAL-001 a VAL-004 | Recomendación |
| CA-010 | Dado un cliente sin aceptar condiciones y privacidad, no puede continuar al pago | VAL-014, RN-026 | Recomendación |
| CA-011 | Dado un administrador, cuando crea o edita una sede o un camper, aparece en la web sin cambios de código | RN-001, RF-020, RF-021 | Recomendación |
| CA-012 | Dado un cambio de tarifa, no altera el precio de reservas ya creadas | RN-010 | Recomendación |
| CA-013 | Dado un cliente, no puede ver reservas de otros | RN-025 | Recomendación |
| CA-014 | Dada la medición en móvil, las páginas clave alcanzan los umbrales acordados en RNF-001 | RNF-001 | Recomendación |

### 2.5 Exclusiones y supuestos del análisis

- **Fuera de alcance:** [Confirmado] migración de datos e integración con sistemas existentes; [Confirmado] estimación de presupuesto y fechas (fuera del contrato); [Recomendación] aplicación móvil nativa y marketplace multiempresa, canales externos de venta (OTA) y GPS o telemática, producción de fotografía y vídeo reales, asesoramiento jurídico y fiscal, campañas de marketing o SEO continuo y garantía de posicionamiento, y las ampliaciones de RF-031 mientras el cliente no las apruebe.
- **Supuestos (todos Supuesto):** español y euros; una sola empresa; clientes particulares; pago con tarjeta; cuenta de cliente o código de reserva; panel con al menos un rol administrador; una reserva = un vehículo; recogida y devolución en la misma sede hasta decidir Q6.
- **Pendientes que no cambian alcance** (se resuelven en diseño o con contenido): valores de tramos de cancelación, porcentajes de depósito y mínimos de noches; textos de condiciones de alquiler; proveedor de correo; contenido de FAQ.

## 3. MVP, backlog y exclusiones

Fuente: [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) (Product Manager). **No aprueba alcance**: es una propuesta en BORRADOR y todas sus decisiones de producto son Recomendación (el cliente delegó pero no confirmó; DEC-029). El MVP es el mínimo que cierra el ciclo *buscar → ver precio → reservar → pagar → recibir confirmación → administrar*, con cumplimiento básico (legal y cookies) y la base SEO que el cliente pidió. Notas del PM sobre el MVP: pago total al reservar; fianza informativa gestionada en la entrega; recogida y devolución en la misma sede; solo español y euros; edad mínima declarada configurable; documentos verificados en persona; reservas telefónicas cubiertas provisionalmente con bloqueo manual (RF-024) porque el alta manual (RF-028) va a F2; imágenes de ejemplo sustituibles desde el panel; valores de cancelación, mínimos de noches, temporadas y extras configurables y cargados como ejemplos «por validar».

### 3.1 Alcance del MVP propuesto, por bloque

| Elemento | ID | Descripción | Prioridad | Estado | Fuente |
|---|---|---|---|---|---|
| MVP · Catálogo | RF-001 | Listado y ficha de camper | Must | Recomendación | [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) |
| MVP · Búsqueda y disponibilidad | RF-002, RF-003, RN-003 | Búsqueda por fechas y sede; disponibilidad validada en servidor; sin solapes | Must | Recomendación | mvp-and-backlog.md |
| MVP · Precio | RF-004, RN-010 | Precio desglosado, calculado en servidor y congelado; temporadas y mínimo de noches | Must | Recomendación | mvp-and-backlog.md |
| MVP · Reserva | RF-006, RN-026 | Datos del conductor principal, aceptación de condiciones y consentimientos con versión | Must | Recomendación | mvp-and-backlog.md |
| MVP · Protección de fechas | RF-007, RN-016 | Bloqueo temporal durante el pago (15 min propuesto, configurable) | Must | Recomendación | mvp-and-backlog.md |
| MVP · Pago | RF-008, RF-009, RN-023, RNF-006 | Pago total con tarjeta y 3-D Secure/SCA vía pasarela; confirmación solo por notificación del servidor de la pasarela | Must | Recomendación | mvp-and-backlog.md |
| MVP · Impagos | RF-032, RN-015 | Expiración de reservas impagadas; pago tardío confirmado solo si hay disponibilidad, o reembolsado | Must | Recomendación | mvp-and-backlog.md |
| MVP · Post-reserva | RF-010, RF-011, RF-012, RF-013, RN-025, RN-027 | Correo de confirmación con justificante; consulta con código + email; cancelación con reembolso según política | Must | Recomendación | mvp-and-backlog.md |
| MVP · Cumplimiento y base web | RF-015 (contacto), RF-016, RF-017, RF-018, RNF-001 a RNF-005 | Contacto, páginas legales, banner de cookies, SEO técnico, responsive, accesibilidad y rendimiento móvil como objetivos | Must | Recomendación | mvp-and-backlog.md |
| MVP · Administración | RF-019 a RF-025, RF-026 (mínimo), RN-001 | Acceso (rol único), flota, sedes, tarifas, temporadas y mínimo de noches, reservas, bloqueo manual, pagos y reembolsos, aviso mínimo por correo | Must | Recomendación | mvp-and-backlog.md |

### 3.2 Priorización (MoSCoW), segunda fase, ampliaciones y exclusiones

| Elemento | ID | Descripción | Prioridad | Estado | Fuente |
|---|---|---|---|---|---|
| Segunda fase (1.ª ola) | RF-005, RF-022 (parte), HU-025 | Extras | Should | Recomendación | mvp-and-backlog.md |
| Segunda fase (1.ª ola) | RF-015 (FAQ), HU-026 | Preguntas frecuentes | Should | Recomendación | mvp-and-backlog.md |
| Segunda fase (1.ª ola) | RF-014, HU-027 | Modificación de reserva | Should | Recomendación | mvp-and-backlog.md |
| Segunda fase (1.ª ola) | RF-028, HU-028 | Reservas manuales | Should | Recomendación | mvp-and-backlog.md |
| Segunda fase (1.ª ola) | RF-027, HU-029 | Plantillas de correo editables | Should | Recomendación | mvp-and-backlog.md |
| Segunda fase (1.ª ola) | HU-030 | Depósito + saldo diferido | Should | Recomendación | mvp-and-backlog.md |
| Segunda fase (1.ª ola) | HU-031 | Factura automática y clientes empresa | Should | Recomendación | mvp-and-backlog.md |
| Segunda fase (2.ª ola) | RF-012, HU-032 | Cuentas de cliente | Could | Recomendación | mvp-and-backlog.md |
| Segunda fase (2.ª ola) | RF-029, HU-033 | Informes y registro de auditoría | Could | Recomendación | mvp-and-backlog.md |
| Segunda fase (2.ª ola) | RF-030, HU-034 | Roles adicionales | Could | Recomendación | mvp-and-backlog.md |
| Segunda fase (2.ª ola) | RF-026 ampliado, HU-035 | Centro de avisos completo | Could | Recomendación | mvp-and-backlog.md |
| Segunda fase (2.ª ola) | HU-036 | Otra sede de devolución con suplemento | Could | Recomendación | mvp-and-backlog.md |
| Posible ampliación (Won't por ahora) | RF-031 | Fianza en línea, otros medios de pago, multi-idioma, cupones, reseñas, documentos del conductor, contrato digital, sincronización de canales | — | Recomendación | mvp-and-backlog.md |
| Exclusión | — | Integraciones con sistemas existentes y migración de datos | — | Confirmado | mvp-and-backlog.md |
| Exclusión | — | Presupuesto y fechas fuera del contrato | — | Confirmado | mvp-and-backlog.md |
| Exclusión | — | Lo no confirmado en «Fuera del MVP» no está comprometido | — | Recomendación | mvp-and-backlog.md |

Una cancelación del cliente con reembolso (RF-013) es **Must (ver P-004)** y el aviso mínimo al administrador (RF-026) es **Must (mínimo)**.

### 3.3 Criterios de aceptación: versión del Product Manager (CA-001 a CA-034)

Fuente: [mvp-and-backlog.md](../02-product/mvp-and-backlog.md), «Criterios de aceptación». CA-001 a CA-014 son la formulación del PM alineada con los títulos del Analista (el propio PM declara «Reconciliación pendiente», ISS-001). CA-015 en adelante son nuevos. Formato resumido (Dado / Cuando / Entonces). Todos Recomendación; CA-014 y CA-030 quedan condicionados al protocolo de medición (P-012, PEND-014).

| ID | Historia o RF | Criterio (Dado / Cuando / Entonces) | Estado |
|---|---|---|---|
| CA-001 | RF-003 | Con una reserva confirmada o un bloqueo en un rango, cuando se buscan fechas solapadas, el camper no aparece reservable | Recomendación |
| CA-002 | RN-003 | Con una reserva o bloqueo existente, cuando se intenta crear otro solapado (web o panel), se rechaza e informa del conflicto | Recomendación |
| CA-003 | RNF-007 | Con dos clientes que reservan a la vez el mismo camper y rango, solo uno obtiene el bloqueo y el otro recibe un aviso claro, sin doble reserva | Recomendación |
| CA-004 | RN-023 | Si el cliente vuelve tras pagar y el servidor no recibió la notificación de la pasarela, la reserva no figura confirmada; se confirma solo al recibir la notificación válida | Recomendación |
| CA-005 | RF-032, RN-015 | Si una reserva no se paga y vence el bloqueo, pasa a expirada y las fechas quedan libres | Recomendación |
| CA-006 | — | Si un pago es rechazado o abandonado con el bloqueo vigente, el cliente puede reintentar sin duplicar la reserva | Recomendación |
| CA-007 | RN-015 | Si llega el pago de una reserva expirada: con fechas libres se confirma; si no, se reembolsa y se avisa a cliente y administrador | Recomendación |
| CA-008 | RF-013 | Con una reserva confirmada y una política de cancelación, al cancelar se calcula el reembolso, se ordena y las fechas se liberan. **El PM aplica la política vigente en el momento de la cancelación; el Analista y la recomendación del Director (DEC-025), la vigente al reservar (ISS-002)**. Valores por validar (P-001) | Recomendación |
| CA-009 | — | Con fechas pasadas, devolución anterior a recogida o mínimo de noches no cumplido, se muestra un mensaje claro y no se continúa | Recomendación |
| CA-010 | RN-026 | Sin aceptar condiciones y privacidad no se puede pagar; al aceptarlas se registran versión y fecha | Recomendación |
| CA-011 | RN-001, RNF-010, RNF-013 | Cuando un administrador crea o edita un camper, sede, tarifa o imagen, los cambios se reflejan en la web sin intervención técnica | Recomendación |
| CA-012 | RN-010 | Un cambio de tarifa no altera el precio ni el desglose de reservas ya creadas | Recomendación |
| CA-013 | RN-025 | Con código y correo que no coinciden, o al intentar acceder a otra reserva, no se muestra ningún dato ni se confirma que la reserva exista | Recomendación |
| CA-014 | RNF-001 | En móvil, la página de inicio, la búsqueda, la ficha y el pago aspiran a LCP ≤ 2,5 s, INP ≤ 200 ms y CLS ≤ 0,1 (protocolo pendiente, P-012) | Recomendación |
| CA-015 | RF-002 | Con sede y fechas válidas, se listan solo los campers disponibles con el precio total del periodo | Recomendación |
| CA-016 | RF-001 | Un camper activo muestra características, imágenes, sede y condiciones; uno desactivado no aparece | Recomendación |
| CA-017 | RF-004 | En el resumen hay un desglose coherente con tarifas y temporadas y el total a cobrar (IVA pendiente, P-005) | Recomendación |
| CA-018 | RF-006 | Si faltan datos obligatorios del conductor o no cumple la edad mínima declarada, no se continúa y se explica el motivo | Recomendación |
| CA-019 | RF-010, RN-027 | Al confirmarse una reserva, el cliente recibe un correo con código y justificante de pago | Recomendación |
| CA-020 | RF-011, RF-012 | Con código y correo correctos, el cliente ve estado, detalle y justificante y puede cancelar si procede | Recomendación |
| CA-021 | RF-019 | Un usuario sin autenticar no ve contenido del panel; con credenciales válidas accede | Recomendación |
| CA-022 | RF-023 | El administrador lista, filtra y abre el detalle de reservas (cliente, camper, fechas, importes y estados) y puede cancelar conforme a las reglas | Recomendación |
| CA-023 | RF-024 | Un bloqueo manual deja al camper no disponible en el rango; si hay reservas en el rango, se rechaza (CA-002) | Recomendación |
| CA-024 | RF-025, RNF-009 | Al emitir o consultar un reembolso, el estado del pago se actualiza y los eventos quedan registrados | Recomendación |
| CA-025 | RF-026 | Ante una reserva nueva, una cancelación o un pago tardío sin disponibilidad, se envía un correo a la dirección configurada | Recomendación |
| CA-026 | RF-017 | En el primer acceso se ve el banner y no se activan cookies no necesarias hasta aceptar; la decisión se respeta y puede cambiarse (detalle legal pendiente, P-005) | Recomendación |
| CA-027 | RF-016 | Desde cualquier página y el paso de reserva se encuentran los enlaces a páginas legales y a la política de cancelación (texto a validar legalmente) | Recomendación |
| CA-028 | RF-018 | Las páginas públicas tienen URL limpia, metadatos propios, sitemap y datos estructurados donde aplique; no se garantiza posicionamiento | Recomendación |
| CA-029 | RF-015 | Un visitante encuentra los datos o el formulario de contacto configurados | Recomendación |
| CA-030 | RNF-003, RNF-004, RNF-005 | El flujo completo es utilizable en móvil, tableta y ordenador y con teclado, y se revisa contra WCAG 2.1 AA como objetivo (alcance pendiente) | Recomendación |
| CA-031 | RNF-006 | Los datos de tarjeta los procesa la pasarela y la web no los almacena | Recomendación |
| CA-032 | RN-021, RN-022 | Solo se permiten las transiciones de estado previstas y se muestran igual en el cliente y en el panel | Recomendación |
| CA-033 | Decisión del Director | En el MVP, la recogida y la devolución son en la misma sede (sin RF ni RN de origen: elemento huérfano en TRACEABILITY §5) | Recomendación |
| CA-034 | RF-022 | Con fechas que cruzan temporadas o no cumplen el mínimo, el precio aplica las tarifas correctas por noche y se bloquea el mínimo no cumplido | Recomendación |

### 3.4 Historias de usuario

Fuente: [mvp-and-backlog.md](../02-product/mvp-and-backlog.md). Todas son Recomendación hasta que se apruebe el alcance. Los CA de Fase 2 se redactarán al planificarla.

| ID | Historia (resumen) | Prioridad | Trazabilidad | CA | Alcance |
|---|---|---|---|---|---|
| HU-001 | Ver el catálogo y la ficha de cada camper | Must | RF-001, RNF-013 | CA-016 | MVP |
| HU-002 | Buscar por fechas y sede | Must | RF-002, RF-003 | CA-015, CA-001, CA-009 | MVP |
| HU-003 | Disponibilidad fiable | Must | RF-003, RN-003, RNF-007 | CA-001, CA-002, CA-003 | MVP |
| HU-004 | Ver el precio total desglosado antes de pagar | Must | RF-004, RN-010 | CA-017, CA-034, CA-012 | MVP |
| HU-005 | Indicar datos como conductor principal y aceptar condiciones | Must | RF-006, RN-026, RNF-008 | CA-018, CA-010 | MVP |
| HU-006 | Que las fechas queden reservadas mientras se paga | Must | RF-007, RN-016, RN-003 | CA-003, CA-002 | MVP |
| HU-007 | Pagar en línea con tarjeta de forma segura | Must | RF-008, RF-009, RNF-006 | CA-031, CA-006 | MVP |
| HU-008 | Reserva confirmada solo con el pago validado | Must | RN-023, RN-021, RN-022, RNF-009 | CA-004, CA-032 | MVP |
| HU-009 | Expiración de impagos y gestión segura de pagos tardíos | Must | RF-032, RN-015 | CA-005, CA-007 | MVP |
| HU-010 | Recibir por correo la confirmación y el justificante | Must | RF-010, RN-027, RNF-014 | CA-019 | MVP |
| HU-011 | Consultar la reserva con código y correo | Must | RF-011, RF-012, RN-025 | CA-020, CA-013 | MVP |
| HU-012 | Cancelar la reserva y recibir el reembolso según política | Must (ver P-004) | RF-013 | CA-008 | MVP |
| HU-013 | Contactar con la empresa | Must | RF-015 (contacto) | CA-029 | MVP |
| HU-014 | Ver páginas legales y decidir sobre cookies | Must | RF-016, RF-017, RN-026 | CA-026, CA-027 | MVP |
| HU-015 | Base SEO técnica y carga rápida en móvil | Must | RF-018, RNF-001, RNF-002 | CA-028, CA-014 | MVP |
| HU-016 | Uso cómodo desde móvil y accesibilidad básica | Must | RNF-003, RNF-004, RNF-005 | CA-030 | MVP |
| HU-017 | Acceso del administrador al panel con credenciales | Must | RF-019, RNF-006 | CA-021 | MVP |
| HU-018 | Gestionar la flota | Must | RF-020, RN-001, RNF-010, RNF-013 | CA-011 | MVP |
| HU-019 | Gestionar las sedes | Must | RF-021, RN-001 | CA-011, CA-033 | MVP |
| HU-020 | Configurar tarifas, temporadas y mínimo de noches | Must | RF-022, RN-010 | CA-011, CA-034, CA-012 | MVP |
| HU-021 | Ver y gestionar las reservas | Must | RF-023, RN-021 | CA-022, CA-032 | MVP |
| HU-022 | Bloquear fechas de un camper | Must | RF-024, RN-003 | CA-023, CA-002 | MVP |
| HU-023 | Ver pagos y emitir reembolsos | Must | RF-025, RN-022, RNF-009 | CA-024 | MVP |
| HU-024 | Correo al administrador por reserva nueva, cancelación o pago tardío | Must (mínimo) | RF-026 | CA-025 | MVP |
| HU-025 | Añadir extras a la reserva | Should | RF-005, RF-022 | — | Segunda fase |
| HU-026 | Consultar preguntas frecuentes | Should | RF-015 | — | Segunda fase |
| HU-027 | Modificar la reserva | Should | RF-014 | — | Segunda fase |
| HU-028 | Crear reservas manuales | Should | RF-028 | — | Segunda fase |
| HU-029 | Editar las plantillas de correo | Should | RF-027 | — | Segunda fase |
| HU-030 | Pagar un depósito y el saldo después | Should | Decisión del Director (P-007) | — | Segunda fase |
| HU-031 | Factura automática | Should | Decisión del Director (P-007) | — | Segunda fase |
| HU-032 | Cuenta de usuario | Could | RF-012 | — | Segunda fase |
| HU-033 | Informes y registro de auditoría | Could | RF-029 | — | Segunda fase |
| HU-034 | Roles adicionales | Could | RF-030 | — | Segunda fase |
| HU-035 | Centro de avisos completo | Could | RF-026 | — | Segunda fase |
| HU-036 | Devolver el camper en otra sede con suplemento | Could | Decisión del Director | — | Segunda fase |

**Dependencias funcionales (PM):** la cadena principal es HU-002/003 → HU-004 → HU-005 → HU-006 → HU-007/008 → HU-010; HU-009 depende de HU-006 y HU-008; HU-011 y HU-012 dependen de HU-008 y HU-010; HU-012 y HU-023 dependen de la política de cancelación (P-001); HU-021 a HU-024 dependen de HU-017; HU-022 comparte regla de no solapes con HU-003 y HU-006; HU-018 a HU-020 deben existir antes de comprobar búsqueda y reserva. Externas: cuenta de comercio con la pasarela, textos legales, remitente y dominio de correo y datos iniciales de flota y tarifas.

### 3.5 Métricas de éxito propuestas y pendientes del producto

Todas Recomendación; no se fijan metas numéricas (P-013): reservas pagadas frente a búsquedas iniciadas; abandono entre inicio del pago y confirmación; reservas dobles o solapadas (expectativa: cero); reservas expiradas y pagos tardíos reembolsados; contactos por dudas sobre el estado de una reserva; tiempo de alta de un camper o cambio de tarifa por un administrador; indicadores Core Web Vitals en móvil; entrega correcta de correos de confirmación.

Pendientes del producto (PM, P-001 a P-016): valores de cancelación y quién asume comisiones (P-001); pago total y fianza informativa (P-002); tiempo de bloqueo (P-003); cancelación por el cliente en el MVP (P-004); validación legal (P-005); edad mínima y permiso (P-006); saldo diferido y factura automática en F2 (P-007); justificante frente a factura (P-008); extras en la salida inicial (P-009); noche frente a día y zona horaria (P-010); regla al desactivar con reservas futuras (P-011); protocolo de rendimiento y accesibilidad (P-012); metas numéricas, disponibilidad y escalabilidad (P-013); titularidad de pasarela, dominio y correo (P-014); alcance de público extranjero para SEO (P-015); antelación mínima y máxima (P-016). Equivalencias en la sección 9.2.

## 4. Experiencia de usuario y mockups

Fuente: [ux-specification.md](../03-ux/ux-specification.md) (Diseñador UX/UI, **BORRADOR**; conflicto de contrato devuelto al Director: GATE-002 PENDING y alcance no aprobado). El diseño sigue la propuesta del PM (DEC-001, 003, 005, 009, 011, 012, 014, 018, 019, 027). **Contradicción abierta (ISS-002):** el diseño no elige el momento de la política de cancelación; P05 y P10 muestran el reembolso que calcula el servidor y la versión de política aplicada. Los mockups ilustrativos están en [mockups/index.html](mockups/index.html) (media fidelidad, **no son diseño final aprobado**).

### 4.1 Usuarios y recorridos

| Usuario | Objetivo | Estado |
|---|---|---|
| Visitante / cliente particular (móvil u ordenador) | Ver campers, comprobar disponibilidad y precio total, reservar y pagar sin llamar; consultar y cancelar su reserva | Supuesto (perfil, nacionalidad y volumen: Pendiente) |
| Administrador (único rol) | Mantener flota, sedes y tarifas; gestionar reservas, bloqueos, pagos y reembolsos sin ayuda técnica | Supuesto (DEC-014) |
| Operador de sede | No existe en el MVP | Segunda fase (HU-034) |

| Recorrido | Pasos (resumen) | Relación | Estado |
|---|---|---|---|
| R1 · Reserva feliz | Inicio → búsqueda → resultados → ficha → resumen de precio → datos del conductor y aceptaciones → pago con 3-D Secure → «verificando pago» → confirmación con código → correo con justificante | HU-002 a HU-010 | Recomendación |
| R2 · Pago fallido | Rechazo o fallo de autenticación; error con tiempo restante del bloqueo; reintento mientras dure; si vence, pasa a R3 | CA-006 | Recomendación |
| R3 · Pago pendiente o expirado | Pendiente de verificación (no se confirma); expirada (se liberan fechas y se ofrece nueva búsqueda); pago tardío (se confirma por correo si hay fechas, si no se reembolsa y se avisa) | CA-004, CA-005, CA-007 | Recomendación |
| R4 · Consulta y cancelación | «Mi reserva» con código + correo → detalle → cancelar → reembolso calculado y confirmación → resultado y correo | HU-011, HU-012 | Recomendación |
| R5 · Administrador | Acceso → alta de sedes, flota (con imágenes), tarifas y temporadas → seguimiento de reservas → bloqueos manuales (cubren reservas telefónicas) → pagos y reembolsos | HU-017 a HU-023 | Recomendación |

### 4.2 Mapa del sitio y navegación

**Público.** Cabecera: Campers · Sedes · Mi reserva · Contacto · botón «Buscar». Pie: legales, cookies, contacto.

| Ruta propuesta | Contenido | Indexable |
|---|---|---|
| `/` | Inicio | Sí |
| `/campers/` | Catálogo | Sí |
| `/campers/{slug}` | Ficha (datos estructurados) | Sí |
| `/sedes/{slug}` | Página de sede (RF-018) | Sí |
| `/buscar?...` | Resultados | No (noindex) |
| `/reserva/{resumen, datos, pago, estado}` | Flujo de reserva | No |
| `/mi-reserva` | Consulta y cancelación | No |
| `/contacto` | Contacto | — |
| `/legal/{aviso-legal, privacidad, cookies, condiciones-alquiler, politica-cancelacion}` | Páginas legales | — |
| `/admin/` | Acceso → Reservas · Flota · Sedes · Tarifas y temporadas · Bloqueos · Pagos y reembolsos | No (noindex, autenticado) |

Las URL son Recomendación (el SEO se define en arquitectura); el código de reserva no debe ir en una URL adivinable. Si hay una sola sede se oculta el selector y no se genera página de sede duplicada del inicio (decisión Pendiente, PEND-028).

### 4.3 Inventario de pantallas

> **Entrega inicial (opción B):** el inventario siguiente corresponde al MVP completo (fase siguiente). Para la entrega inicial se ilustran seis pantallas (inicio, catálogo, ficha, tarifas y condiciones, solicitud de reserva y vista móvil, con las variantes `-entrega-inicial`, el catálogo `13` y los mockups 11 y 12) y cualquier otra pantalla del inventario queda para la fase siguiente. Los estados alternativos de ambos alcances están en [mockups/14-estados.html](mockups/14-estados.html) y la dirección visual propuesta en [mockups/direccion-visual.md](mockups/direccion-visual.md). Véase [mockups/index.html](mockups/index.html).

| Pantalla | Propósito | Requisitos / historias / criterios | Mockup | Estado | Fuente |
|---|---|---|---|---|---|
| P01 Inicio | Hero, destacados de flota activa y sedes; buscar | RF-002, RF-018 · HU-001, HU-002, HU-015 · CA-028 | [01-inicio.html](mockups/01-inicio.html), [10-movil-inicio-y-resultados.html](mockups/10-movil-inicio-y-resultados.html) | Recomendación | [ux-specification.md](../03-ux/ux-specification.md) §4 |
| P02 Catálogo | Campers activos con foto, plazas, precio orientativo «desde» (Pendiente) y sede | RF-001 · HU-001 · CA-016 | [13-catalogo-entrega-inicial.html](mockups/13-catalogo-entrega-inicial.html) (versión simplificada de la entrega inicial) | Recomendación | ux-specification.md §4 |
| P03 Ficha | Galería, descripción, plazas, equipamiento, sede, fianza informativa, condiciones; elegir fechas y reservar | RF-001, RF-003 · HU-001, HU-003 · CA-016 | [03-ficha-camper.html](mockups/03-ficha-camper.html) | Recomendación | ux-specification.md §4 |
| P04 Resultados | Campers disponibles con precio total del periodo; vacío: «Sin disponibilidad» | RF-002, RF-003 · HU-002, HU-003 · CA-001, CA-009, CA-015 | [02-resultados-busqueda.html](mockups/02-resultados-busqueda.html), [10-movil-inicio-y-resultados.html](mockups/10-movil-inicio-y-resultados.html) | Recomendación | ux-specification.md §4 |
| P05 Resumen de precio | Desglose por temporada, impuestos (Pendiente), total a pagar hoy, fianza informativa, política de cancelación | RF-004 · HU-004 · CA-017, CA-034 | [04-resumen-y-datos-conductor.html](mockups/04-resumen-y-datos-conductor.html) | Recomendación | ux-specification.md §4 |
| P06 Datos del conductor | Nombre, correo (con confirmación), teléfono, fecha de nacimiento, ocupantes y aceptaciones; crea el bloqueo temporal | RF-006 · HU-005 · CA-010, CA-018 | [04-resumen-y-datos-conductor.html](mockups/04-resumen-y-datos-conductor.html) | Recomendación | ux-specification.md §4 |
| P07 Pago | Resumen, temporizador del bloqueo y área de pago de la pasarela (alojada o embebida: Pendiente) | RF-007, RF-008, RF-009 · HU-006, HU-007 · CA-003, CA-006, CA-031 | [05-pago.html](mockups/05-pago.html) | Recomendación | ux-specification.md §4 |
| P08 Estado y confirmación | Estado, código de reserva, resumen y próximos pasos; variantes verificando, rechazado, expirado | RF-010, RF-032 · HU-008, HU-009, HU-010 · CA-004, CA-005, CA-007, CA-019 | [06-confirmacion.html](mockups/06-confirmacion.html) | Recomendación | ux-specification.md §4 |
| P09 Consulta de reserva | Código + correo; detalle con estados, importes, sede y justificante | RF-011, RF-012 · HU-011 · CA-013, CA-020 | [07-consulta-reserva.html](mockups/07-consulta-reserva.html) | Recomendación | ux-specification.md §4 |
| P10 Cancelación | Reembolso calculado por el servidor, versión de política aplicada, confirmación explícita | RF-013 · HU-012 · CA-008 | [07-consulta-reserva.html](mockups/07-consulta-reserva.html) | Recomendación | ux-specification.md §4 |
| P11 Contacto | Datos de contacto y formulario con antispam | RF-015 · HU-013 · CA-029 | — | Recomendación | ux-specification.md §4 |
| P12 Legales / P13 Cookies | Textos con título, fecha y versión; banner y centro de preferencias | RF-016, RF-017 · HU-014 · CA-026, CA-027 | — | Recomendación (contenido legal Pendiente) | ux-specification.md §4 |
| P14 Acceso admin | Usuario y contraseña, límite de intentos, error genérico; recuperación de contraseña Pendiente | RF-019 · HU-017 · CA-021 | [08-admin-panel-reservas.html](mockups/08-admin-panel-reservas.html) (menciona el acceso) | Recomendación | ux-specification.md §4 |
| P15 Reservas (admin) | Lista con filtros y detalle con línea de tiempo; cancelar y anotar | RF-023 · HU-021 · CA-022, CA-032 | [08-admin-panel-reservas.html](mockups/08-admin-panel-reservas.html) | Recomendación | ux-specification.md §4 |
| P16 Flota / P17 Sedes | Alta, edición y desactivación; imágenes con texto alternativo obligatorio | RF-020, RF-021 · HU-018, HU-019 · CA-011, CA-033 | [09-admin-flota-tarifas.html](mockups/09-admin-flota-tarifas.html) | Recomendación | ux-specification.md §4 |
| P18 Tarifas y temporadas | Precio por noche y temporada sin solapes; mínimo de noches; aviso «los cambios no afectan a reservas ya creadas» | RF-022 · HU-020 · CA-012, CA-034 | [09-admin-flota-tarifas.html](mockups/09-admin-flota-tarifas.html) | Recomendación | ux-specification.md §4 |
| P19 Bloqueos | Camper, rango y motivo; conflicto rechazado con reservas mostradas | RF-024 · HU-022 · CA-023, CA-002 | — | Recomendación | ux-specification.md §4 |
| P20 Pagos y reembolsos | Transacciones con estado; reembolso total o parcial; fallidos «gestión manual» | RF-025 · HU-023 · CA-024 | — | Recomendación | ux-specification.md §4 |
| P21 Aviso admin | No es pantalla: campo de configuración del correo de aviso (ubicación Pendiente, PEND-027) | RF-026 · HU-024 · CA-025 | — | Pendiente | ux-specification.md §4 |

Los CA se citan como en la fuente (ISS-023). Transversal: RNF-001 a RNF-005 · HU-015, HU-016 · CA-014, CA-030.

### 4.4 Estados de interfaz, formularios y comportamiento responsive

| Pantalla | Carga | Vacío | Éxito | Error | Sin permisos | Sin conexión |
|---|---|---|---|---|---|---|
| Resultados | Esqueleto con altura reservada | Sin disponibilidad, con «cambiar fechas» y «contacto» | Lista | Fechas inválidas o fallo de servidor con reintento | n/a | Aviso y reintento sin perder datos |
| Ficha y catálogo | Esqueleto | Sin campers activos | Contenido | 404 si está desactivado (Pendiente) | n/a | Aviso |
| Resumen y datos | Cálculo en curso | n/a | Total mostrado | Fechas no disponibles, mínimo de noches, edad mínima | n/a | Conserva los campos |
| Pago | «Preparando pago seguro» | n/a | Pasa a estado | Rechazo o 3-D Secure fallido (reintento mientras dure el bloqueo); bloqueo vencido | Sin bloqueo → volver | El pago puede estar en curso: no reenviar, consultar estado |
| Estado | «Verificando tu pago» | n/a | Confirmada | Expirada, fallida | Sin contexto → «Mi reserva» | «No podemos comprobar tu pago ahora…» |
| Mi reserva | Cargando | n/a | Detalle | Datos no coinciden (mensaje genérico), límite de intentos | n/a | Aviso |
| Cancelación | Calculando reembolso | n/a | Cancelada | No cancelable; fallo de reembolso (gestión manual) | Sin sesión → volver | Aviso, sin enviar dos veces |
| Panel (listas) | Esqueleto | «Aún no hay {flota/sedes/reservas}» | Guardado con aviso | Validación, conflicto de fechas, desactivar con reservas | Sesión caducada → acceso | Cambios no guardados |

- **Formularios [Recomendación]:** etiquetas siempre visibles; error junto al campo y en un resumen; texto que explica cómo corregir; datos escritos conservados. Búsqueda: VAL-001 a VAL-004 (formato dd/mm/aaaa con alternativa de texto al calendario). Conductor: VAL-008 a VAL-011, VAL-013, VAL-014, VAL-016. Consulta: código + correo, límite de intentos y error genérico. Panel: VAL-020 a VAL-022.
- **Responsive [Recomendación]:** mobile-first; menú compacto con «Buscar» y «Mi reserva» siempre accesibles; resumen con total y botón principal en barra inferior fija en móvil; panel usable en escritorio y tableta (tablas como tarjetas o con scroll); puntos de quiebre definidos en implementación.

### 4.5 Accesibilidad y marca provisional

- **Accesibilidad (objetivo WCAG 2.1 AA, Recomendación; alcance de la revisión Pendiente, PEND-014):** un H1 por página, jerarquía de encabezados, landmarks, «saltar al contenido», títulos únicos; todo operable con teclado con foco visible; banner de cookies y modales con foco atrapado y devuelto; formularios con etiquetas, `autocomplete`, errores asociados al campo y mensajes anunciados; acciones reversibles o con confirmación en pago y cancelación; aviso accesible antes de vencer el bloqueo (si se puede ampliar: Pendiente); contraste 4,5:1 en texto y 3:1 en elementos de interfaz (a verificar con herramienta cuando se apruebe la marca); zoom y reflow sin pérdida; estados nunca solo por color; texto alternativo en cada imagen (campo obligatorio en el panel); calendario y galería operables sin ratón.
- **Marca provisional (PROPUESTA, no aprobada; la define la empresa):** nombre provisional «Ruta Camper» (sin comprobar disponibilidad de marca ni de dominio); concepto: viaje, libertad y confianza; paleta propuesta: primario bosque `#1F4D3F`, acento terracota `#A64B20`, fondo cálido `#F6F1E7`, texto `#1E2420`, error `#B3261E`; tipografía: sans-serif legible con pila de fuentes del sistema; tono cercano de «tú» (tú/usted Pendiente); logotipo a crear por la empresa. Pendientes de marca: nombre, logotipo, paleta, tipografía, tono, estilo fotográfico e iconografía (PEND-025).
- **Rendimiento visual (RNF-001, protocolo Pendiente):** imágenes en formatos modernos con alternativa, tamaños responsivos y dimensiones declaradas (evita saltos); imagen principal con prioridad y el resto con carga diferida; fuente de sistema por defecto; esqueletos con altura final reservada; scripts de terceros (analítica, mapa) solo con consentimiento; el componente de pago se carga solo en la pantalla de pago.
- **Microcopy [Recomendación]:** textos propuestos para búsqueda vacía, fechas inválidas, bloqueo, pérdida de fechas, pago rechazado, verificando, expirada, acceso fallido, cancelación, fianza y consentimiento (ver ux-specification.md §10).
- **Riesgos de experiencia:** R-UX-01 a R-UX-10 (sección 8.3). **Pendientes del cliente de UX:** PEND-025 a PEND-033 (sección 9.2).

## 5. Arquitectura propuesta

Fuente: [solution-architecture.md](../04-architecture/solution-architecture.md) (Arquitecto de Soluciones, **BORRADOR**, COMPLETADO_CON_PENDIENTES). **Todo lo técnico es Recomendación; ninguna tecnología es obligatoria** (obligatoria: ninguna; existente: ninguna, no hay repositorio ni sistemas ni migración, Confirmado). ADR-001 a ADR-012 son **PROPUESTA** pendientes de aprobación ([DECISIONS.md](../00-control/DECISIONS.md) §2). La arquitectura se diseña según el MVP del PM (DEC-029). El reporte contiene dos erratas de redacción que el Gestor transcribió tal cual y que el Director mantuvo (ver nota del Gestor en la fuente).

| Tema | Resumen | Estado | ADR | Fuente |
|---|---|---|---|---|
| Estilo y componentes | Monolito modular desplegable como una unidad, con un worker para tareas programadas (expirar bloqueos, enviar correos, conciliar con la pasarela). Módulos: Catálogo, Tarifas, Disponibilidad, Reservas, Pagos, Políticas, Notificaciones y Admin. Alternativas descartadas: SPA + API separadas, CMS headless con servicios, motor de reservas SaaS | Recomendación | ADR-001 | [solution-architecture.md](../04-architecture/solution-architecture.md) |
| Datos | PostgreSQL como única base transaccional (restricción de exclusión por rango contra solapes, transacciones, JSON para instantáneas) | Recomendación | ADR-002 | solution-architecture.md |
| Integraciones | Ninguna con sistemas existentes (Confirmado). Pasarela de pago (proveedor Pendiente) detrás de la interfaz `PaymentProvider`; correo transaccional gestionado (Pendiente); CDN y almacén de imágenes | Confirmado (sin sistemas existentes) · Pendiente (proveedores) | ADR-004, ADR-005 | solution-architecture.md |
| Tecnologías | SSR/ISR con caché en CDN para las páginas públicas y consultas de disponibilidad sin caché pública; hosting por decidir (PaaS en la UE con PostgreSQL gestionado, contenedores en un VPS o serverless) | Recomendación (no obligatoria hasta decisión) | ADR-010 | solution-architecture.md |

### 5.1 Decisiones de arquitectura (ADR-001 a ADR-012)

Todas PROPUESTA; decisor pendiente (cliente, vía Director).

| ID | Decisión | Alternativas | Consecuencias |
|---|---|---|---|
| ADR-001 | Monolito modular con worker y una sola base de datos | SPA + API, microservicios, motor SaaS | Menos piezas y transacciones simples; menor escalado independiente, aceptable para el MVP |
| ADR-002 | PostgreSQL como única base transaccional | MySQL, NoSQL | Restricción de exclusión y consistencia; hay que encontrar un hosting que lo ofrezca |
| ADR-003 | Anti doble reserva en tres capas: restricción de exclusión por rango (`vehicle_id` + rango) en `occupancy`; hold con `expires_at` creado en la misma transacción que la reserva pendiente; limpieza de holds vencidos (perezosa en la inserción y periódica en el worker) | Comprobación en aplicación, bloqueo pesimista | La BD garantiza RN-003 y RNF-007 aunque la aplicación falle; una violación se traduce en «no disponible»; el rango es semiabierto e incluye el tiempo de preparación (RN-004) |
| ADR-004 | Interfaz `PaymentProvider` con un adaptador por proveedor | Integración directa | Permite elegir pasarela tarde (PEND-012); pequeño coste de abstracción |
| ADR-005 | Pago alojado o tokenizado, importe fijado en servidor y confirmación solo por webhook firmado; pasarela a elegir por el cliente entre Stripe, Redsys, Adyen u otra | Formulario propio de tarjeta, confirmar por redirección | Sin datos de tarjeta en la web (RNF-006); dependencia del proveedor |
| ADR-006 | Webhooks idempotentes: `payment_event` con id único, procesado en transacción, verificación de importe y moneda, tolerancia a duplicados y desorden; conciliación diaria | Procesar sin registro | Seguridad ante reintentos (RNF-009); requiere tarea de conciliación |
| ADR-007 | Pago tardío: el worker intenta recrear la ocupación; si falla, reembolsa y avisa al cliente y al administrador (RN-015, CA-007) | Confirmar siempre o rechazar siempre | Sin cobros sin servicio; hay que probar la ventana de carrera |
| ADR-008 | Políticas versionadas: la reserva guarda la versión de cancelación y el reembolso se calcula contra una versión | Texto fijo en código | Admite cualquiera de las dos lecturas de ISS-002; la regla definitiva depende de DEC-025 y PEND-010 |
| ADR-009 | Correo mediante cola de salida (outbox) con reintentos y estado, enviado por el worker | Envío síncrono | No se pierden correos si el proveedor falla (RNF-014); más piezas |
| ADR-010 | SSR/ISR con caché en CDN para páginas públicas; disponibilidad sin caché pública | SPA, SSG puro | Cumple SEO y rendimiento (RNF-001, RNF-002); exige invalidar caché al editar |
| ADR-011 | Acceso del cliente por código aleatorio + email, con límite de intentos y errores uniformes; cuentas en Fase 2 mediante `customer_id` opcional | Cuenta obligatoria | Menos fricción y menos datos; seguridad basada en la entropía del código y el límite de intentos (ver SEG-001) |
| ADR-012 | Puntos de extensión modelados desde el MVP (líneas de precio, tipo de pago, sede de devolución, rol enumerado, contenido traducible) sin implementar su lógica | Rediseñar en Fase 2 | Evita migraciones costosas; riesgo de sobrediseño: solo estructura mínima |

### 5.2 Modelo de datos conceptual

| Entidad | Contenido clave | Nota |
|---|---|---|
| `branch` (sede) | Nombre, dirección, horarios, contacto, activa | Soporta RN-001 |
| `vehicle` | Sede base, plazas, equipamiento, fianza informativa, activo, imágenes | Se desactiva, no se borra (DEC-028) |
| `season` y `rate` | Rango de fechas sin solape, precio por noche por vehículo, mínimo de noches | RN-007, RN-008 |
| `occupancy` (bloqueo de fechas) | `vehicle_id`, rango `[recogida, devolución)`, tipo (reserva o bloqueo manual), `reservation_id` o nulo, `expires_at` o nulo | Núcleo anti-solape (ADR-003) |
| `reservation` | Código, estado (RN-021), vehículo, sedes de recogida y devolución, fechas, conductor, instantánea de precio, referencias a versiones de políticas | `return_branch_id` existe aunque sea igual a la de recogida |
| `reservation_price_line` | Concepto, importe, impuestos | Admite extras sin cambiar el esquema |
| `payment` | Reserva, proveedor, referencia externa, importe, estado (RN-022), tipo `FULL` | `DEPOSIT`/`BALANCE` entran en Fase 2 |
| `refund` | Pago, importe, motivo, estado, clave de idempotencia, origen | RF-025 |
| `payment_event` | Proveedor, id de evento (único), tipo, carga bruta, estado de proceso | RNF-009, idempotencia |
| `policy_version` | Tipo (condiciones, privacidad, cancelación), versión, contenido o tramos, vigencia | RN-014, RN-026 |
| `consent` | Reserva, versión aceptada, finalidad, marca de tiempo, marketing sí/no | Sin datos de más |
| `admin_user` | Email, hash de contraseña, rol (un valor), MFA | RF-019 |
| `email_outbox` | Tipo, destinatario, plantilla, estado, reintentos | RNF-014 |
| `reservation_status_history` | Cambios de estado con actor y hora | RNF-009 |

Preparado para Fase 2 sin construirlo ahora: `customer_id` opcional, `payment.kind`, líneas de precio, `return_branch_id`, rol enumerado, campos traducibles y tabla de auditoría (RF-029). Convenciones: importes en céntimos enteros con moneda explícita; fechas en Europe/Madrid como `date` hasta que PEND-013 defina horas; errores con códigos estables e idempotencia en las creaciones.

### 5.3 Autenticación, seguridad, integraciones, operación y despliegue (resumen)

- **Cliente [Recomendación]:** sin cuenta; código aleatorio de alta entropía, error idéntico ante cualquier fallo, límite de intentos por IP y por código, autorización por objeto; alternativa más segura: enlace mágico por correo.
- **Administrador [Recomendación]:** email y contraseña con hash adaptativo, cookie `HttpOnly/Secure/SameSite`, protección CSRF, bloqueo por intentos; MFA recomendado (la revisión de seguridad lo exige obligatorio, SEG-006).
- **Seguridad y privacidad [Recomendación]:** OWASP Top 10 y ASVS como guía; pago alojado o tokenizado (el cumplimiento PCI depende del proveedor: validar); secretos fuera del repositorio con claves por entorno; límites de frecuencia en búsqueda, consulta, acceso, contacto y creación de reserva; RGPD sujeto a validación legal (minimización, consentimientos con versión, contratos de encargado, región UE preferida, plazos de retención por definir); cookies no técnicas solo tras el consentimiento; copias cifradas con restauración probada (RPO/RTO Pendiente).
- **Pasarela (comparación orientativa, sin imponer ni comparar costes):** Stripe (pago alojado, API y webhooks; contratación directa; riesgo: condiciones de cuenta y medios locales), Redsys (TPV virtual bancario; redirección con parámetros firmados; depende del banco), Adyen o similar (orientado a mayor volumen: verificar). Criterios: titularidad de la cuenta, comisiones, reembolsos parciales, sesión de pago configurable y entorno de pruebas.
- **Observabilidad y operación [Recomendación]:** logs estructurados con identificador de correlación y sin datos personales; seguimiento de errores, comprobación de disponibilidad y latido del worker; alertas ante webhooks fallidos, discrepancias de conciliación, correos rebotados, reservas pendientes con pago confirmado y pagos tardíos sin disponibilidad; runbook mínimo.
- **Escalabilidad y rendimiento:** un único nodo de aplicación más base gestionada (sin cifras: PEND-015); páginas públicas con caché y caché invalidada al editar; imágenes AVIF/WebP con `srcset`; poco JavaScript en catálogo y ficha; fuentes autoalojadas; presupuesto de rendimiento en integración continua más medición de campo (protocolo Pendiente).
- **Despliegue (estrategia; no se ejecuta nada y requiere autorización expresa):** entornos local, *staging* (noindex, acceso restringido, sandbox de la pasarela, datos de prueba) y producción; pipeline con lint, pruebas, compilación, revisión de migraciones y auditoría de dependencias, con aprobación manual; SEO técnico con `sitemap.xml`, `robots.txt`, `canonical`, `noindex` en panel, flujo de reserva, consulta y búsquedas parametrizadas, y JSON-LD (sin garantía de elegibilidad ni posicionamiento).
- **Pruebas recomendadas (no ejecutadas):** unitarias (precio, reembolsos, máquina de estados), concurrencia contra la BD, pagos (firma inválida, duplicado, desorden, importe distinto, pago tardío, contrato con el sandbox), extremo a extremo, accesibilidad, rendimiento, seguridad, y operación (restauración de copia y envío real de correo en *staging*).
- **Supuestos técnicos (Supuesto):** volumen bajo o moderado, un único mercado y un idioma; una persona o equipo pequeño administra el panel; fechas por noches hasta resolver PEND-013; el cliente acepta correo transaccional gestionado y servicios en la UE; el MVP se limita a la propuesta del PM (cualquier otra cosa exige solicitud de cambio).

### 5.4 Trazabilidad de la arquitectura con RF, RNF y RN

Fuente: matriz del Arquitecto, transcrita en [TRACEABILITY.md](../00-control/TRACEABILITY.md) §7. Estado BORRADOR. No cubre explícitamente RF-023, RN-004 (solo dentro de ADR-003), RN-017, RN-020 ni RN-024 (ISS-020).

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
| RN-021, RN-002, RN-005, RN-006 | Estados, modelo de reserva, Europe/Madrid |
| RNF-003 a RNF-005 | Frontend responsive y accesible; validación con QA |
| RNF-011, RNF-012 | Sin cifras (PEND-015); recomendaciones de copia y escalado |

## 6. Seguridad y cumplimiento

Fuente: [security-review.md](../08-security/security-review.md) (Revisor de Seguridad, **BORRADOR**). **Revisión estática y documental de diseño; no se ejecutó ninguna prueba de seguridad.** Estado de los 17 hallazgos: **OPEN**. El veredicto del Revisor («APROBADO CON CONDICIONES» para continuar el diseño y pasar a PLANNING; **no** se aprueba BUILD ni producción mientras no se cumplan los controles obligatorios y se resuelvan SEG-001 a SEG-007 y SEG-010) **no es una aprobación del proyecto, de una puerta ni de un riesgo** (ISS-025). Ningún riesgo ha sido aceptado. **Un diseño sin hallazgos no se declara seguro; solo se informa lo revisado.** Los puntos legales se marcan «validar con asesoría» (esto no es asesoramiento jurídico).

| Tema | Resumen | Estado | ID | Fuente |
|---|---|---|---|---|
| Autenticación y roles | Panel con rol único: el MFA solo se «recomienda» en arquitectura; el Revisor exige MFA obligatorio, cuentas nominales, política de sesión, recuperación con enfriamiento y CSRF (SEG-006); autorización denegada por defecto en servidor (SEG-017) | Recomendación | SEG-006, SEG-017, RNF-006 | [security-review.md](../08-security/security-review.md) |
| Acceso del cliente | El email no es un secreto: riesgo de cancelar y disparar un reembolso; código CSPRNG, errores uniformes, límites, `no-store` y segundo factor para cancelar (SEG-001) | Recomendación | SEG-001, RN-025 | security-review.md |
| Datos personales | RGPD sin cerrar: retención, supresión, contratos de encargado, transferencias, fecha de nacimiento frente a «mayor de edad» (SEG-010); logs sin datos personales (SEG-011) | Recomendación (validar con asesoría) | SEG-010, SEG-011, RNF-008 | security-review.md |
| Hallazgos conocidos | 17 hallazgos de diseño: 7 Altas (SEG-001 a SEG-007), 1 Alta «validar legal» (SEG-010), 8 Medias (SEG-008, SEG-009, SEG-011 a SEG-016), 1 Baja (SEG-017). Ninguna Crítica identificada en diseño | Recomendación | SEG-001 a SEG-017 | security-review.md |

### 6.1 Hallazgos SEG-001 a SEG-017

| ID | Severidad | Riesgo (resumen) | Control requerido (resumen) | Estado | Tarea del plan que lo cierra |
|---|---|---|---|---|---|
| SEG-001 | Alta | Acceso por código + email: quien conozca el email y obtenga el código accede a datos personales y puede **cancelar y disparar un reembolso**; sin mínimo de entropía ni política de bloqueo | Código CSPRNG (≥ 64 bits, valor a fijar); respuesta, estado y tiempos idénticos ante fallos; límites por IP, código y email; código y email solo por POST; `no-store`, `Referrer-Policy`, `noindex`; segundo factor o enlace mágico antes de **cancelar**; datos mínimos hasta verificar | OPEN | TASK-041 |
| SEG-002 | Alta | Webhook como punto único de confirmación: firma sobre cuerpo ya parseado, replay, confianza en metadatos | Firma sobre cuerpo crudo con tiempo constante, fail-closed, cruce de referencia, importe, moneda y estado contra la BD, máquina de estados, secreto propio por entorno, sin cookies ni CORS | OPEN | TASK-033 |
| SEG-003 | Alta | Concurrencia: borrado perezoso de holds frente a pago en curso, sesión de pago más larga que el hold, pago tardío, bloqueo manual: doble reserva o cobro sin servicio | Restricción de exclusión como garantía final; hold que no expira con un pago en vuelo o sesión expirada por API; transiciones atómicas y reembolso idempotente; todos los orígenes de ocupación por la misma restricción | OPEN | TASK-034 |
| SEG-004 | Alta | Abuso de negocio: un bot crea holds sobre toda la flota; *card testing* | Límites de holds y de sesiones de pago, anti-bot y antifraude de la pasarela; verificación de email antes de enviar enlaces de pago | OPEN | TASK-035 |
| SEG-005 | Alta | Manipulación de importes y reembolsos; VAL-020 admite precios ≥ 0 | Reembolso solo en servidor con tope e idempotencia, al medio original; tarifas > 0 con confirmación de cambios grandes y flujo definido para importe 0; reautenticación en reembolsos del admin; instantánea de la política aplicada | OPEN | TASK-041, TASK-043 |
| SEG-006 | Alta | Autenticación del panel insuficiente (MFA solo recomendado, rol potencialmente compartido, sin política de sesión ni recuperación) | MFA obligatorio y códigos de recuperación; contraseñas largas; cuentas nominales; sesión con caducidad y rotación; recuperación con enfriamiento y aviso; cookie `__Host-`, CSRF y reautenticación en acciones críticas | OPEN | TASK-042 |
| SEG-007 | Alta | Auditoría del panel aplazada a Fase 2 mientras el admin ya cambia tarifas, bloquea, cancela y reembolsa | Registro de auditoría **mínimo en el MVP** (quién, cuándo, qué, valores antes y después) para acceso, tarifas, bloqueos, cancelaciones, reembolsos y exportaciones | OPEN | TASK-043 |
| SEG-008 | Media | CSRF, XSS, inyección, cabeceras y caché (CDN/ISR puede exponer páginas personalizadas) | Codificación de salida, consultas parametrizadas, CSRF en toda mutación, CSP estricta, HSTS, CORS cerrado, sin caché pública con sesión o código | OPEN | TASK-023 (base) |
| SEG-009 | Media | Subida de imágenes maliciosas o con metadatos | Lista cerrada de formatos (sin SVG), validación por *magic bytes*, reprocesado sin EXIF, límites, nombres aleatorios, servido con `nosniff` | OPEN | TASK-043 |
| SEG-010 | Alta (validar legal) | RGPD sin cerrar: retención, supresión, brechas, contratos, transferencias; cargas brutas y outbox con datos personales | Inventario y mínimos por campo, retención y anonimizado, consentimiento con versión, cifrado, contratos y región UE, purga y política de supresión con copias | OPEN | TASK-053 con B4 y B7 |
| SEG-011 | Media | Logs y errores con datos personales o código de reserva | Redacción obligatoria, lista de campos prohibidos, retención y acceso limitados | OPEN | TASK-023 |
| SEG-012 | Media | Secretos y entornos: *staging* con datos reales, privilegios de BD excesivos, origen accesible saltándose el CDN | Gestor de secretos, sin datos reales fuera de producción, roles de BD de mínimo privilegio, TLS, sin depuración en producción, detección de secretos | OPEN | TASK-020, TASK-021, TASK-022 |
| SEG-013 | Media | Copias y restauración: RPO/RTO sin definir; ransomware | Copias cifradas, aisladas y con acceso separado; restauración probada con RPO/RTO acordados | OPEN | TASK-060, TASK-061 |
| SEG-014 | Media | Cadena de suministro: sin *lockfile*, SDK de terceros ni protección de ramas | Lockfile, SCA y SBOM en CI, acciones fijadas por hash, ramas protegidas, mínimo de scripts de terceros | OPEN | TASK-020, TASK-063 |
| SEG-015 | Media | Correo: *email bombing*, inyección de cabeceras, falta de DMARC | Límite por destinatario, verificación de email, SPF/DKIM/DMARC, plantillas sin datos innecesarios | OPEN | TASK-040 |
| SEG-016 | Media | Cookies y antispam de terceros sin consentimiento definido | Inventario de cookies, nada no técnico antes del consentimiento, rechazar tan fácil como aceptar, prueba del consentimiento | OPEN | TASK-045 |
| SEG-017 | Baja | Autorización en servidor solo en el frontend o rol de Fase 2 sin pruebas | Denegar por defecto en `/admin`, comprobar sesión y rol en cada operación, pruebas negativas | OPEN | TASK-042 |

### 6.2 Controles obligatorios para BUILD (según el Revisor) y cambios de alcance que exige

1. Acceso del cliente (SEG-001); 2. Webhook (SEG-002); 3. Concurrencia (SEG-003); 4. Antiabuso (SEG-004); 5. Importes y reembolsos (SEG-005); 6. Panel (SEG-006); 7. Auditoría mínima en el MVP (SEG-007); 8. Web segura (SEG-008); 9. Imágenes (SEG-009); 10. Datos (SEG-010); 11. Logs y secretos (SEG-011, SEG-012); 12. Copias y dependencias (SEG-013, SEG-014); 13. Pruebas de seguridad en CI (SAST, SCA, detección de secretos).

**Escalado al Director (cambios de alcance frente al PM, sin solicitud de cambio registrada; ISS-029, PEND-037 a PEND-039):** MFA obligatorio; auditoría mínima en el MVP; precio > 0 (o flujo de importe 0); segundo factor para cancelar. **Limitaciones de la revisión:** solo diseño; no se leyeron por completo `requirements.md` ni `mvp-and-backlog.md`; no se eligieron pasarela, hosting ni proveedor de correo; la ausencia de hallazgos en un área no implica seguridad; falta modelar la amenaza interna del cliente y el impacto de contracargos.

## 7. Plan de trabajo y estimación de plazo

Fuente: [implementation-plan.md](../05-planning/implementation-plan.md) (Planificador de Proyecto, **BORRADOR**, COMPLETADO_CON_PENDIENTES). **No autoriza BUILD ni despliegues**; GATE-001 y GATE-002 siguen PENDING. Los tamaños S/M/L son esfuerzo relativo (no calendario, costo ni dimensión de equipo). El Planificador declara que no pudo leer `RISKS` ni `requirements` completos (ISS-033).

| Fase | Objetivo | Entregables | Dependencias / puerta de salida (humana) | Estado | Fuente |
|---|---|---|---|---|---|
| P0 Preparación (DESIGN/PLANNING) | Reconciliar ISS, decisiones bloqueantes, aprobar alcance y plan | Decisiones B1 a B9, plan aprobado, UX y arquitectura persistidos | GATE-002 y PLANNING → BUILD | Recomendación | [implementation-plan.md](../05-planning/implementation-plan.md) |
| P1 Fundaciones (BUILD) | Repo, CI, modelo de datos, esqueleto, tokens UI | Repositorio, CI, esquema y migraciones | Esquema y CI verdes; SEG-012 y SEG-014 base | Recomendación | implementation-plan.md |
| P2 Núcleo de reserva y pago | Precio, disponibilidad, hold, pago, webhook, worker | Módulos de precio, disponibilidad, reserva, pago y worker, con pruebas | Concurrencia y pago en verde con sandbox | Recomendación | implementation-plan.md |
| P3 Post-reserva, panel y web | Correo, consulta, cancelación, panel, auditoría, SEO, legales | Correo, consulta y cancelación, panel, web pública con SEO y legales | Funcionalidad completa del MVP, sin las 7 Altas abiertas | Recomendación | implementation-plan.md |
| P4 QUALITY | QA integral, revisión de seguridad final, correcciones | `test-report.md` y revisión de seguridad final, con defectos cerrados | Revisión SEC aprobada y 0 Altas abiertas | Recomendación | implementation-plan.md |
| P5 OPERATIONS y DOCUMENTATION | Entornos, copias, restauración, runbook, manual, datos reales | `deployment-runbook.md`, manual admin, acta de restauración, índice documental | Autorización explícita de despliegue | Recomendación | implementation-plan.md |
| P6 DELIVERY | Auditoría, go/no-go | `delivery-audit.md` | Aprobación del cliente | Recomendación | implementation-plan.md |

**Estrategia de ejecución (resumen):** puertas primero (sin código sin alcance aprobado, GATE-002 y aprobación humana PLANNING → BUILD); núcleo transaccional primero; mocks y sandbox para pasarela, correo y anti-bot; seguridad desde el diseño (los SEG son criterios de cierre de cada tarea); despliegue fuera del plan de código (autorización específica y adicional); equipo mínimo. Roles del plan: DIR (único portavoz), TL, BE, FE, DAT (absorbible por BE si el volumen lo permite), DO, QA, SEC (independiente), RT, GD, AUD. No se activan: móvil, desarrollador genérico, Delivery Manager (lo cubre DIR) ni Analista, PM, UX y Arquitecto en BUILD (solo consulta puntual). Sin agente: decisiones del cliente, validación legal, contratación de pasarela, dominio y hosting, fotos y textos finales, aprobación de puertas. Fronteras lógicas (Recomendación; repo y stack aún no existen): BE → `server/modules/*` y `server/worker`; FE → `web/public` y `web/admin`; DAT → `db/migrations` y `db/seed`; DO → `infra/` y `.github/workflows`; QA → `tests/`; RT → `docs/`.

### 7.1 Estimación preliminar de plazo

> **Esta estimación (28 a 36 semanas) corresponde al MVP completo, que pasa a ser la fase siguiente.** La estimación de la oferta principal (opción B, 1 semana para entrega a revisión) está en la sección «Opción B». No se reestimó el MVP completo considerando lo reutilizable de la entrega inicial.

**Origen:** estimación sustentada del Planificador de Proyecto, persistida en [estimacion-plazo.md](../05-planning/estimacion-plazo.md) y transcrita aquí tal como la entregó el Director (el plan declara «sin fechas»). Es una **Recomendación a confirmar, no un compromiso**; no contiene fechas de calendario ni costos. Se cuenta desde la autorización de construcción (H0).

| Concepto | Valor | Estado |
|---|---|---|
| Rango en semanas | **Recomendado a comunicar: 28 a 36 semanas** desde H0; valor más probable 30–31 semanas | Recomendación a confirmar |
| Método | Tamaños S/M/L (S 0,5–1; M 1–2; L 2–4 semanas-persona); esfuerzo total ≈ 63 semanas-persona; plazo determinado por la ruta crítica | Recomendación |
| Supuestos de equipo y capacidad | 2 backend a tiempo completo; 1 frontend a tiempo completo; datos 1 en la fase 1 y luego 0,5; DevOps 0,5; QA 0,5 desde la fase 1 y 1 desde la fase 2; seguridad, redacción, tech lead y director puntuales. Con **un solo backend** el plazo sube un 25–40 % (≈ 38–42 semanas) | Supuesto |
| Condiciones (decisiones bloqueantes, tiempos de respuesta del cliente) | Decisiones bloqueantes B1 a B9 resueltas antes de H0; MFA, auditoría mínima y precio > 0 dentro del alcance; el cliente responde cada entrega en ≤ 3 días hábiles | Pendiente |
| Holgura | Contingencia del 15–20 % ya incluida en el extremo alto del rango. Se revisará en H1 y H2 | Recomendación |
| Fecha de inicio confirmada | PENDIENTE | Pendiente |
| Fecha calendario de entrega | PENDIENTE: se confirmará al fijar la fecha de inicio. Se necesitan: fecha de autorización de BUILD, dedicación real, fecha objetivo y estacionalidad del cliente, proveedor de pasarela y su plazo, hosting, asesoría legal y calendario de feedback y entrega de fotos y textos | Pendiente |

**Duración por fase** (semanas desde H0; «probable» y rango optimista–pesimista del método). **Los extremos del método son una referencia técnica y no se ofrecen al cliente:** la propuesta comunica solo el rango recomendado de 28 a 36 semanas.

| Fase | Probable | Rango (optimista – pesimista) | Hito de cierre (semana relativa aprox.) |
|---|---|---|---|
| P0 Decisiones y aprobación de alcance | Fuera del reloj: ≈ 3 | 2 – 4 o más | — |
| P1 Fundaciones | 4 | 3 – 6 | H1 (~S4) |
| P2 Núcleo de reserva y pago | 9 | 7 – 12 | H2 (~S13) |
| P3 Post-reserva, panel y web | 6 | 4 – 9 | H3 (~S19) |
| P4 Calidad y seguridad | 6 | 4 – 9 | H4 (~S25) |
| P5 Operación y documentación | 3 | 2 – 6 | H5 (~S28) |
| P6 Auditoría y cierre | 2 | 2 – 3 | H6 (~S30) |
| **Total P1–P6** | **30** | 22 – 45 (referencia del método, no es oferta) | |

Las fases se suceden en secuencia (duración probable acumulada: 4, 13, 19, 25, 28 y 30 semanas), por lo que los hitos coinciden con los cierres de fase.

**Hitos relativos al inicio:** S0 · H0 BUILD autorizado; ~S4 · H1 esqueleto, CI y esquema con exclusión probada (revisión de componentes y marca); ~S8 · revisión intermedia: catálogo, búsqueda y precio; ~S13 · H2 reserva y pago en sandbox sin doble reserva; ~S19 · H3 MVP funcional completo; ~S25 · H4 calidad y seguridad aprobadas; ~S28 · H5 operable con restauración probada, runbook y manual; ~S30 · H6 auditoría y go/no-go.

**Límites aproximados de las decisiones del cliente (si el plan arranca con ellas abiertas):** B1 pasarela y titularidad ~S6; B6 MFA ~S8; B2, B8 y B9 hosting, RPO/RTO, dominio y cuentas ~S10; B3 y B5 cancelación y segundo factor ~S14; B4 y B7 legal y retención, antes de ~S20.

**No incluye:** tiempos de terceros (alta de la pasarela, DNS, dominio de correo, asesoría legal); esperas de decisión del cliente (se suman 1:1); Fase 2; ampliaciones; cambios no registrados como solicitud de cambio; puesta en producción con tráfico real (requiere autorización específica).

**Observación del Redactor (para el Director):** el supuesto «B1 a B9 resueltas antes de H0» y los «límites aproximados» de cada decisión (S6 a S20) conviven en la estimación recibida. Se interpretan así: la estimación asume las decisiones resueltas antes de H0; si no lo están, cada una tiene un límite aproximado tras el cual el plazo se mueve 1:1. Se pide confirmación del Planificador. Además, la propia estimación de tamaños no tiene base histórica (R-PL-007) y se revisará tras H1.

### 7.2 Desglose de tareas del plan (TASK-010 a TASK-071)

Estado de todas: **BACKLOG**, sin asignar y **sin autorización** (TASKS.md §2.1). El responsable es una propuesta. T = tamaño relativo (S/M/L). «TL» = TASK-014; «ARR» = arranque (H0). Los IDs TASK-010, TASK-011 y TASK-012 del plan figuran en el registro como TASK-010 [PLAN], TASK-011 [PLAN] y TASK-012 [PLAN] por colisión de identificadores (ISS-024); no se reutilizan IDs.

| ID | Objetivo → salida | Resp. | T | Dependencias (del plan) | Cierre (evidencia) |
|---|---|---|---|---|---|
| TASK-010 [PLAN] | Paquete de decisiones bloqueantes → registro en DECISIONS | DIR | S | TASK-004, 007, 008 | Las 9 decisiones B1 a B9 respondidas por escrito |
| TASK-011 [PLAN] | Formalizar UX, arquitectura y seguridad en `03-ux`, `04-architecture`, `08-security` | GD | S | GATE-002 | Archivos persistidos y revisados por DIR |
| TASK-012 [PLAN] | Validación legal (= TASK-006) → informe de la asesoría | Cliente | M | — | Informe sobre RGPD, cookies, IVA, desistimiento y SCA |
| TASK-013 | Aprobación del plan y solicitud PLANNING → BUILD | DIR/Humano | S | 010, 011, 014 | Aprobación registrada en APPROVALS |
| TASK-014 | Stack, convenciones, ADR finales y contratos de API | TL | S | GATE-002 | ADR-001 a 012 aprobados o modificados |
| TASK-020 | Repo, ramas protegidas, CI (lint, test, SCA, secretos, SAST, presupuesto Lighthouse), entorno local | DO | M | ARR, 014 | CI verde en repo vacío; escaneo de secretos activo |
| TASK-021 | Esquema y migraciones: `occupancy` con exclusión, reserva, pago, `payment_event`, `consent`, `policy_version`, auditoría, outbox, roles de BD de mínimo privilegio | DAT | L | ARR, 014 | Migraciones con marcha atrás; pruebas de exclusión (CA-002) |
| TASK-022 | Semillas de ejemplo «por validar», sin datos reales | DAT | S | 021 | Datos sintéticos; sin PII (SEG-012) |
| TASK-023 | Esqueleto BE: config por entorno, errores, idempotencia, logs con redacción, cabeceras (CSP, HSTS) | BE | M | 014, 021 | SEG-008 base y SEG-011 verificados con pruebas |
| TASK-024 | Sistema de componentes FE con tokens de marca provisionales y accesibilidad base | FE | M | ARR, UX | Storybook o equivalente; axe sin críticos |
| TASK-030 | Precio y temporadas en servidor, mínimo de noches, instantánea | BE | M | 021, 023 | CA-012, 017, 034 con pruebas unitarias |
| TASK-031 | Disponibilidad y búsqueda | BE | M | 021, 023 | CA-001, 002, 009, 015 |
| TASK-032 | Reserva pendiente, hold, consentimientos versionados, conductor, edad mínima | BE | M | 030, 031 | CA-003, 010, 018, 033; concurrencia OK |
| TASK-033 | `PaymentProvider`, adaptador mock y sandbox, webhook firmado, máquina de estados, idempotencia | BE | L | 032 | CA-004, 006, 031, 032; SEG-002 en pruebas |
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
| TASK-052 | E2E, accesibilidad, SEO y CWV | QA | L | 044, 045, «B-P12» (ID no definido, ISS-031) | CA-014, 028, 030 con protocolo acordado |
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

### 7.3 Orden, ruta crítica y dependencias

- **Orden de implementación:** P0: 010, 011, 012, 014, 013 (012 en paralelo). P1: 020, 021, 024 en paralelo; después 022, 023. P2: 030 y 031, luego 032, 033, 034; 035 y 036 en paralelo a 033; 037 sigue a 036. P3: 040, 041, 042 y 046; después 043, luego 044, y 045 en paralelo; 050 puede arrancar en P1. P4: 051, 052, 053, 054. P5: 060, 061, 062, 064, 063, 065. P6: 070 y 071.
- **Ruta crítica:** aprobación de alcance y GATE-002 → decisiones B1 a B9 → TASK-014 → TASK-021 → 031/030 → 032 → 033 (adaptador real) → 034 → 041 → 051 → 053 → 061 + legal final + 064 → autorización de despliegue → 063. Fuera de la ruta crítica: FE y panel (036, 037, 044, 045), correo (040), SEO y documentación.
- **Decisiones bloqueantes B1 a B9** (el plan afirma que «el cliente las eligió como puerta de inicio de BUILD»; no hay evidencia en APPROVALS, ISS-027): B1 pasarela y titularidad; B2 hosting y región (UE, Recomendación); B3 política de cancelación (valores, momento y comisiones); B4 validación legal (el PM la trata como bloqueo de producción; el plan recomienda que para BUILD baste asesoría contratada, alcance legal e inventario de datos, y los textos finales antes de producción); B5 acceso y cancelación con segundo factor o enlace mágico; B6 MFA obligatorio; B7 retención de datos; B8 RPO/RTO; B9 dominio y titularidad de cuentas. Del Director, que acompañan: resolver ISS-004 a ISS-011 incluido el pago total; auditoría mínima en el MVP; VAL-020 con precio > 0; prioridades P-004, P-007 y P-009.
- **Pueden empezar con dependencias abiertas** (mock, sandbox o aislamiento): 020, 021, 022 (B2 abierto); 023, 024, 030, 031, 032 (marca, B3); 033 (B1; `PaymentProvider` con mock y sandbox); 034, 035 (B1; contra mock); 036, 037, 045, 046 (marca, textos legales como marcadores); 040 (B9; proveedor simulado); 042, 043, 044 (B6; MFA por defecto como obligatorio). **No pueden empezar o cerrar sin su decisión:** adaptador real de 033 (B1); cierre de 041 (B3 y B5); 060 y 063 (B2, B8, B9 y autorización); 053 con SEG-010 (B4 y B7); cierre de 030 y 031 (PEND-013, con `date` por defecto).

### 7.4 Definición de preparado y de terminado

- **Preparado:** alcance y puerta aprobados; dependencias cerradas o mock acordado; archivos propios asignados sin solapes; CA y SEG aplicables identificados; datos de prueba y sandbox disponibles.
- **Terminado (por tarea):** cumple los CA y SEG de su fila; pruebas ejecutadas con evidencia; pasa CI (lint, SCA, SAST, secretos); revisión de TL; sin secretos ni PII en repo y logs; trazabilidad actualizada.
- **Del MVP completo:** CA-001 a CA-034 trazados, 0 Altas abiertas, revisión SEC aprobada, restauración probada, manual y runbook entregados. Nada se declara terminado sin evidencia.
- **Plan de validación (propuesto; nada ejecutado):** unitarias, concurrencia, pago, E2E (R1 a R5), accesibilidad y CWV (protocolo acordado antes de P4), SEO, seguridad, operación.
- **Entregables por fase:** P0 decisiones B1 a B9, plan aprobado, UX y arquitectura persistidos; P1 repo, CI, esquema y migraciones; P2 módulos con pruebas; P3 correo, consulta y cancelación, panel, web con SEO y legales; P4 `test-report.md` y `security-review.md` final; P5 `deployment-runbook.md`, manual admin, acta de restauración, índice documental; P6 `delivery-audit.md`.

## 8. Riesgos

Fuente: [RISKS.md](../00-control/RISKS.md) (riesgos de cada reporte, copiados como los redactó cada fuente). Probabilidad e impacto solo constan donde la fuente los evaluó (el plan); el resto es «no evaluado» (—) para no inventarlos. Ningún riesgo ha sido aceptado. Los identificadores R-001 a R-013 del Analista colisionan con R-001 a R-010 del Product Manager (ISS-003); se conserva el calificador provisional [AN], [PM], [UX], [ARQ] o [PLAN] (DEC-031 pendiente).

### 8.1 Riesgos del Analista de Negocio [AN]

| ID | Riesgo | Prob. | Impacto | Mitigación (según la fuente) | Estado | Fuente |
|---|---|---|---|---|---|---|
| R-001 [AN] | Requisitos legales sin validar a tiempo (RGPD, cookies, consumidores, IVA, facturación) | — | — | Revisión por asesoría legal antes de DESIGN | OPEN | [RISKS.md](../00-control/RISKS.md) §1 |
| R-002 [AN] | Política de pago y cancelación sin definir bloquea el flujo y los estados | — | — | Decidir Q1 en DISCOVERY | OPEN | RISKS.md §1 |
| R-003 [AN] | Doble reserva por concurrencia | — | — | RN-003, RN-016, RNF-007 y pruebas específicas | OPEN | RISKS.md §1 |
| R-004 [AN] | Proveedor de pasarela no elegido (comisiones, reembolsos parciales, preautorización) | — | — | Decisión del cliente; evaluación técnica posterior | OPEN | RISKS.md §1 |
| R-005 [AN] | Imágenes de ejemplo afectan la confianza y la conversión | — | — | Plan de sustitución con fotos reales (RNF-013) | OPEN | RISKS.md §1 |
| R-006 [AN] | Expectativa de SEO como «garantía» de posicionamiento | — | — | Dejar claro que se aplican buenas prácticas, no resultados | OPEN | RISKS.md §1 |
| R-007 [AN] | «Completa» y «robusto» no están acotados y favorecen la ampliación de alcance | — | — | Fijar MVP, F2 y AMP y gestionar cambios con CR | OPEN | RISKS.md §1 |
| R-008 [AN] | «Velocidad» sin objetivo medible | — | — | Adoptar RNF-001 si el cliente lo acepta | OPEN | RISKS.md §1 |
| R-009 [AN] | Pedir documentos de identidad o carnet aumenta riesgo y obligaciones de privacidad | — | — | Resolver Q5 | OPEN | RISKS.md §1 |
| R-010 [AN] | Fianza y saldo pendiente generan operación manual y riesgo de impago | — | — | Decidir Q1 y Q2 | OPEN | RISKS.md §1 |
| R-011 [AN] | Volumen y picos estacionales desconocidos | — | — | Pedirlos en DISCOVERY (RNF-012) | OPEN | RISKS.md §1 |
| R-012 [AN] | Mala entregabilidad de correos transaccionales | — | — | RNF-014 | OPEN | RISKS.md §1 |
| R-013 [AN] | Costes de pasarela, correo y hosting fuera del contrato pueden sorprender al cliente | — | — | Informarlos como costes recurrentes, sin estimarlos | OPEN | RISKS.md §1 |

### 8.2 Riesgos del Product Manager [PM]

| ID | Riesgo | Prob. | Impacto | Mitigación (según la fuente) | Estado | Fuente |
|---|---|---|---|---|---|---|
| R-001 [PM] | Políticas de pago, cancelación y precios no se validan a tiempo | — | — | Valores de ejemplo «por validar», configurables, y validación del cliente antes de publicar | OPEN | [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) |
| R-002 [PM] | Textos legales o cumplimiento sin revisar (RGPD, cookies, precontractual, desistimiento, IVA, PSD2) | — | — | Revisión por asesoría legal antes de salir (no es asesoramiento legal) | OPEN | mvp-and-backlog.md |
| R-003 [PM] | Sin alta manual de reservas en el MVP, la reserva telefónica depende del bloqueo manual | — | — | Comunicar la limitación; valorar RF-028 como primera ola de Fase 2 | OPEN | mvp-and-backlog.md |
| R-004 [PM] | Sin cuentas de usuario, el cliente depende del código: si lo pierde, tiene que contactar | — | — | Reenvío del correo de confirmación y contacto visible | OPEN | mvp-and-backlog.md |
| R-005 [PM] | Pago total al reservar puede aumentar el abandono frente a depósito | — | — | Medir abandono; depósito + saldo en Fase 2 | OPEN | mvp-and-backlog.md |
| R-006 [PM] | Reembolsos automáticos con política mal configurada | — | — | Valores por validar; pruebas de los casos de la política antes de salir | OPEN | mvp-and-backlog.md |
| R-007 [PM] | Expectativas de SEO y velocidad más altas que lo prometido | — | — | Comunicar que el SEO es técnico y sin garantía (RNF-002) y que las métricas son objetivo | OPEN | mvp-and-backlog.md |
| R-008 [PM] | Imágenes de ejemplo en producción | — | — | Marcar su sustitución como tarea previa a la publicación | OPEN | mvp-and-backlog.md |
| R-009 [PM] | Desactivar un camper con reservas futuras, regla sin definir | — | — | Ver P-011 | OPEN | mvp-and-backlog.md |
| R-010 [PM] | Pago tardío o fallo de notificación de la pasarela genera estados inconsistentes | — | — | CA-004, CA-007 y trazabilidad de eventos (RNF-009) | OPEN | mvp-and-backlog.md |

### 8.3 Riesgos de experiencia [UX] y técnicos [ARQ]

| ID | Riesgo | Prob. | Impacto | Mitigación (según la fuente) | Estado | Fuente |
|---|---|---|---|---|---|---|
| R-UX-01 | ISS-002: el momento de la política de cancelación cambia el texto y el cálculo de P05 y P10 | — | — | El diseño no elige; P10 muestra el reembolso del servidor y la versión de política | OPEN | [ux-specification.md](../03-ux/ux-specification.md) §15 |
| R-UX-02 | Pago total al reservar puede aumentar el abandono (R-005 [PM]) | — | — | Se mide | OPEN | ux-specification.md §15 |
| R-UX-03 | Fotos de ejemplo reducen la confianza y la conversión | — | — | Plan de sustitución previo a la publicación | OPEN | ux-specification.md §15 |
| R-UX-04 | Sin cuentas: si el cliente pierde el código depende del reenvío del correo y del contacto | — | — | Mostrarlos con claridad | OPEN | ux-specification.md §15 |
| R-UX-05 | El bloqueo vence mientras el cliente autentica el pago: frustración y pagos tardíos | — | — | Avisos del temporizador | OPEN | ux-specification.md §15 |
| R-UX-06 | El estado «verificando» puede generar consultas si la pasarela tarda | — | — | Mensaje que tranquilice y explique el correo posterior | OPEN | ux-specification.md §15 |
| R-UX-07 | Textos legales sin validar en el pie y en los pasos de reserva | — | — | Validación legal (PEND-010) | OPEN | ux-specification.md §15 |
| R-UX-08 | Reservas por teléfono solo con bloqueo manual, con riesgo de error del administrador | — | — | R-003 [PM] | OPEN | ux-specification.md §15 |
| R-UX-09 | Fianza informativa: el cliente puede esperar que se cobre en la web | — | — | Texto muy explícito | OPEN | ux-specification.md §15 |
| R-UX-10 | Marca: tipografía y paleta provisionales; cambiarlas tarde implica rehacer componentes | — | — | PEND-025 | OPEN | ux-specification.md §15 |
| R-ARQ-01 | Pasarela no elegida, o con particularidades que obliguen a rediseñar el pago | — | — | ADR-004; prueba de concepto con el sandbox al elegir | OPEN | [solution-architecture.md](../04-architecture/solution-architecture.md) |
| R-ARQ-02 | Caducidad mínima de la sesión de pago mayor que el hold de 15 min (verificar por proveedor) | — | — | Alinear hold y sesión; ADR-007 cubre el pago tardío | OPEN | solution-architecture.md |
| R-ARQ-03 | Pago tardío y doble gestión en condiciones de carrera | — | — | Transacciones y pruebas de concurrencia (ADR-003, ADR-006, ADR-007) | OPEN | solution-architecture.md |
| R-ARQ-04 | Política de cancelación indefinida (ISS-002) | — | — | ADR-008 admite ambas; regla tras validación legal | OPEN | solution-architecture.md |
| R-ARQ-05 | Noche frente a día y horas de recogida sin definir (PEND-013); puede forzar cambiar `date` por fecha-hora | — | — | Aislar el cálculo del rango en un solo módulo | OPEN | solution-architecture.md |
| R-ARQ-06 | Hosting no definido y objetivos RNF-011 y RNF-012 sin cifras | — | — | Decidir hosting temprano; no comprometer SLA | OPEN | solution-architecture.md |
| R-ARQ-07 | Acceso por código + email adivinable o enumerable | — | — | Entropía alta, errores uniformes, límite de intentos, enlace mágico opcional | OPEN | solution-architecture.md |
| R-ARQ-08 | Cumplimiento legal incompleto (RGPD, cookies, consumidores, IVA, facturación) | — | — | PEND-010; consentimientos versionados y retención configurable | OPEN | solution-architecture.md |
| R-ARQ-09 | Entregabilidad del correo | — | — | Dominio propio (PEND-011), SPF/DKIM/DMARC y cola con reintentos | OPEN | solution-architecture.md |
| R-ARQ-10 | Sobrediseño en puntos de extensión | — | — | ADR-012: solo estructura mínima | OPEN | solution-architecture.md |
| R-ARQ-11 | Fotos reales no disponibles y rendimiento bajo | — | — | Imágenes de ejemplo sustituibles, límites de peso y optimización | OPEN | solution-architecture.md |
| R-ARQ-12 | Reembolsos y comisiones: titularidad y quién asume las comisiones (PEND-009) | — | — | Decisión del cliente | OPEN | solution-architecture.md |

### 8.4 Riesgos del plan [PLAN] y hallazgos de seguridad

| ID | Riesgo | Prob. | Impacto | Mitigación (según la fuente) | Estado | Fuente |
|---|---|---|---|---|---|---|
| R-PL-001 | Decisiones B1 a B9 llegan tarde y paran el núcleo de pago | Alta | Alta | Paquete único TASK-010 [PLAN]; mock; seguimiento en DECISIONS | OPEN | [implementation-plan.md](../05-planning/implementation-plan.md) |
| R-PL-002 | Cambio de alcance (MFA, auditoría, precio > 0) sin CR | Media | Alta | DIR lo registra como CR antes de H0 | OPEN | implementation-plan.md |
| R-PL-003 | Sesión de pago con caducidad mayor que el hold (R-ARQ-02) | Media | Alta | PoC con el sandbox elegido en TASK-033 | OPEN | implementation-plan.md |
| R-PL-004 | Carrera hold, expiración y webhook produce doble reserva o cobro sin servicio (SEG-003) | Media | Alta | Exclusión en BD; pruebas de concurrencia en CI | OPEN | implementation-plan.md |
| R-PL-005 | Política de cancelación indefinida cambia el cálculo (ISS-002) | Alta | Media | Políticas versionadas (ADR-008); cierre de 041 condicionado a B3 | OPEN | implementation-plan.md |
| R-PL-006 | Validación legal tardía retrasa producción | Alta | Alta | Contratar asesoría pronto; textos como marcadores | OPEN | implementation-plan.md |
| R-PL-007 | Estimaciones S/M/L sin base histórica | Alta | Media | Usar solo como orden relativo; revisar tras H1 | OPEN | implementation-plan.md |
| R-PL-008 | Contratos de API cambian y rompen FE y BE | Media | Media | TL fija contratos; FE usa mock hasta que BE publique | OPEN | implementation-plan.md |
| R-PL-009 | Cliente no entrega datos reales y fotos | Media | Media | TASK-064 con dueño; imágenes de ejemplo sustituibles | OPEN | implementation-plan.md |
| R-PL-010 | Hosting sin PostgreSQL con exclusión o worker persistente | Baja | Alta | B2 antes de 060; criterios de hosting en TASK-014 | OPEN | implementation-plan.md |
| R-PL-011 | Sobrediseño en puntos de extensión (ADR-012) | Media | Baja | Solo estructura mínima | OPEN | implementation-plan.md |
| SEG-001 a SEG-017 | Hallazgos de seguridad de diseño (sección 6.1): 7 Altas, 1 Alta «validar legal», 8 Medias, 1 Baja | Alta / Media / Baja (según el Revisor) | — | Controles de la sección 6.2 | OPEN | [security-review.md](../08-security/security-review.md) |

Varios riesgos del plan se solapan con riesgos ya registrados (R-PL-003 con R-ARQ-02; R-PL-004 con R-ARQ-03 y SEG-003; R-PL-005 con ISS-002, R-ARQ-04 y R-UX-01; R-PL-006 con R-001 [AN] y R-002 [PM]; R-PL-009 con R-008 [PM] y R-UX-03; R-PL-010 con R-ARQ-06; R-PL-011 con R-ARQ-10). No se fusionan (ISS-033).

## 9. Decisiones pendientes

Fuente: [DECISIONS.md](../00-control/DECISIONS.md). **Ninguna decisión está aprobada.** Hay 32 propuestas generales (DEC-001 a DEC-032), 12 de arquitectura (ADR-001 a ADR-012, sección 5.1), 40 pendientes de confirmación (PEND-001 a PEND-040) y 9 decisiones bloqueantes de BUILD según el plan (B1 a B9). El Director aprobó DEC-001 a DEC-032 solo como *registro de propuestas pendientes*; el cliente delegó («pon tu las reglas», «lo que creas conveniente», «crealo») pero no las ha confirmado. **Criterio de prevalencia (DEC-029):** en las diferencias de alcance entre Analista y PM se registra como propuesta la versión del PM, pendiente de aprobación del cliente (excepción: CA-008, ver DEC-025). No es una resolución.

### 9.1 Propuestas generales (DEC-001 a DEC-032)

Estado de todas: PROPUESTA. Decisor: pendiente (cliente, vía Director).

| ID | Propuesta | Impacto |
|---|---|---|
| DEC-001 | Pago **total** al reservar en el MVP (alternativa del AN: depósito + saldo; ISS-005) | RN-013, RN-022, RF-008, HU-007 |
| DEC-002 | Depósito + saldo diferido en **Fase 2** (HU-030, Should) (ISS-004) | RF-031, RN-013, RN-022, HU-030 |
| DEC-003 | Solo **tarjeta** en el MVP; otros medios como ampliación | RF-008, RF-031 |
| DEC-004 | Fianza **informativa**, gestionada en la entrega; fianza en línea como ampliación; importe y texto Pendiente (PEND-018) | RN-017, RF-004, RF-020 |
| DEC-005 | Acceso a la reserva con **código + email** en el MVP (ISS-008) | RF-012, RN-025, HU-011 |
| DEC-006 | **Cuentas de cliente** en Fase 2 (Could, HU-032) | RF-012, HU-032 |
| DEC-007 | **Justificante** de pago en el MVP; **factura automática** en Fase 2 (HU-031, Should) (ISS-004) | RN-027, RF-010, RF-031, HU-031 |
| DEC-008 | **Clientes empresa** (con NIF) en Fase 2, junto con la factura automática | RN-027, Q4 |
| DEC-009 | **Español** como idioma único y **euros** como moneda; multi-idioma como ampliación (público extranjero para SEO: PEND-016) | RN-005, RF-031 |
| DEC-010 | Verificar los documentos del conductor **en persona** en la recogida; subida de documentos como ampliación (ISS-014) | RN-024, VAL-012, RF-031 |
| DEC-011 | **Edad mínima declarada configurable** como validación del MVP; valor Pendiente (PEND-019) | RN-024, VAL-011, CA-018 |
| DEC-012 | Recogida y devolución en la **misma sede** en el MVP (ISS-011) | RN-002, RN-006, CA-033 |
| DEC-013 | Devolución en **otra sede con suplemento** en Fase 2 (Could, HU-036) | RN-006, HU-036 |
| DEC-014 | **Rol único** (administrador) en el MVP | RF-019, HU-017 |
| DEC-015 | **Reservas manuales** en Fase 2 (RF-028); cubiertas en el MVP por el bloqueo manual de fechas (RF-024) | RF-024, RF-028 |
| DEC-016 | **Informes y registro de auditoría** en Fase 2 (RF-029) (la seguridad recomienda auditoría mínima en el MVP: PEND-038) | RF-029, HU-033 |
| DEC-017 | **Roles adicionales** (operador de sede) en Fase 2 (RF-030) | RF-030, HU-034 |
| DEC-018 | **Extras** en Fase 2 (RF-005 y parte de RF-022); si se necesitan en la salida inicial, sería una solicitud de cambio (ISS-006) | RF-005, RF-022, RN-012, HU-025 |
| DEC-019 | **Contacto** en el MVP; **FAQ** en Fase 2 (ISS-007) | RF-015, HU-013, HU-026 |
| DEC-020 | **Modificación de reserva** en Fase 2 (RF-014) | RF-014, HU-027 |
| DEC-021 | **Plantillas de correo editables** en Fase 2 (RF-027) | RF-027, HU-029 |
| DEC-022 | **Aviso mínimo por correo al administrador** en el MVP (reserva nueva, cancelación, pago tardío sin disponibilidad); centro de avisos completo en Fase 2 (ISS-010) | RF-026, HU-024, HU-035 |
| DEC-023 | **Correos al cliente en el MVP:** confirmación con código y justificante (CA-019); los demás tipos de RN-018 sin asignar (propuesta parcial; ISS-009) | RF-010, RN-018, CA-019 |
| DEC-024 | **Cancelación por el cliente con reembolso automático** en el MVP; alternativa: cancelación solo por el administrador (P-004) | RF-013, HU-012 |
| DEC-025 | Aplicar la política de cancelación **vigente al reservar** (recomendación adicional del Director: más previsible para el consumidor), pendiente de validación legal (PEND-010); resuelve ISS-002 | RN-014, CA-008, RF-013 |
| DEC-026 | **Cancelación por la empresa:** reembolso total o alternativa de vehículo, con aviso inmediato; regla detallada Pendiente (PEND-008) | RN-019, RN-021 |
| DEC-027 | **Bloqueo temporal de 15 min**, configurable (valor no confirmado, P-003) | RF-007, RN-016, CA-003, CA-005 |
| DEC-028 | **Desactivar, no eliminar**, un vehículo o sede con reservas futuras, con aviso del impacto; regla detallada Pendiente (PEND-024) | RF-020, RF-021, VAL-021 |
| DEC-029 | **Criterio de prevalencia:** ante diferencias de alcance o prioridad entre AN y PM se registra como propuesta la versión del PM; excepción CA-008 (DEC-025) | ISS-004 a ISS-008, ISS-010, ISS-011, ISS-014 |
| DEC-030 | **Reconciliación de CA-001 a CA-014** entre AN y PM. Sin propuesta en las fuentes | ISS-001 |
| DEC-031 | **Colisión de IDs de riesgo** R-001 a R-013 y R-001 a R-010: mantener el calificador [AN]/[PM] o renumerar. Sin propuesta | ISS-003 |
| DEC-032 | **Registro de los prefijos** VAL-, Q- y P- en el catálogo de identificadores. Sin propuesta | ISS-013 |

### 9.2 Pendientes de confirmación (PEND-001 a PEND-040)

Todos pendientes. «Cliente» = cliente, vía Director.

| ID | Pendiente | Responsable |
|---|---|---|
| PEND-001 | Q1. Modelo de cobro: pago total o depósito + saldo; otros medios además de tarjeta | Cliente |
| PEND-002 | Q2. Fianza: en la entrega o con preautorización en línea | Cliente |
| PEND-003 | Q3. Acceso del cliente: cuenta de usuario o código + email | Cliente |
| PEND-004 | Q4. Facturación y tipo de cliente: factura automática o justificante; clientes empresa; más idiomas | Cliente |
| PEND-005 | Q5. Verificación del conductor: documentos en la web o en la recogida; edad mínima; conductores adicionales | Cliente |
| PEND-006 | Q6. Devolución en otra sede y suplemento | Cliente |
| PEND-007 | Q7. Panel: número de personas, permisos, reservas manuales o informes en el MVP | Cliente |
| PEND-008 | P-001 (parte 1). Valores de la política de cancelación escalonada, regla cuando cancela la empresa, porcentaje de depósito y mínimos de noches | Cliente |
| PEND-009 | P-001 (parte 2). Quién asume las comisiones de la pasarela en los reembolsos | Cliente |
| PEND-010 | P-005. Validación legal (privacidad, cookies, precontractual, desistimiento, IVA, PSD2/SCA, facturación, seguros y licencias; incluye DEC-025) | Cliente / asesoría legal |
| PEND-011 | P-014. Titularidad de la cuenta de la pasarela, del dominio y del remitente de correo | Cliente |
| PEND-012 | Proveedor de la pasarela de pago | Cliente |
| PEND-013 | P-010. «Noche» frente a «día», horas de recogida y devolución, y zona horaria (Canarias) | Cliente |
| PEND-014 | P-012. Protocolo de medición del rendimiento y alcance de la revisión de accesibilidad | Director / cliente |
| PEND-015 | P-013. Metas numéricas de métricas y valores de disponibilidad y escalabilidad (RNF-011, RNF-012) | Cliente |
| PEND-016 | P-015. Alcance de público extranjero para el SEO siendo solo en español | Cliente |
| PEND-017 | P-016. Antelación mínima y máxima de reserva y duración máxima (RN-009) | Cliente |
| PEND-018 | P-002 (parte). Importe y texto de la fianza informativa | Cliente |
| PEND-019 | P-006. Edad mínima del conductor y requisitos de permiso | Cliente |
| PEND-020 | Datos y contenidos iniciales: flota, sedes, tarifas, fotos reales y FAQ | Cliente |
| PEND-021 | Proceso actual del cliente, tamaño de la flota y volumen esperado | Cliente |
| PEND-022 | Textos de condiciones de alquiler y proveedor de correo | Cliente |
| PEND-023 | Condiciones de no presentación y devolución tardía (RN-020) y cliente sin acceso a su email | Cliente |
| PEND-024 | P-011. Regla al desactivar un vehículo o sede con reservas futuras | Cliente |
| PEND-025 | Marca: nombre, logotipo, paleta, tipografía, tono, estilo fotográfico e iconografía; ¿hay material de marca? | Cliente |
| PEND-026 | Recuperación de contraseña del administrador (UX P14) | Cliente |
| PEND-027 | Dónde se configura el correo de aviso al administrador (UX P21) | Cliente / Director |
| PEND-028 | Una o varias sedes y cobertura SEO por sede | Cliente |
| PEND-029 | Precio orientativo «desde» en el catálogo | Cliente / Director |
| PEND-030 | Comportamiento público de las fichas desactivadas (404 o redirección) | Cliente / Director |
| PEND-031 | Ampliación del tiempo del bloqueo (WCAG 2.2.1) y mensaje «verificando pago» | Director / cliente |
| PEND-032 | Pantalla de inicio en el panel o «Reservas» como entrada | Director |
| PEND-033 | Activar el diseño formal pese a GATE-002 PENDING. **Resuelta por el Director (2026-10-26):** el diseño continúa como BORRADOR con GATE-002 PENDING; ningún artefacto se considera aprobado | Director |
| PEND-034 | Hosting y región (UE como recomendación) | Cliente |
| PEND-035 | Acceso del cliente por código + email o enlace mágico; MFA del administrador | Cliente |
| PEND-036 | Plazos de retención de datos y procedimiento de anonimizado o supresión | Cliente / asesoría legal |
| PEND-037 | Segundo factor o reautenticación por correo antes de **cancelar** (SEG-001; parte de B5) | Cliente |
| PEND-038 | Auditoría mínima en el MVP (SEG-007); cambio de alcance (R-PL-002) | Director / cliente |
| PEND-039 | VAL-020 con precio > 0 o flujo de importe 0 (SEG-005); cambio de alcance | Director / cliente |
| PEND-040 | Resolver ISS-004 a ISS-011, incluido el pago total, y priorizar P-004, P-007 y P-009 | Director |

### 9.3 Decisiones bloqueantes de BUILD (B1 a B9) según el plan

Fuente: [implementation-plan.md](../05-planning/implementation-plan.md) «Dependencias críticas» y [DECISIONS.md](../00-control/DECISIONS.md) §4. **Ninguna está resuelta.** Los IDs B1 a B9 son del plan (prefijo fuera del catálogo, ISS-013).

| ID | Decisión | Opciones | Recomendación | Impacto | Responsable | Fuente |
|---|---|---|---|---|---|---|
| B1 | Pasarela de pago y titularidad de la cuenta (PEND-012, PEND-011) | Stripe, Redsys, Adyen u otra (ADR-005) | Ninguna propuesta de proveedor | Plazo e inversión; adaptador real de TASK-033 y TASK-060 | Cliente, vía Director | DECISIONS.md §4 |
| B2 | Hosting y región (PEND-034) | PaaS UE con PostgreSQL gestionado / contenedores en VPS / serverless | UE (Recomendación) | Plazo e inversión; TASK-060 y TASK-063 | Cliente, vía Director | DECISIONS.md §4 |
| B3 | Política de cancelación: valores, momento (al reservar / al cancelar, ISS-002) y comisiones (PEND-008, PEND-009) | Al reservar (DEC-025, pendiente de validación legal) / al cancelar (CA-008 del PM) | Políticas versionadas (ADR-008) | Alcance y plazo; cierre de TASK-041 | Cliente, vía Director | DECISIONS.md §4 |
| B4 | Validación legal (PEND-010) | — | Para BUILD basta asesoría contratada, alcance legal definido e inventario de datos; textos finales antes de producción (el PM la trata como bloqueo de producción: contradicción, ISS-028) | Plazo; TASK-053 con SEG-010 | Cliente / asesoría legal | DECISIONS.md §4 |
| B5 | Acceso y cancelación con segundo factor, o enlace mágico (SEG-001, PEND-035, PEND-037) | Código + email / enlace mágico | — | Alcance; cierre de TASK-041 | Cliente, vía Director | DECISIONS.md §4 |
| B6 | MFA obligatorio del administrador (SEG-006) | Obligatorio / recomendado | MFA por defecto como obligatorio | Alcance; TASK-042 | Cliente, vía Director | DECISIONS.md §4 |
| B7 | Retención de datos (SEG-010, PEND-036) | — | — | Plazo; TASK-053 con SEG-010 | Cliente / asesoría legal | DECISIONS.md §4 |
| B8 | RPO/RTO (PEND-015, SEG-013) | — | — | Plazo e inversión; TASK-060, TASK-061 | Cliente, vía Director | DECISIONS.md §4 |
| B9 | Dominio y titularidad de cuentas (pasarela, dominio, correo, hosting) (PEND-011) | — | Correo simulado hasta decidir (TASK-040) | Plazo; TASK-060 | Cliente, vía Director | DECISIONS.md §4 |

Decisiones del Director que acompañan a B1 a B9 (cambio de alcance frente al PM; sin solicitud de cambio registrada): resolver ISS-004 a ISS-011 incluido el pago total (PEND-040); auditoría mínima en el MVP (PEND-038); VAL-020 con precio > 0 (PEND-039). No bloquean BUILD según el plan: marca, nombre y tono; duración del hold; fianza; edad mínima y antelación; noche frente a día (con `date` por defecto); recuperación de contraseña; correo de aviso; desactivación con reservas futuras; protocolo de CWV y accesibilidad (antes de P4); metas de métricas; sede única o múltiple.

### 9.4 Inconsistencias abiertas (ISS-001 a ISS-033) y su tratamiento en esta propuesta

Fuente: [RISKS.md](../00-control/RISKS.md) §2. **Las 33 siguen abiertas.** ISS-001 a ISS-014 son discrepancias entre el Analista (AN) y el Product Manager (PM); ISS-015 a ISS-023 entre UX, arquitectura, PM y AN; ISS-024 a ISS-033 entre seguridad, plan y las demás fuentes (ISS-024 a ISS-033 sin revisar por el Director). El auditor de trazabilidad emitió el veredicto **TRAZABILIDAD_PARCIAL** (informado por el Director). **Tratamiento general:** esta propuesta usa la versión del PM como propuesta pendiente de aprobación (DEC-029), **no resuelve ninguna inconsistencia por cuenta propia** y traslada la decisión al cliente en la sección 10 de la propuesta comercial.

| ID | Inconsistencia (resumen) | Tratamiento en la propuesta | Decisión requerida |
|---|---|---|---|
| ISS-001 | CA-001 a CA-014 con el mismo ID y distinto contenido entre AN y PM (p. ej. CA-001, CA-002, CA-013) | Se muestran ambas versiones (secciones 2.4 y 3.3); la versión del PM es la vigente como propuesta | Director: reconciliar (TASK-007, DEC-030) |
| ISS-002 | Política de cancelación: AN y recomendación del Director «al reservar»; PM (CA-008) «al cancelar» | No se elige; se pregunta al cliente (B3); ADR-008 admite ambas; los mockups no fijan el momento | Cliente y Director, tras validación legal (DEC-025, PEND-010) |
| ISS-003 | Colisión de IDs de riesgo R-001..R-013 [AN] y R-001..R-010 [PM] | Se usa el calificador [AN]/[PM] | Director (DEC-031) |
| ISS-004 | RF-031: saldo diferido y factura automática: AMP (AN) frente a Fase 2 (PM) | Se usa Fase 2 (PM) como propuesta; pregunta 18 y 14 | Cliente (DEC-002, DEC-007) |
| ISS-005 | Modelo de cobro: depósito + saldo (AN) frente a pago total (PM) | Se usa pago total (PM) como propuesta; pregunta 14 | Cliente (PEND-001, DEC-001) |
| ISS-006 | Extras: MVP (AN) frente a Fase 2 (PM) | Se usa Fase 2 (PM); pregunta 22 (pasar al MVP sería solicitud de cambio) | Cliente (DEC-018) |
| ISS-007 | RF-015: contacto y FAQ juntos en MVP (AN) frente a contacto en MVP y FAQ en F2 (PM) | Se usa la división del PM | Decisión (DEC-019) |
| ISS-008 | RF-012: cuenta o código + email (AN) frente a solo código + email, cuentas en F2 (PM) | Se usa código + email (PM); pregunta 17 | Cliente (PEND-003, DEC-005, DEC-006) |
| ISS-009 | Correos transaccionales mínimos: 8 tipos (AN) frente a confirmación y aviso al admin (PM); el resto sin asignar | Se usa el mínimo del PM; pregunta 24 | Director (DEC-023) |
| ISS-010 | RF-026: aviso por reserva o cancelación (AN) frente a aviso mínimo con pago tardío y centro de avisos en F2 (PM) | Se usa el aviso mínimo del PM | Decisión (DEC-022) |
| ISS-011 | Sede de devolución: «no se asume» [P] (AN) frente a misma sede decidida (PM) | Se usa misma sede (PM) como propuesta; pregunta 20 | Cliente (PEND-006, DEC-012, DEC-013) |
| ISS-012 | Zona horaria Europe/Madrid [S] frente a posible zona distinta (Canarias) | Se mantiene como Supuesto; pregunta 26 | Cliente (PEND-013) |
| ISS-013 | Prefijos VAL-, Q-, P-, B-, R-PL- fuera del catálogo corporativo | Se conservan tal cual | Director (DEC-032) |
| ISS-014 | Verificación y edad del conductor: pendiente (AN) frente a edad mínima declarada y documentos en persona (PM) | Se usa la versión del PM; pregunta 19 | Cliente (PEND-005, PEND-019, DEC-010, DEC-011) |
| ISS-015 | ISS-002 propagado a UX y arquitectura sin resolverse | UX y arquitectura no eligen; se transcribe | Director tras validación legal (DEC-025) |
| ISS-016 | Conflicto de contrato declarado solo por UX (el Arquitecto declara «no hay conflicto») | Se registran ambas posiciones; ambos documentos son BORRADOR | Director (PEND-033, resuelta como procedimiento) |
| ISS-017 | Acceso del admin: UX sin MFA ni recuperación; arquitectura recomienda MFA; AN/PM no lo mencionan | MFA obligatorio como recomendación de seguridad (cambio de alcance, pregunta 6 y 10) | Cliente (PEND-026, PEND-035) |
| ISS-018 | Reenvío de correos y del código no definido de extremo a extremo | No se promete; pregunta 24 | Director (DEC-023) |
| ISS-019 | Pago alojado o embebido; bloqueo frente a sesión de pago | Se mantiene «alojado o tokenizado» como Recomendación; los mockups muestran pago alojado | Cliente (PEND-012) y Director (PEND-031) |
| ISS-020 | La matriz del arquitecto no cita RF-023, RN-017, RN-020, RN-024; RN-004 solo en ADR-003 | Se señala en las secciones 5.4 y 10 | Arquitecto vía Director |
| ISS-021 | Precio «desde» y ficha frente a caché; correo de aviso sin entidad en el modelo de datos | Se muestran como Pendiente (PEND-029, PEND-027) | Director |
| ISS-022 | `Europe/Madrid` y tipo `date` fijados en arquitectura mientras PEND-013 sigue abierto | Se mantienen como Supuesto | Cliente (PEND-013) |
| ISS-023 | CA citados por UX y arquitectura sin indicar la versión (AN o PM) | Se transcriben como en la fuente | Director (TASK-007) |
| ISS-024 | Colisión de IDs de tareas del plan con TASK-010 a TASK-012 | Se usa el calificador [PLAN] | Director |
| ISS-025 | Estado de puertas asumido distinto (plan y veredicto del Revisor frente a GATE-002 PENDING) | El veredicto del Revisor no se presenta como aprobación | Director |
| ISS-026 | Momento de cierre de SEG-001 a SEG-007 y SEG-010 («antes de BUILD» frente a P2/P3/P4) | Se transcriben ambas lecturas (secciones 6 y 7) | Director |
| ISS-027 | B1 a B9 como «bloqueantes de BUILD» sin evidencia de elección del cliente | Se presentan como decisiones previas recomendadas; el plan permite empezar con varias abiertas | Director |
| ISS-028 | Validación legal (B4): cuatro lecturas (PM, AN, plan, seguridad) | Se presenta la lectura del plan como Recomendación y la contradicción | Director (PEND-010) |
| ISS-029 | Cambios de alcance que exige seguridad (MFA, auditoría mínima, VAL-020, segundo factor) sin solicitud de cambio | Se presentan como cambios recomendados pendientes de decisión (preguntas 10 a 13); el plazo asume los tres primeros | Director y cliente (PEND-037 a PEND-039) |
| ISS-030 | Controles de seguridad que alteran flujos de UX/PM (verificar correo antes del pago, «mayor de edad», reautenticación en reembolsos, recuperación con enfriamiento) | Se señalan en los mockups y en las notas | Director |
| ISS-031 | IDs mal citados en el plan («B-P12»; «PEND-012/P-012») | Se transcriben sin corregir (TASK-052) | Director (DEC-032) |
| ISS-032 | Dos revisiones con el nombre `security-review.md` (diseño y final) | Se cita solo la revisión de diseño existente | Director |
| ISS-033 | Lecturas parciales del Planificador y del Revisor; riesgos duplicados | Se declaran las limitaciones (secciones 6 y 7); no se fusionan riesgos | Director |

## 10. Trazabilidad

Fuentes: matrices de [TRACEABILITY.md](../00-control/TRACEABILITY.md) (§1, §6, §7, §8, §9), HU y CA de [mvp-and-backlog.md](../02-product/mvp-and-backlog.md), pantallas de [ux-specification.md](../03-ux/ux-specification.md) §14, ADR de [solution-architecture.md](../04-architecture/solution-architecture.md) y tareas de [implementation-plan.md](../05-planning/implementation-plan.md). **La auditoría de trazabilidad emitió TRAZABILIDAD_PARCIAL (informado por el Director).** Las celdas con «—» indican que la fuente no cita el vínculo; no se infieren vínculos nuevos salvo los marcados «†» (asignados por la matriz del Gestor en TRACEABILITY §9). Los CA se citan como en la fuente (ISS-001, ISS-023). Estado de todos los vínculos: PROPUESTO; no hay implementación, pruebas ni defectos.

### 10.1 Requisitos funcionales del MVP propuesto

| Requisito | Historia | Criterio | Pantalla o mockup | Arquitectura | Seguridad | Tareas del plan | Riesgo | Cobertura en la propuesta |
|---|---|---|---|---|---|---|---|---|
| RF-001 | HU-001 | CA-016 | P02, P03 · [03](mockups/03-ficha-camper.html) | ADR-010 (módulo Catálogo) | — | TASK-036† | R-005 [AN], R-008 [PM], R-ARQ-11 | §3.1, §4 |
| RF-002 | HU-002 | CA-015, CA-001, CA-009 | P01, P04 · [01](mockups/01-inicio.html), [02](mockups/02-resultados-busqueda.html), [10](mockups/10-movil-inicio-y-resultados.html) | ADR-003 (módulo Disponibilidad) | — | TASK-031, TASK-036 | — | §3.1, §4 |
| RF-003 | HU-002, HU-003 | CA-001, CA-002, CA-003 | P03, P04 · [02](mockups/02-resultados-busqueda.html), [03](mockups/03-ficha-camper.html) | ADR-003 | SEG-003 | TASK-031 | R-003 [AN], R-PL-004 | §3.1, §4.2 |
| RF-004 | HU-004 | CA-017, CA-034, CA-012 | P05 · [04](mockups/04-resumen-y-datos-conductor.html) | Módulo Tarifas | — | TASK-030, TASK-036 | R-001 [PM], R-002 [PM] | §3.1, §4 |
| RF-006 | HU-005 | CA-018, CA-010 | P06 · [04](mockups/04-resumen-y-datos-conductor.html) | Políticas, `consent` | SEG-010 (vía RN-026, VAL-011) | TASK-032, TASK-036 | R-009 [AN] | §3.1, §4 |
| RF-007 | HU-006 | CA-003, CA-002 | P07 · [05](mockups/05-pago.html) | ADR-003 | SEG-003, SEG-004 | TASK-032, TASK-035 | R-ARQ-02, R-PL-003 | §3.1, §4.1 |
| RF-008 | HU-007 | CA-031, CA-006 | P07 · [05](mockups/05-pago.html) | ADR-004, ADR-005, ADR-006 | SEG-002 | TASK-033, TASK-037 | R-004 [AN], R-ARQ-01, R-010 [PM] | §3.1, §4.2 |
| RF-009 | HU-007 | CA-031, CA-006 | P07 · [05](mockups/05-pago.html) | ADR-004 a ADR-006 | SEG-002 | TASK-033 | R-002 [PM] | §3.1, §4.2 |
| RF-010 | HU-010 | CA-019 | P08 · [06](mockups/06-confirmacion.html) | ADR-009 | SEG-015 | TASK-040 | R-012 [AN], R-ARQ-09 | §3.1, §4 |
| RF-011 | HU-011 | CA-020, CA-013 | P09 · [07](mockups/07-consulta-reserva.html) | ADR-011 | SEG-001 | TASK-041, TASK-045 | R-004 [PM], R-ARQ-07 | §3.1, §4 |
| RF-012 | HU-011 | CA-020, CA-013 | P09 · [07](mockups/07-consulta-reserva.html) | ADR-011 | SEG-001 | TASK-041 | R-004 [PM], R-ARQ-07 | §3.1, §10 (pregunta 17) |
| RF-013 | HU-012 | CA-008 | P10 · [07](mockups/07-consulta-reserva.html) | ADR-008 | SEG-001, SEG-005 | TASK-041, TASK-045 | R-006 [PM], R-ARQ-04, R-PL-005 | §3.1, §10 (preguntas 3, 5, 12, 23) |
| RF-015 (contacto) | HU-013 | CA-029 | P11 | Contacto | SEG-016 | TASK-045, TASK-046 | — | §3.1 |
| RF-016 | HU-014 | CA-027 | P12 | Legales | — | TASK-045 | R-001 [AN], R-002 [PM] | §3.1 |
| RF-017 | HU-014 | CA-026 | P13 | Cookies | SEG-016 | TASK-045, TASK-046 | R-001 [AN] | §3.1 |
| RF-018 | HU-015 | CA-028 | P01 · [01](mockups/01-inicio.html) | ADR-010 | — | TASK-045 | R-006 [AN], R-007 [PM] | §3.1, §4.2 |
| RF-019 | HU-017 | CA-021 | P14 · [08](mockups/08-admin-panel-reservas.html) | Módulo Admin (autenticación) | SEG-006, SEG-017 | TASK-042, TASK-044 | — | §3.1, §10 (preguntas 6, 10) |
| RF-020 | HU-018 | CA-011 | P16 · [09](mockups/09-admin-flota-tarifas.html) | Módulo Admin, almacén de imágenes | SEG-009 | TASK-043, TASK-044 | R-009 [PM] | §3.1, §4 |
| RF-021 | HU-019 | CA-011, CA-033 | P17 · [09](mockups/09-admin-flota-tarifas.html) | Módulo Admin | — | TASK-043, TASK-044 | R-009 [PM] | §3.1, §4 |
| RF-022 | HU-020 | CA-011, CA-034, CA-012 | P18 · [09](mockups/09-admin-flota-tarifas.html) | Módulo Tarifas | SEG-005 (vía VAL-020) | TASK-030, TASK-043, TASK-044 | R-001 [PM] | §3.1, §10 (pregunta 13) |
| RF-023 | HU-021 | CA-022, CA-032 | P15 · [08](mockups/08-admin-panel-reservas.html) | Módulo Admin (sin fila propia en la matriz del Arquitecto, ISS-020) | SEG-007† | TASK-043, TASK-044 | R-003 [PM] | §3.1, §4 |
| RF-024 | HU-022 | CA-023, CA-002 | P19 | ADR-003 | SEG-003 | TASK-043, TASK-044 | R-003 [PM] | §3.1 |
| RF-025 | HU-023 | CA-024 | P20 | ADR-008 | SEG-005 | TASK-041, TASK-043, TASK-044 | R-006 [PM] | §3.1 |
| RF-026 | HU-024 | CA-025 | P21 (campo de configuración) | ADR-009 | SEG-015 | TASK-040 | — | §3.1, §10 (pregunta 29) |
| RF-032 | HU-009 | CA-005, CA-007 | P08 · [06](mockups/06-confirmacion.html) | ADR-003, ADR-007 | SEG-003 | TASK-034 | R-010 [PM], R-ARQ-03, R-PL-004 | §3.1, §4.1 |

### 10.2 Requisitos no funcionales

| Requisito | Criterio | Arquitectura | Seguridad | Tareas del plan | Cobertura en la propuesta |
|---|---|---|---|---|---|
| RNF-001 | CA-014 | ADR-010 | — | TASK-045, TASK-052 | §1, §3.1, §4.2 |
| RNF-002 | CA-028 | ADR-010 | — | TASK-045, TASK-052 | §3.1, §4.2 |
| RNF-003 | CA-030 | Frontend responsive | — | TASK-024†, TASK-052 | §3.1 |
| RNF-004 | CA-030 | — | — | TASK-052 | §3.1 |
| RNF-005 | CA-030 | Frontend accesible | — | TASK-024 (axe), TASK-052 | §3.1 |
| RNF-006 | CA-031, CA-021 | ADR-004 a ADR-006 | SEG-002, SEG-006 | TASK-033 | §1, §4.2 |
| RNF-007 | CA-003 | ADR-003 | SEG-003 | TASK-032†, TASK-051 | §1, §4.2 |
| RNF-008 | CA-010, CA-018 | Políticas, `consent` | SEG-010, SEG-011 | TASK-053 (SEG-010) | §4.2, §10 |
| RNF-009 | CA-024, CA-004, CA-032 | ADR-006 | SEG-007 | TASK-033†, TASK-043† | §4.2 |
| RNF-010 | CA-011 | Módulo Admin | — | TASK-043†, TASK-044† | §3.1 |
| RNF-011 | — | Recomendación de copias | SEG-013 | TASK-060, TASK-061 | §10 (pregunta 8) |
| RNF-012 | — | Sin cifras (PEND-015) | — | Sin tarea | §10 (pregunta 31) |
| RNF-013 | CA-011 | Almacén de imágenes | SEG-009 | TASK-043† | §3.1 |
| RNF-014 | CA-019 | ADR-009 | SEG-015 | TASK-040 | §3.1, §4.2 |

† Asignación inferida por el Gestor de Documentación en TRACEABILITY §9 a partir de la descripción de cada tarea o de la matriz de UX; el plan solo cita CA y SEG.

### 10.3 Segunda fase y ampliaciones

Sin criterios de aceptación, tareas ni mockups (fuera del MVP; los CA de Fase 2 se redactarían al planificarla).

| Requisito | Historia | Destino | Observación |
|---|---|---|---|
| RF-005 | HU-025 | Segunda fase (AN: MVP, ISS-006) | Extras; DEC-018; pregunta 22 |
| RF-014 | HU-027 | Segunda fase | DEC-020 |
| RF-015 (FAQ) | HU-026 | Segunda fase | DEC-019 |
| RF-012 (cuentas) | HU-032 | Segunda fase | DEC-006 |
| RF-026 ampliado | HU-035 | Segunda fase | DEC-022 |
| RF-027 | HU-029 | Segunda fase | DEC-021 |
| RF-028 | HU-028 | Segunda fase | DEC-015; mientras tanto RF-024 |
| RF-029 | HU-033 | Segunda fase | DEC-016; auditoría mínima recomendada para el MVP (SEG-007, PEND-038) |
| RF-030 | HU-034 | Segunda fase | DEC-017 |
| RF-031 (depósito + saldo, factura automática) | HU-030, HU-031 | Segunda fase (PM) o ampliación (AN) | ISS-004; DEC-002, DEC-007 |
| RF-031 (resto) | — | Ampliación | Fianza en línea, otros medios de pago, multi-idioma, cupones, reseñas, documentos del conductor, contrato digital, sincronización de canales |
| — | HU-036 | Segunda fase | Devolución en otra sede con suplemento; DEC-013 |

### 10.4 Elementos huérfanos y huecos señalados

- CA-033 no traza a un RF o RN (decisión del Director, DEC-012). HU-030, HU-031 y HU-036 con origen «decisión del Director» sin RF de origen.
- CA-001 a CA-014: mismo ID con contenido distinto (ISS-001, ISS-023).
- RF-023, RN-017, RN-020 y RN-024 no aparecen en la matriz del Arquitecto (ISS-020).
- SEG-004 a SEG-007, SEG-009 a SEG-013 y SEG-016 no se vinculan a un ADR concreto; SEG-014 no tiene RF, RN, ADR ni DEC asociados.
- Ningún requisito tiene tarea autorizada, pruebas, implementación ni defectos (esperado en esta fase); TASK-062, TASK-065 y TASK-071 no tienen RF, CA ni SEG propios.
- Todo requisito del MVP propuesto tiene fila en 10.1; RNF-012 no tiene tarea del plan.

## 11. Resumen por estado

> Los conteos de esta sección se refieren al **catálogo del MVP completo (fase siguiente)**. La cobertura de la entrega inicial (opción B) se presenta aparte en la sección «Opción B», apartado B.3; no cambia el estado de ningún requisito. Solicitudes de cambio: **CR-001** (opción B) está registrada en el control (WAITING_FOR_APPROVAL).

Los conteos se obtienen contando filas de las tablas de las secciones 2.1, 2.2 y 2.3 (estado principal de cada requisito, ver leyenda); no se estiman porcentajes de avance.

| Estado | Cantidad | Detalle |
|---|---|---|
| Confirmado | 15 | RF-001, RF-002, RF-003, RF-008, RF-011, RF-018, RF-020, RF-021, RF-022, RNF-001, RNF-002, RNF-004, RNF-006, RNF-010, RN-001 |
| Supuesto | 4 | RF-012, RF-019, RN-002, RN-005 |
| Recomendación | 47 | RF-004, RF-005, RF-006, RF-007, RF-009, RF-010, RF-013 a RF-017, RF-023 a RF-030, RF-032 (20 RF); RNF-003, RNF-005, RNF-007, RNF-008, RNF-009, RNF-013, RNF-014 (7); RN-003, RN-004, RN-007 a RN-019, RN-021, RN-022, RN-023, RN-025, RN-026 (20) |
| Pendiente | 7 | RF-031, RNF-011, RNF-012, RN-006, RN-020, RN-024, RN-027 |
| **Total** | **73** | RF-001 a RF-032 (32), RNF-001 a RNF-014 (14) y RN-001 a RN-027 (27) |

**Otros registros** (cantidades según [TRACEABILITY.md](../00-control/TRACEABILITY.md) §4, a 2026-10-26; ninguno aprobado): historias de usuario 36 (HU-001 a HU-036: 24 MVP, 12 Fase 2); criterios de aceptación del PM 34 y del Analista 14 (mismos IDs, ISS-001); decisiones propuestas 32 (DEC-001 a DEC-032); decisiones de arquitectura propuestas 12 (ADR-001 a ADR-012); pendientes de confirmación 40 (PEND-001 a PEND-040); decisiones bloqueantes según el plan 9 (B1 a B9); impedimentos abiertos 33 (ISS-001 a ISS-033); hallazgos de seguridad abiertos 17 (SEG-001 a SEG-017, revisión de diseño sin pruebas); tareas del plan en BACKLOG 38; riesgos del plan 11; pantallas diseñadas 21 (P01 a P21; P21 no es pantalla); riesgos de experiencia y técnicos 22; requisitos aprobados 0; solicitudes de cambio registradas 0.

Enlaces: [propuesta comercial](propuesta-comercial.md) · [mockups](mockups/index.html) · [perfil de empresa](perfil-empresa.md) · [checklist de calidad](checklist-calidad-propuesta.md) · [estado del proyecto](../00-control/PROJECT-STATE.md).
