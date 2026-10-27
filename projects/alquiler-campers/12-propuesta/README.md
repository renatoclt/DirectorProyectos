# Propuesta comercial — Web de alquiler de campers (España)

| Campo | Valor |
|---|---|
| Proyecto | Web de alquiler de campers (España) (`alquiler-campers`) |
| Estado de la carpeta | **BORRADOR** (no entregada al cliente; no enviada) |
| Versión | 0.2 (reestructurada alrededor de la **opción B: entrega inicial acotada**; la 0.1 proponía solo el MVP completo) |
| Oferta principal | **Opción B**: entrega inicial acotada (sitio público con solicitud de reserva), objetivo de **1 semana** para entrega a revisión, **400 USD** (precio fijado por el usuario; moneda de facturación e IVA pendientes), con margen de negociación. Solicitud de cambio **CR-001** (WAITING_FOR_APPROVAL; registrada en [CHANGE-REQUESTS.md](../00-control/CHANGE-REQUESTS.md); pendiente de aprobación formal del cliente, PEND-044) |
| Fase siguiente | MVP completo: estimación preliminar de **28 a 36 semanas** desde la autorización de su construcción, **sin precio**, a cotizar aparte |
| Fecha | 2026-10-26 |
| Elaborada por | Redactor de Propuestas, por indicación del Director de Proyectos, a partir de la plantilla `templates/propuesta/` y de los resultados ya existentes en el expediente |
| Escritura | Solo dentro de `projects/alquiler-campers/12-propuesta/` |

> **Esta propuesta no equivale a aprobar el alcance ni la puerta de PLANNING a BUILD.** Pasa a EN REVISIÓN cuando el Director la reciba y a APROBADO solo con una aprobación humana explícita registrada en el control del proyecto. El alcance del proyecto **no está aprobado** (GATE-001 y GATE-002 PENDING según [APPROVALS.md](../00-control/APPROVALS.md)).

## Índice

| Archivo | Para qué sirve | Audiencia | Estado |
|---|---|---|---|
| **[PROPUESTA-EJECUTIVA.md](PROPUESTA-EJECUTIVA.md)** | **Resumen para decisión en 2–3 minutos**: objetivo, solución, plazo, inversión, riesgos, próximos pasos y dónde encontrar detalle. Empiece aquí. | Cliente + Director | **BORRADOR v0.1** |
| **[INDICE-ADJUNTOS.md](INDICE-ADJUNTOS.md)** | Índice completo de todo el material: documentos comerciales, mockups por audiencia y tema, cómo leer según perfil, navegación rápida, bloqueadores. | Interno | **BORRADOR v0.1** |
| **[AUDITORIA-PROPUESTA.md](AUDITORIA-PROPUESTA.md)** | Verificación de completitud, hallazgos (5 bloqueadores y mejoras), matriz de responsabilidades, estado actual vs. listo para cliente, GATE-001. Para el Director. | Director | **BORRADOR v0.1** |
| [propuesta-comercial.md](propuesta-comercial.md) | Documento para el cliente, con la **opción B** como oferta principal: presentación, comprensión, alcance incluido y no incluido, solución y mockups, plan D1–D7, plazo (1 semana para entrega a revisión), comunicación, inversión (400 USD y margen de negociación), riesgos, decisiones previas, **fase siguiente (MVP completo, sin precio)** y aceptación | Cliente | BORRADOR v0.2 |
| [analisis-consolidado.md](analisis-consolidado.md) | **Todo el análisis en un solo archivo**: sección destacada «Opción B: entrega inicial acotada» y, como fase siguiente, brief, requisitos, MVP, historias, UX, arquitectura, seguridad, plan y estimación, riesgos, decisiones, inconsistencias abiertas y trazabilidad | Cliente e interna | BORRADOR v0.2 |
| [mockups/index.html](mockups/index.html) | Galería de 17 pantallas ilustrativas de media fidelidad (HTML y CSS locales): 6 de la **entrega inicial** (insignia «ENTREGA INICIAL»), 10 de la **fase siguiente** (insignia «FASE SIGUIENTE») y una de estados alternativos (ambas insignias) | Cliente | BORRADOR v0.3 |
| [mockups/README.md](mockups/README.md) | Qué son los mockups y mapa pantalla → RF/HU/CA | Interna | BORRADOR |
| [mockups/direccion-visual.md](mockups/direccion-visual.md) | Dirección visual «cuaderno de ruta» (PROPUESTA, no aprobada): plan de diseño, tokens, decisiones pendientes, criterios de aceptación visual, handoff y autorrevisión | Interna | BORRADOR v0.1 |
| [perfil-empresa.md](perfil-empresa.md) | Datos de la empresa (con marcadores pendientes) y esquema de comunicación recomendado · **40 PENDIENTE: BLOQUEADOR** | Interna | BORRADOR v0.2 |
| [checklist-calidad-propuesta.md](checklist-calidad-propuesta.md) | Verificaciones realizadas antes de entregar, con su evidencia | Interna | BORRADOR |

## Cómo leer esta carpeta

1. Empiece por la **tabla «Qué está confirmado y qué no»** y el **resumen ejecutivo** de la [propuesta comercial](propuesta-comercial.md).
2. Lea la sección 3 (alcance de la entrega inicial), la 6 (plazo), la 8 (inversión), la 10 (decisiones que necesitamos del cliente) y la 11 (fase siguiente).
3. Abra la [galería de mockups](mockups/index.html) en el navegador; las pantallas llevan la insignia **ENTREGA INICIAL** o **FASE SIGUIENTE**. Los datos son de ejemplo y la marca «Ruta Camper» es una **propuesta no aprobada**.
4. Para el detalle y la trazabilidad (RF → HU → CA → ADR → SEG → TASK), use el [análisis consolidado](analisis-consolidado.md); la opción B está en su sección «Opción B: entrega inicial acotada».

**Leyenda:** Confirmado = indicado o aprobado por el cliente · Supuesto = interpretación a validar · Recomendación = propuesta del equipo · Pendiente = decisión o dato faltante. Los marcadores `{{PENDIENTE: ...}}` son visibles a propósito: no se rellenan sin dato confirmado.

## Fuentes y su estado

Todas en **BORRADOR** (ninguna aprobada): [client-brief.md](../00-intake/client-brief.md), [requirements.md](../01-discovery/requirements.md), [mvp-and-backlog.md](../02-product/mvp-and-backlog.md), [ux-specification.md](../03-ux/ux-specification.md), [solution-architecture.md](../04-architecture/solution-architecture.md), [security-review.md](../08-security/security-review.md) (revisión de diseño; no se ejecutó ninguna prueba), [implementation-plan.md](../05-planning/implementation-plan.md) y los registros de `00-control/`. **Las estimaciones de plazo están persistidas**: la del MVP completo en [estimacion-plazo.md](../05-planning/estimacion-plazo.md) y la de la opción B en [estimacion-opcion-b.md](../05-planning/estimacion-opcion-b.md). Este último contiene una sección **interna** (aritmética de costo y estrategia de negociación) que **no se copió** a ningún documento de esta carpeta. La solicitud de cambio **CR-001** figura en [CHANGE-REQUESTS.md](../00-control/CHANGE-REQUESTS.md) (WAITING_FOR_APPROVAL).

## Marcadores PENDIENTE

Conteo por búsqueda en los archivos (sin contar ejemplos de sintaxis `{{PENDIENTE: ...}}`).

| Archivo | Marcadores `{{PENDIENTE: ...}}` | Otros «PENDIENTE» (sin llaves) |
|---|---|---|
| [perfil-empresa.md](perfil-empresa.md) | 40 | 0 reales (1 mención en la explicación) |
| [propuesta-comercial.md](propuesta-comercial.md) | 20 | 18 (fecha de inicio y de entrega, tabla «día relativo → fecha», aceptación del cliente y menciones en el resumen y la vista rápida) |
| [analisis-consolidado.md](analisis-consolidado.md) | 0 | Solo menciones explicativas (la estimación, la fecha de inicio y de entrega, y la moneda y el IVA figuran como Pendiente) |
| Mockups | 0 | El marcador visible es la clase `pendiente` («pendiente», fondo amarillo) |

Total con llaves: 60 (40 en el perfil y 20 en la propuesta). En la versión 0.1 eran 55 (36 y 19).

### Qué datos faltan (bloquean la entrega al cliente)

| Grupo | Marcadores | Quién debe aportarlos |
|---|---|---|
| Cliente | Nombre del cliente | Director |
| Empresa: identidad y presentación | Nombre comercial, razón social, descripción, sitio web; presentación de la empresa; argumentos de diferenciación y evidencia | Director o usuario |
| Empresa: experiencia y credenciales | Proyectos o sector autorizados para citar, resultado verificable, credenciales o «no aplica» | Director o usuario |
| Empresa: equipo | Nombres o «por asignar» de cada rol; confirmación de la disponibilidad real y de la dedicación supuesta; dedicación de gestión documental y auditoría | Director |
| Empresa: contacto y comunicación | Responsable y cargo, correo, teléfono o canal, canales de seguimiento, horario con zona horaria, tiempo de respuesta, formato de revisión, canal y formato de feedback | Director |
| Condiciones comerciales | Modelo de contratación, vigencia, forma de pago, **moneda de facturación e IVA**, garantía o soporte, propiedad y confidencialidad | Director |
| Responsable de la propuesta | Nombre y cargo | Director |
| Inversión | El valor de 400 USD está confirmado por el usuario; **faltan** moneda de facturación, IVA y forma de pago. La fase siguiente **no tiene precio** | Director (cotización de la fase siguiente) |
| Plazo | Fecha de inicio (solo si el cliente la confirma) y, por tanto, fecha de entrega y tabla de fechas (entrega inicial y fase siguiente) | Cliente |
| Aceptación | Decisión, nombre y cargo, fecha y observaciones del cliente; aprobación de CR-001 | Cliente |

Las decisiones de la **entrega inicial** (OB-01 a OB-14: quién edita el contenido, aceptación del núcleo recortado y de la desviación de RN-001/RNF-010, moneda e IVA, contenido y accesos del D1, marca, etc.) y las de la **fase siguiente** (B1 a B9, cambios de seguridad y preguntas de producto) están en la sección 10 de la propuesta; no son marcadores de datos de la empresa, pero también están **Pendientes**.

## Cómo se actualiza

Antes de modificar un documento existente se lee y se conservan sus decisiones, identificadores y marcadores vigentes. Cada cambio se registra aquí, en esta tabla.

| Fecha | Cambio |
|---|---|
| 2026-10-26 | Versión 0.1: creación de la carpeta a partir de la plantilla, en estado BORRADOR |
| 2026-10-26 | Versión 0.2: la **opción B (entrega inicial acotada, 1 semana, 400 USD, margen de negociación; CR-001)** pasa a ser la oferta principal. `propuesta-comercial.md` reestructurada (el MVP completo pasa a la sección 11, fase siguiente, sin precio); `analisis-consolidado.md` con sección nueva «Opción B» y resumen e índice; mockups 11 y 12 nuevos, variantes `-entrega-inicial` de 01, 03 y 10, insignias ENTREGA INICIAL / FASE SIGUIENTE en la galería y en cada pantalla, y estilos nuevos en `_base.css`; `perfil-empresa.md` y `checklist-calidad-propuesta.md` actualizados. Se conservaron identificadores, marcadores y el análisis del MVP completo |
| 2026-10-26 | Versión 0.3 (solo mockups y documentos que los enlazan): rediseño de las 15 pantallas, la galería y `_base.css` con las Skills `frontend-design` (Modo A) y `frontend-design-review` (autocontrol); dirección «cuaderno de ruta» (PROPUESTA, no aprobada). Nuevos: `mockups/13-catalogo-entrega-inicial.html`, `mockups/14-estados.html` y `mockups/direccion-visual.md`; `mockups/README.md` reescrito; la versión anterior se conserva en `mockups/_archivo-v0.2/`. Enlaces añadidos en `propuesta-comercial.md` (sección 4 y anexo) y `analisis-consolidado.md` (sección 4); `checklist-calidad-propuesta.md` actualizado (grupo E y nuevo grupo H). No cambian precio, plazo ni alcance |
