# Propuesta comercial — Web de alquiler de campers (España)

| Campo | Valor |
|---|---|
| Cliente | {{PENDIENTE: nombre del cliente}} |
| Proyecto | Web de alquiler de campers (España) (`alquiler-campers`) |
| Oferta principal | **Opción B: entrega inicial acotada** (sitio público con solicitud de reserva), objetivo de **1 semana** para entrega a revisión, **400 USD**. Solicitud de cambio **CR-001** (WAITING_FOR_APPROVAL) |
| Fase siguiente | MVP completo (pago seguro, disponibilidad en tiempo real, panel y seguridad): estimación preliminar de **28 a 36 semanas**, **sin precio**, a cotizar aparte (sección 11) |
| Estado del documento | BORRADOR |
| Versión | 0.2 (reestructurada alrededor de la opción B; la 0.1 proponía solo el MVP completo) |
| Fecha | 2026-10-26 (fecha de elaboración del documento; no es una fecha de inicio ni de entrega) |
| Vigencia de la propuesta | {{PENDIENTE: vigencia}} |
| Preparada por | Director de Proyectos (portavoz único) · {{PENDIENTE: nombre y cargo del responsable de la propuesta}} |
| Análisis completo | [analisis-consolidado.md](analisis-consolidado.md) (sección «Opción B: entrega inicial acotada») |
| Mockups | [mockups/index.html](mockups/index.html) |

> **Estado:** este documento es un borrador comercial para revisión. **No equivale a aprobar el alcance** ni la solicitud de cambio CR-001, ni autoriza el inicio del desarrollo ni el paso a construcción. Los elementos marcados `{{PENDIENTE: ...}}` aún no cuentan con información confirmada.

**Leyenda:** **Confirmado** = indicado o aprobado por el cliente o por el usuario que encargó la propuesta · **Supuesto** = interpretación a validar · **Recomendación** = propuesta de nuestro equipo · **Pendiente** = decisión o dato faltante.

## Qué está confirmado y qué no (vista rápida)

| Estado | Contenido en esta propuesta |
|---|---|
| **Confirmado** (instrucción explícita del usuario) | Se ofrece la **opción B**: una entrega inicial acotada. Plazo objetivo de **1 semana**. Valor de la entrega inicial: **400 USD** (precio fijado por el usuario). Existe margen de negociación (disposición a ajustar condiciones y alcance en una conversación; no hay cifras de descuento). El MVP completo pasa a ser la **fase siguiente**, a cotizar aparte |
| **Confirmado** (brief del cliente) | Una web de alquiler de campers en España, con atención a la experiencia de uso, la velocidad y el posicionamiento en buscadores (SEO técnico, sin garantía de posicionamiento). Sin migración de datos ni integración con sistemas existentes. El cliente confirmó que flota y sedes sean configurables desde un panel (esa parte pasa a la fase siguiente, ver sección 3.4) |
| **Supuesto** | Español y zona horaria de Madrid; cliente particular; una sola empresa; una reserva = un camper; «contenido editable» significa, en la entrega inicial, que lo edita el proveedor mediante archivos de datos; una persona de desarrollo dedicada a tiempo completo durante la semana |
| **Recomendación** | El núcleo recortado de la entrega inicial; los hitos D1 a D7; la publicación en D7–D10 según DNS y aprobación; la pila tecnológica compatible con la fase siguiente; el esquema de comunicación; la marca provisional «Ruta Camper»; el alcance y la arquitectura del MVP completo para la fase siguiente |
| **Pendiente** | **Aceptación de esta oferta por el cliente** y aprobación de CR-001; moneda de facturación e IVA; forma de pago; contenido y accesos del D1; fecha de inicio; nombre del cliente; vigencia; datos de la empresa; marca definitiva; fotos y textos reales; validación legal; cotización de la fase siguiente |

## Resumen ejecutivo

| Tema | Resumen | Estado |
|---|---|---|
| Qué entendimos | Necesitan cuanto antes una presencia propia en internet para mostrar su flota de campers, explicar tarifas y condiciones y recibir solicitudes de reserva, con buena velocidad, buen SEO técnico y buen aspecto en móvil. La web completa de reservas con pago seguro y panel de administración sigue siendo el objetivo a medio plazo | Supuesto (sobre la base de lo confirmado en la fila «Confirmado» anterior) |
| Qué proponemos (oferta principal) | Una **entrega inicial acotada**: sitio público adaptable a móvil con inicio, catálogo y fichas de campers, tarifas orientativas, condiciones, contacto, páginas legales y de cookies (borrador a validar por su asesoría), SEO técnico base y un **formulario de solicitud de reserva** que avisa por correo a su empresa para que confirmen manualmente. Incluye una guía breve de edición de contenido y **una ronda de ajustes** | Recomendación (pendiente de su aceptación y de CR-001) |
| Qué no incluye la entrega inicial | Pago en línea, disponibilidad automática en tiempo real, panel de administración, cuentas y acceso del cliente a sus reservas, reembolsos, segundo factor de autenticación y auditoría. Pasan a la fase siguiente. Tampoco incluye hosting, dominio, correo de terceros, asesoría legal, mantenimiento posterior ni garantía de posicionamiento (sección 3.3) | Recomendación |
| Plazo | **1 semana (5 días hábiles) para la entrega a revisión** en una dirección de pruebas; **publicación en D7–D10 según DNS y aprobación**. Plazo con riesgo alto y sin holgura; depende de que el cliente aporte contenido y accesos el primer día. Sin fechas de calendario hasta confirmar el inicio | Confirmado (objetivo de 1 semana, por el usuario) · Recomendación a confirmar (calificación como entrega a revisión y condiciones) |
| Inversión | **400 USD** por esta entrega inicial. Moneda de facturación, IVA y forma de pago pendientes. Costes de terceros (hosting, dominio, correo, asesoría legal) no incluidos. Existe margen de negociación (sección 8) | Confirmado (400 USD, por el usuario) · Pendiente (moneda, IVA, forma de pago) |
| Fase siguiente | MVP completo: **28 a 36 semanas** desde la autorización de su construcción (estimación preliminar), **sin precio**, a cotizar aparte tras confirmar las decisiones previas (sección 11) | Recomendación a confirmar |
| Decisiones que necesitamos de ustedes | Sección 10 (primero las de la entrega inicial; después las de la fase siguiente) | Pendiente |

## 1. Quiénes somos y por qué somos la opción ideal

Fuente: [perfil-empresa.md](perfil-empresa.md). Solo se afirma lo que allí tiene respaldo. Al no haberse recibido un perfil de empresa, la presentación, la experiencia y las credenciales quedan pendientes y se muestran visibles; lo que sí podemos sostener es **cómo trabajamos** y **qué aporta esa forma de trabajo a este proyecto**.

| Tema | Contenido | Estado |
|---|---|---|
| Presentación de la empresa | {{PENDIENTE: presentación de la empresa (nombre comercial, qué hace, sitio web)}} | Pendiente |
| Experiencia relevante | {{PENDIENTE: experiencia autorizada para citar (proyectos o sector y resultado verificable)}} | Pendiente |
| Credenciales o certificaciones | {{PENDIENTE: credenciales o «no aplica»}} | Pendiente |
| Otros argumentos de diferenciación | {{PENDIENTE: argumentos de la empresa con su evidencia}} | Pendiente |
| Forma de trabajo | Trabajamos **por fases con puertas de aprobación**: no se construye nada sin su aprobación del alcance y su autorización expresa. **Controlamos el alcance** (entrega inicial, fase siguiente, ampliaciones y exclusiones separados; todo cambio se registra y se decide con ustedes). Mantenemos **trazabilidad**: cada requisito se relaciona con su historia, su criterio de aceptación, su decisión técnica, sus pruebas y sus hallazgos. Aplicamos **calidad antes de la entrega** (lista de pruebas contra lo prometido) y entregamos una **guía de edición de contenido**. Tienen **un único portavoz**: el Director de Proyectos | Recomendación (práctica de trabajo) |

### Cómo esa forma de trabajo beneficia a este proyecto

| Necesidad de su proyecto | Qué haremos | Estado |
|---|---|---|
| Salir pronto con una web presentable | Un núcleo recortado y priorizado, con un plan día a día y entrega a revisión en una dirección de pruebas. Decimos claramente qué entra y qué no para no prometer más de lo que cabe en la semana | Recomendación |
| Velocidad y SEO técnico | Páginas ligeras, imágenes optimizadas, direcciones limpias, metadatos, mapa del sitio y datos estructurados básicos. El rendimiento es un objetivo; **no garantizamos posicionamiento ni resultados reales de rendimiento** | Recomendación |
| Cumplimiento de la normativa de privacidad y de consumo | Páginas legales y de cookies a partir de plantilla, marcadas como **borrador a validar** por la asesoría legal de ustedes: **esto no es asesoramiento jurídico** | Recomendación |
| No perder solicitudes | Cada solicitud llega por correo a su empresa, con una copia a un segundo buzón, y registra la fecha y la versión de la privacidad aceptada | Recomendación |
| Crecer después sin rehacerlo todo | Elegiremos una base tecnológica compatible con la arquitectura de la fase siguiente (a verificar). Aun así puede haber partes públicas que se ajusten al migrar (riesgo R-007 [OPB]) | Recomendación |
| Pagos seguros y cero dobles reservas | **No forman parte de la entrega inicial**: son objetivos de diseño de la fase siguiente, que solo podremos afirmar cuando existan y se prueben | Recomendación |

## 2. Cómo entendemos su proyecto

| Tema | Contenido | Estado | Fuente |
|---|---|---|---|
| Problema u oportunidad | Un negocio de alquiler de campers en España que necesita un canal propio en línea para darse a conocer y recibir solicitudes, y a medio plazo reservar y cobrar sin intermediación manual | Supuesto | [client-brief.md](../00-intake/client-brief.md) |
| Usuarios principales | El cliente particular que consulta la flota y solicita su reserva desde móvil u ordenador, y el equipo de la empresa que recibe y confirma las solicitudes. Perfil, nacionalidad y volumen de usuarios no están informados | Supuesto | [requirements.md](../01-discovery/requirements.md) |
| Resultado esperado de la entrega inicial | Un sitio público rápido y claro, con base de SEO técnico (sin garantía de posicionamiento), con el que su empresa reciba solicitudes de reserva por correo y confirme manualmente | Confirmado (opción B, plazo y valor, por el usuario) · Recomendación (detalle del contenido) | Instrucción del usuario; [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) |
| Resultado esperado a medio plazo (fase siguiente) | Reservar y pagar en línea con disponibilidad fiable y panel de administración | Confirmado (necesidad, en el brief) · Recomendación (detalle) | [client-brief.md](../00-intake/client-brief.md) |
| Ejemplo de funcionamiento (entrega inicial) | Una persona entra desde el móvil, mira los campers, consulta tarifas y condiciones, rellena el formulario de solicitud (fechas, camper, datos del conductor, aceptación de privacidad) y la empresa recibe un correo; la empresa responde y confirma manualmente | Recomendación | [requirements.md](../01-discovery/requirements.md) |

**Lo que el cliente nos indicó (respuestas literales del brief):** «esta en españa»; «que sea configurable»; «pon tu las reglas»; «lo que creas conveniente»; «crealo»; «no y ponlo que no abra migracion»; «no entra en el contrato». Entendimos que delega en nuestro equipo las reglas de negocio y de producto. Por eso **todo lo que aquí se propone como regla o decisión es Recomendación hasta que lo confirmen**: la delegación no equivale a una aprobación.

> **Tensión que señalamos:** en el brief se indicó que presupuesto y fechas no entran en el contrato; ahora se nos pide una oferta con un valor (400 USD) y un plazo objetivo (1 semana), ambos confirmados por el usuario que encargó esta propuesta. No elegimos en silencio: les pedimos que confirmen cómo desean tratar el valor y el plazo (sección 10, pregunta OB-12).

## 3. Alcance

El alcance de la **entrega inicial** se basa en los requisitos y el MVP del expediente, recortados según la estimación de nuestro Planificador. **Ninguna parte está aprobada todavía**: su aprobación requiere la decisión sobre la solicitud de cambio **CR-001**. Una idea nueva no es alcance aprobado: se registra como solicitud de cambio.

### 3.1 Incluido en la entrega inicial (propuesta)

Todo es **Recomendación** pendiente de su aceptación; la elección de la opción B, el plazo y el valor son **Confirmado** por el usuario.

| # | Entregable | Requisitos relacionados (cobertura) | Estado |
|---|---|---|---|
| 1 | Sitio público **adaptable a móvil y rápido**: inicio, catálogo y fichas de campers (**máximo 3 o 4 campers de ejemplo**; contenido y fotos de ejemplo sustituibles) | RF-001 (parcial: catálogo sin gestión en panel), RNF-003, RNF-001 (como objetivo, sin garantía) | Recomendación |
| 2 | **Tarifas orientativas y condiciones** en una sola página | RF-001 (precio orientativo), RF-016 (condiciones, borrador) | Recomendación |
| 3 | **Contacto** | RF-015 (parcial; las preguntas frecuentes ya estaban en la segunda fase) | Recomendación |
| 4 | **Páginas legales y de cookies** como **borrador a validar** con la asesoría legal del cliente; aviso de cookies **informativo, sin analítica** | RF-016 (parcial), RF-017 (parcial: sin categorías de consentimiento) | Recomendación |
| 5 | **SEO técnico base**: metadatos, mapa del sitio, robots, datos estructurados básicos (organización y vehículo) y direcciones limpias | RF-018 (parcial), RNF-002 | Recomendación |
| 6 | **Formulario de solicitud de reserva** (fechas, camper, datos del conductor, aceptación de la privacidad con fecha y versión indicadas en el correo) que **avisa por correo a la empresa** para su confirmación manual, con protección antispam y copia a un segundo buzón | RF-006 (parcial: solicitud, sin resumen ni pago), RF-010 (parcial: aviso por correo, sin justificante), RF-026 (parcial: aviso por solicitud), RN-026 (parcial) | Recomendación |
| 7 | **Guía breve de edición de contenido** (el contenido de la flota lo mantiene el proveedor mediante archivos de datos) | RF-001 / RNF-013 (parcial) | Recomendación |
| 8 | **Una ronda de ajustes** tras su feedback, y publicación en su dominio si el acceso al DNS y su aprobación llegan a tiempo | — | Recomendación |

**Condición para que el cliente edite el contenido por sí mismo:** si prefieren editar la flota sin pasar por el proveedor, hace falta un gestor de contenidos ligero (**+1 a 2 días** o fase siguiente). Es una decisión pendiente (pregunta OB-01).

### 3.2 Cobertura de requisitos de la entrega inicial

Resumen para el cliente (el detalle con identificadores está en el [análisis consolidado](analisis-consolidado.md), sección «Opción B»).

| Cobertura | Requisitos |
|---|---|
| **Cubre** | RNF-001 (como objetivo, sin garantía), RNF-002, RNF-003 |
| **Cubre parcialmente** | RF-001, RF-006, RF-010, RF-015, RF-016, RF-017, RF-018, RF-026, RN-026, RNF-004, RNF-005, RNF-006, RNF-008, RNF-013, RNF-014 (accesibilidad solo básica, sin auditoría de nivel AA) |
| **No cubre (fase siguiente)** | RF-002 a RF-005 (búsqueda, disponibilidad, precio y extras); RF-007 a RF-009 (bloqueo y pago); RF-011 a RF-013 (consulta, código y cancelación); RF-019 a RF-025 (panel); RF-032 (expiración de reservas); RN-003 y RN-010; RNF-007, RNF-009, RNF-010 y RNF-011 |

### 3.3 No incluido en la entrega inicial

| Exclusión | Motivo | Estado |
|---|---|---|
| Pago en línea, disponibilidad automática en tiempo real, panel de administración, cuentas y acceso del cliente a sus reservas, reembolsos, segundo factor de autenticación (MFA) y auditoría | Pasan a la fase siguiente | Recomendación |
| Hosting, dominio y correo de terceros, y sus costes | Los contrata y paga el cliente (o se acuerda otra cosa) | Recomendación |
| Asesoría legal y fiscal | La empresa propone y su asesoría valida | Recomendación |
| Mantenimiento posterior a la entrega | Fuera de esta entrega | Recomendación |
| Garantía de posicionamiento y de resultados reales de rendimiento (Core Web Vitals) | No se garantizan | Confirmado (SEO sin garantía, en el brief) |
| Otras rondas de cambios, extras, preguntas frecuentes y varios idiomas | Fuera de esta entrega; entrarían como solicitud de cambio | Recomendación |
| Migración de datos e integración con sistemas existentes | El cliente indicó que no hay sistemas previos ni datos que migrar | Confirmado |
| Producción de fotografía y vídeo reales | Las fotos las aporta el cliente; mientras tanto, imágenes de ejemplo sustituibles | Recomendación |
| Puesta en producción con tráfico real fuera de lo indicado en el plazo | Requiere autorización específica y adicional | Recomendación |

### 3.4 Desviación que el cliente debe aceptar

El cliente confirmó que **la flota y las sedes sean configurables desde un panel** (RN-001, RNF-010). En la entrega inicial **no hay panel**: la flota y las sedes se gestionan **mediante contenido editado por el proveedor**. El panel y la configurabilidad completa pasan a la fase siguiente. Esta desviación se registra en CR-001 y requiere su aceptación expresa (pregunta OB-03). No la damos por aceptada.

### 3.5 Después de la entrega inicial

El MVP completo (búsqueda con disponibilidad, precio total, pago seguro, confirmación, consulta y cancelación, panel, seguridad reforzada) es la **fase siguiente** (sección 11). Cualquier otra idea se trata como ampliación mediante solicitud de cambio.

## 4. Solución propuesta y mockups

Los mockups son ilustrativos, de media fidelidad. **No son diseño final aprobado.** La marca mostrada («Ruta Camper», colores y tipografía del sistema) es una **PROPUESTA, no aprobada**; nombre, logotipo, colores y estilo visual definitivos son decisiones pendientes del cliente. Todos los datos son de ejemplo. En la galería, cada pantalla lleva una insignia visible: **ENTREGA INICIAL** o **FASE SIGUIENTE**.

### 4.1 Pantallas de la entrega inicial

| Pantalla | Mockup | Requisitos e historias | Estado |
|---|---|---|---|
| Inicio con catálogo y llamada a «Solicitar reserva» | [mockups/01-inicio-entrega-inicial.html](mockups/01-inicio-entrega-inicial.html) | RF-001, RF-018 · HU-001, HU-015 | Recomendación |
| Ficha de camper con «Solicitar reserva» | [mockups/03-ficha-camper-entrega-inicial.html](mockups/03-ficha-camper-entrega-inicial.html) | RF-001 · HU-001 | Recomendación |
| Formulario de solicitud de reserva y confirmación de recepción | [mockups/11-solicitud-reserva.html](mockups/11-solicitud-reserva.html) | RF-006 (parcial), RF-010 (parcial), RF-026 (parcial), RN-026 · HU-005 | Recomendación |
| Tarifas orientativas y condiciones | [mockups/12-tarifas-y-condiciones.html](mockups/12-tarifas-y-condiciones.html) | RF-001, RF-016 · HU-001 | Recomendación |
| Catálogo de campers (3 o 4 campers) | [mockups/13-catalogo-entrega-inicial.html](mockups/13-catalogo-entrega-inicial.html) | RF-001 · HU-001 | Recomendación |
| Vista móvil: inicio y solicitud | [mockups/10-movil-entrega-inicial.html](mockups/10-movil-entrega-inicial.html) | RNF-003, RF-001, RF-006 (parcial) · HU-016 | Recomendación |

El catálogo de la entrega inicial (hasta 3 o 4 campers) tiene su propia pantalla y además se adelanta en el inicio. Contacto, páginas legales y cookies se describen en la [especificación de experiencia de usuario](../03-ux/ux-specification.md) y en el [análisis consolidado](analisis-consolidado.md), sección 4. Los estados alternativos (sin disponibilidad, errores del formulario, solicitud enviada, pago rechazado, panel vacío y carga) están en [mockups/14-estados.html](mockups/14-estados.html), y la dirección visual propuesta («cuaderno de ruta», **PROPUESTA, no aprobada**) en [mockups/direccion-visual.md](mockups/direccion-visual.md).

### 4.2 Pantallas de la fase siguiente

Ilustran el MVP completo; **no forman parte de la entrega inicial**.

| Pantalla | Mockup | Requisitos e historias | Estado |
|---|---|---|---|
| Inicio con buscador por fechas (versión completa) | [mockups/01-inicio.html](mockups/01-inicio.html) | RF-002, RF-018 · HU-001, HU-002, HU-015 | Recomendación |
| Resultados de búsqueda (disponibilidad y precio) | [mockups/02-resultados-busqueda.html](mockups/02-resultados-busqueda.html) | RF-002, RF-003, RF-004 · HU-002, HU-003, HU-004 | Recomendación |
| Ficha de camper con disponibilidad (versión completa) | [mockups/03-ficha-camper.html](mockups/03-ficha-camper.html) | RF-001, RF-003 · HU-001, HU-003 | Recomendación |
| Resumen de precio y datos del conductor | [mockups/04-resumen-y-datos-conductor.html](mockups/04-resumen-y-datos-conductor.html) | RF-004, RF-006 · HU-004, HU-005 | Recomendación |
| Pago seguro (alojado por la pasarela) | [mockups/05-pago.html](mockups/05-pago.html) | RF-007, RF-008, RF-009 · HU-006, HU-007 | Recomendación |
| Estado y confirmación de la reserva | [mockups/06-confirmacion.html](mockups/06-confirmacion.html) | RF-010, RF-032 · HU-008, HU-009, HU-010 | Recomendación |
| Consulta de reserva (código + correo) y cancelación | [mockups/07-consulta-reserva.html](mockups/07-consulta-reserva.html) | RF-011, RF-012, RF-013 · HU-011, HU-012 | Recomendación |
| Panel de administración: reservas | [mockups/08-admin-panel-reservas.html](mockups/08-admin-panel-reservas.html) | RF-019, RF-023 · HU-017, HU-021 | Recomendación |
| Panel de administración: flota, sedes y tarifas | [mockups/09-admin-flota-tarifas.html](mockups/09-admin-flota-tarifas.html) | RF-020, RF-021, RF-022 · HU-018, HU-019, HU-020 | Recomendación |
| Vista móvil: inicio y resultados con disponibilidad | [mockups/10-movil-inicio-y-resultados.html](mockups/10-movil-inicio-y-resultados.html) | RF-002, RF-003 · HU-002, HU-016 | Recomendación |

### 4.3 Cómo funcionaría la entrega inicial (recorrido principal)

Recomendación, derivada del recorrido R1 de [03-ux/ux-specification.md](../03-ux/ux-specification.md) simplificado para la solicitud de reserva.

1. La persona entra en el **inicio** y ve los campers de ejemplo, con precio orientativo.
2. Abre la **ficha** del camper que le interesa y consulta **tarifas y condiciones**.
3. Pulsa **«Solicitar reserva»** e indica fechas, camper, datos del conductor y acepta la política de privacidad (casilla sin marcar de origen).
4. Ve una **confirmación de recepción** que le explica que la empresa responderá; **no se confirma ninguna disponibilidad ni se cobra nada** en la web.
5. La empresa recibe un **correo** con la solicitud (incluidas la fecha y la versión de la privacidad aceptada) y una copia en un segundo buzón, y **confirma manualmente** por sus propios medios.

### 4.4 Enfoque técnico (resumen para el cliente)

Todo lo técnico es **Recomendación**; **ninguna tecnología es obligatoria** hasta que ustedes decidan. La coherencia con la arquitectura de la fase siguiente ([solution-architecture.md](../04-architecture/solution-architecture.md)) está **por verificar** (PEND-047).

| Tema | Resumen | Estado |
|---|---|---|
| Alojamiento | Sitio estático con una función sencilla para el formulario (sin base de datos propia). Los alojamientos y servicios los contrata el cliente | Recomendación |
| Contenido | Los campers, tarifas y textos viven en archivos de datos que edita el proveedor. Una base de contenidos editable por el cliente es una decisión pendiente (OB-01) | Recomendación · Pendiente |
| Correo del formulario | Servicio de correo o función sin almacenamiento propio; protección antispam; copia a un segundo buzón para no perder solicitudes. Se configuran los registros SPF, DKIM y DMARC del dominio (los que evitan que los correos se marquen como spam) cuando el cliente da acceso al DNS | Recomendación |
| Velocidad y SEO | Páginas ligeras, imágenes optimizadas, direcciones limpias, mapa del sitio, robots, datos estructurados básicos. Sin garantía de posicionamiento ni de resultados reales | Recomendación |
| Seguridad | Dirección segura (HTTPS), mínimo de datos personales y sin guardar datos de tarjeta (no hay pago). La revisión de seguridad del expediente es **de diseño** del MVP completo y no se ejecutó ninguna prueba; para la entrega inicial no existe una revisión de seguridad propia. No declaramos seguro un sistema por ausencia de hallazgos | Recomendación |
| Operación | Despliegue a una dirección de pruebas; publicación solo con su aprobación y con acceso al DNS. Ningún despliegue sin autorización específica | Recomendación |

## 5. Plan de trabajo

### 5.1 Hitos y entregables (días relativos al arranque)

Fuente: estimación del Planificador (núcleo B, variante recomendada), transcrita en [analisis-consolidado.md](analisis-consolidado.md). D1 a D5 son días hábiles; D6 y D7 sirven de colchón y para la publicación. Son una **Recomendación a confirmar**, no un compromiso.

| Día | Hito | Entregable | Dependencia del cliente | Estado |
|---|---|---|---|---|
| D1 | Arranque | Contenido y accesos recibidos; repositorio y base lista | Contenido, datos legales, correo de destino y marca (sección 5.3) | Recomendación |
| D2 | Esqueleto | Sitio en la dirección de revisión, con inicio y una ficha | Accesos de hosting y DNS (o permiso de dirección provisional) | Recomendación |
| D3 | Catálogo | Catálogo, fichas y contacto completos | — | Recomendación |
| D4 | Formulario | Formulario de solicitud de extremo a extremo, páginas legales en borrador y SEO base | Correo de destino confirmado | Recomendación |
| D5 | **Entrega a revisión** | Pruebas de calidad (móvil, formulario, enlaces, rendimiento) y entrega del sitio en la dirección de revisión | — | Recomendación |
| D6 | Ajustes | **Una ronda** de cambios según su feedback | Feedback en un día hábil como máximo (D5→D6) | Recomendación |
| D7 | Publicación | Sitio en su dominio y guía de edición de contenido, **solo si el DNS y su aprobación llegaron**; si no, D8 o después (hasta D10) | Aprobación final (D6–D7) y acceso al DNS | Recomendación |

### 5.2 Equipo y recursos

Sin nombres ni costes. La dedicación es el **supuesto de la estimación** (no un compromiso contractual) y debe confirmarse con la empresa ({{PENDIENTE: confirmar la disponibilidad real del equipo}}).

| Rol | Responsabilidad | Dedicación supuesta | Estado |
|---|---|---|---|
| Director de Proyectos | Coordina y es el único portavoz ante el cliente | Puntual | Supuesto |
| Desarrollo de la solución completa («full-stack») | Páginas, formulario, SEO base, legales en borrador, despliegue, pruebas y ajustes | **1 persona dedicada al 100 % durante la semana** (alternativa: 1 persona con apoyo parcial de contenido y calidad) | Supuesto |
| Calidad, diseño y redacción técnica dedicados | No hay perfiles dedicados; los mockups sirven de base visual | Sin dedicación | Supuesto |

Recursos del cliente: contenido, accesos, correo de destino y asesoría legal (sección 5.3). Disponibilidad real: {{PENDIENTE: confirmar disponibilidad del equipo para la semana de arranque}}.

### 5.3 Responsabilidades del cliente

Todas son **condiciones del plazo**. Si fallan, la entrega se mueve **día a día (1:1)** porque la semana no tiene holgura.

| Día | Qué necesitamos del cliente | Si falla |
|---|---|---|
| D1 | Datos de los campers (plazas, equipamiento, tarifas orientativas) y fotos reales, **o** aceptar las de ejemplo | Cada día de retraso mueve la entrega 1:1 |
| D1 | Datos legales (razón social, NIF, domicilio), datos de contacto, correo de destino de las solicitudes y nombre de marca (PEND-025) | Páginas legales incompletas |
| D1–D2 | Acceso a DNS y hosting, **o** permiso para usar una dirección provisional | Publicación en su dominio en riesgo |
| D2 | Textos de condiciones, **o** aceptar un borrador genérico | Se publica un texto genérico |
| D5→D6 | **Feedback en un día hábil como máximo** | Se pierde la ronda de ajustes |
| D6–D7 | Aprobación final | La publicación pasa a D8 o después |
| Antes de publicar | Validación de los textos legales por su asesoría | Se publican como borrador |

### 5.4 Dependencias

| Dependencia | Responsable | Estado |
|---|---|---|
| Hosting estático con función para el formulario y dominio con acceso al DNS | Cliente (y proveedor del servicio) | Pendiente |
| Registros SPF, DKIM y DMARC del dominio de correo | Cliente (acceso) y proveedor (configuración) | Pendiente |
| Validación legal de los borradores | Cliente y su asesoría | Pendiente |
| Contenido, fotos y marca | Cliente | Pendiente (PEND-020, PEND-025) |
| Aprobación de CR-001 y aceptación de esta oferta | Cliente | Pendiente |

## 6. Plazo estimado

> Estimación preliminar sustentada, entregada por el Planificador de Proyecto (evaluación de la opción B). El objetivo de **1 semana** lo confirmó el usuario; su **calificación como entrega a revisión y sus condiciones** son una **Recomendación a confirmar**, no un compromiso. **No incluye fechas de calendario.**

| Concepto | Valor |
|---|---|
| Plazo | **1 semana (5 días hábiles) para la entrega a revisión; publicación en D7–D10 según DNS y aprobación** |
| Nivel de riesgo | **Alto**: el núcleo de la entrega inicial cabe en la semana sin holgura. Cualquier retraso en el contenido, los accesos o el feedback **mueve la entrega 1:1** |
| Holgura incluida | Ninguna. D6 y D7 son colchón no contado |
| Qué cabe en la semana | El **núcleo recortado** (sección 3.1): máximo 3 o 4 campers, tarifas y condiciones en una sola página, legales desde plantilla, aviso de cookies informativo, formulario por correo sin base de datos propia, datos estructurados básicos y **una sola ronda** de cambios |
| Fecha de inicio | PENDIENTE: fecha de inicio (solo se completa si el cliente la confirma) |
| Fecha de entrega | **Se confirmará al fijar la fecha de inicio (PENDIENTE)** |
| Alternativas si prefieren más margen | Ampliar el plazo a la entrega completa de la opción B en un plazo mayor, o reforzar el equipo. Quedan como opciones a decidir con ustedes; no se calculan aquí |

### 6.1 Condiciones necesarias (todas)

| # | Condición | Estado |
|---|---|---|
| 1 | Dedicación de **1 persona al 100 %** durante la semana (o 1 persona más apoyo parcial de contenido y calidad) | Supuesto |
| 2 | El cliente entrega **todo el contenido el D1** | Pendiente |
| 3 | Acceso a dominio/DNS y hosting el D1–D2 (o permiso para una dirección provisional) | Pendiente |
| 4 | **Feedback del cliente en un día hábil como máximo** | Pendiente |
| 5 | Hosting estático con función para el formulario | Recomendación |

### 6.2 De día relativo a fecha: fórmula (sin fechas)

**Fecha del día Dn = fecha de inicio confirmada (D1) + (n − 1) días hábiles, más las esperas del cliente y de terceros (contenido, DNS, feedback, aprobación).** Mientras no exista una fecha de inicio confirmada, ninguna fecha se calcula.

| Día relativo | Hito | Fórmula | Fecha |
|---|---|---|---|
| D1 | Arranque con contenido y accesos | Fecha de inicio confirmada | PENDIENTE |
| D2 | Esqueleto en la dirección de revisión | D1 + 1 día hábil | PENDIENTE |
| D3 | Catálogo, fichas y contacto | D1 + 2 días hábiles | PENDIENTE |
| D4 | Formulario, legales en borrador y SEO | D1 + 3 días hábiles | PENDIENTE |
| D5 | Entrega a revisión | D1 + 4 días hábiles | PENDIENTE |
| D6 | Ronda de ajustes | D1 + 5 días hábiles (con feedback en un día hábil) | PENDIENTE |
| D7 a D10 | Publicación, si llegaron el DNS y la aprobación | D1 + 6 a 9 días hábiles | PENDIENTE |

**Datos que necesitamos para convertir días en fecha:** fecha de inicio confirmada por el cliente, fecha objetivo y estacionalidad del negocio (la web debería publicarse antes de la temporada alta), entrega de contenido y accesos, y calendario de feedback.

### 6.3 Supuestos de la estimación

| Supuesto | Estado |
|---|---|
| Una persona de desarrollo completo dedicada al 100 %, sin perfiles dedicados de calidad ni diseño | Supuesto |
| «Contenido editable» significa que lo edita el proveedor mediante archivos de datos; si el cliente debe editar solo hace falta un gestor de contenidos ligero (+1 a 2 días o fase siguiente) | Supuesto |
| Los mockups sirven de base visual y la marca provisional se mantiene | Supuesto |
| La pila tecnológica es coherente con la arquitectura de la fase siguiente (por verificar) | Supuesto |

### 6.4 Condiciones que podrían mover el plazo

| Condición | Efecto |
|---|---|
| Contenido o fotos tardíos o de baja calidad | Cada día de retraso mueve la entrega 1:1 |
| Acceso al DNS tardío | La publicación en su dominio pasa de D7 a D8–D10 o más |
| Feedback fuera del día hábil | Se pierde la ronda de ajustes de D6 o se desplaza la entrega |
| Aprobación final tardía | La publicación pasa a D8 o después |
| Cambios de alcance no registrados como solicitud de cambio | No incluidos; se analizan y se suman si se aprueban |
| Tiempos de terceros (hosting, dominio, correo, asesoría legal) | No incluidos; se suman |

**No incluye:** tiempos de terceros; esperas de decisión o de feedback del cliente (se suman uno a uno); la fase siguiente (su plazo está en la sección 11); ampliaciones; cambios no registrados como solicitud de cambio.

## 7. Disponibilidad y comunicación

Fuente: [perfil-empresa.md](perfil-empresa.md), sección 6. Lo marcado «Recomendación» es el esquema que proponemos para este proyecto; canales, horarios y tiempos de respuesta concretos no están definidos.

| Tema | Detalle | Estado |
|---|---|---|
| Contacto del proyecto | El Director de Proyectos, portavoz único. {{PENDIENTE: nombre, cargo y correo}} | Pendiente |
| Canales | {{PENDIENTE: canales de seguimiento (correo, mensajería, videollamada)}} | Pendiente |
| Horario de atención | {{PENDIENTE: días, horas y zona horaria}} | Pendiente |
| Tiempo de respuesta de nuestro equipo | {{PENDIENTE: tiempo de respuesta comprometido}} | Pendiente |
| Frecuencia de revisión de avances | **Por hitos diarios**: D1 (arranque), D2 (esqueleto en la dirección de revisión), D5 (entrega a revisión), D6 (ajustes) y D7 (publicación) | Recomendación |
| Formato de revisión | {{PENDIENTE: formato}}. Recomendamos una revisión sobre la dirección de pruebas y un informe breve de avance con decisiones pendientes | Recomendación |
| Proceso para recibir feedback | {{PENDIENTE: canal y formato}}. Recomendamos que el cliente responda **en un día hábil como máximo**; es una **condición del plazo estimado** | Recomendación |
| Revisión de la estimación | Al final de D2 y de D5, si el contenido o los accesos llegaron con retraso | Recomendación |
| Aprobaciones | La aceptación de esta oferta, la entrega a revisión y la publicación se aprueban **por escrito**. El silencio no es aprobación | Recomendación |

## 8. Inversión

> La cifra de esta sección proviene de la instrucción explícita del usuario (precio fijado por el usuario). No se ha convertido a ninguna otra moneda ni se han añadido impuestos.

### 8.1 Entrega inicial (oferta principal)

| Concepto | Valor | Estado |
|---|---|---|
| Inversión de la entrega inicial | **400 USD** (precio único por la entrega descrita en la sección 3.1) | Confirmado (por el usuario) |
| Moneda de facturación | **Pendiente.** La cifra se expresa en dólares estadounidenses tal como se fijó; al estar el cliente en España, la moneda de facturación se definirá **antes de facturar**. No se convierte ninguna moneda | Pendiente |
| IVA e impuestos | **Pendiente**: tratamiento a definir antes de facturar | Pendiente |
| Forma de pago | {{PENDIENTE: forma de pago}} | Pendiente |
| Qué incluye | Lo listado en la sección 3.1: sitio público adaptable a móvil (inicio, catálogo de hasta 3 o 4 campers de ejemplo, fichas, tarifas y condiciones, contacto), páginas legales y de cookies en borrador, SEO técnico base, formulario de solicitud de reserva por correo, guía breve de edición de contenido y una ronda de ajustes | Recomendación |
| Qué no incluye | Lo listado en la sección 3.3: pago en línea, disponibilidad automática, panel, cuentas, reembolsos, MFA y auditoría; hosting, dominio y correo de terceros; asesoría legal; mantenimiento; garantía de posicionamiento o de rendimiento real; otras rondas de cambios, extras, FAQ y varios idiomas | Recomendación |

**Costes de terceros no incluidos** (los contrata y paga el cliente, o se acuerda otra cosa; sin cifras):

| Concepto | Observación |
|---|---|
| Alojamiento (hosting) con función para el formulario | Según el proveedor elegido |
| Dominio y certificado | Titularidad del cliente |
| Servicio de correo y buzones de destino | Según el proveedor elegido |
| Asesoría legal y fiscal | Del cliente; fuera de esta propuesta |
| Fotografía profesional | Del cliente; fuera de esta propuesta |

### 8.2 Margen de negociación

Entendemos que esta oferta puede necesitar ajustarse a sus prioridades. **Estamos abiertos a conversar y ajustar las condiciones y el alcance** para encontrar juntos la mejor solución: por ejemplo, las prioridades de contenido, el número de campers de ejemplo, el número de rondas de cambio, los plazos de pago o el calendario de entrega. No presentamos cifras de descuento: cualquier ajuste se acordaría por escrito, se registraría como solicitud de cambio y mantendría claro qué se entrega y qué no. Estado: **Confirmado** (existe margen, por el usuario) · **Pendiente** (los términos concretos, que se definirían en la conversación).

### 8.3 Fase siguiente

La fase siguiente (MVP completo, sección 11) **no tiene precio en esta propuesta**: se cotizará aparte cuando se confirmen las decisiones previas y se autorice su planificación. **Pendiente.**

## 9. Riesgos y supuestos

Los identificadores del expediente se conservan (el calificador [AN], [PM], [PLAN] o [OPB] distingue el origen cuando un número se repite). Los riesgos de la estimación de la opción B se señalan con **[OPB]**; sus números coinciden con los de otros riesgos del expediente y el Director debe asignarles identificadores definitivos al registrarlos. El estado de todos es **OPEN** (abierto).

### 9.1 Riesgos de la entrega inicial

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Estado |
|---|---|---|---|---|---|
| R-001 [OPB] | Contenidos y fotos tardíos o de baja calidad | Alta | Alto | Contenido de ejemplo marcado; fecha límite el D1 | OPEN |
| R-002 [OPB] | Textos legales y de cookies sin validar | Media | Alto | Publicar como borrador; la asesoría legal es del cliente y queda fuera del alcance | OPEN |
| R-003 [OPB] | Entregabilidad del correo (spam, DNS tardío) | Media | Alto | SPF, DKIM y DMARC; copia en el servicio de correo; prueba con la cuenta real | OPEN |
| R-004 [OPB] | Solicitudes perdidas al no haber base de datos | Baja | Alto | Registro del proveedor de correo y copia a un segundo buzón | OPEN |
| R-005 [OPB] | SEO sin garantías de posicionamiento | Alta | Medio | Prometer solo lo técnico, no posiciones | OPEN |
| R-006 [OPB] | Sin margen: cualquier retraso rompe la semana | Alta | Alto | Núcleo recortado; ampliar el plazo o el equipo si se prefiere | OPEN |
| R-007 [OPB] | Rehacer parte de la web pública al migrar al MVP completo | Media | Medio | Elegir una pila compatible con la arquitectura de la fase siguiente (por verificar) | OPEN |
| R-008 [OPB] | Estacionalidad: la web debe estar publicada antes de la temporada alta | Media | Medio | Confirmar con el cliente su temporada | OPEN |

### 9.2 Riesgos de la fase siguiente (resumen)

Los riesgos completos del MVP completo (R-PL-001 a R-PL-011 [PLAN], R-001 a R-013 [AN], R-001 a R-008 [PM], R-ARQ, R-UX y SEG-001 a SEG-017) se mantienen en el [análisis consolidado](analisis-consolidado.md), sección 8, y en [RISKS](../00-control/RISKS.md). Los más relevantes: decisiones B1 a B9 tardías (R-PL-001), validación legal tardía (R-PL-006 [PLAN] / R-001 [AN]), doble reserva por concurrencia (R-003 [AN] / R-PL-004 [PLAN]), pasarela no elegida (R-004 [AN] / R-ARQ-01), siete hallazgos de severidad alta de la revisión de seguridad **de diseño** (SEG-001 a SEG-007) y privacidad sin cerrar (SEG-010). Ninguna prueba de seguridad se ejecutó: no hay sistema construido.

**Supuestos principales** (todos **Supuesto**, no confirmados): español y zona horaria de Madrid; cliente particular; una sola empresa; una reserva = un camper; recogida y devolución en la misma sede; volumen bajo o moderado. Los supuestos del plazo están en la sección 6.3.

## 10. Decisiones y preguntas previas para el cliente

Antes de fijar alcance y plazo necesitamos su respuesta a lo siguiente. Si algo no está claro, preferimos consultarlo antes de construir. **Ninguna de las propuestas de este documento se considera aceptada por silencio.** Las preguntas **OB-01 a OB-14** son etiquetas locales de esta propuesta, no identificadores del expediente.

### A. Decisiones para la entrega inicial (opción B)

| # | Pregunta o decisión | Por qué importa | Impacto si cambia | Estado |
|---|---|---|---|---|
| OB-01 | **¿Quién edita el contenido de la flota?** (PEND-045) Proponemos que lo edite el proveedor mediante archivos de datos. Si prefieren editar ustedes, hace falta un gestor de contenidos ligero | Cambia el plazo (+1 a 2 días) o el alcance | Plazo y alcance | Pendiente |
| OB-02 | **¿Aceptan el núcleo recortado?** (PEND-046) Máximo 3 o 4 campers de ejemplo, tarifas y condiciones en una sola página, legales desde plantilla, aviso de cookies informativo, formulario por correo y una sola ronda de ajustes | Es lo que cabe en una semana | Plazo y alcance | Pendiente |
| OB-03 | **¿Aceptan la desviación de que la flota y las sedes configurables desde un panel pasen a la fase siguiente?** (RN-001, RNF-010, CR-001, PEND-044) | Es un cambio frente a lo confirmado en el brief | Alcance | Pendiente |
| OB-04 | **Moneda de facturación e IVA** (PEND-043), sin convertir la cifra de 400 USD | Necesario antes de facturar | Inversión | Pendiente |
| OB-05 | **Forma de pago** y condiciones comerciales | Cierre del documento | Inversión | Pendiente |
| OB-06 | **Contenido del D1**: datos de campers (plazas, equipamiento, tarifas orientativas), fotos reales o aceptar las de ejemplo | Condición del plazo | Plazo | Pendiente |
| OB-07 | **Datos legales y de contacto**: razón social, NIF, domicilio, correo de destino de las solicitudes y segundo buzón de copia | Condición del plazo; páginas legales y formulario | Plazo | Pendiente |
| OB-08 | **Accesos**: hosting y DNS (D1–D2) o permiso para usar una dirección provisional | Condición de la publicación en su dominio | Plazo | Pendiente |
| OB-09 | **Marca**: nombre, logotipo, colores, tipografía, tono (tú o usted) y estilo fotográfico (PEND-025) | Los mockups usan una marca provisional **no aprobada** | Plazo | Pendiente |
| OB-10 | **Condiciones de alquiler y política de cancelación**: ¿aportan sus textos o aceptan un borrador genérico? ¿Contratarán asesoría legal? (PEND-010, PEND-022, PEND-023) | Textos que el cliente define y la asesoría valida | Contenido | Pendiente |
| OB-11 | **Fecha de inicio**, fecha objetivo y estacionalidad del negocio | Permiten convertir días relativos en fechas | Plazo | Pendiente |
| OB-12 | **Presupuesto y fechas:** el brief indicaba que no entraban en el contrato; ahora se ofrece un valor y un plazo objetivo. ¿Cómo desean tratarlos? | Resolver la tensión señalada en la sección 2 | Inversión y plazo | Pendiente |
| OB-13 | **Margen de negociación:** ¿qué prioridades desean ajustar (número de campers, rondas de cambio, calendario de pagos, plazo)? | Punto de partida de la conversación (sección 8.2) | Alcance e inversión | Pendiente |
| OB-14 | **Datos del cliente y vigencia de esta propuesta** | Cierre del documento | — | Pendiente |

### B. Decisiones previas a la fase siguiente (MVP completo)

Se necesitan antes de autorizar la construcción de la fase siguiente y de cotizarla. Las marcadas con (*) también inciden en la entrega inicial.

#### B.1 Decisiones previas (B1 a B9)

| # | Pregunta o decisión | Por qué importa | Impacto si cambia | Estado |
|---|---|---|---|---|
| 1 | **B1 · Pasarela de pago y titularidad de la cuenta.** ¿Qué proveedor eligen y a nombre de quién estará la cuenta? (PEND-012, PEND-011) | Es el corazón del pago seguro. Límite aproximado: S6 desde la autorización de la fase siguiente | Plazo e inversión (comisiones) | Pendiente |
| 2 | **B2 · Hosting y región.** Recomendamos un servicio gestionado en la UE con base de datos compatible (PEND-034) (*) | Condiciona entornos, copias y privacidad. Límite aproximado: S10 | Plazo e inversión | Pendiente |
| 3 | **B3 · Política de cancelación.** Tramos y porcentajes de reembolso; **¿se aplica la política vigente al reservar (nuestra recomendación, más previsible para el consumidor, pendiente de validación legal) o la vigente al cancelar?**; quién asume las comisiones de la pasarela en los reembolsos (PEND-008, PEND-009, ISS-002, DEC-025) | Define el cálculo del reembolso y los textos de la reserva. Límite aproximado: S14 | Alcance y plazo | Pendiente |
| 4 | **B4 · Validación legal.** ¿Contratarán asesoría legal y fiscal? Necesitamos el alcance legal definido y el inventario de datos antes de construir; los textos finales antes de producción (PEND-010) (*) | Privacidad, cookies, información precontractual, desistimiento, IVA y pagos con autenticación reforzada. Límite aproximado: antes de S20 | Plazo | Pendiente |
| 5 | **B5 · Acceso a la reserva y segundo paso para cancelar.** ¿Código + correo con un segundo paso (por ejemplo, enlace al correo) antes de cancelar, o enlace por correo para todo? (SEG-001, PEND-035, PEND-037) | El correo no es un secreto; sin segundo paso, quien conozca el código y el correo podría cancelar y provocar un reembolso. Límite aproximado: S14 | Alcance y plazo | Pendiente |
| 6 | **B6 · MFA obligatorio del administrador.** ¿Aceptan segundo factor de autenticación obligatorio para el panel? (SEG-006, PEND-035) | El panel maneja datos personales, tarifas y reembolsos. Límite aproximado: S8 | Alcance (cambio frente a la propuesta de producto) | Pendiente |
| 7 | **B7 · Retención de datos.** ¿Durante cuánto tiempo se conservan los datos de clientes y cómo se suprimen? (SEG-010, PEND-036) (*) | Privacidad. Límite aproximado: antes de S20 | Alcance y plazo | Pendiente |
| 8 | **B8 · Recuperación ante desastres.** ¿Cuánta pérdida de datos y cuánto tiempo sin servicio pueden tolerar? (RPO/RTO, PEND-015) | Define copias y restauración. Límite aproximado: S10 | Plazo e inversión | Pendiente |
| 9 | **B9 · Dominio y titularidad de cuentas.** ¿Quién contrata y titulariza dominio, correo, hosting y pasarela? (PEND-011) (*) | Entregabilidad de correo y control de las cuentas. Límite aproximado: S10 | Plazo | Pendiente |

#### B.2 Cambios de seguridad que recomendamos incorporar al MVP completo

La revisión de seguridad del diseño recomienda estos cuatro cambios. Si ustedes los aceptan, el Director de Proyectos los registrará como **solicitudes de cambio** antes de la autorización de construcción de la fase siguiente. El plazo de la sección 11.4 asume los tres primeros dentro del alcance.

| # | Cambio recomendado | Por qué importa | Impacto si cambia | Estado |
|---|---|---|---|---|
| 10 | **MFA obligatorio del administrador** (ver B6) | Un acceso comprometido al panel permite cambiar tarifas y reembolsar | Alcance | Pendiente |
| 11 | **Auditoría mínima en el MVP:** registro de quién hizo qué y cuándo en inicios de sesión, tarifas, bloqueos, cancelaciones, reembolsos y exportaciones (SEG-007, PEND-038). Hoy el registro de auditoría completo está en la segunda fase | Sin registro no se puede investigar un abuso interno o una cuenta comprometida | Alcance | Pendiente |
| 12 | **Segundo paso para cancelar** una reserva (ver B5, SEG-001, PEND-037) | Evita cancelaciones y reembolsos indebidos | Alcance | Pendiente |
| 13 | **Precio mayor que cero** (o un flujo definido para importe cero) en tarifas (SEG-005, PEND-039, VAL-020) | Una tarifa en cero, por error o por abuso, generaría reservas sin cobro | Alcance | Pendiente |

#### B.3 Alcance y reglas de negocio

| # | Pregunta o decisión | Por qué importa | Impacto si cambia | Estado |
|---|---|---|---|---|
| 14 | **Modelo de cobro.** Proponemos pago **total** al reservar. Alternativa: depósito y saldo posterior (el análisis la recomendaba; exige un segundo cobro, recordatorios y estado de pago parcial) (Q1, PEND-001, DEC-001, DEC-002, ISS-005) | Cambia estados de pago y alcance | Alcance, plazo e inversión | Pendiente |
| 15 | **Otros medios de pago** además de tarjeta (Q1, DEC-003) | Hoy solo tarjeta | Alcance | Pendiente |
| 16 | **Fianza.** Proponemos que se gestione en la entrega y se muestre como información. ¿Importe y texto? ¿O preautorización en línea (ampliación)? (Q2, PEND-002, PEND-018, DEC-004) (*) | Define el texto y la integración de pago | Alcance | Pendiente |
| 17 | **Acceso del cliente.** Proponemos código + correo (sin cuenta). Alternativa: cuenta de usuario (segunda fase) (Q3, PEND-003, DEC-005, DEC-006) | Esfuerzo y fricción | Alcance y plazo | Pendiente |
| 18 | **Facturación.** ¿Basta un justificante de pago o necesitan factura automática? ¿Habrá clientes empresa con NIF? ¿Más idiomas? (Q4, PEND-004, DEC-007, DEC-008, DEC-009, ISS-004) | Propuesta actual: justificante en el MVP y factura en la segunda fase | Alcance e inversión | Pendiente |
| 19 | **Verificación del conductor.** Proponemos verificar carnet y documento en persona en la recogida, no en la web. ¿Edad mínima, requisitos de permiso y conductores adicionales? (Q5, PEND-005, PEND-019, DEC-010, DEC-011, ISS-014) (*) | Privacidad y flujo de reserva | Alcance | Pendiente |
| 20 | **Otra sede de devolución.** Proponemos misma sede en el MVP. ¿Se permitirá devolver en otra sede y con qué suplemento? (Q6, PEND-006, DEC-012, DEC-013, ISS-011) | Cambia el modelo de disponibilidad | Alcance y plazo | Pendiente |
| 21 | **Panel.** ¿Cuántas personas lo usarán y con qué permisos? ¿Reservas manuales e informes en el MVP? Proponemos un solo rol y reservas por teléfono cubiertas con bloqueo manual de fechas (Q7, PEND-007, DEC-014 a DEC-017) | Cambia el alcance del panel | Alcance y plazo | Pendiente |
| 22 | **Extras (equipamiento adicional).** El análisis los incluía en el MVP; el equipo de producto los pasa a la segunda fase. ¿Los necesitan en la salida inicial? Si sí, sería una solicitud de cambio (P-009, DEC-018, ISS-006) | Amplía el MVP | Alcance, plazo e inversión | Pendiente |
| 23 | **Cancelación por el cliente con reembolso automático en el MVP.** Alternativa: cancelación solo por el administrador (P-004, DEC-024) | Define el flujo de cancelación | Alcance | Pendiente |
| 24 | **Correos al cliente.** Además de la confirmación, ¿cuáles se envían en el MVP (reenvío de código, enlace para reintentar un pago, aviso de expiración, recordatorio)? (DEC-023, ISS-009, ISS-018) | Alcance de notificaciones | Alcance | Pendiente |
| 25 | **Una o varias sedes** y cobertura de SEO por sede (PEND-028) (*) | Navegación y páginas indexables | Alcance | Pendiente |
| 26 | **Definición de «noche» frente a «día», horas de recogida y devolución, y zona horaria** (relevante si hay sedes en Canarias) (PEND-013, ISS-012, ISS-022) | Cálculo de precios y disponibilidad | Alcance y plazo | Pendiente |
| 27 | **Duración del bloqueo** durante el pago (15 minutos es solo una propuesta) y si se puede ampliar; **antelación mínima y máxima** y duración máxima de reserva (DEC-027, PEND-031, PEND-017) | Disponibilidad y experiencia de pago | Alcance | Pendiente |
| 28 | **Regla al desactivar** un camper o sede con reservas futuras (PEND-024, DEC-028) | Integridad de reservas | Alcance | Pendiente |
| 29 | **Panel:** recuperación de contraseña del administrador y dónde se configura el correo de aviso (PEND-026, PEND-027) | Seguridad y operación | Alcance | Pendiente |
| 30 | **Público extranjero y SEO,** siendo la web solo en español (PEND-016) (*) | Estrategia de SEO | Alcance | Pendiente |
| 31 | **Volumen esperado, tamaño de flota, proceso actual y metas** (PEND-021, PEND-015) | Dimensionamiento y métricas de éxito | Plazo e inversión | Pendiente |

#### B.4 Contenido, marca y calidad

| # | Pregunta o decisión | Por qué importa | Impacto si cambia | Estado |
|---|---|---|---|---|
| 32 | **Marca:** nombre, logotipo, colores, tipografía, tono y estilo fotográfico (PEND-025) (*). Véase OB-09 | Cambiarla tarde obliga a rehacer componentes | Plazo | Pendiente |
| 33 | **Datos y contenidos iniciales:** flota, sedes, tarifas, fotos reales y textos (PEND-020, PEND-022) (*). Véase OB-06 | Necesarios para publicar | Plazo | Pendiente |
| 34 | **Condiciones de alquiler:** kilometraje, combustible, limpieza, mascotas, viaje al extranjero, franquicia y seguro; no presentación y devolución tardía (PEND-022, PEND-023) (*). Véase OB-10 | Textos que el cliente define y la asesoría valida | Contenido | Pendiente |
| 35 | **Medición de rendimiento y accesibilidad:** protocolo y alcance de la revisión (PEND-014) | Para poder afirmar que se cumplen los objetivos | Alcance y plazo | Pendiente |

#### B.5 Condiciones del contrato de la fase siguiente

| # | Pregunta o decisión | Por qué importa | Impacto si cambia | Estado |
|---|---|---|---|---|
| 36 | **Cómo desean tratar la inversión y el plazo de la fase siguiente** (el brief indicaba que presupuesto y fechas no entraban en el contrato) | La fase siguiente no tiene precio y su plazo es una estimación | Plazo e inversión | Pendiente |
| 37 | **Fecha de inicio** de la fase siguiente y estacionalidad | Permiten convertir semanas relativas en fechas | Plazo | Pendiente |

## 11. Fase siguiente: MVP completo

> **Sin precio. Plazo preliminar: 28 a 36 semanas desde la autorización de su construcción (H0). Se cotizará aparte** cuando se confirmen las decisiones previas (sección 10, grupo B). Es una **Recomendación a confirmar**, no un compromiso. No se ha reestimado considerando lo reutilizable de la entrega inicial: {{PENDIENTE: confirmar con el Planificador cuánto se reutiliza y si cambia el rango}}.

### 11.1 Qué incluiría (propuesta del equipo de producto)

Todo es **Recomendación** y **no está aprobado**. Prioridad: Must. El detalle y la trazabilidad están en el [análisis consolidado](analisis-consolidado.md), secciones 2 y 3.

| ID | Descripción | Estado |
|---|---|---|
| RF-001 | Catálogo de campers y ficha, con gestión desde el panel | Confirmado (necesidad) · Recomendación (contenido) · Pendiente (fotos reales) |
| RF-002 | Búsqueda por fechas de recogida y devolución y por sede | Confirmado |
| RF-003 | Disponibilidad por camper y fechas, validada en el servidor | Confirmado |
| RF-004 | Precio total desglosado calculado en el servidor y congelado al reservar | Recomendación (impuestos: Pendiente de validación legal) |
| RF-006 | Reserva: datos del conductor principal, resumen, aceptación de condiciones y pago | Recomendación |
| RF-007 | Bloqueo temporal de las fechas durante el pago (15 minutos es solo una propuesta) | Recomendación |
| RF-008 | Pago en línea mediante pasarela segura; pago total con tarjeta al reservar | Confirmado (necesidad) · Pendiente (proveedor) · Supuesto (tarjeta) |
| RF-009 | Autenticación reforzada del pago (3-D Secure), gestionada por la pasarela | Recomendación |
| RF-010 | Confirmación en pantalla y por correo con código de reserva y justificante de pago | Recomendación |
| RF-011 | Consulta de la reserva por el cliente | Confirmado |
| RF-012 | Acceso a la reserva con código de reserva y correo (sin cuenta de usuario) | Supuesto |
| RF-013 | Cancelación por el cliente con cálculo automático del reembolso según la política | Recomendación (a confirmar) |
| RF-015 (contacto) | Formulario o datos de contacto | Recomendación |
| RF-016, RF-017 | Páginas legales y banner de consentimiento de cookies | Recomendación (contenido: Pendiente de asesoría legal) |
| RF-018 | Páginas indexables para SEO: páginas por camper y sede | Confirmado (SEO) · Recomendación (técnicas) |
| RF-019 a RF-022 | Panel de administración (rol único), gestión de flota, de sedes y de tarifas | Supuesto (RF-019) · Confirmado (configurable, RF-020 a RF-022) |
| RF-023 a RF-025 | Gestión de reservas, bloqueo manual de fechas, gestión de pagos y reembolsos | Recomendación |
| RF-026 | Aviso mínimo por correo al administrador (reserva nueva, cancelación, pago tardío sin disponibilidad) | Recomendación |
| RF-032 | Expiración automática de reservas impagadas y liberación de fechas | Recomendación |

Objetivos transversales (**Recomendación**): rendimiento en móvil (RNF-001), SEO técnico sin garantía (RNF-002), diseño adaptable (RNF-003), flujo claro (RNF-004) y accesibilidad con objetivo WCAG 2.1 nivel AA (RNF-005, alcance de la revisión pendiente).

**Cambios de seguridad recomendados para la fase siguiente** (requieren su decisión; ver sección 10, grupo B.2): MFA obligatorio para el administrador, auditoría mínima, segundo paso para cancelar y precio mayor que cero.

### 11.2 Segunda fase, ampliaciones y exclusiones del MVP completo

Todo es **Recomendación** y no está comprometido.

| Concepto | Elementos | Estado |
|---|---|---|
| Segunda fase (después del MVP completo) | Extras opcionales (RF-005 / HU-025); preguntas frecuentes (RF-015 / HU-026); modificación de reserva (RF-014 / HU-027); reservas manuales en el panel (RF-028 / HU-028); plantillas de correo editables (RF-027 / HU-029); depósito y saldo posterior (HU-030); factura automática y clientes empresa (HU-031); cuentas de cliente (RF-012 / HU-032); informes y auditoría completa (RF-029 / HU-033); roles adicionales (RF-030 / HU-034); centro de avisos completo (RF-026 ampliado / HU-035); devolución en otra sede (HU-036) | Recomendación |
| Posibles ampliaciones | Fianza en línea; otros medios de pago; varios idiomas; cupones; reseñas; subida de documentos del conductor; contrato digital; sincronización con canales externos. Entrarían como solicitud de cambio (RF-031) | Recomendación |
| Exclusiones | Migración de datos e integración con sistemas existentes (Confirmado); aplicación móvil nativa y marketplace; canales externos y GPS; producción de fotografía y vídeo; asesoramiento jurídico y fiscal; campañas de marketing y garantía de posicionamiento; puesta en producción con tráfico real sin autorización específica; tiempos de terceros | Confirmado / Recomendación |

### 11.3 Plan por fases (desde la autorización de construcción, H0)

Fuente: [implementation-plan.md](../05-planning/implementation-plan.md). Cada fase termina en una **puerta de aprobación humana**; la fase P0 queda fuera del reloj.

| Fase | Objetivo | Duración probable | Estado |
|---|---|---|---|
| P0 · Preparación | Reconciliar el análisis, resolver las decisiones previas, aprobar alcance y plan | Fuera del reloj: ≈ 3 semanas (2–4 o más) | Recomendación |
| P1 · Fundaciones | Entorno, base de datos y esqueleto de la aplicación | 4 semanas (3–6) | Recomendación |
| P2 · Núcleo de reserva y pago | Precio, disponibilidad, bloqueo temporal, pago y expiración | 9 semanas (7–12) | Recomendación |
| P3 · Post-reserva, panel y web | Correos, consulta y cancelación, panel, auditoría mínima, SEO y legales | 6 semanas (4–9) | Recomendación |
| P4 · Calidad y seguridad | Pruebas integrales, revisión de seguridad de la implementación y correcciones | 6 semanas (4–9) | Recomendación |
| P5 · Operación y documentación | Entornos, copias con restauración probada, guía operativa y manual | 3 semanas (2–6) | Recomendación |
| P6 · Auditoría y cierre | Auditoría de trazabilidad y de entrega; decisión go/no-go | 2 semanas (2–3) | Recomendación |

### 11.4 Plazo preliminar

| Concepto | Valor |
|---|---|
| Rango estimado recomendado | **28 a 36 semanas** desde H0. Valor más probable: 30–31 semanas. Contingencia del 15 al 20 % incluida en el extremo alto |
| Fecha de inicio | PENDIENTE: fecha de inicio (solo si el cliente la confirma) |
| Fecha de entrega | Se confirmará al fijar la fecha de inicio (PENDIENTE) |
| Supuestos | 2 personas de backend a tiempo completo, 1 de frontend a tiempo completo, datos, DevOps y calidad parciales, decisiones B1 a B9 resueltas antes de H0, MFA, auditoría mínima y precio mayor que cero dentro del alcance, respuesta del cliente en 3 días hábiles. Con un solo desarrollador de backend el plazo sube entre un 25 y un 40 % |

Hitos relativos a H0: H1 ~S4 · revisión intermedia ~S8 · H2 ~S13 · H3 ~S19 · H4 ~S25 · H5 ~S28 · H6 ~S30. **Fecha = H0 + N semanas, más las esperas del cliente y de terceros** (todas las fechas: PENDIENTE hasta confirmar el inicio). El método y los extremos técnicos están en el [análisis consolidado](analisis-consolidado.md), sección 7.1.

### 11.5 Enfoque técnico y seguridad (resumen)

Todo es **Recomendación**; ninguna tecnología es obligatoria. Aplicación única organizada por módulos, con regla de base de datos contra reservas solapadas, bloqueo temporal durante el pago, pago alojado por la pasarela confirmado solo por aviso firmado, páginas públicas con caché y datos estructurados, entornos de pruebas y producción con copias cifradas y restauración probada. La revisión de seguridad realizada es **de diseño**: 17 hallazgos abiertos (siete de severidad alta, SEG-001 a SEG-007; SEG-010 alta a validar con asesoría legal; ocho medias; una baja) y **no se ejecutó ninguna prueba**. Detalle en el [análisis consolidado](analisis-consolidado.md), secciones 5 y 6.

### 11.6 Inversión

**Sin precio en esta propuesta. Se cotizará aparte** una vez confirmadas las decisiones previas. Costes recurrentes de terceros a considerar (sin cifras, a cargo del cliente salvo acuerdo): comisiones de la pasarela de pago (quién asume las de reembolsos: PEND-009), hosting y base de datos (B2), correo transaccional, dominio y certificado (B9), almacenamiento de imágenes, seguimiento de errores, asesoría legal y fiscal, y fotografía profesional.

### 11.7 Relación con la entrega inicial

La entrega inicial es una **desviación acotada** del alcance confirmado (CR-001): sustituye temporalmente el MVP completo por un sitio público con solicitud de reserva. Elegiremos una base compatible para reducir el rehacer (R-007 [OPB]). El panel (flota y sedes configurables) y el pago seguro se construyen en esta fase siguiente, con su propia autorización.

## 12. Condiciones, control de cambios y aprobación

### 12.1 Condiciones

| Tema | Condición | Estado |
|---|---|---|
| Vigencia | {{PENDIENTE: vigencia}} | Pendiente |
| Propiedad y confidencialidad | {{PENDIENTE: condiciones}} | Pendiente |
| Garantía o soporte | {{PENDIENTE: garantía}} | Pendiente |
| Alcance | Esta propuesta no aprueba el alcance ni CR-001. Sin su aprobación explícita no se inicia ningún desarrollo | Confirmado (regla del equipo) |
| Despliegue y publicación | Ningún despliegue, publicación ni acción externa sin una autorización específica y adicional (incluida la publicación en su dominio) | Confirmado (regla del equipo) |
| Plazo | El plazo de 1 semana es de **entrega a revisión** y depende de las condiciones de la sección 6.1 | Recomendación |
| Rondas de cambio | Una ronda de ajustes; lo adicional es otro alcance | Recomendación |

### 12.2 Control de cambios

Todo cambio posterior a la aprobación del alcance se registra como solicitud de cambio (`CR-###`), se analiza su impacto en alcance, plazo e inversión y requiere la decisión del cliente antes de ejecutarse. La oferta principal de esta propuesta corresponde a la solicitud de cambio **CR-001** (estado WAITING_FOR_APPROVAL, registrada en [CHANGE-REQUESTS.md](../00-control/CHANGE-REQUESTS.md); pendiente de su aprobación formal, PEND-044): sustituye el MVP completo por la entrega inicial acotada y deja el MVP completo como fase siguiente (su plazo de 28 a 36 semanas sigue vigente, DEC-033). Los cambios de seguridad de la sección 10, grupo B.2, se registrarían como solicitudes aparte si ustedes los aceptan.

### 12.3 Aceptación

| Campo | Valor |
|---|---|
| Decisión del cliente | PENDIENTE (aprobada, con cambios, rechazada) |
| Nombre y cargo | PENDIENTE |
| Fecha de decisión | PENDIENTE |
| Observaciones y condiciones | PENDIENTE |

La aceptación debe ser explícita; el silencio no es aprobación. Al aceptar, el Director registra la decisión en el control del proyecto. Este espacio no está firmado ni se presume ninguna firma.

## Anexos

| Anexo | Contenido |
|---|---|
| A | [analisis-consolidado.md](analisis-consolidado.md): análisis completo con trazabilidad (incluye la sección «Opción B: entrega inicial acotada») |
| B | [mockups/index.html](mockups/index.html): galería de mockups ilustrativos, con las pantallas de la entrega inicial y de la fase siguiente diferenciadas ([dirección visual](mockups/direccion-visual.md) y [estados alternativos](mockups/14-estados.html)) |
| C | [perfil-empresa.md](perfil-empresa.md): datos de la empresa utilizados |
| D | [checklist-calidad-propuesta.md](checklist-calidad-propuesta.md): verificaciones realizadas |
| E | Lista de marcadores PENDIENTE: [README.md](README.md), sección «Marcadores PENDIENTE» |
