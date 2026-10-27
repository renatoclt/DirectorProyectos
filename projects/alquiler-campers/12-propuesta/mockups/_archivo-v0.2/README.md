# Mockups de la propuesta: Web de alquiler de campers

| Campo | Valor |
|---|---|
| Proyecto | Web de alquiler de campers (España) (`alquiler-campers`) |
| Estado | BORRADOR |
| Fecha | 2026-10-26 |

Los mockups muestran de forma visual **lo que se crearía** si el cliente aprueba el alcance. Son **ilustrativos, de media fidelidad**, y **no son diseño final aprobado**. No tienen funcionalidad real: los botones y formularios no ejecutan acciones.

## Entrega inicial y fase siguiente

La oferta principal es la **opción B** (entrega inicial acotada, CR-001): un sitio público con **solicitud de reserva**, sin pago, sin disponibilidad automática y sin panel. El MVP completo es la **fase siguiente**. Cada pantalla lleva una insignia visible en su cabecera y en la galería:

| Insignia | Significado | Pantallas |
|---|---|---|
| **ENTREGA INICIAL** (relleno oscuro) | Forma parte de la oferta principal (opción B) | `01-inicio-entrega-inicial`, `03-ficha-camper-entrega-inicial`, `11-solicitud-reserva`, `12-tarifas-y-condiciones`, `10-movil-entrega-inicial` |
| **FASE SIGUIENTE** (borde discontinuo) | Ilustra el MVP completo; no forma parte de la entrega inicial | `01-inicio`, `02-resultados-busqueda`, `03-ficha-camper`, `04-resumen-y-datos-conductor`, `05-pago`, `06-confirmacion`, `07-consulta-reserva`, `08-admin-panel-reservas`, `09-admin-flota-tarifas`, `10-movil-inicio-y-resultados` |

Las pantallas `01`, `03` y `10` tienen dos versiones: la de la entrega inicial (sufijo `-entrega-inicial`, con llamada a «Solicitar reserva») y la de la fase siguiente (buscador, disponibilidad y precio total). Ninguna se rompió ni se sustituyó. No existe una pantalla de catálogo independiente: el catálogo de la entrega inicial se ilustra en el inicio.

## Qué son y qué no son

| Son | No son |
|---|---|
| Ilustraciones de estructura, flujo y contenido previstos (según [03-ux/ux-specification.md](../../../03-ux/ux-specification.md)) | Diseño final ni marca aprobada |
| HTML y CSS locales, autocontenidos (sin scripts ni recursos remotos) | Una versión funcional de la web |
| Datos ficticios marcados «dato de ejemplo» e imágenes marcadas «IMAGEN DE EJEMPLO» | Datos reales de la empresa, de flota, tarifas o clientes |

**Marca provisional (PROPUESTA, no aprobada):** nombre «Ruta Camper», paleta y tipografía del sistema propuestos en 03-ux, sección 11. No se verificó disponibilidad de marca ni de dominio. Los contrastes de color se calcularon con la fórmula de WCAG en esta revisión y deben verificarse con herramienta cuando la marca se apruebe (PEND-025).

## Archivos

| Archivo | Uso |
|---|---|
| `index.html` | Galería que enlaza todos los mockups |
| `_base.css` | Estilos compartidos y autocontenidos |
| `01-inicio.html` … `10-movil-inicio-y-resultados.html` | Una pantalla por archivo (fase siguiente: MVP completo) |
| `01-inicio-entrega-inicial.html`, `03-ficha-camper-entrega-inicial.html`, `10-movil-entrega-inicial.html` | Variantes de la entrega inicial (opción B) |
| `11-solicitud-reserva.html`, `12-tarifas-y-condiciones.html` | Pantallas nuevas de la entrega inicial (opción B) |

## Mapa pantalla → requisitos, historias y criterios

### Entrega inicial (opción B, CR-001)

Estas pantallas no figuran en la matriz de 03-ux, sección 14; derivan de las pantallas indicadas y se recortan según la estimación de la opción B (los CA del MVP completo no se aplican a ellas sin revisión).

| Mockup | Pantalla UX de origen | RF | HU | Alcance |
|---|---|---|---|---|
| [01-inicio-entrega-inicial.html](01-inicio-entrega-inicial.html) | P01 simplificada | RF-001, RF-018 | HU-001, HU-015 | ENTREGA INICIAL |
| [03-ficha-camper-entrega-inicial.html](03-ficha-camper-entrega-inicial.html) | P03 simplificada | RF-001 | HU-001 | ENTREGA INICIAL |
| [11-solicitud-reserva.html](11-solicitud-reserva.html) | Nueva; deriva de P05 y P06 | RF-006 (parcial), RF-010 (parcial), RF-026 (parcial), RN-026 | HU-005 | ENTREGA INICIAL |
| [12-tarifas-y-condiciones.html](12-tarifas-y-condiciones.html) | Nueva; deriva de P03 y P12 | RF-001, RF-016 (borrador) | HU-001 | ENTREGA INICIAL |
| [10-movil-entrega-inicial.html](10-movil-entrega-inicial.html) | P01 y P05/P06 en ancho móvil (03-ux, sección 8) | RNF-003, RF-001, RF-006 (parcial) | HU-016 | ENTREGA INICIAL |

### Fase siguiente (MVP completo)

Origen: matriz pantalla → requisito de [03-ux/ux-specification.md](../../../03-ux/ux-specification.md), sección 14 (los CA se citan como en la fuente; ver ISS-001 y ISS-023 sobre su reconciliación pendiente).

| Mockup | Pantalla UX | RF | HU | CA | Alcance |
|---|---|---|---|---|---|
| [01-inicio.html](01-inicio.html) | P01 Inicio | RF-002, RF-018 | HU-001, HU-002, HU-015 | CA-028 | MVP propuesto |
| [02-resultados-busqueda.html](02-resultados-busqueda.html) | P04 Resultados (disponibilidad y precio) | RF-002, RF-003, RF-004 | HU-002, HU-003, HU-004 | CA-001, CA-009, CA-015 | MVP propuesto |
| [03-ficha-camper.html](03-ficha-camper.html) | P03 Ficha | RF-001, RF-003 | HU-001, HU-003 | CA-016 | MVP propuesto |
| [04-resumen-y-datos-conductor.html](04-resumen-y-datos-conductor.html) | P05 Resumen · P06 Datos del conductor | RF-004, RF-006 | HU-004, HU-005 | CA-017, CA-034, CA-010, CA-018 | MVP propuesto |
| [05-pago.html](05-pago.html) | P07 Pago | RF-007, RF-008, RF-009 | HU-006, HU-007 | CA-003, CA-006, CA-031 | MVP propuesto |
| [06-confirmacion.html](06-confirmacion.html) | P08 Estado y confirmación | RF-010, RF-032 | HU-008, HU-009, HU-010 | CA-004, CA-005, CA-007, CA-019 | MVP propuesto |
| [07-consulta-reserva.html](07-consulta-reserva.html) | P09 Consulta · P10 Cancelación | RF-011, RF-012, RF-013 | HU-011, HU-012 | CA-013, CA-020, CA-008 | MVP propuesto |
| [08-admin-panel-reservas.html](08-admin-panel-reservas.html) | P14 Acceso · P15 Reservas | RF-019, RF-023 | HU-017, HU-021 | CA-021, CA-022, CA-032 | MVP propuesto |
| [09-admin-flota-tarifas.html](09-admin-flota-tarifas.html) | P16 Flota · P17 Sedes · P18 Tarifas | RF-020, RF-021, RF-022 | HU-018, HU-019, HU-020 | CA-011, CA-012, CA-033, CA-034 | MVP propuesto |
| [10-movil-inicio-y-resultados.html](10-movil-inicio-y-resultados.html) | P01 y P04 en ancho móvil (03-ux, sección 8) | RF-002, RF-003 | HU-002, HU-016 | CA-030 | MVP propuesto |

Pantallas del MVP completo que no se ilustran: P02 Catálogo (RF-001), P11 Contacto (RF-015), P12 Legales y P13 Cookies (RF-016, RF-017), P19 Bloqueos (RF-024) y P20 Pagos y reembolsos (RF-025). Ninguna pantalla ilustrada pertenece a la segunda fase del MVP; las pantallas de la tabla «Fase siguiente» ilustran el MVP completo, no la entrega inicial.

## Pendientes visibles en los mockups

Lo que el cliente debe definir se marca con fondo amarillo y la palabra «pendiente» (por ejemplo: pasarela B1, política de cancelación ISS-002/B3, impuestos PEND-010, fianza PEND-018, segundo paso para cancelar B5, MFA B6, auditoría mínima PEND-038, precio mayor que 0 PEND-039, marca PEND-025, fotos reales PEND-020).

## Convenciones

1. Una pantalla por archivo; cada una indica su origen (`RF`, `HU`, pantalla UX y `CA`).
2. Se conserva la franja «MOCKUP ILUSTRATIVO» y el estado BORRADOR.
3. Solo HTML y `_base.css`: sin `<script>`, sin atributos de evento y sin recursos remotos.
4. Accesibilidad básica: idioma, título, jerarquía de encabezados, etiquetas de formulario, foco visible, enlace «Saltar al contenido», estados con texto y no solo color.
5. Una idea nueva se devuelve al Director como posible `CR-###`.
6. Cada pantalla declara su alcance con una insignia visible con texto («ENTREGA INICIAL» o «FASE SIGUIENTE»), no solo con color.

## Cómo verlos

Abrir `index.html` en el navegador. Los enlaces internos son relativos y funcionan sin conexión.

Los resultados de las verificaciones de estos archivos están en [../checklist-calidad-propuesta.md](../../checklist-calidad-propuesta.md).
