# MVP y backlog de producto: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fase:** DISCOVERY/DESIGN en borrador. La puerta DISCOVERY → DESIGN está PENDING y PLANNING → BUILD no ha sido solicitada (ver [APPROVALS](../00-control/APPROVALS.md)).  
> **Fuente:** Reporte del agente Product Manager, entregado por el Director de Proyectos. Archivo de origen: `C:\Users\User\AppData\Local\Temp\1793039211782-copilot-tool-output-6c3a7fb759614e97a6cb9217c579a670.txt`. Basado en [requirements.md](../01-discovery/requirements.md).  
> **Decisiones pendientes:** [DECISIONS](../00-control/DECISIONS.md) §3 y [REQUIREMENTS](../00-control/REQUIREMENTS.md) §6. La fuente lista P-001 a P-016.  
> **Aprobación:** ninguna. El propio Product Manager declara que no aprueba el alcance. Este documento no aprueba contenido ni alcance.

## Notas del Gestor de Documentación (no forman parte de la fuente)

- Debajo de la línea `---` final de esta nota se reproduce **sin cambios de significado** el contenido del Product Manager. No se han alterado identificadores (RF, RNF, RN, HU, CA, R, P).
- Este documento presenta discrepancias con [requirements.md](../01-discovery/requirements.md). No se resuelven aquí. Quedan registradas como ISS-001 a ISS-014 en [RISKS](../00-control/RISKS.md) §2. Las propuestas pendientes de decisión están en [DECISIONS](../00-control/DECISIONS.md).
- **Recomendación del Director sobre CA-008, pendiente de validación legal:** aplicar la política de cancelación vigente **al reservar**. El texto de CA-008 de la fuente (más abajo) dice "vigente en el momento de la cancelación". No se modifica el texto de la fuente. La divergencia queda en ISS-002 y la propuesta en DEC-025.
- La numeración CA-001 a CA-014 de este documento difiere en contenido del Analista (CA-001, CA-002). El propio Product Manager lo declara como "Reconciliación pendiente" (ISS-001, DEC-030).
- Los identificadores R-001 a R-010 de este documento colisionan con los R-001 a R-013 del Analista (ISS-003).
- Enlaces: [Resumen del cliente](../00-intake/client-brief.md) · [Estado del proyecto](../00-control/PROJECT-STATE.md) · [Trazabilidad](../00-control/TRACEABILITY.md).

---

# Reporte de Producto: web de alquiler de campers en España

**Destinatario:** Director de Proyectos. **Fase:** DISCOVERY/DESIGN. **Archivos modificados:** ninguno. Solo leí el contrato y las reglas corporativas.

**Leyenda:** **[C]** Confirmado · **[S]** Supuesto · **[R]** Recomendación · **[P]** Pendiente.

**Alcance de las recomendaciones:** todas las decisiones de producto del Director (pago total, fianza informativa, código+email, etc.) son **[R]**. El cliente delegó pero no las ha confirmado.

---

## Visión del producto

- **[C]** Web para gestionar el alquiler de campers en España. Incluye reservas en línea (elegir fechas, ver disponibilidad, gestionar alquileres) y pago seguro. Busca buena experiencia de uso, velocidad de carga y SEO.
- **[C]** La flota y las sedes se configuran desde un panel.
- **[R]** Visión operativa: que un cliente encuentre un camper disponible, vea el precio total, pague y reciba su confirmación sin contactar con la empresa. Que la empresa administre flota, tarifas y reservas sin ayuda técnica.

## Usuarios objetivo

- **[S]** Cliente final (particular), que reserva desde móvil u ordenador y es conductor principal.
- **[S]** Administrador de la empresa, un único rol en el MVP.
- **[P]** No hay datos del perfil del cliente (nacionalidad, turista o residente), ni volumen de usuarios. No se inventan.

## Resultado de negocio esperado

- **[C]** Canal propio en línea para reservar y pagar, con gestión desde panel y base SEO técnica.
- **[R]** Reducir la gestión manual de disponibilidad y cobros, y evitar dobles reservas.
- **[C]** SEO técnico sin garantía de posicionamiento (RNF-002).
- **[P]** Metas cuantitativas de negocio: no están definidas y no se inventan.

---

## Alcance del MVP

**Criterio [R]:** el MVP es el mínimo que cierra el ciclo *buscar → ver precio → reservar → pagar → recibir confirmación → administrar*. Incluye solo lo imprescindible para ello, más el cumplimiento básico (legal y cookies) y la base SEO que el cliente pidió expresamente.

| Bloque | Qué entra | RF/RN/RNF | Por qué entra |
|---|---|---|---|
| Catálogo | Listado y ficha de camper | RF-001 | Sin catálogo no hay qué reservar |
| Búsqueda y disponibilidad | Búsqueda por fechas y sede; disponibilidad validada en servidor; sin solapes | RF-002, RF-003, RN-003 | Núcleo del problema |
| Precio | Precio desglosado, calculado en servidor y congelado en la reserva; temporadas y mínimo de noches | RF-004, RN-010 | Transparencia y coherencia de cobro |
| Reserva | Datos del conductor principal, aceptación de condiciones y consentimientos con versión | RF-006, RN-026 | Requisito para contratar |
| Protección de fechas | Bloqueo temporal durante el pago (15 min propuesto, configurable) | RF-007, RN-016 | Evita conflictos mientras se paga |
| Pago | Pago total con tarjeta y 3-D Secure/SCA vía pasarela; confirmación solo por notificación del servidor de la pasarela | RF-008, RF-009, RN-023, RNF-006 | Cobro seguro y fiable |
| Impagos | Expiración de reservas impagadas; pago tardío confirmado solo si hay disponibilidad, o reembolsado | RF-032, RN-015 | Libera inventario y evita incoherencias |
| Post-reserva | Correo de confirmación con justificante; consulta con código+email; cancelación con reembolso según política | RF-010, RF-011, RF-012, RF-013, RN-025, RN-027 | Cliente autónomo, menos carga operativa |
| Cumplimiento y base web | Contacto, páginas legales, banner de cookies, SEO técnico, responsive, accesibilidad como objetivo, rendimiento móvil como objetivo | RF-015 (contacto), RF-016, RF-017, RF-018, RNF-001 a RNF-005 | Exigencia legal y expectativa explícita del cliente |
| Administración | Login (rol único), flota, sedes, tarifas, temporadas y mínimo de noches, gestión de reservas, bloqueo manual, pagos y reembolsos, aviso mínimo por correo al administrador | RF-019 a RF-025, RF-026 (mínimo), RN-001 | Permite administrar sin intervención técnica |

**Notas sobre el MVP:**
- **[R]** Cobro: pago total al reservar. Fianza informativa, gestionada en la entrega. Recogida y devolución en la misma sede. Solo español y EUR. Edad mínima declarada configurable; los documentos se verifican en persona en la recogida.
- **[R]** Las **reservas telefónicas o presenciales** no tienen alta manual en el MVP (RF-028 va a F2). Se cubren provisionalmente con el **bloqueo manual de fechas** (RF-024).
- **[R]** **Imágenes de ejemplo sustituibles** desde el panel (RNF-013). Fotos reales no confirmadas **[C]**.
- **[R]** Los valores de cancelación escalonada, mínimos de noches, temporadas y extras son **configurables** y se cargarán como ejemplos "por validar".

## Fuera del MVP

- **[C]** Integraciones con sistemas existentes y migración de datos (exclusión confirmada).
- **[C]** Presupuesto y fechas están fuera de este documento y del contrato.
- **[R]** Pasan a Fase 2 o ampliaciones, con el detalle en sus secciones: extras, FAQ, modificación de reserva, cuentas de cliente, depósito+saldo diferido, otra sede de devolución, factura automática, plantillas de correo editables, reservas manuales, informes y auditoría, roles adicionales, centro de avisos. Las ampliaciones son fianza en línea, otros medios de pago, multi-idioma, cupones, reseñas, documentos del conductor, contrato digital y sincronización de canales.

---

## Priorización (MoSCoW)

**Criterio [R]:** el MVP contiene solo los **Must**. Los **Should** son la primera ola de Fase 2. Los **Could** son Fase 2 tardía o ampliaciones. "Won't por ahora" queda excluido del alcance actual.

| Elemento | Prioridad | Destino |
|---|---|---|
| RF-001, RF-002, RF-003, RF-004 | Must | MVP |
| RF-006, RF-007, RF-008, RF-009, RF-032 | Must | MVP |
| RF-010 (confirmación y justificante), RF-011, RF-012 (código+email) | Must | MVP |
| RF-013 cancelación con reembolso | Must (ver P-004) | MVP |
| RF-015 contacto, RF-016, RF-017, RF-018 | Must | MVP |
| RF-019 a RF-025 (rol único) | Must | MVP |
| RF-026 aviso mínimo por correo al administrador | Must (mínimo) | MVP |
| Responsive, rendimiento, accesibilidad como objetivos (RNF-001 a RNF-005) | Must (como objetivos verificables) | MVP |
| RF-005 extras (y la parte de extras de RF-022) | Should | Fase 2 |
| RF-015 FAQ | Should | Fase 2 |
| RF-014 modificar reserva | Should | Fase 2 |
| RF-028 reservas manuales | Should | Fase 2 |
| RF-027 plantillas de correo editables | Should | Fase 2 |
| Depósito + saldo diferido | Should | Fase 2 |
| Factura automática y clientes empresa | Should | Fase 2 |
| Cuentas de cliente | Could | Fase 2 |
| RF-029 informes y auditoría | Could | Fase 2 |
| RF-030 roles adicionales | Could | Fase 2 |
| Centro de avisos completo (RF-026 ampliado) | Could | Fase 2 |
| Otra sede de devolución con suplemento | Could | Fase 2 |
| Fianza en línea, otros medios de pago, multi-idioma, cupones, reseñas, documentos del conductor, contrato digital, sincronización de canales | Won't por ahora | Ampliaciones |
| Integraciones con sistemas existentes, migración de datos | Won't (excluido, **[C]**) | Fuera de alcance |

**[R]** Los extras (RF-005) pasan a Fase 2 aunque son comunes en este negocio. No son imprescindibles para reservar y pagar. Ver P-009.

---

## Historias de usuario

Todas las historias son **[R]** hasta que el alcance sea aprobado. Los RF y RN vienen del análisis previo.

### MVP: cliente

| ID | Historia | Prio | Trazabilidad | CA |
|---|---|---|---|---|
| HU-001 | Como cliente, quiero ver el catálogo y la ficha de cada camper, para decidir cuál me conviene. | Must | RF-001, RNF-013 | CA-016 |
| HU-002 | Como cliente, quiero buscar por fechas y sede, para ver solo los campers que puedo alquilar. | Must | RF-002, RF-003 | CA-015, CA-001, CA-009 |
| HU-003 | Como cliente, quiero que la disponibilidad que veo sea fiable, para no perder tiempo con una reserva que no se pueda hacer. | Must | RF-003, RN-003, RNF-007 | CA-001, CA-002, CA-003 |
| HU-004 | Como cliente, quiero ver el precio total desglosado antes de pagar, para saber cuánto pagaré. | Must | RF-004, RN-010 | CA-017, CA-034, CA-012 |
| HU-005 | Como cliente, quiero indicar mis datos como conductor principal y aceptar las condiciones, para formalizar la reserva. | Must | RF-006, RN-026, RNF-008 | CA-018, CA-010 |
| HU-006 | Como cliente, quiero que las fechas queden reservadas mientras pago, para que nadie me las quite. | Must | RF-007, RN-016, RN-003 | CA-003, CA-002 |
| HU-007 | Como cliente, quiero pagar en línea con tarjeta de forma segura, para completar mi reserva. | Must | RF-008, RF-009, RNF-006 | CA-031, CA-006 |
| HU-008 | Como cliente, quiero que mi reserva solo se confirme cuando el pago esté realmente validado, para tener certeza. | Must | RN-023, RN-021, RN-022, RNF-009 | CA-004, CA-032 |
| HU-009 | Como empresa, quiero que las reservas impagadas expiren y que los pagos tardíos se gestionen con seguridad, para no bloquear flota ni cobrar sin servicio. | Must | RF-032, RN-015 | CA-005, CA-007 |
| HU-010 | Como cliente, quiero recibir por correo la confirmación y el justificante, para tener constancia. | Must | RF-010, RN-027, RNF-014 | CA-019 |
| HU-011 | Como cliente, quiero consultar mi reserva con código y email, para ver su estado y detalle sin crear cuenta. | Must | RF-011, RF-012, RN-025 | CA-020, CA-013 |
| HU-012 | Como cliente, quiero cancelar mi reserva y recibir el reembolso que corresponda según la política, para no depender de llamadas. | Must | RF-013 | CA-008 |
| HU-013 | Como cliente, quiero poder contactar con la empresa, para resolver dudas. | Must | RF-015 (contacto) | CA-029 |
| HU-014 | Como cliente, quiero ver las páginas legales y decidir sobre las cookies, para conocer mis derechos. | Must | RF-016, RF-017, RN-026 | CA-026, CA-027 |
| HU-015 | Como empresa, quiero una web con base SEO técnica y carga rápida en móvil, para ser encontrada y no perder reservas. | Must | RF-018, RNF-001, RNF-002 | CA-028, CA-014 |
| HU-016 | Como cliente, quiero usar la web cómodamente desde móvil y con accesibilidad básica, para reservar sin barreras. | Must | RNF-003, RNF-004, RNF-005 | CA-030 |

### MVP: administración

| ID | Historia | Prio | Trazabilidad | CA |
|---|---|---|---|---|
| HU-017 | Como administrador, quiero acceder al panel con credenciales, para proteger los datos. | Must | RF-019, RNF-006 | CA-021 |
| HU-018 | Como administrador, quiero gestionar la flota (alta, edición, activación/desactivación, imágenes), para mantener el catálogo al día. | Must | RF-020, RN-001, RNF-010, RNF-013 | CA-011 |
| HU-019 | Como administrador, quiero gestionar las sedes, para operar en distintas ubicaciones. | Must | RF-021, RN-001 | CA-011, CA-033 |
| HU-020 | Como administrador, quiero configurar tarifas, temporadas y mínimo de noches, para controlar los precios. | Must | RF-022, RN-010 | CA-011, CA-034, CA-012 |
| HU-021 | Como administrador, quiero ver y gestionar las reservas (listar, filtrar, detalle, cancelar), para operar el negocio. | Must | RF-023, RN-021 | CA-022, CA-032 |
| HU-022 | Como administrador, quiero bloquear fechas de un camper (mantenimiento, reservas fuera de la web), para evitar conflictos. | Must | RF-024, RN-003 | CA-023, CA-002 |
| HU-023 | Como administrador, quiero ver pagos y emitir reembolsos, para controlar el dinero. | Must | RF-025, RN-022, RNF-009 | CA-024 |
| HU-024 | Como administrador, quiero recibir un correo cuando haya una reserva nueva, una cancelación o un pago tardío que requiera acción, para enterarme sin vigilar el panel. | Must (mínimo) | RF-026 | CA-025 |

### Fase 2 (esbozos)

Los CA de Fase 2 se redactarán al planificarla y no se enlazan aquí, porque no hay base confirmada.

| ID | Historia | Prio | Origen |
|---|---|---|---|
| HU-025 | Como cliente, quiero añadir extras a mi reserva. | Should | RF-005, RF-022 |
| HU-026 | Como cliente, quiero consultar preguntas frecuentes. | Should | RF-015 |
| HU-027 | Como cliente, quiero modificar mi reserva. | Should | RF-014 |
| HU-028 | Como administrador, quiero crear reservas manuales. | Should | RF-028 |
| HU-029 | Como administrador, quiero editar las plantillas de correo. | Should | RF-027 |
| HU-030 | Como cliente, quiero pagar un depósito y el saldo después. | Should | Decisión del Director (ver P-007) |
| HU-031 | Como cliente o empresa, quiero una factura automática. | Should | Decisión del Director (ver P-007) |
| HU-032 | Como cliente, quiero tener cuenta de usuario. | Could | RF-012 |
| HU-033 | Como administrador, quiero informes y registro de auditoría. | Could | RF-029 |
| HU-034 | Como administrador, quiero roles adicionales. | Could | RF-030 |
| HU-035 | Como administrador, quiero un centro de avisos completo. | Could | RF-026 |
| HU-036 | Como cliente, quiero devolver el camper en otra sede con suplemento. | Could | Decisión del Director |

---

## Criterios de aceptación

**Reconciliación pendiente.** Los títulos de CA-001 a CA-014 vienen del Analista de Negocio. No tengo su redacción literal; la que sigue es mi formulación verificable alineada con esos títulos. El Director debe reconciliarla con el análisis original antes de consolidar. CA-015 en adelante son nuevos.

**CA-001 Disponibilidad (RF-003)**
- Dado que un camper tiene una reserva confirmada o un bloqueo en un rango de fechas,
- Cuando un cliente busca fechas que se solapan con ese rango,
- Entonces el camper no aparece como reservable para esas fechas.

**CA-002 Sin solapes (RN-003)**
- Dado que existe una reserva o bloqueo para un camper,
- Cuando se intenta crear otra reserva o bloqueo (web o panel) que se solapa,
- Entonces el sistema lo rechaza e informa del conflicto.

**CA-003 Concurrencia (RNF-007)**
- Dado que dos clientes intentan reservar a la vez el mismo camper en el mismo rango,
- Cuando ambos inician la reserva,
- Entonces solo uno obtiene el bloqueo y el otro recibe un aviso claro, sin doble reserva.

**CA-004 Confirmación solo por la pasarela (RN-023)**
- Dado que el cliente vuelve a la web tras pagar,
- Cuando el servidor aún no ha recibido la notificación de la pasarela,
- Entonces la reserva no figura como confirmada. Se confirma solo al recibir la notificación válida.

**CA-005 Expiración (RF-032, RN-015)**
- Dado que una reserva no ha sido pagada,
- Cuando vence el tiempo de bloqueo configurado,
- Entonces la reserva pasa a estado expirada y las fechas quedan libres.

**CA-006 Reintento de pago**
- Dado que un pago es rechazado o abandonado,
- Cuando el bloqueo sigue vigente,
- Entonces el cliente puede reintentar sin duplicar la reserva.

**CA-007 Pago tardío (RN-015)**
- Dado que llega la confirmación de un pago de una reserva ya expirada,
- Cuando las fechas siguen libres,
- Entonces la reserva se confirma.
- Cuando las fechas ya no están libres,
- Entonces se reembolsa el pago y se avisa al cliente y al administrador.

**CA-008 Cancelación con reembolso (RF-013)**
- Dado que existe una reserva confirmada y una política de cancelación configurada,
- Cuando el cliente cancela,
- Entonces se calcula el reembolso según la política vigente en el momento de la cancelación, se ordena el reembolso y la reserva queda cancelada con las fechas liberadas.
- Los valores de la política están por validar (P-001).

**CA-009 Validación de fechas**
- Dado un formulario de búsqueda o reserva,
- Cuando las fechas son pasadas, la devolución es anterior a la recogida o no se cumple el mínimo de noches,
- Entonces se muestra un mensaje claro y no se continúa.

**CA-010 Consentimiento obligatorio (RN-026)**
- Dado el paso previo al pago,
- Cuando el cliente no ha aceptado las condiciones y la política de privacidad,
- Entonces no puede pagar.
- Cuando las acepta,
- Entonces se registra la versión y la fecha de lo aceptado.

**CA-011 Configuración sin código (RN-001, RNF-010, RNF-013)**
- Dado un administrador autenticado,
- Cuando da de alta o edita un camper, una sede, una tarifa o una imagen,
- Entonces los cambios se reflejan en la web sin intervención técnica.

**CA-012 Precios congelados (RN-010)**
- Dado una reserva creada con un precio,
- Cuando el administrador cambia después las tarifas,
- Entonces la reserva existente conserva su precio y desglose originales.

**CA-013 Aislamiento (RN-025)**
- Dado un código de reserva y un email,
- Cuando no coinciden, o un cliente intenta acceder a otra reserva,
- Entonces no se muestra ningún dato ni se confirma que la reserva exista.

**CA-014 Rendimiento móvil (RNF-001, recomendación)**
- Dado un dispositivo móvil en condiciones de prueba a definir,
- Cuando se mide la página de inicio, la búsqueda, la ficha de camper y el pago,
- Entonces se aspira a LCP ≤ 2,5 s, INP ≤ 200 ms y CLS ≤ 0,1.
- Verificación sujeta a un protocolo de medición pendiente (P-012).

**CA-015 Búsqueda (RF-002)**
- Dado que se indican sede y fechas válidas,
- Cuando se busca,
- Entonces se listan solo los campers disponibles, con el precio total del periodo.

**CA-016 Ficha (RF-001)**
- Dado un camper activo,
- Cuando el cliente abre su ficha,
- Entonces ve las características, imágenes, sede y condiciones configuradas.
- Un camper desactivado no aparece.

**CA-017 Desglose de precio (RF-004)**
- Dado una selección de camper y fechas,
- Cuando el cliente llega al resumen,
- Entonces ve un desglose coherente con las tarifas y temporadas configuradas y el total que se cobrará.
- El tratamiento de IVA está pendiente de validación legal (P-005).

**CA-018 Datos del conductor (RF-006)**
- Dado el formulario de reserva,
- Cuando faltan datos obligatorios del conductor principal o este no cumple la edad mínima declarada configurada,
- Entonces no se puede continuar y el motivo se explica.

**CA-019 Correo y justificante (RF-010, RN-027)**
- Dado que una reserva se confirma,
- Cuando el servidor procesa la confirmación,
- Entonces el cliente recibe un correo con el código de reserva y el justificante de pago.

**CA-020 Consulta de reserva (RF-011, RF-012)**
- Dado un código de reserva y un email correctos,
- Cuando el cliente los introduce,
- Entonces ve el estado, el detalle y el justificante, y puede cancelar si procede.

**CA-021 Acceso al panel (RF-019)**
- Dado un usuario sin autenticar,
- Cuando intenta abrir una pantalla del panel,
- Entonces se le pide autenticación y no se muestra contenido.
- Con credenciales válidas accede al panel.

**CA-022 Gestión de reservas (RF-023)**
- Dado que existen reservas,
- Cuando el administrador las lista, filtra o abre el detalle,
- Entonces ve el cliente, camper, fechas, importes y estados de reserva y de pago.
- Puede cancelar una reserva conforme a las reglas.

**CA-023 Bloqueo manual (RF-024)**
- Dado un camper sin reservas en un rango,
- Cuando el administrador crea un bloqueo,
- Entonces el camper deja de estar disponible en ese rango.
- Si el rango tiene reservas, se rechaza (CA-002).

**CA-024 Pagos y reembolsos (RF-025, RNF-009)**
- Dado una reserva con pago,
- Cuando el administrador emite o consulta un reembolso,
- Entonces el estado del pago se actualiza y los eventos de pago quedan registrados.

**CA-025 Aviso al administrador (RF-026)**
- Dado una reserva nueva, una cancelación o un pago tardío sin disponibilidad,
- Cuando ocurre el evento,
- Entonces se envía un correo a la dirección configurada.

**CA-026 Cookies (RF-017)**
- Dado un primer acceso,
- Cuando el visitante no ha decidido,
- Entonces ve el banner y no se activan cookies no necesarias hasta que acepte.
- Su decisión se respeta y puede cambiarse.
- El detalle legal está pendiente (P-005).

**CA-027 Páginas legales (RF-016)**
- Dado cualquier página y el paso de reserva,
- Cuando el visitante busca la información legal,
- Entonces encuentra los enlaces a las páginas legales y a la política de cancelación.
- El texto debe validarse legalmente (P-005).

**CA-028 SEO técnico (RF-018)**
- Dado que existen páginas públicas,
- Cuando se revisan,
- Entonces tienen URL limpia, metadatos propios, sitemap y datos estructurados donde aplique.
- No se garantiza posicionamiento (RNF-002).

**CA-029 Contacto (RF-015)**
- Dado un visitante,
- Cuando busca cómo contactar,
- Entonces encuentra los datos o formulario de contacto configurados.

**CA-030 Responsive y accesibilidad (RNF-003, RNF-004, RNF-005)**
- Dado el flujo completo de reserva,
- Cuando se usa en móvil, tableta y ordenador, y con teclado,
- Entonces es utilizable en todos y se revisa contra WCAG 2.1 AA como objetivo.
- El alcance de la revisión de accesibilidad está pendiente.

**CA-031 Sin datos de tarjeta (RNF-006)**
- Dado el pago,
- Cuando el cliente introduce su tarjeta,
- Entonces los datos los procesa la pasarela y la web no los almacena.

**CA-032 Estados coherentes (RN-021, RN-022)**
- Dado el ciclo de vida de una reserva y su pago,
- Cuando cambia un estado,
- Entonces solo se permiten las transiciones previstas y se muestran igual en el cliente y en el panel.

**CA-033 Misma sede (decisión del Director)**
- Dado una reserva en el MVP,
- Cuando se selecciona la sede,
- Entonces la recogida y la devolución son en esa misma sede.

**CA-034 Temporadas y mínimo de noches (RF-022)**
- Dado tarifas, temporadas y mínimo de noches configurados,
- Cuando el cliente elige fechas que cruzan temporadas o no cumplen el mínimo,
- Entonces el precio aplica las tarifas correctas por noche y se bloquea el mínimo no cumplido.

---

## Dependencias funcionales

- **[S]** Las historias dependen de la alta de flota, sedes y tarifas (HU-018, HU-019, HU-020) antes de que la búsqueda y la reserva sean comprobables.
- **Cadena principal:** HU-002/003 → HU-004 → HU-005 → HU-006 → HU-007/008 → HU-010. HU-009 depende de HU-006 y HU-008. HU-011 y HU-012 dependen de HU-008 y HU-010.
- **Cancelación:** HU-012 y HU-023 dependen de la política de cancelación (P-001) y de HU-008.
- **Panel:** HU-021 a HU-024 dependen de HU-017.
- **Bloqueo manual:** HU-022 comparte la regla de no solapes con HU-003 y HU-006.
- **Externas [P]:** cuenta de comercio con la pasarela, textos legales, remitente y dominio de correo, y datos iniciales de flota y tarifas.
- **Fase 2:** HU-030 y HU-031 requieren decisiones previas de cobro y facturación (P-007).

---

## Métricas de éxito propuestas

Todas son **[R]**. No se fijan metas numéricas, porque no hay datos de partida ni confirmación del cliente (P-013).

- Reservas pagadas completadas frente a búsquedas iniciadas.
- Abandono entre el inicio del pago y la confirmación.
- Reservas dobles o solapadas: la expectativa es cero.
- Reservas expiradas y pagos tardíos reembolsados.
- Contactos recibidos por dudas sobre el estado de una reserva.
- Tiempo que tarda un administrador en dar de alta un camper o cambiar una tarifa.
- Indicadores Core Web Vitals en móvil frente a RNF-001.
- Entrega correcta de los correos de confirmación.

## Segunda fase

Es **[R]**, con prioridad **Should** y después **Could**, según la tabla de priorización.

- Primera ola (Should): extras, FAQ, modificación de reserva, reservas manuales, plantillas de correo editables, depósito+saldo diferido, factura automática y clientes empresa.
- Segunda ola (Could): cuentas de cliente, informes y auditoría, roles adicionales, centro de avisos completo, otra sede de devolución con suplemento.

## Ampliaciones (Won't por ahora)

Todas son **[R]** y fuera del alcance actual. Cualquier ampliación entraría como solicitud de cambio.
- Fianza en línea.
- Otros medios de pago.
- Multi-idioma.
- Cupones.
- Reseñas.
- Documentos del conductor.
- Contrato digital.
- Sincronización de canales.

## Exclusiones

- **[C]** Integraciones con sistemas existentes y migración de datos.
- **[C]** Presupuesto y fechas, fuera de este reporte.
- **[R]** Lo no confirmado en el apartado "Fuera del MVP" no está comprometido.

---

## Riesgos de producto

| ID | Riesgo | Mitigación [R] |
|---|---|---|
| R-001 | Las políticas de pago, cancelación y precios no se validan a tiempo | Valores de ejemplo "por validar", configurables, y validación del cliente antes de publicar |
| R-002 | Textos legales o cumplimiento sin revisar (RGPD, cookies, precontractual, desistimiento, IVA, PSD2) | Revisión por asesoría legal antes de salir. Esto no es asesoramiento legal |
| R-003 | Sin alta manual de reservas en el MVP, la reserva telefónica depende del bloqueo manual | Comunicar la limitación. Valorar RF-028 como primera ola de Fase 2 |
| R-004 | Sin cuentas de usuario, el cliente depende del código: si lo pierde, tiene que contactar | Reenvío del correo de confirmación y contacto visible |
| R-005 | Pago total al reservar puede aumentar el abandono frente a depósito | Medir abandono. Depósito+saldo diferido en Fase 2 |
| R-006 | Reembolsos automáticos con política mal configurada | Valores por validar, pruebas de los casos de la política antes de salir |
| R-007 | Expectativas de SEO y velocidad más altas que lo prometido | Comunicar que el SEO es técnico y sin garantía (RNF-002) y que las métricas son objetivo |
| R-008 | Imágenes de ejemplo en producción | Marcar su sustitución como tarea previa a la publicación |
| R-009 | Desactivar un camper con reservas futuras, regla sin definir | Ver P-011 |
| R-010 | Pago tardío o fallo de notificación de la pasarela genera estados inconsistentes | CA-004, CA-007 y trazabilidad de eventos (RNF-009) |

---

## Decisiones pendientes

**Para el cliente, vía Director [P]:**
- **P-001:** valores de la política de cancelación escalonada, quién asume las comisiones de la pasarela en reembolsos y regla cuando cancela la empresa.
- **P-002:** confirmar pago total al reservar y fianza informativa (importe y texto a mostrar).
- **P-003:** tiempo de bloqueo temporal (15 min es solo una propuesta).
- **P-004:** confirmar que la cancelación por el cliente con reembolso automático entra en el MVP. Si se quisiera reducir, la alternativa sería cancelación solo por el administrador (HU-021, HU-023).
- **P-005:** validación legal de privacidad, cookies, información precontractual, desistimiento, IVA y su presentación en precios, PSD2/SCA, facturación y seguros o licencias.
- **P-006:** edad mínima del conductor y requisitos de permiso.
- **P-007:** clasificación de saldo diferido y factura automática. El análisis (RF-031) los lista como ampliaciones y el Director los sitúa en Fase 2. Hay una contradicción que debe resolverse. Aquí quedan en Fase 2 provisionalmente.
- **P-008:** justificante frente a factura (RN-027) y obligaciones de facturación.
- **P-009:** si los extras se necesitan en la salida inicial. Esto movería RF-005 al MVP y ampliaría el alcance, por lo que sería una solicitud de cambio.
- **P-010:** definición de "noche" frente a "día", horas de recogida y devolución, y zona horaria aplicable, relevante si hay sedes en Canarias.
- **P-011:** regla al desactivar un camper o sede con reservas futuras.
- **P-012:** protocolo de medición del rendimiento y alcance de la revisión de accesibilidad.
- **P-013:** metas numéricas de las métricas y valores de disponibilidad y escalabilidad (RNF-011, RNF-012).
- **P-014:** titularidad de la cuenta de la pasarela, del dominio y del remitente de correo.
- **P-015:** si, siendo solo en español, se acepta el alcance de público extranjero para el SEO.
- **P-016:** antelación mínima y máxima de reserva, si aplica.

## Escalaciones al Director (reglas del contrato)

- **Prioridad no decidida:** P-004, P-007 y P-009.
- **Dependencia funcional abierta:** P-001, P-005, P-014 (pasarela, legales, política). Bloquean la salida a producción, no la planificación.
- **MVP viable:** sí. El MVP propuesto resuelve el problema principal de extremo a extremo (HU-002 a HU-012 más administración). No obstante, no puede ponerse en producción sin P-001, P-005 y P-014.
- **Criterios de completitud:** CA-001 a CA-034 son verificables. CA-014 y CA-030 quedan condicionados a P-012.
- **Aprobación:** no apruebo el alcance. Esto queda a decisión del Director y del cliente, y cualquier cambio posterior se registra como CR-001 en adelante.
