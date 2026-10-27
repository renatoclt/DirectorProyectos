# Requisitos y análisis de negocio: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fase:** DISCOVERY en borrador. GATE-001 y la puerta DISCOVERY → DESIGN están PENDING (ver [APPROVALS](../00-control/APPROVALS.md)).  
> **Fuente:** Reporte del agente Analista de Negocio, entregado por el Director de Proyectos. Archivo de origen: `C:\Users\User\AppData\Local\Temp\1793039049995-copilot-tool-output-474cacf2ca9f466da1d1527e7996fdb1.txt`. Resultado declarado por la fuente: **COMPLETADO_CON_PENDIENTES**.  
> **Decisiones pendientes:** [DECISIONS](../00-control/DECISIONS.md) §3 y [REQUIREMENTS](../00-control/REQUIREMENTS.md) §6.  
> **Aprobación:** ninguna. Este documento no aprueba contenido ni alcance.

## Notas del Gestor de Documentación (no forman parte de la fuente)

- Debajo de la línea `---` final de esta nota se reproduce **sin cambios de significado** el contenido del Analista de Negocio. No se han alterado identificadores (RF, RNF, RN, CA, R, VAL, Q).
- Este documento presenta discrepancias con [mvp-and-backlog.md](../02-product/mvp-and-backlog.md). No se resuelven aquí. Quedan registradas como ISS-001 a ISS-014 en [RISKS](../00-control/RISKS.md) §2. Las propuestas pendientes de decisión están en [DECISIONS](../00-control/DECISIONS.md).
- Los identificadores R-001 a R-013 de este documento colisionan con los R-001 a R-010 del Product Manager (ISS-003).
- Enlaces: [Resumen del cliente](../00-intake/client-brief.md) · [Estado del proyecto](../00-control/PROJECT-STATE.md) · [Trazabilidad](../00-control/TRACEABILITY.md).

---

# Reporte de agente

- **Agente:** Analista de Negocio
- **Objetivo:** Convertir la idea del cliente y sus respuestas en requisitos, reglas, validaciones, criterios de aceptación y preguntas abiertas para el proyecto de alquiler de campers en España.
- **Contrato aplicado:** `governance/contracts/analista-negocio.contract.json`. Fase DISCOVERY, solo lectura y búsqueda. No hay conflicto: no se editó nada, no se programó, no se aprobó nada y no se habló con el cliente.
- **Elementos relacionados:** Escenario AN-001 (pagos y sedes marcados como pendientes o configurables, sin inventar). Identificadores generados: RF-001 a RF-032, RNF-001 a RNF-014, RN-001 a RN-027, CA-001 a CA-014, R-001 a R-013, VAL-001 a VAL-022.
- **Tareas realizadas:**
  - Análisis del contexto recibido.
  - Revisión de reglas corporativas, contrato y plantilla de reporte.
  - Comprobación de que `projects/` solo contiene `.gitkeep`, es decir, no hay documentación previa del producto.
- **Archivos consultados:**
  - `.github/copilot-instructions.md`
  - `governance/contracts/analista-negocio.contract.json`
  - `testing/scenarios/analista-negocio/an-001-no-inventar.json`
  - Extractos de `templates/agent-report.md` y `.github/instructions/project-governance.instructions.md` (vía búsqueda)
  - Listado de `projects/`
- **Archivos modificados:** Ninguno.
- **Comandos o pruebas ejecutadas:** Ninguna. No se ejecutaron pruebas.
- **Evidencia:** Solo el contexto del Director y las reglas citadas. No existe repositorio ni sistema actual del cliente que inspeccionar.

**Leyenda de estado:** **[C]** Confirmado · **[S]** Supuesto (pendiente de confirmar) · **[R]** Recomendación del equipo (pendiente de confirmar) · **[P]** Pendiente.

---

## 1. Resumen del problema

El negocio de alquiler de campers en España necesita una web completa que permita reservar en línea, pagar con seguridad y gestionar los alquileres sin intermediación manual.

- **[C]** Debe tener un sistema robusto de reservas con selección de fechas, disponibilidad y gestión de alquileres por el usuario.
- **[C]** Debe integrar una pasarela de pago segura.
- **[C]** Debe estar optimizada en experiencia de usuario, velocidad y SEO.
- **[C]** La flota y las sedes son configurables desde un panel.
- **[P]** Se desconoce el proceso manual actual del cliente, el tamaño de la flota y el volumen esperado.

## 2. Objetivos del negocio

| Objetivo | Estado |
|---|---|
| Vender reservas 24/7 sin gestión manual | [C] (implícito en "reservas en línea") |
| Cobrar de forma segura en el momento de reservar | [C] |
| Evitar dobles reservas y errores de disponibilidad | [C] ("robusto") / reglas detalladas [R] |
| Ser administrable por la empresa sin desarrollo (flota, sedes, tarifas) | [C] |
| Captar tráfico orgánico | [C] |
| Cumplir normativa española aplicable | [R]: validar con asesoría legal |
| Métricas de éxito (conversión, ocupación, ingresos) | [P] no informadas; no se inventan |

## 3. Actores y responsabilidades

| Actor | Responsabilidad | Estado |
|---|---|---|
| Visitante / cliente particular | Buscar, reservar, pagar, consultar y cancelar su reserva | [C] usuario / [S] particular |
| Administrador de la empresa | Gestiona flota, sedes, tarifas, extras, reservas, pagos y reembolsos | [S] al menos 1 rol |
| Operador / personal de sede | Consulta reservas del día, entrega y recogida | [R] Fase 2 |
| Pasarela de pago | Procesa cobros, autenticación reforzada y reembolsos | [C] (proveedor [P]) |
| Servicio de correo transaccional | Envía confirmaciones y avisos | [R] |
| Asesoría legal / fiscal de la empresa | Valida textos legales, IVA y facturación | [R] |

## 4. Proceso actual

**[P]** No hay información. El Director lo confirmó: no existen sistemas previos que integrar ni datos que migrar. Se desconoce cómo gestiona hoy el cliente consultas, reservas y cobros.

## 5. Proceso propuesto

El flujo es una **[R]** salvo que se indique otra cosa.

1. El cliente elige fechas de recogida y devolución, y sede si hay varias.
2. El sistema muestra los campers disponibles con precio total desglosado.
3. El cliente elige vehículo y extras, y ve el resumen con las políticas de pago y cancelación.
4. El cliente introduce los datos del conductor principal y acepta condiciones y privacidad.
5. El sistema bloquea las fechas temporalmente y redirige al pago con autenticación reforzada.
6. La pasarela confirma el pago al servidor. La reserva pasa a Confirmada y se envían los correos.
7. El cliente consulta, y si procede cancela, su reserva. El administrador la gestiona desde el panel.
8. Las reservas no pagadas expiran y liberan las fechas.

## 6. Requisitos funcionales

Prioridad: **MVP**, **F2** (Fase 2) o **AMP** (Ampliación).

### Cliente

| ID | Requisito | Prior. | Estado |
|---|---|---|---|
| RF-001 | Catálogo de campers con ficha (descripción, plazas, equipamiento, fotos, precio orientativo). Las fotos serán de ejemplo hasta que existan reales | MVP | Necesidad [C]; contenido de ficha [R]; fotos reales [P] |
| RF-002 | Búsqueda por fechas de recogida y devolución, y por sede cuando haya varias | MVP | [C] fechas; sede [C] por flota/sedes configurables |
| RF-003 | Visualización de disponibilidad por vehículo y fechas, validada en servidor | MVP | [C] |
| RF-004 | Cálculo y desglose de precio (tarifa por noche, temporadas, extras, impuestos, fianza informativa) antes de pagar | MVP | [R] |
| RF-005 | Selección de extras opcionales configurables | MVP | [R] |
| RF-006 | Flujo de reserva: datos del conductor principal, resumen, aceptación de condiciones y pago | MVP | [R] |
| RF-007 | Bloqueo temporal de fechas durante el pago | MVP | [R] |
| RF-008 | Pago en línea mediante pasarela segura | MVP | Necesidad [C]; proveedor [P]; con tarjeta [S] |
| RF-009 | Autenticación reforzada del pago (3-D Secure/SCA) gestionada por la pasarela | MVP | [R]: validar PSD2 |
| RF-010 | Confirmación en pantalla y correos transaccionales (ver RN-018) | MVP | [R] |
| RF-011 | Gestión de la reserva por el cliente: consultar estado, detalle y justificante | MVP | [C] ("gestionar sus alquileres") |
| RF-012 | Acceso a la reserva mediante cuenta de cliente **o** código de reserva + email | MVP | [S] |
| RF-013 | Cancelación por el cliente con cálculo automático de reembolso según política | MVP | [R] |
| RF-014 | Modificación de fechas, vehículo o extras por el cliente | F2 | [R] |
| RF-015 | Formulario de contacto y página de preguntas frecuentes | MVP | [R] |
| RF-016 | Páginas legales: aviso legal, privacidad, cookies, condiciones de alquiler | MVP | [R]: contenido a validar con asesoría legal |
| RF-017 | Banner de consentimiento de cookies con categorías | MVP | [R]: validar LSSI-CE |
| RF-018 | Datos y páginas indexables para SEO: URLs limpias, metadatos, sitemap, datos estructurados, páginas por vehículo y sede | MVP | [C] SEO |

### Administración

| ID | Requisito | Prior. | Estado |
|---|---|---|---|
| RF-019 | Panel de administración con acceso autenticado por rol | MVP | [S] |
| RF-020 | Gestión de flota: alta, edición, desactivación, fotos, equipamiento, plazas, fianza, sede base | MVP | [C] configurable |
| RF-021 | Gestión de sedes: alta, edición, desactivación, horarios y contacto | MVP | [C] configurable |
| RF-022 | Gestión de tarifas, temporadas, mínimos de noches y extras | MVP | [C] configurable / detalle [R] |
| RF-023 | Gestión de reservas: listar, filtrar, ver detalle, cancelar y anotar | MVP | [R] |
| RF-024 | Bloqueo manual de fechas de un vehículo (mantenimiento, uso propio) | MVP | [R] |
| RF-025 | Gestión de pagos: ver transacciones y emitir reembolsos totales o parciales | MVP | [R] |
| RF-026 | Aviso interno al administrador por nueva reserva o cancelación | MVP | [R] |
| RF-027 | Edición de plantillas de correo y de textos de políticas con versionado | F2 | [R] |
| RF-028 | Creación manual de reservas (por teléfono o mostrador) | F2 | [R] |
| RF-029 | Informes básicos (reservas, ocupación, ingresos) y registro de auditoría de cambios en el panel | F2 | [R] |
| RF-030 | Roles adicionales (operador de sede) | F2 | [R] |

### Ampliaciones

| ID | Requisito | Prior. | Estado |
|---|---|---|---|
| RF-031 | Preautorización de fianza en línea, saldo de pago diferido con recordatorios, factura automática, otros medios de pago, multi-idioma, cupones, reseñas, subida de documentos del conductor, contrato digital con firma, sincronización con canales externos | AMP | [P] solo si el cliente lo decide |
| RF-032 | Expiración automática de reservas impagadas y liberación de fechas (RN-015) | MVP | [R] |

## 7. Reglas de negocio

**Reglas base**

| ID | Regla | Estado |
|---|---|---|
| RN-001 | Flota y sedes son datos configurables desde el panel. No se fijan cifras en el sistema | [C] |
| RN-002 | Una reserva = 1 vehículo + rango de fechas + sede de recogida y de devolución | [S] |
| RN-003 | Un vehículo no puede tener dos reservas confirmadas o bloqueadas solapadas, ni solaparse con un bloqueo manual | [R] derivada de "robusto" [C] |
| RN-004 | El alquiler se calcula por noches (de la fecha de recogida a la de devolución). Se admite tiempo de preparación entre reservas, configurable (valor [P]) | [R] |
| RN-005 | Moneda EUR, idioma español, zona horaria Europe/Madrid | [S] |
| RN-006 | Recogida y devolución en distinta sede: no se asume | [P] (pregunta Q6) |

**Precios**

| ID | Regla | Estado |
|---|---|---|
| RN-007 | Precio por noche por vehículo, variable por temporada. Las temporadas son rangos de fechas configurables sin solapes | [R] |
| RN-008 | Mínimo de noches configurable por temporada. Los valores los fija el cliente (un ejemplo ilustrativo sería menos noches en temporada baja que en alta) | [R] / valores [P] |
| RN-009 | Antelación mínima y duración máxima de reserva configurables | [R] / valores [P] |
| RN-010 | El precio se calcula siempre en servidor y se congela al crear la reserva. Cambios posteriores de tarifa no afectan a reservas existentes | [R] |
| RN-011 | Se muestra precio final con impuestos y desglose (alquiler, extras, fianza). Tratamiento de IVA a validar con asesoría | [R] / validar legal |
| RN-012 | Extras: precio fijo por reserva o por noche, con stock opcional. Los precios los define la empresa | [R] |

**Política de pago, cancelación y fianza**

| ID | Regla | Estado |
|---|---|---|
| RN-013 | **Pago:** opción recomendada: depósito (% a definir) al reservar y saldo hasta una fecha límite configurable. Si la recogida está dentro de ese plazo, pago total. Alternativa más simple: pago total al reservar. Impacto: el depósito exige segundo cobro, recordatorios y estado de pago parcial | [R]: decisión Q1 |
| RN-014 | **Cancelación por el cliente:** reembolso escalonado por antelación (tramos y porcentajes a definir). La reserva se cancela al instante y el reembolso se calcula según la política vigente al reservar | [R] / valores [P] |
| RN-015 | **Reservas impagadas:** una reserva en Pendiente de pago expira al terminar el bloqueo y libera las fechas. Si llega un pago tras expirar, se confirma solo si las fechas siguen libres. Si no, se reembolsa y se avisa al cliente | [R] |
| RN-016 | **Bloqueo temporal:** el bloqueo durante el pago dura un tiempo configurable. Se propone 15 min como valor inicial, no confirmado | [R] |
| RN-017 | **Fianza:** importe configurable por vehículo, mostrado antes de pagar. En el MVP se gestiona en la entrega (no se cobra en la web) | [R]: decisión Q2 |
| RN-018 | **Correos transaccionales (mínimo):** reserva iniciada con enlace de pago si procede, pago recibido y reserva confirmada, pago fallido, reserva expirada, cancelación y reembolso, recordatorio previo a la recogida, aviso interno al administrador | [R] |
| RN-019 | **Cancelación por la empresa** (avería, imposibilidad): reembolso total o alternativa de vehículo, con aviso inmediato | [R] |
| RN-020 | **No presentación** y **devolución tardía:** condiciones y penalizaciones a definir en las condiciones de alquiler | [P] |

**Estados**

| ID | Regla | Estado |
|---|---|---|
| RN-021 | **Estados de reserva:** Pendiente de pago (bloqueada) → Confirmada → En curso → Completada. Salidas: Expirada, Cancelada por cliente, Cancelada por empresa, No presentada | [R] |
| RN-022 | **Estados de pago:** Pendiente, Pagado, Parcialmente pagado (solo si hay depósito), Fallido, Reembolsado parcialmente, Reembolsado totalmente. Disputa/contracargo queda para Fase 2 | [R] |
| RN-023 | Una reserva solo pasa a Confirmada cuando el servidor recibe la confirmación del pago desde la pasarela. La redirección del navegador no basta | [R] |

**Conductor, acceso y datos**

| ID | Regla | Estado |
|---|---|---|
| RN-024 | **Conductor:** edad mínima, antigüedad y tipo de permiso (puede depender del peso del vehículo), conductores adicionales y verificación de documentos. No se fija ningún valor | [P]: Q5 y validación legal |
| RN-025 | **Acceso:** el cliente solo ve sus reservas. El acceso por código requiere un segundo dato (email) y el código no debe ser adivinable | [R] |
| RN-026 | **Datos personales y consentimientos:** solo datos necesarios, con registro de fecha y versión de condiciones y privacidad aceptadas. Marketing opcional, aparte y no premarcado | [R]: validar RGPD/LOPDGDD |
| RN-027 | **Facturación:** se emite justificante de pago al cobrar. La factura formal según normativa se define con asesoría | [P]: Q4 y validar legal |

### Puntos para validación legal

Esto no es asesoramiento jurídico ni requisito confirmado.

- **Protección de datos (RGPD/LOPDGDD):** base legal, información al usuario, encargados de tratamiento (pasarela, hosting, correo), plazos de conservación, derechos de las personas.
- **Cookies y servicios de la sociedad de la información (LSSI-CE):** consentimiento previo para cookies no técnicas, aviso legal con datos del prestador, comunicaciones comerciales.
- **Consumidores:** información precontractual, condiciones generales, precio final con impuestos, confirmación en soporte duradero, y si procede o no desistimiento en alquileres con fecha concreta.
- **IVA** aplicable al alquiler y a los extras.
- **Pagos (PSD2/SCA):** que la pasarela elegida cumpla la autenticación reforzada.
- **Facturación:** requisitos de factura y de sistemas de facturación, si aplican.
- **Otros:** seguro y responsabilidad del vehículo, accesibilidad web si aplica, y licencias o autorizaciones de la actividad.

## 8. Validaciones

El prefijo VAL es local de este reporte y no está en el catálogo corporativo de identificadores. El Director decide si lo registra. Todas son **[R]**, salvo los valores que dependen de decisiones **[P]**.

**Fechas y disponibilidad**

- **VAL-001:** Las fechas deben ser reales (no 31/02), en formato dd/mm/aaaa y con zona horaria Europe/Madrid.
- **VAL-002:** La recogida no puede ser anterior a hoy más la antelación mínima (RN-009).
- **VAL-003:** La devolución debe ser posterior a la recogida.
- **VAL-004:** La duración debe estar entre el mínimo de noches de la temporada (RN-008) y la duración máxima (RN-009).
- **VAL-005:** El rango no puede solaparse con reservas ni con bloqueos.
- **VAL-006:** Las horas de recogida y devolución deben estar dentro del horario de la sede.
- **VAL-007:** La disponibilidad se revalida en servidor al buscar, al resumir, al iniciar el pago y al confirmar.

**Formularios del cliente**

- **VAL-008:** Nombre y apellidos obligatorios, con límite de longitud y saneamiento de entrada.
- **VAL-009:** Email con formato válido y doble introducción o verificación.
- **VAL-010:** Teléfono con formato internacional (admite +34).
- **VAL-011:** Edad mínima del conductor según fecha de nacimiento (valor [P], RN-024).
- **VAL-012:** Documento de identidad: solo si se decide pedirlo en la web (Q5).
- **VAL-013:** El número de ocupantes no puede superar las plazas del vehículo.
- **VAL-014:** La aceptación de condiciones y privacidad es obligatoria, con casilla no premarcada. El marketing es opcional y aparte.
- **VAL-015:** La cantidad de extras debe ser mayor o igual a 0 y no superar su stock.
- **VAL-016:** Protección antispam y límite de intentos en formularios y acceso por código.

**Pago**

- **VAL-017:** El importe lo calcula el servidor, nunca el navegador. Moneda EUR.
- **VAL-018:** Se verifica la autenticidad de las notificaciones de la pasarela, y se procesan de forma idempotente (sin duplicar efectos).
- **VAL-019:** Los reintentos de pago solo se permiten mientras dure el bloqueo.

**Panel**

- **VAL-020:** Las temporadas no se solapan. Precios mayores o iguales a 0. Mínimo de noches mayor o igual a 1.
- **VAL-021:** No se elimina una sede o vehículo con reservas futuras. Se desactiva y se avisa del impacto.
- **VAL-022:** Alta de vehículo con campos obligatorios y validación de formato y peso de imágenes.

## 9. Excepciones y casos alternativos

- **Pago rechazado o autenticación fallida:** se permite reintento dentro del bloqueo. Después la reserva expira.
- **Abandono del pago o cierre del navegador:** el bloqueo expira y se liberan las fechas.
- **Pago recibido tras expirar:** ver RN-015.
- **Dos usuarios en las mismas fechas:** gana la primera reserva bloqueada. El segundo recibe aviso y alternativas.
- **Pasarela caída o notificación retrasada:** no se confirma hasta recibir el pago. Se muestra estado "en verificación".
- **Correo no entregado:** el cliente puede consultar la reserva en la web y el administrador puede reenviarlo.
- **Avería de un vehículo tras confirmar:** RN-019.
- **Reembolso fallido:** queda marcado para gestión manual del administrador.
- **Rango que cruza temporadas:** el precio se calcula por noche según su temporada.
- **Sin disponibilidad para las fechas:** se informa y se sugieren otros vehículos o fechas cercanas. Las sugerencias automáticas pueden ir a Fase 2 [R].
- **Solicitud de acceso o supresión de datos (RGPD):** procedimiento a validar con asesoría, respetando obligaciones de conservación.
- **Contracargo:** gestión manual en el MVP.
- **Cliente sin acceso a su email:** [P].

## 10. Información y entidades necesarias

- **Vehículo:** modelo, plazas, equipamiento, fotos, estado, sede base, fianza.
- **Sede:** dirección, horarios, contacto, estado.
- **Temporada y tarifa.**
- **Extra.**
- **Reserva y líneas de reserva.**
- **Cliente y conductor.**
- **Pago, reembolso y transacción.**
- **Bloqueo de fechas:** temporal por pago o manual por mantenimiento.
- **Políticas con versión:** pago, cancelación y condiciones.
- **Consentimientos y aceptaciones.**
- **Usuario administrador y rol.**
- **Plantillas de correo.**
- **Registro de eventos de pago y auditoría.**

## 11. Integraciones

| Integración | Estado |
|---|---|
| Pasarela de pago segura | [C] necesidad; proveedor y medios distintos de tarjeta [P]; tarjeta [S] |
| Sistemas existentes y migración de datos | [C] no hay, y no se incluyen |
| Servicio de correo transaccional | [R] |
| Analítica web, activada solo con consentimiento | [R] |
| Mapa de ubicación de sedes | [R] (opcional) |
| Sistema de facturación externo | [P] (depende de Q4) |

## 12. Requisitos no funcionales preliminares

| ID | Requisito | Estado |
|---|---|---|
| RNF-001 | **Rendimiento:** meta recomendada de Core Web Vitals "buenos" en móvil (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1). Imágenes optimizadas y carga diferida | Necesidad [C] ("velocidad"); métricas [R] |
| RNF-002 | **SEO técnico:** HTML indexable, URLs limpias, metadatos, sitemap, datos estructurados, versión móvil. No se garantiza posicionamiento concreto | [C] necesidad / [R] técnicas |
| RNF-003 | **Responsive, mobile-first** y compatibilidad con navegadores modernos | [R] |
| RNF-004 | **Usabilidad:** flujo de reserva corto y claro, con indicación de progreso y mensajes de error comprensibles | [C] "excelente UX" / métrica [R] |
| RNF-005 | **Accesibilidad:** objetivo WCAG 2.1 AA, a validar si es obligatoria | [R] |
| RNF-006 | **Seguridad:** HTTPS, sin almacenar datos de tarjeta (pago alojado o tokenizado en la pasarela), control de acceso por rol, contraseñas protegidas, protección contra vulnerabilidades web habituales, límites de intentos | [C] "pago seguro" / medidas [R] |
| RNF-007 | **Integridad y concurrencia:** operaciones de reserva y pago transaccionales, sin doble reserva | [R] |
| RNF-008 | **Privacidad por diseño:** minimización, retención definida | [R]: validar legal |
| RNF-009 | **Trazabilidad:** registro de eventos de pago y cambios de estado | [R] |
| RNF-010 | **Configurabilidad:** flota, sedes, tarifas y políticas editables sin cambios de código | [C] |
| RNF-011 | **Disponibilidad y copias de seguridad:** objetivos y plazos de recuperación | [P] (no se inventan porcentajes) |
| RNF-012 | **Escalabilidad:** dimensionar según tráfico y reservas esperadas | [P] (no informados) |
| RNF-013 | **Contenido sustituible:** las imágenes de ejemplo deben poder reemplazarse sin desarrollo | [R] |
| RNF-014 | **Fiabilidad de correo:** entregabilidad configurada correctamente | [R] |

## 13. Criterios de aceptación clave

Estos criterios son **[R]** y se validarán con el cliente antes de usarse como base de prueba.

| ID | Criterio | Traza |
|---|---|---|
| CA-001 | Dado un rango con un camper libre, cuando el cliente busca, entonces lo ve disponible con precio total desglosado | RF-002, RF-003, RF-004 |
| CA-002 | Dado un camper reservado o bloqueado en parte del rango, cuando el cliente busca, entonces no aparece disponible | RN-003, VAL-005 |
| CA-003 | Dados dos clientes que intentan reservar el mismo camper y fechas a la vez, entonces solo uno obtiene el bloqueo y el otro recibe aviso | RN-003, RN-016, RNF-007 |
| CA-004 | Dado un pago correcto, entonces la reserva pasa a Confirmada solo tras la notificación de la pasarela y se envían los correos | RN-023, RN-018 |
| CA-005 | Dado un pago no completado, entonces la reserva expira al terminar el bloqueo y las fechas quedan libres | RN-015, RN-016 |
| CA-006 | Dado un pago fallido o una autenticación rechazada, entonces no se confirma y se permite reintento mientras dure el bloqueo | RF-008, RF-009, VAL-019 |
| CA-007 | Dado un pago tras expirar la reserva, entonces se confirma si las fechas siguen libres. Si no, se reembolsa y se avisa | RN-015 |
| CA-008 | Dada una cancelación del cliente, entonces el reembolso corresponde al tramo de la política vigente al reservar | RF-013, RN-014 |
| CA-009 | Dadas fechas inválidas (pasadas, devolución anterior, bajo el mínimo de noches), entonces el sistema las rechaza con mensaje claro | VAL-001 a VAL-004 |
| CA-010 | Dado un cliente sin aceptar condiciones y privacidad, entonces no puede continuar al pago | VAL-014, RN-026 |
| CA-011 | Dado un administrador, cuando crea o edita una sede o un camper, entonces aparece en la web sin cambios de código | RN-001, RF-020, RF-021 |
| CA-012 | Dado un cambio de tarifa, entonces no altera el precio de reservas ya creadas | RN-010 |
| CA-013 | Dado un cliente, entonces no puede ver reservas de otros | RN-025 |
| CA-014 | Dada la medición en móvil, entonces las páginas clave alcanzan los umbrales acordados en RNF-001 | RNF-001 |

## 14. Fuera de alcance

Las exclusiones marcadas **[C]** están confirmadas. Las marcadas **[R]** son recomendaciones del equipo.

- **[C]** Migración de datos e integración con sistemas existentes.
- **[C]** Estimación de presupuesto y fechas (fuera del contrato).
- **[R]** Aplicación móvil nativa y marketplace multi-empresa.
- **[R]** Canales externos de venta (OTA) y GPS o telemática.
- **[R]** Producción de fotografía y vídeo reales.
- **[R]** Asesoramiento jurídico y fiscal: la empresa solo propone y el cliente valida con su asesoría.
- **[R]** Campañas de marketing o SEO continuo, y cualquier garantía de posicionamiento.
- **[R]** Ampliaciones de RF-031 mientras el cliente no las apruebe.

## 15. Supuestos

Todos están pendientes de confirmación **[S]**:

- Idioma español y moneda EUR.
- Una sola empresa.
- Clientes particulares (no empresas con facturación a NIF).
- Pago con tarjeta.
- Cuenta de cliente o acceso por código de reserva.
- Panel con al menos un rol administrador.
- Una reserva = un vehículo.
- Recogida y devolución en la misma sede, hasta que se decida Q6.

## 16. Riesgos

| ID | Riesgo | Mitigación propuesta |
|---|---|---|
| R-001 | Requisitos legales sin validar a tiempo (RGPD, cookies, consumidores, IVA, facturación) | Revisión por asesoría legal antes de la fase DESIGN |
| R-002 | Política de pago y cancelación sin definir bloquea el flujo y los estados | Decidir Q1 en DISCOVERY |
| R-003 | Doble reserva por concurrencia | RN-003, RN-016, RNF-007 y pruebas específicas |
| R-004 | Proveedor de pasarela no elegido (comisiones, reembolsos parciales, preautorización) | Decisión del cliente. Evaluación técnica posterior |
| R-005 | Imágenes de ejemplo afectan la confianza y la conversión | Plan de sustitución con fotos reales (RNF-013) |
| R-006 | Expectativa de SEO como "garantía" de posicionamiento | Dejar claro que se aplican buenas prácticas, no resultados |
| R-007 | "Completa" y "robusto" no están acotados y favorecen la ampliación de alcance | Fijar MVP, F2 y AMP y gestionar cambios con CR |
| R-008 | "Velocidad" sin objetivo medible | Adoptar RNF-001 si el cliente lo acepta |
| R-009 | Pedir documentos de identidad o carnet aumenta riesgo y obligaciones de privacidad | Resolver Q5 |
| R-010 | Fianza y saldo pendiente generan operación manual y riesgo de impago | Decidir Q1 y Q2 |
| R-011 | Volumen y picos estacionales desconocidos | Pedirlos en DISCOVERY (RNF-012) |
| R-012 | Mala entregabilidad de correos transaccionales | RNF-014 |
| R-013 | Costes de pasarela, correo y hosting fuera del contrato pueden sorprender al cliente | Informarlos como costes recurrentes, sin estimarlos |

## 17. Preguntas abiertas para el Director

Son las preguntas para trasladar al cliente. Hay 7 y todas cambian el alcance.

1. **Modelo de cobro (Q1):** ¿prefiere pago total al reservar, o depósito más saldo posterior? ¿Aceptará otros medios además de tarjeta? Decide RN-013, los estados de pago, los recordatorios y RF-031.
2. **Fianza (Q2):** ¿se gestionará en la entrega o con preautorización en línea? Decide RN-017 y la integración de pago.
3. **Acceso del cliente (Q3):** ¿cuenta de usuario o solo código de reserva más email? Decide RF-012, RN-025 y el esfuerzo de cuentas.
4. **Facturación y tipo de cliente (Q4):** ¿se necesita factura automática o basta un justificante inicial? ¿Habrá clientes empresa con NIF? ¿Se necesitan más idiomas? Decide RN-027, RF-031 y las integraciones.
5. **Verificación del conductor (Q5):** ¿se pedirá carnet o documentos en la web, o solo se verificará en la recogida? ¿Hay edad mínima o conductores adicionales? Decide RN-024, VAL-011 y VAL-012, y el riesgo R-009.
6. **Devolución en otra sede (Q6):** ¿se permitirá y con qué suplemento? Decide RN-006 y el modelo de disponibilidad.
7. **Operación del panel (Q7):** ¿cuántas personas lo usarán y con qué permisos (solo administrador o también operador de sede)? ¿Hace falta crear reservas manuales o informes en el MVP? Decide RF-028 a RF-030.

## 18. Pendientes que no cambian alcance

Se resuelven en DESIGN o contenido junto con la empresa, no necesitan pregunta al cliente:

- Valores concretos de tramos de cancelación, porcentajes de depósito y mínimos de noches.
- Textos de condiciones de alquiler: kilometraje, combustible, limpieza, mascotas, viaje al extranjero, franquicia y seguro.
- Proveedor de correo.
- Contenido de FAQ.

## Resultado

**COMPLETADO_CON_PENDIENTES**

- No se detectó contradicción en el contexto. Sí hay tensión entre "completa y robusta" y la separación MVP/F2/AMP (R-007).
- No se inventaron cifras, proveedores, fechas, costes ni requisitos legales confirmados. Los valores citados como ejemplo o referencia están marcados [R] o [P].

## Siguiente acción recomendada

1. El Director traslada al cliente las 7 preguntas y solicita validación legal de la sección "Puntos para validación legal".
2. Con las respuestas, el Director consolida DISCOVERY y evalúa activar Product Manager para definir el MVP y el backlog.
3. Después, el Director decide la activación de Seguridad y UX/UI.
4. No iniciar desarrollo sin aprobación explícita del alcance, según las reglas corporativas.
