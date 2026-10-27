# Resumen del cliente y propuesta inicial: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fase:** INTAKE (GATE-001 PENDING, ver [APPROVALS](../00-control/APPROVALS.md))  
> **Fuente:** Mensajes del Director de Proyectos al Gestor de Documentación (mensaje inicial del cliente, respuestas del cliente y propuesta inicial). Contrastado con las confirmaciones `[C]` de [requirements.md](../01-discovery/requirements.md) y [mvp-and-backlog.md](../02-product/mvp-and-backlog.md).  
> **Decisiones pendientes:** Ver [DECISIONS](../00-control/DECISIONS.md) §3 y [REQUIREMENTS](../00-control/REQUIREMENTS.md) §6.

**Leyenda:** **[C]** Confirmado · **[S]** Supuesto · **[R]** Recomendación · **[P]** Pendiente.

## 1. Mensaje inicial del cliente

**Limitación documental:** el Gestor recibió el mensaje inicial como un resumen del Director, no como texto literal. No se reproduce una cita textual para no inventarla. El texto literal queda **[P]** hasta que el Director lo aporte.

Resumen recibido: el cliente pide una **web de alquiler de campers con reservas**, con **pasarela de pago segura**, y con atención a la **experiencia de usuario (UX)**, la **velocidad** y el **SEO**.

## 2. Respuestas del cliente (literales)

Respuestas a las 7 preguntas de la propuesta inicial, tal como las entregó el Director:

| N.º | Respuesta literal del cliente |
|---|---|
| 1 | "esta en españa" |
| 2 | "que sea configurable" |
| 3 | "pon tu las reglas" |
| 4 | "lo que creas conveniente" |
| 5 | "crealo" |
| 6 | "no y ponlo que no abra migracion" |
| 7 | "no entra en el contrato" |

**Limitación documental:** el Gestor no recibió el texto de cada una de las 7 preguntas. Por eso no se asigna cada respuesta a un tema concreto salvo lo que las fuentes registran como confirmado. Esas 7 preguntas de la propuesta inicial **no son** las preguntas Q1 a Q7 del Analista de Negocio. Las Q1 a Q7 del Analista siguen abiertas (ver [REQUIREMENTS](../00-control/REQUIREMENTS.md) §6, PEND-001 a PEND-007).

### Relación con lo que las fuentes marcan como confirmado

Esta relación no se ha verificado contra el texto de las preguntas. Queda pendiente de confirmar por el Director.

| Respuesta | Lo que las fuentes registran como [C] |
|---|---|
| 1 | El negocio de alquiler de campers está en España. Idioma español, EUR y zona horaria Europe/Madrid se mantienen como **[S]** (RN-005). |
| 2 | La flota y las sedes son configurables desde un panel (RN-001, RNF-010). |
| 3, 4, 5 | Delegación del cliente en el equipo. Las decisiones resultantes son **[R]** y el cliente **no las ha confirmado** (mvp-and-backlog.md, "Alcance de las recomendaciones"). |
| 6 | No hay sistemas previos que integrar ni datos que migrar. Migración e integración quedan excluidas. |
| 7 | Presupuesto y fechas quedan fuera del contrato. |

## 3. Propuesta inicial presentada al cliente

El Gestor recibió el contenido como lista de apartados, no como texto íntegro. Se registra únicamente lo indicado por el Director.

- **Interpretación del sitio.**
- **Ejemplo de funcionamiento.**
- **MVP propuesto:** catálogo, búsqueda por fechas y disponibilidad, reserva con pago en línea, correos de confirmación, consulta y cancelación por el cliente, panel básico, diseño adaptable, SEO técnico y rendimiento, idioma único.
- **Ampliaciones posibles:** multi-idioma y multi-moneda, extras y seguros, descuentos, contratos digitales, reseñas, calendarios externos, facturación automática, app móvil.
- **Supuestos.**
- **7 preguntas** al cliente.

**[P]** El texto literal de la interpretación, del ejemplo de funcionamiento, de los supuestos y de las 7 preguntas no fue suministrado al Gestor.

**Nota de contraste:** esta propuesta inicial y el MVP del Product Manager no coinciden en todo. Por ejemplo, la propuesta inicial incluye "consulta/cancelación por el cliente" y "panel básico" en el MVP, y lista "extras y seguros" y "facturación automática" como ampliaciones. El Product Manager sitúa los extras y la factura automática en Fase 2 (ver ISS-004 e ISS-006 en [RISKS](../00-control/RISKS.md) §2). El Gestor no resuelve estas diferencias.

## 4. Estado de la información

| Tipo | Contenido |
|---|---|
| **[C]** | Web para alquiler de campers en España, con reservas en línea (fechas, disponibilidad, gestión de alquileres), pasarela de pago segura, y atención a UX, velocidad y SEO. Flota y sedes configurables desde un panel. Sin migración ni integración con sistemas existentes. Presupuesto y fechas fuera del contrato. |
| **[S]** | Idioma español, moneda EUR, zona horaria Europe/Madrid, cliente particular, pago con tarjeta, una sola empresa. Detalle en requirements.md §15. |
| **[R]** | El MVP, el backlog y las reglas de negocio propuestos por el Analista de Negocio y el Product Manager. Ninguno está aprobado. |
| **[P]** | Ver [REQUIREMENTS](../00-control/REQUIREMENTS.md) §6 y [DECISIONS](../00-control/DECISIONS.md) §3. |

## 5. Alcance

- **No hay alcance aprobado.** Ningún documento de este expediente aprueba alcance.
- El MVP y el backlog son una **propuesta en BORRADOR** (ver [mvp-and-backlog.md](../02-product/mvp-and-backlog.md)).
- No se autoriza ningún desarrollo. La puerta PLANNING a BUILD **no ha sido solicitada** (ver [APPROVALS](../00-control/APPROVALS.md)).

## 6. Enlaces relativos

- [Requisitos (Analista de Negocio)](../01-discovery/requirements.md)
- [MVP y backlog (Product Manager)](../02-product/mvp-and-backlog.md)
- [Estado del proyecto](../00-control/PROJECT-STATE.md)
- [Aprobaciones](../00-control/APPROVALS.md)
- [Decisiones](../00-control/DECISIONS.md)
