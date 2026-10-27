# Registro de requisitos: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** [requirements.md](../01-discovery/requirements.md) (Analista de Negocio) y [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) (Product Manager). Este índice no añade requisitos. Resume y enlaza.

Este archivo es el índice controlado de requisitos. El detalle está en los documentos de descubrimiento y producto.

## Estados

`PROPUESTO`, `CONFIRMADO`, `APROBADO`, `RECHAZADO`, `SUSTITUIDO`.

## Aviso sobre estados y marcas

- **Todos los requisitos figuran como `PROPUESTO`.** Ninguno está `APROBADO`: no existe alcance aprobado y GATE-001 y GATE-002 están PENDING (ver [APPROVALS](APPROVALS.md)).
- Las marcas originales de las fuentes se conservan en la columna **Fuente**: **[C]** confirmado, **[S]** supuesto, **[R]** recomendación, **[P]** pendiente. Una marca [C] significa que la necesidad la indicó el cliente. No significa que el detalle esté aprobado.
- **Prioridad:** se muestra la del Analista (AN: MVP, F2 o AMP) y la del Product Manager (PM: MoSCoW y destino). Si difieren, se indica la discrepancia ISS (ver [RISKS](RISKS.md) §2).
- **Criterios:** numeración CA del Product Manager. Los CA-001 a CA-014 no están reconciliados con los del Analista (ISS-001).
- **Tareas y Pruebas:** `—`. No hay tareas de implementación ni pruebas porque no existe alcance aprobado.

## 1. Requisitos funcionales

| ID | Resumen | Fuente | Prioridad (AN / PM) | Estado | Criterios | Tareas | Pruebas | Documento detallado |
|---|---|---|---|---|---|---|---|---|
| RF-001 | Catálogo de campers con ficha (descripción, plazas, equipamiento, fotos, precio orientativo). Fotos de ejemplo hasta tener reales | AN. Necesidad [C]; ficha [R]; fotos reales [P] | MVP / Must, MVP | PROPUESTO | CA-016 | — | — | requirements.md §6; mvp-and-backlog.md HU-001 |
| RF-002 | Búsqueda por fechas de recogida y devolución y por sede si hay varias | AN. Fechas [C]; sede [C] | MVP / Must, MVP | PROPUESTO | CA-015, CA-001, CA-009 | — | — | requirements.md §6; mvp-and-backlog.md HU-002 |
| RF-003 | Disponibilidad por vehículo y fechas, validada en servidor | AN [C] | MVP / Must, MVP | PROPUESTO | CA-001, CA-002, CA-003 | — | — | requirements.md §6; mvp-and-backlog.md HU-003 |
| RF-004 | Cálculo y desglose de precio antes de pagar (noche, temporadas, extras, impuestos, fianza informativa) | AN [R] | MVP / Must, MVP | PROPUESTO | CA-017, CA-034, CA-012 | — | — | requirements.md §6; mvp-and-backlog.md HU-004 |
| RF-005 | Selección de extras opcionales configurables | AN [R] | MVP / Should, Fase 2 (**ISS-006**) | PROPUESTO | — (Fase 2 sin CA) | — | — | requirements.md §6; mvp-and-backlog.md HU-025 |
| RF-006 | Flujo de reserva: datos del conductor principal, resumen, aceptación de condiciones y pago | AN [R] | MVP / Must, MVP | PROPUESTO | CA-018, CA-010 | — | — | requirements.md §6; mvp-and-backlog.md HU-005 |
| RF-007 | Bloqueo temporal de fechas durante el pago | AN [R] | MVP / Must, MVP | PROPUESTO | CA-003, CA-002 | — | — | requirements.md §6; mvp-and-backlog.md HU-006 |
| RF-008 | Pago en línea mediante pasarela segura | AN. Necesidad [C]; proveedor [P]; tarjeta [S] | MVP / Must, MVP | PROPUESTO | CA-031, CA-006 | — | — | requirements.md §6; mvp-and-backlog.md HU-007 |
| RF-009 | Autenticación reforzada del pago (3-D Secure/SCA) gestionada por la pasarela | AN [R]; validar PSD2 | MVP / Must, MVP | PROPUESTO | CA-031, CA-006 | — | — | requirements.md §6; mvp-and-backlog.md HU-007 |
| RF-010 | Confirmación en pantalla y correos transaccionales (RN-018) | AN [R] | MVP / Must, MVP (confirmación y justificante) (**ISS-009**) | PROPUESTO | CA-019, CA-004 | — | — | requirements.md §6; mvp-and-backlog.md HU-010 |
| RF-011 | Consulta del estado, detalle y justificante de la reserva por el cliente | AN [C] | MVP / Must, MVP | PROPUESTO | CA-020, CA-013 | — | — | requirements.md §6; mvp-and-backlog.md HU-011 |
| RF-012 | Acceso a la reserva por cuenta **o** código + email | AN [S] | MVP / Must, MVP solo con código + email; cuentas en Fase 2 (**ISS-008**) | PROPUESTO | CA-020, CA-013 | — | — | requirements.md §6; mvp-and-backlog.md HU-011, HU-032 |
| RF-013 | Cancelación por el cliente con cálculo automático de reembolso según política | AN [R] | MVP / Must (ver P-004), MVP (**ISS-002**) | PROPUESTO | CA-008 | — | — | requirements.md §6; mvp-and-backlog.md HU-012 |
| RF-014 | Modificación de fechas, vehículo o extras por el cliente | AN [R] | F2 / Should, Fase 2 | PROPUESTO | — | — | — | requirements.md §6; mvp-and-backlog.md HU-027 |
| RF-015 | Formulario de contacto y página de preguntas frecuentes | AN [R] | MVP / contacto Must, MVP; FAQ Should, Fase 2 (**ISS-007**) | PROPUESTO | CA-029 (contacto) | — | — | requirements.md §6; mvp-and-backlog.md HU-013, HU-026 |
| RF-016 | Páginas legales: aviso legal, privacidad, cookies, condiciones de alquiler | AN [R]; validar con asesoría | MVP / Must, MVP | PROPUESTO | CA-027 | — | — | requirements.md §6; mvp-and-backlog.md HU-014 |
| RF-017 | Banner de consentimiento de cookies con categorías | AN [R]; validar LSSI-CE | MVP / Must, MVP | PROPUESTO | CA-026 | — | — | requirements.md §6; mvp-and-backlog.md HU-014 |
| RF-018 | Páginas indexables para SEO: URLs limpias, metadatos, sitemap, datos estructurados, páginas por vehículo y sede | AN [C] SEO | MVP / Must, MVP | PROPUESTO | CA-028 | — | — | requirements.md §6; mvp-and-backlog.md HU-015 |
| RF-019 | Panel de administración con acceso autenticado por rol | AN [S] | MVP / Must, MVP (rol único) | PROPUESTO | CA-021 | — | — | requirements.md §6; mvp-and-backlog.md HU-017 |
| RF-020 | Gestión de flota: alta, edición, desactivación, fotos, equipamiento, plazas, fianza, sede base | AN [C] configurable | MVP / Must, MVP | PROPUESTO | CA-011 | — | — | requirements.md §6; mvp-and-backlog.md HU-018 |
| RF-021 | Gestión de sedes: alta, edición, desactivación, horarios y contacto | AN [C] configurable | MVP / Must, MVP | PROPUESTO | CA-011, CA-033 | — | — | requirements.md §6; mvp-and-backlog.md HU-019 |
| RF-022 | Gestión de tarifas, temporadas, mínimos de noches y extras | AN. [C] configurable; detalle [R] | MVP / Must, MVP; la parte de extras Should, Fase 2 (**ISS-006**) | PROPUESTO | CA-011, CA-034, CA-012 | — | — | requirements.md §6; mvp-and-backlog.md HU-020, HU-025 |
| RF-023 | Gestión de reservas: listar, filtrar, ver detalle, cancelar y anotar | AN [R] | MVP / Must, MVP | PROPUESTO | CA-022, CA-032 | — | — | requirements.md §6; mvp-and-backlog.md HU-021 |
| RF-024 | Bloqueo manual de fechas de un vehículo | AN [R] | MVP / Must, MVP | PROPUESTO | CA-023, CA-002 | — | — | requirements.md §6; mvp-and-backlog.md HU-022 |
| RF-025 | Gestión de pagos: ver transacciones y emitir reembolsos totales o parciales | AN [R] | MVP / Must, MVP | PROPUESTO | CA-024 | — | — | requirements.md §6; mvp-and-backlog.md HU-023 |
| RF-026 | Aviso interno al administrador por nueva reserva o cancelación | AN [R] | MVP / Must (mínimo), MVP; centro de avisos Could, Fase 2 (**ISS-010**) | PROPUESTO | CA-025 | — | — | requirements.md §6; mvp-and-backlog.md HU-024, HU-035 |
| RF-027 | Edición de plantillas de correo y de textos de políticas con versionado | AN [R] | F2 / Should, Fase 2 | PROPUESTO | — | — | — | requirements.md §6; mvp-and-backlog.md HU-029 |
| RF-028 | Creación manual de reservas (teléfono o mostrador) | AN [R] | F2 / Should, Fase 2 | PROPUESTO | — | — | — | requirements.md §6; mvp-and-backlog.md HU-028 |
| RF-029 | Informes básicos y registro de auditoría de cambios en el panel | AN [R] | F2 / Could, Fase 2 | PROPUESTO | — | — | — | requirements.md §6; mvp-and-backlog.md HU-033 |
| RF-030 | Roles adicionales (operador de sede) | AN [R] | F2 / Could, Fase 2 | PROPUESTO | — | — | — | requirements.md §6; mvp-and-backlog.md HU-034 |
| RF-031 | Ampliaciones: preautorización de fianza, saldo diferido con recordatorios, factura automática, otros medios de pago, multi-idioma, cupones, reseñas, documentos del conductor, contrato digital, sincronización de canales | AN [P] solo si el cliente lo decide | AMP / saldo diferido y factura automática Should, Fase 2 (**ISS-004**); el resto Won't por ahora | PROPUESTO | — | — | — | requirements.md §6; mvp-and-backlog.md HU-030, HU-031 |
| RF-032 | Expiración automática de reservas impagadas y liberación de fechas (RN-015) | AN [R] | MVP / Must, MVP | PROPUESTO | CA-005, CA-007 | — | — | requirements.md §6; mvp-and-backlog.md HU-009 |

## 2. Requisitos no funcionales

La medida verificable es la que redacta la fuente. Si es [P], no se inventa.

| ID | Categoría | Resumen y medida verificable | Fuente | Prioridad | Estado | Tareas | Pruebas |
|---|---|---|---|---|---|---|---|
| RNF-001 | Rendimiento | Core Web Vitals "buenos" en móvil: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1. Protocolo de medición pendiente (PEND-014) | AN. Necesidad [C]; métricas [R] | PM: Must (objetivo verificable) | PROPUESTO | — | — |
| RNF-002 | SEO técnico | HTML indexable, URLs limpias, metadatos, sitemap, datos estructurados. Sin garantía de posicionamiento | AN. Necesidad [C]; técnicas [R] | PM: Must (objetivo) | PROPUESTO | — | — |
| RNF-003 | Responsive | Mobile-first y navegadores modernos | AN [R] | PM: Must (objetivo) | PROPUESTO | — | — |
| RNF-004 | Usabilidad | Flujo de reserva corto y claro, con progreso y errores comprensibles. Métrica [R] | AN. [C] "excelente UX"; métrica [R] | PM: Must (objetivo) | PROPUESTO | — | — |
| RNF-005 | Accesibilidad | Objetivo WCAG 2.1 AA, a validar si es obligatoria. Alcance de la revisión pendiente (PEND-014) | AN [R] | PM: Must (objetivo) | PROPUESTO | — | — |
| RNF-006 | Seguridad | HTTPS, sin almacenar datos de tarjeta, control de acceso por rol, contraseñas protegidas, protección contra vulnerabilidades habituales, límites de intentos | AN. [C] "pago seguro"; medidas [R] | No asignada explícitamente en el PM; referenciada en HU-007 y HU-017 | PROPUESTO | — | — |
| RNF-007 | Integridad | Operaciones de reserva y pago transaccionales, sin doble reserva | AN [R] | No asignada explícitamente; referenciada en HU-003 | PROPUESTO | — | — |
| RNF-008 | Privacidad | Minimización y retención definida. Validar con asesoría | AN [R] | No asignada explícitamente; referenciada en HU-005 | PROPUESTO | — | — |
| RNF-009 | Trazabilidad | Registro de eventos de pago y cambios de estado | AN [R] | No asignada explícitamente; referenciada en HU-008 y HU-023 | PROPUESTO | — | — |
| RNF-010 | Configurabilidad | Flota, sedes, tarifas y políticas editables sin cambios de código | AN [C] | No asignada explícitamente; referenciada en HU-018 | PROPUESTO | — | — |
| RNF-011 | Disponibilidad y copias | Objetivos y plazos de recuperación. Sin valores (PEND-015) | AN [P] | No asignada | PROPUESTO | — | — |
| RNF-012 | Escalabilidad | Dimensionar según tráfico esperado. Sin datos (PEND-015, PEND-021) | AN [P] | No asignada | PROPUESTO | — | — |
| RNF-013 | Contenido sustituible | Imágenes de ejemplo sustituibles sin desarrollo | AN [R] | No asignada explícitamente; referenciada en HU-001 y HU-018 | PROPUESTO | — | — |
| RNF-014 | Fiabilidad de correo | Entregabilidad configurada correctamente | AN [R] | No asignada explícitamente; referenciada en HU-010 | PROPUESTO | — | — |

## 3. Reglas de negocio

"Requisitos relacionados" recoge solo las relaciones explícitas en las fuentes.

| ID | Regla | Fuente | Estado | Requisitos relacionados | Excepciones |
|---|---|---|---|---|---|
| RN-001 | Flota y sedes son datos configurables desde el panel | AN [C] | PROPUESTO | RF-020, RF-021, RNF-010 | — |
| RN-002 | Una reserva = 1 vehículo + rango de fechas + sede de recogida y de devolución | AN [S] | PROPUESTO | — | ISS-011 |
| RN-003 | Sin reservas o bloqueos solapados para un vehículo | AN [R] | PROPUESTO | RF-003, RF-024 | — |
| RN-004 | Alquiler por noches. Tiempo de preparación configurable (valor [P]) | AN [R] | PROPUESTO | — | PEND-013 |
| RN-005 | Moneda EUR, idioma español, zona horaria Europe/Madrid | AN [S] | PROPUESTO | — | ISS-012 |
| RN-006 | Recogida y devolución en distinta sede: no se asume | AN [P] (Q6) | PROPUESTO | — | ISS-011 |
| RN-007 | Precio por noche por vehículo y temporada, sin solapes | AN [R] | PROPUESTO | RF-022 | — |
| RN-008 | Mínimo de noches configurable por temporada (valores [P]) | AN [R] | PROPUESTO | RF-022 | — |
| RN-009 | Antelación mínima y duración máxima configurables (valores [P]) | AN [R] | PROPUESTO | — | PEND-017 |
| RN-010 | Precio calculado en servidor y congelado al crear la reserva | AN [R] | PROPUESTO | RF-004 | — |
| RN-011 | Precio final con impuestos y desglose. IVA a validar con asesoría | AN [R]; validar legal | PROPUESTO | RF-004 | PEND-010 |
| RN-012 | Extras: precio fijo por reserva o por noche, con stock opcional | AN [R] | PROPUESTO | RF-005, RF-022 | ISS-006 |
| RN-013 | Pago: depósito + saldo (recomendado por el AN) o pago total (alternativa) | AN [R] (Q1) | PROPUESTO | RF-008, RF-031 | ISS-005 |
| RN-014 | Cancelación por el cliente con reembolso escalonado según la política vigente al reservar | AN [R]; valores [P] | PROPUESTO | RF-013 | ISS-002 |
| RN-015 | Reservas impagadas expiran. El pago tardío se confirma solo si hay disponibilidad; si no, se reembolsa | AN [R] | PROPUESTO | RF-032 | — |
| RN-016 | Bloqueo temporal durante el pago. 15 min como valor inicial no confirmado | AN [R] | PROPUESTO | RF-007 | — |
| RN-017 | Fianza configurable por vehículo, informativa. Gestionada en la entrega en el MVP | AN [R] (Q2) | PROPUESTO | RF-004, RF-020 | PEND-018 |
| RN-018 | Correos transaccionales mínimos (8 tipos) | AN [R] | PROPUESTO | RF-010 | ISS-009 |
| RN-019 | Cancelación por la empresa: reembolso total o alternativa de vehículo | AN [R] | PROPUESTO | — | PEND-008 |
| RN-020 | No presentación y devolución tardía: a definir en las condiciones | AN [P] | PROPUESTO | — | PEND-023 |
| RN-021 | Estados de reserva (Pendiente de pago → Confirmada → En curso → Completada; salidas) | AN [R] | PROPUESTO | CA-032 | — |
| RN-022 | Estados de pago (Pendiente, Pagado, Parcialmente pagado, Fallido, Reembolsado parcial o total) | AN [R] | PROPUESTO | CA-032 | — |
| RN-023 | La reserva se confirma solo con la notificación del servidor de la pasarela | AN [R] | PROPUESTO | RF-008, RF-009 | — |
| RN-024 | Conductor: edad, antigüedad, permiso, conductores adicionales y verificación. Sin valores | AN [P] (Q5) | PROPUESTO | RF-006 | ISS-014, PEND-019 |
| RN-025 | El cliente solo ve sus reservas. Acceso por código requiere email | AN [R] | PROPUESTO | RF-012 | — |
| RN-026 | Datos personales y consentimientos con registro de fecha y versión | AN [R]; validar RGPD/LOPDGDD | PROPUESTO | RF-006 | PEND-010 |
| RN-027 | Justificante de pago al cobrar. La factura formal se define con asesoría | AN [P] (Q4) | PROPUESTO | RF-010 | ISS-004 |

## 4. Historias y criterios de aceptación

Historias del Product Manager, todas [R]. "Valor" es la parte "para..." de la historia. Las de Fase 2 no tienen CA.

| Historia | Actor | Necesidad | Valor | Estado | Criterios de aceptación |
|---|---|---|---|---|---|
| HU-001 | Cliente | Ver el catálogo y la ficha de cada camper | Decidir cuál le conviene | PROPUESTO | CA-016 |
| HU-002 | Cliente | Buscar por fechas y sede | Ver solo los campers que puede alquilar | PROPUESTO | CA-015, CA-001, CA-009 |
| HU-003 | Cliente | Que la disponibilidad sea fiable | No perder tiempo con una reserva imposible | PROPUESTO | CA-001, CA-002, CA-003 |
| HU-004 | Cliente | Ver el precio total desglosado antes de pagar | Saber cuánto pagará | PROPUESTO | CA-017, CA-034, CA-012 |
| HU-005 | Cliente | Indicar sus datos como conductor principal y aceptar las condiciones | Formalizar la reserva | PROPUESTO | CA-018, CA-010 |
| HU-006 | Cliente | Que las fechas queden reservadas mientras paga | Que nadie se las quite | PROPUESTO | CA-003, CA-002 |
| HU-007 | Cliente | Pagar en línea con tarjeta de forma segura | Completar su reserva | PROPUESTO | CA-031, CA-006 |
| HU-008 | Cliente | Que la reserva solo se confirme con el pago validado | Tener certeza | PROPUESTO | CA-004, CA-032 |
| HU-009 | Empresa | Que las reservas impagadas expiren y los pagos tardíos se gestionen con seguridad | No bloquear flota ni cobrar sin servicio | PROPUESTO | CA-005, CA-007 |
| HU-010 | Cliente | Recibir por correo la confirmación y el justificante | Tener constancia | PROPUESTO | CA-019 |
| HU-011 | Cliente | Consultar su reserva con código y email | Ver estado y detalle sin crear cuenta | PROPUESTO | CA-020, CA-013 |
| HU-012 | Cliente | Cancelar su reserva y recibir el reembolso que corresponda | No depender de llamadas | PROPUESTO | CA-008 |
| HU-013 | Cliente | Contactar con la empresa | Resolver dudas | PROPUESTO | CA-029 |
| HU-014 | Cliente | Ver las páginas legales y decidir sobre las cookies | Conocer sus derechos | PROPUESTO | CA-026, CA-027 |
| HU-015 | Empresa | Una web con base SEO técnica y carga rápida en móvil | Ser encontrada y no perder reservas | PROPUESTO | CA-028, CA-014 |
| HU-016 | Cliente | Usar la web desde móvil con accesibilidad básica | Reservar sin barreras | PROPUESTO | CA-030 |
| HU-017 | Administrador | Acceder al panel con credenciales | Proteger los datos | PROPUESTO | CA-021 |
| HU-018 | Administrador | Gestionar la flota (alta, edición, activación/desactivación, imágenes) | Mantener el catálogo al día | PROPUESTO | CA-011 |
| HU-019 | Administrador | Gestionar las sedes | Operar en distintas ubicaciones | PROPUESTO | CA-011, CA-033 |
| HU-020 | Administrador | Configurar tarifas, temporadas y mínimo de noches | Controlar los precios | PROPUESTO | CA-011, CA-034, CA-012 |
| HU-021 | Administrador | Ver y gestionar las reservas (listar, filtrar, detalle, cancelar) | Operar el negocio | PROPUESTO | CA-022, CA-032 |
| HU-022 | Administrador | Bloquear fechas de un camper (mantenimiento, reservas fuera de la web) | Evitar conflictos | PROPUESTO | CA-023, CA-002 |
| HU-023 | Administrador | Ver pagos y emitir reembolsos | Controlar el dinero | PROPUESTO | CA-024 |
| HU-024 | Administrador | Recibir un correo por reserva nueva, cancelación o pago tardío que requiera acción | Enterarse sin vigilar el panel | PROPUESTO | CA-025 |
| HU-025 | Cliente | Añadir extras a su reserva (Fase 2, Should) | — | PROPUESTO | — |
| HU-026 | Cliente | Consultar preguntas frecuentes (Fase 2, Should) | — | PROPUESTO | — |
| HU-027 | Cliente | Modificar su reserva (Fase 2, Should) | — | PROPUESTO | — |
| HU-028 | Administrador | Crear reservas manuales (Fase 2, Should) | — | PROPUESTO | — |
| HU-029 | Administrador | Editar las plantillas de correo (Fase 2, Should) | — | PROPUESTO | — |
| HU-030 | Cliente | Pagar un depósito y el saldo después (Fase 2, Should). Origen: decisión del Director (P-007) | — | PROPUESTO | — |
| HU-031 | Cliente o empresa | Una factura automática (Fase 2, Should). Origen: decisión del Director (P-007) | — | PROPUESTO | — |
| HU-032 | Cliente | Tener cuenta de usuario (Fase 2, Could) | — | PROPUESTO | — |
| HU-033 | Administrador | Informes y registro de auditoría (Fase 2, Could) | — | PROPUESTO | — |
| HU-034 | Administrador | Roles adicionales (Fase 2, Could) | — | PROPUESTO | — |
| HU-035 | Administrador | Un centro de avisos completo (Fase 2, Could) | — | PROPUESTO | — |
| HU-036 | Cliente | Devolver el camper en otra sede con suplemento (Fase 2, Could). Origen: decisión del Director | — | PROPUESTO | — |

**Criterios de aceptación:** CA-001 a CA-034 (numeración del Product Manager) están en [mvp-and-backlog.md](../02-product/mvp-and-backlog.md). CA-001 a CA-014 del Analista están en [requirements.md](../01-discovery/requirements.md) §13. Ambos conjuntos no están reconciliados (ISS-001, DEC-030). **CA-033** (misma sede) se registra en la fuente como "decisión del Director" y no traza a un RF o RN.

## 5. Requisitos rechazados o sustituidos

| ID | Decisión | Motivo | Sustituido por | Referencia |
|---|---|---|---|---|
| — | Ninguno | — | — | — |

## 6. Pendientes de confirmación

El detalle de cada pendiente, con opciones y recomendación, está en [DECISIONS](DECISIONS.md) §3. Aquí se resume el impacto.

| ID temporal | Pregunta | Impacto | Responsable de responder | Estado |
|---|---|---|---|---|
| PEND-001 | Q1. Modelo de cobro y medios de pago | RN-013, estados de pago, RF-031 | Cliente, vía Director | OPEN |
| PEND-002 | Q2. Fianza en la entrega o en línea | RN-017, integración de pago | Cliente, vía Director | OPEN |
| PEND-003 | Q3. Acceso del cliente: cuenta o código + email | RF-012, RN-025 | Cliente, vía Director | OPEN |
| PEND-004 | Q4. Factura, clientes empresa e idiomas | RN-027, RF-031 | Cliente, vía Director | OPEN |
| PEND-005 | Q5. Verificación del conductor, edad y conductores adicionales | RN-024, VAL-011, VAL-012 | Cliente, vía Director | OPEN |
| PEND-006 | Q6. Devolución en otra sede y suplemento | RN-006, modelo de disponibilidad | Cliente, vía Director | OPEN |
| PEND-007 | Q7. Operación del panel: usuarios, permisos, reservas manuales, informes | RF-028 a RF-030 | Cliente, vía Director | OPEN |
| PEND-008 | P-001. Valores de cancelación, regla de cancelación por la empresa, % de depósito, mínimos de noches | RN-008, RN-013, RN-014, RN-019 | Cliente, vía Director | OPEN |
| PEND-009 | P-001. Comisiones de la pasarela en reembolsos | RF-025, RF-013 | Cliente, vía Director | OPEN |
| PEND-010 | P-005. Validación legal | RN-011, RN-026, RF-016, RF-017, DEC-025 | Cliente / asesoría, vía Director | OPEN |
| PEND-011 | P-014. Titularidad de pasarela, dominio y remitente de correo | RF-008, RF-010 | Cliente, vía Director | OPEN |
| PEND-012 | Proveedor de la pasarela | RF-008 | Cliente, vía Director | OPEN |
| PEND-013 | P-010. Noche/día, horas y zona horaria | RN-004, RN-005, VAL-001, VAL-006 | Cliente, vía Director | OPEN |
| PEND-014 | P-012. Protocolo de rendimiento y alcance de accesibilidad | RNF-001, RNF-005, CA-014, CA-030 | Director / cliente | OPEN |
| PEND-015 | P-013. Metas numéricas, disponibilidad y escalabilidad | RNF-011, RNF-012 | Cliente, vía Director | OPEN |
| PEND-016 | P-015. Alcance de público extranjero para el SEO | RNF-002, RN-005 | Cliente, vía Director | OPEN |
| PEND-017 | P-016. Antelación mínima y máxima | RN-009, VAL-002, VAL-004 | Cliente, vía Director | OPEN |
| PEND-018 | P-002. Importe y texto de la fianza informativa | RN-017, RF-004 | Cliente, vía Director | OPEN |
| PEND-019 | P-006. Edad mínima y requisitos de permiso | RN-024, VAL-011, CA-018 | Cliente, vía Director | OPEN |
| PEND-020 | Datos y contenidos iniciales (flota, sedes, tarifas, fotos reales, FAQ) | RF-001, RF-020 a RF-022, RNF-013 | Cliente, vía Director | OPEN |
| PEND-021 | Proceso actual, tamaño de flota y volumen esperado | RNF-012, R-011 [AN] | Cliente, vía Director | OPEN |
| PEND-022 | Textos de condiciones de alquiler y proveedor de correo | RF-016, RNF-014 | Cliente, vía Director | OPEN |
| PEND-023 | No presentación, devolución tardía y cliente sin acceso al email | RN-020 | Cliente, vía Director | OPEN |
| PEND-024 | P-011. Desactivación con reservas futuras | RF-020, RF-021, VAL-021 | Cliente, vía Director | OPEN |

## Enlaces

[Estado del proyecto](PROJECT-STATE.md) · [Decisiones](DECISIONS.md) · [Trazabilidad](TRACEABILITY.md) · [Riesgos e impedimentos](RISKS.md) · [requirements.md](../01-discovery/requirements.md) · [mvp-and-backlog.md](../02-product/mvp-and-backlog.md)
