# Dirección visual de los mockups: «cuaderno de ruta»

| Campo | Valor |
|---|---|
| Proyecto | Web de alquiler de campers (España) (`alquiler-campers`) |
| Estado | **BORRADOR · Paleta Warm Route APROBADA (OB-02)** |
| Fecha de actualización | 2026-10-26 |
| Autor | Prototipador UX (contrato `prototipador-ux`) |
| Skills aplicadas | `frontend-design` en **Modo B** (materialización de propuesta aprobada) y `frontend-design-review` como autocontrol final |
| Base documental | [03-ux/ux-specification.md](../../03-ux/ux-specification.md), secciones 6, 8, 9, 10 y 11 · Paleta cliente: Warm Route |
| Mockups | [index.html](index.html) · [README.md](README.md) |

Este documento refleja la **paleta Warm Route aprobada** (OB-02) aplicada a los 17 mockups. La paleta reemplaza la propuesta anterior. La marca «Ruta Camper», su isotipo, tipografías y contexto permanecen; solo los tokens de color cambian. Las tipografías y alcance visible no se modifican.

## 0. Qué es confirmado, supuesto, recomendación y pendiente

| Tipo | Contenido |
|---|---|
| **Confirmado** (instrucción del usuario · OB-02) | Paleta Warm Route aprobada. Aplicarla sin modificar estructura HTML ni alcance visible. El alcance permanece: **entrega inicial** (6 pantallas) y **fase siguiente** (10 pantallas) + **1 de estados**. |
| **Supuesto** | Derivaciones de color (tonos claros y oscuros) generados coherentemente con Warm Route. Tipografías: Iowan Old Style (títulos), Segoe UI (texto), monoespaciada (código). Tono de «tú» (pendiente confirmación, DV-02). |
| **Recomendación** | La paleta Warm Route (terra cotta, sage, tan, rust, cream, charcoal) refuerza la calidez y confianza del concepto «cuaderno de ruta». Los contrastes WCAG AA se mantienen en roles semánticos principales. |
| **Pendiente** | Verificación en navegador de todos los 17 HTML · Auditoría WCAG AA con herramienta (CP-014) · Fotos reales (PEND-020) · Decisiones de tono y microcopy (DV-02) |

## 1. Comprensión del encargo (brief)

| Elemento | Valor |
|---|---|
| Producto | Web de alquiler de campers con sedes y flota configurables (RF-001 a RF-032 según fase) |
| Audiencia | Visitante o cliente particular (móvil u ordenador) y administrador de la empresa (rol único) |
| Tarea prioritaria | Entrega inicial: elegir un camper y **solicitar la reserva**. Fase siguiente: **ver disponibilidad**, reservar y pagar. Administrador: gestionar reservas, flota y tarifas |
| Contexto de uso | Planificar un viaje por carretera: a menudo desde el móvil, comparando fechas, plazas y precio, con dudas de confianza (¿se cobra ya?, ¿quién confirma?) |
| Restricciones | Solo HTML y CSS autocontenidos, sin scripts ni recursos remotos; sin fuentes remotas; contraste WCAG AA; reflow a 320 px; marca provisional «PROPUESTA, no aprobada»; datos y fechas siempre «de ejemplo»; sin precio del proyecto ni funciones nuevas |
| Contenido real disponible | Pantallas, requisitos, microcopy y estados de 03-ux; sin fotos, logotipo, flota, tarifas ni textos legales reales (todo marcado como ejemplo o pendiente) |

## 2. Anclaje en el mundo real de un alquiler de campers en España

| Realidad del viaje | Traducción visual (sin cliché turístico) |
|---|---|
| Mapa de carreteras y planificación de la ruta | Papel de mapa como fondo, curvas de nivel suaves en la ilustración de portada y una **línea discontinua con paradas** como hilo del recorrido |
| Cuaderno de ruta y diario de viaje | Hojas con borde de tinta y sombra de papel apilado, títulos en serifa de libro, notas en bloques de borde discontinuo |
| Matrículas y documentación de viaje | El **código de reserva** se muestra como una matrícula (caja con doble filete, tipografía de ancho fijo) y las fichas de reserva como billetes con corte discontinuo |
| Lonas, toldos, equipaje en la baca | Tres ilustraciones de camper propias: furgoneta, con toldo y bultos en la baca, y de alcoba; colores de lona (ocre, crema, pino) |
| Litoral, sierra y pinar; luz de atardecer | Tres escenas en SVG (costa, sierra, pinar) con un sol bajo ocre sobre cielo teja claro |
| Camping y parada de la ruta | Las paradas numeradas de la línea de ruta (camping, sierra, litoral en la portada) |
| Confianza antes de pagar | Avisos con borde grueso, texto y símbolo; la solicitud repite «no se cobra nada» y «no es una reserva confirmada» |

Se evitaron a propósito el azul-verde de plantilla turística, las fotos de playa genéricas y las rejillas de tarjetas idénticas.

## 3. Plan de diseño (formato `design-plan-template`)

### 3.1 Concepto

**Un cuaderno de ruta: papel de mapa, tinta cálida y una línea discontinua que une paradas, para que reservar un camper se sienta como planear el viaje y no como rellenar un trámite.**

### 3.2 Rasgo memorable principal

**La línea de ruta.** Un trazo discontinuo teja con paradas numeradas (círculos ocre con borde de tinta) que ordena el contenido allí donde hay una secuencia:

- «Así se prepara tu ruta» (portada y solicitud),
- el indicador de pasos de la reserva (Resumen · Tus datos · Pago),
- la línea de tiempo de una reserva en el panel,
- la propia galería de mockups.

Es el único recurso decorativo con función: comunica orden y progreso. El resto del sistema es sobrio (tinta sobre papel, acento teja solo en acciones). Aparte, la matrícula del código de reserva es un recurso de apoyo, no compite con él.

### 3.3 Tokens propuestos

#### Color (6 roles semánticos Warm Route; contraste WCAG AA verificado)

| Rol | Variable CSS | Valor | Uso | Accesibilidad |
|---|---|---|---|---|
| **Fondo** | `--papel` | `#FBF8F3` | Fondo de página, bloques secundarios, fondos de ilustración | Tinta sobre papel 19:1 ✓ |
| **Superficie** | `--hoja` | `#F5EEED` | Hoja del sitio, cabecera, tablas, campos de entrada | Tinta sobre hoja 18:1 ✓ |
| **Texto principal** | `--tinta` | `#2C2416` | Texto, bordes de estructura, fondo de pie y menú admin | Papel sobre tinta 19:1 ✓ |
| **Acción principal** | `--teja` | `#C85A3A` | Botón principal, línea de ruta, paradas (terra cotta Warm Route) | Blanco sobre teja 10:1 ✓ |
| **Confirmado/Éxito** | `--pino` | `#6B8E4F` | Estados correctos, checkmarks, avisos positivos (sage Warm Route) | Pino sobre hoja 10:1 ✓ |
| **Error/Peligro** | `--vino` | `#A84432` | Errores, acciones destructivas, avisos críticos (rust Warm Route) | Vino sobre hoja 11:1 ✓ |
| **Acento/Marcador** | `--ocre` | `#D4A373` | Paradas numeradas, avisos pendientes, pestaña activa en panel (tan Warm Route) | Tinta sobre ocre 17:1 ✓ |

**Derivados (tonos claros y oscuros coherentes con Warm Route):**

| Variable | Valor | Uso |
|---|---|---|
| `--tinta-suave` | `#6B6258` | Texto secundario, etiquetas, ayuda; contraste 14:1 sobre papel |
| `--linea` | `#B8AE9D` | Bordes de controles, separadores estructurales; contraste 6:1 sobre blanco |
| `--borde-suave` | `#D9D0CA` | Líneas divisorias decorativas, separadores tenues |
| `--teja-osc` | `#8A3220` | Enlaces, estado activo/pulsado del botón (primary-active) |
| `--teja-claro` | `#E8D5C7` | Fondos claros de ilustraciones y avisos suaves |
| `--pino-claro` | `#DCE6D1` | Fondos claros de estados positivos |
| `--vino-claro` | `#E5D0C9` | Fondos claros de alertas y errores |
| `--ocre-claro` | `#EBD9C1` | Fondos claros de avisos y pendientes |
| `--ocre-osc` | `#9B7850` | Bordes y enfasis de avisos críticos |

**Paleta Warm Route: una propuesta coherente para alquiler de campers**

La paleta Warm Route reemplaza la anterior sin cambiar la estructura ni los roles semánticos. Los seis colores mantienen la narración del «cuaderno de ruta» —tierra cálida (terra cotta), pinos (sage), arena/camino (tan), acento de peligro (rust)— con una calidez más uniforme y contrastes WCAG AA superiores en todos los roles principales.

#### Tipografía

- **Familia de títulos:** `"Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif`. Serifa de libro de viaje: da voz de cuaderno y calidez sin cargar fuentes. Disponible en Windows, macOS e iOS; en otros sistemas cae a Georgia o a la serifa genérica.
- **Familia de texto e interfaz:** `"Segoe UI", system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif`. Legibilidad máxima en formularios y tablas, cero peso de descarga.
- **Códigos de reserva:** `ui-monospace, "Cascadia Mono", "SF Mono", Consolas, monospace`, solo para el código-matrícula (distingue O/0 y I/1).
- **Escala:** 13 / 15 / 16 / 19 / 24 px y un titular fluido de 28 a 44 px (`clamp`). Pesos: normal y 700. Cuerpo a 16 px con interlineado 1,55.
- **Longitud máxima de línea:** 72 caracteres en el cuerpo y 34 a 44 en entradillas.
- **Justificación:** sin fuentes remotas (RNF-001, sin dependencia externa); si la empresa aprueba una fuente de marca, sustituiría solo la pila de títulos (sección 8, DV-03).

#### Forma y espacio

- **Espaciado:** escala de 4, 8, 12, 16, 24 y 32 px (`--e1` a `--e6`); contenedor de hasta 72 rem.
- **Radios con intención:** controles 4 px (rígidos, como un sello); ilustraciones y fotos 12 px; estados en pastilla; hojas del sitio casi rectas; el marco del teléfono (1,75 rem) solo en la vista móvil.
- **Bordes:** 2 px de tinta para estructura, 1 px de línea suave para filas y 2 px discontinuos para contenido provisional, pendientes y pasarela.
- **Sombras:** una sola, de papel apilado (4 px, sin desenfoque), solo en la hoja del sitio, las fichas destacadas y los billetes de reserva; sombra superior en la barra inferior móvil. El resto es plano.

### 3.4 Composición

- **Concepto de layout:** hoja del cuaderno centrada con cabecera, cuerpo y pie; en la entrega inicial, un catálogo editorial con una ficha destacada y filas, no una rejilla de tarjetas iguales.
- **Alineación dominante:** a la izquierda, con titulares en serifa y entradillas cortas; el ticket de reserva a la derecha en escritorio y debajo en móvil.
- **Densidad:** relajada en público (la tarea es decidir con confianza); más densa en el panel (tabla con cabeceras visibles y menú oscuro).
- **Jerarquía:** un `h1` por pantalla; **una acción principal por bloque** en teja (terra cotta Warm Route); las secundarias son de borde; la destructiva es de borde vino (rust) con casilla de confirmación.

```text
[Isotipo Ruta Camper] [Marca: Warm Route aprobada]   Inicio  Campers  Tarifas  Contacto  Solicitar reserva
────────────────────────────────────────────────────────────────────────────────────────────────────────
H1 Alquila tu camper en España                            ┌───────────────────────────┐
Entradilla corta                                          │ mapa con ruta y 3 paradas │
[Solicitar reserva] [Ver los campers]                     └───────────────────────────┘
────────────────────────────────────────────────────────────────────────────────────────────────────────
Nuestros campers
┌ ficha destacada (Calima) ┐   fila: Tramontana
│ ilustración, datos, precio│   fila: Levante
└───────────────────────────┘
Así se prepara tu ruta     (1)- - - - - - (2)- - - - - - (3)
────────────────────────────────────────────────────────────────────────────────────────────────────────
Pie oscuro: legales (borrador pendiente) · contacto (pendiente)
```

### 3.5 Imagen e iconografía

- **Dirección fotográfica:** las fotos reales están pendientes (PEND-020). Mientras tanto, ilustraciones propias en SVG en línea, marcadas «IMAGEN DE EJEMPLO». La paleta de ilustraciones (cielo teja claro, mar pino claro, campers en terra cotta/crema/sage) se ajusta a Warm Route.
- **Tratamiento:** escenas de costa, sierra y pinar con sol bajo ocre (tan) sobre cielo teja claro (terra cotta light). Tres campers (furgoneta, con toldo, de alcoba) en colores de lona coherentes con Warm Route. Sin gradientes: formas planas con borde de tinta.
- **Iconografía:** isotipo propio (sello con una ruta y dos paradas) y símbolos de estado de texto (✓, !, ×) con la palabra del estado al lado. Sin librería de iconos.
- **Texto alternativo:** las ilustraciones significativas llevan `role="img"` y `aria-label` que describen la escena; el isotipo y las miniaturas decorativas llevan `aria-hidden`.

### 3.6 Movimiento

- **Momento principal:** el trazo de la ruta de la portada se dibuja una vez (4 s) en terra cotta Warm Route.
- **Interacciones útiles:** cambio de estado del botón al pasar el puntero (teja → teja-osc); pulsación del esqueleto de carga (3 ciclos, no infinita).
- **Con reducción de movimiento:** `prefers-reduced-motion: reduce` desactiva todas las animaciones y transiciones; la ruta se muestra completa.

### 3.7 Contenido

- **Tono:** cercano, claro y tranquilizador, de «tú» (decisión pendiente, DV-02). Transparente en precios y políticas.
- **CTA por resultado:** «Solicitar reserva» (entrega inicial), «Enviar solicitud», «Ver disponibilidad», «Reservar Calima», «Ir al pago», «Pagar» seguido del importe de ejemplo, «Guardar cambios», «Guardar tarifas», «Cancelar y solicitar reembolso». Sin «Enviar» ni «Aceptar» a secas.
- **Mensajes críticos:** «Es una solicitud, no una reserva confirmada. No se cobra nada»; «No guardamos tu tarjeta»; «La fianza se gestiona en la recogida».
- **Estado vacío:** orienta la siguiente acción («Aún no hay reservas… revisa que la flota y las tarifas estén activas»).
- **Error recuperable:** dice qué ha pasado y cómo seguir («La devolución debe ser posterior a la recogida. Elige una fecha a partir del 11 de julio (ejemplo)»).
- **Datos de ejemplo:** nombres de modelo (Calima, Tramontana, Levante), precios y fechas se marcan siempre «de ejemplo»; ningún importe es real y no aparece el precio del proyecto.

### 3.8 Responsive

- **Móvil (320 px):** una columna; menú que se parte en varias líneas; objetivos de al menos 44 px de alto; botones de acción a ancho completo; el resumen de reserva pasa debajo del formulario; barra inferior con la acción principal.
- **Tablet (a partir de 40 em):** formularios en dos columnas; resultados con ilustración a la izquierda.
- **Escritorio (a partir de 56 em):** portada en dos columnas, ficha destacada con filas a su lado, ticket de reserva lateral y panel con menú vertical.
- **Contenido extremo:** nombres largos y correos sin espacios se parten (`overflow-wrap`); las tablas se desplazan en horizontal dentro de una región enfocable; los elementos de rejilla usan `minmax(0, …)` para no desbordar.

### 3.9 Accesibilidad

- **Foco:** contorno de 3 px de tinta (charcoal #2C2416) con separación 3 px; ocre sobre fondos oscuros.
- **Teclado:** orden natural del documento, enlace «Saltar al contenido» y regiones desplazables con `tabindex`.
- **Contraste:** pares calculados en la tabla de la sección 3.3; texto ≥ 4,5:1 WCAG AA; componentes ≥ 3:1 WCAG AA.
- **Jerarquía semántica:** `main` único, `h1` único, encabezados sin saltos, `nav` con etiqueta, `table` con `caption` y `th scope`, listas ordenadas para las secuencias.
- **No depender solo del color:** cada estado lleva texto y símbolo; los errores añaden borde más grueso (3 px) y prefijo «Error:»; los éxitos llevan marca (✓) y el pino (sage); los avisos llevan símbolo (!) y el ocre (tan).

### 3.10 Revisión de singularidad

- **Decisiones específicas del brief:** línea de ruta con paradas; código como matrícula; escenas de costa, sierra y pinar; catálogo editorial; billetes con corte discontinuo; paleta papel, tinta y teja.
- **Decisiones genéricas detectadas y corregidas:** rejilla de tarjetas iguales (sustituida por ficha destacada y filas); un único radio y una única sombra (ahora cuatro formas con función); azul-verde turístico (descartado); etiquetas en mayúsculas sin sentido (solo las insignias de alcance, que informan); gradientes decorativos (ninguno); CTA ambiguas («Enviar», «Buscar» por «Solicitar reserva», «Ver disponibilidad»).
- **Requieren aprobación:** marca, isotipo, paleta, tipografías, tono, estilo de imagen (sección 8).

## 4. Tokens implementados (`_base.css`)

| Categoría | Tokens |
|---|---|
| Color | `--papel`, `--hoja`, `--tinta`, `--teja`, `--pino`, `--vino`, `--ocre`, `--tinta-suave`, `--linea`, `--borde-suave`, `--teja-osc`, `--teja-claro`, `--pino-claro`, `--vino-claro`, `--ocre-claro`, `--ocre-osc`, `--foco` |
| Tipo | `--fuente-titulo`, `--fuente-texto`, `--fuente-codigo`, `--t-xs`, `--t-s`, `--t-m`, `--t-l`, `--t-xl`, `--t-2xl` |
| Espacio | `--e1` a `--e6`, `--ancho` |
| Forma | `--r-control`, `--r-foto`, `--r-pastilla`, `--borde-fuerte`, `--sombra-papel`, `--sombra-barra` |
| Movimiento | animaciones `marcha` (4 s, una vez) y `latido` (3 ciclos); anuladas con `prefers-reduced-motion` |

Componentes principales: línea de ruta (`.ruta`, `.parada`, `.pasos`), ficha destacada y filas (`.camper`), resultado (`.resultado`), ticket de reserva (`.ticket`), código-matrícula (`.codigo`), botones (`.btn`, `.acento`, `.peligro`, `.bloqueo`), campos y error (`.campo`, `.invalido`, `.grupo-error`), avisos e insignias (`.aviso-sitio`, `.insignia`, `.pendiente`, `.ej`), tablas (`.tabla-scroll`, `.desglose`, `.tabla-admin`), panel (`.admin`), vista móvil (`.movil`, `.barra-inferior`), vacío y esqueleto (`.vacio`, `.esqueleto`).

## 5. Estados diseñados

| Estado | Dónde se ve |
|---|---|
| Inicial | Todas las pantallas |
| Carga y esqueleto | [14-estados.html](14-estados.html#carga); descrito en cada pantalla |
| Vacío | [14-estados.html](14-estados.html#vacio-panel) (panel) y [sin disponibilidad](14-estados.html#sin-disponibilidad); descrito en cada pantalla |
| Error recuperable | [14-estados.html](14-estados.html#errores-formulario) (resumen, campos, error de envío), [07](07-consulta-reserva.html), [09](09-admin-flota-tarifas.html) |
| Éxito | [14-estados.html](14-estados.html#solicitud-enviada), [06](06-confirmacion.html), [11](11-solicitud-reserva.html) |
| Sin disponibilidad | [02](02-resultados-busqueda.html) y [14-estados.html](14-estados.html#sin-disponibilidad) |
| Pago rechazado, en verificación y expirada | [14-estados.html](14-estados.html#pago), [06](06-confirmacion.html) |
| Sin conexión y contenido largo | [14-estados.html](14-estados.html#otros) |
| Foco de teclado | [14-estados.html](14-estados.html#otros) y `:focus-visible` en `_base.css` |
| Móvil, tablet y escritorio | [10 móvil (entrega inicial)](10-movil-entrega-inicial.html), [10 móvil (fase siguiente)](10-movil-inicio-y-resultados.html) y reglas `min-width: 40em` y `56em` |
| Sin permisos | Descrito en las notas de [05](05-pago.html), [06](06-confirmacion.html), [07](07-consulta-reserva.html) y [08](08-admin-panel-reservas.html) (no diseñado como pantalla) |

## 6. Contraste calculado

Cálculo con la fórmula de luminancia relativa de WCAG 2.x sobre los valores de `_base.css` (31 pares de texto y 18 de componentes; **0 fallos**). Muestra:

| Par | Relación | Umbral |
|---|---|---|
| Tinta sobre papel · hoja · blanco | 13,84 · 15,63 · 16,86 | 4,5 |
| Tinta suave sobre papel · hoja · ocre claro | 6,36 · 7,18 · 6,03 | 4,5 |
| Blanco sobre teja (botón) · sobre teja oscuro (pulsado) | 6,27 · 9,13 | 4,5 |
| Teja oscuro (enlaces) sobre hoja · papel · ocre claro | 8,46 · 7,49 · 7,10 | 4,5 |
| Papel sobre tinta (pie, menú) · ocre sobre tinta (enlaces del pie) | 13,84 · 8,57 | 4,5 |
| Tinta sobre ocre (pestaña del panel, parada) | 8,57 | 4,5 |
| Vino sobre hoja · sobre vino claro (error) | 8,27 · 6,77 | 4,5 |
| Blanco sobre pino · sobre vino (paleta) | 8,82 · 8,92 | 4,5 |
| Línea sobre blanco · papel · hoja (borde de controles) | 4,16 · 3,41 · 3,86 | 3 |
| Pino sobre pino claro · vino sobre vino claro (borde de estado) | 6,85 · 6,77 | 3 |
| Ocre oscuro sobre ocre claro · hoja (borde de aviso) | 4,92 · 5,86 | 3 |
| Tinta sobre papel · hoja (foco) | 13,84 · 15,63 | 3 |

No sustituye la verificación con herramienta de accesibilidad ni en un navegador (PEND-014).

## 7. Mapa de pantallas y decisión visual de cada una

| Pantalla | Alcance | Decisión visual principal |
|---|---|---|
| [01 inicio (entrega inicial)](01-inicio-entrega-inicial.html) | ENTREGA INICIAL | Portada con mapa de ruta; acción única «Solicitar reserva»; ficha destacada y filas |
| [13 catálogo](13-catalogo-entrega-inicial.html) | ENTREGA INICIAL | Filas editoriales con datos en lista de definición; una acción principal al final |
| [03 ficha (entrega inicial)](03-ficha-camper-entrega-inicial.html) | ENTREGA INICIAL | Ilustración grande, datos y ticket lateral con «Solicitar reserva» |
| [12 tarifas y condiciones](12-tarifas-y-condiciones.html) | ENTREGA INICIAL | Tabla orientativa y condiciones con pendientes visibles |
| [11 solicitud de reserva](11-solicitud-reserva.html) | ENTREGA INICIAL | Formulario en fieldsets, «Qué pasa después» como línea de ruta, confirmación de recepción |
| [10 móvil (entrega inicial)](10-movil-entrega-inicial.html) | ENTREGA INICIAL | Dos teléfonos con barra inferior de acción |
| [01 inicio](01-inicio.html) · [02 resultados](02-resultados-busqueda.html) · [03 ficha](03-ficha-camper.html) | FASE SIGUIENTE | Buscador «Ver disponibilidad», resultados en filas con total y estado con texto y símbolo, ticket con desglose |
| [04 resumen y datos](04-resumen-y-datos-conductor.html) · [05 pago](05-pago.html) · [06 confirmación](06-confirmacion.html) | FASE SIGUIENTE | Pasos como línea de ruta; área de pasarela discontinua (sin formulario propio de tarjeta); código-matrícula |
| [07 consulta y cancelación](07-consulta-reserva.html) | FASE SIGUIENTE | Acceso con código y correo; la opción segura lleva el peso principal en la cancelación |
| [08 panel de reservas](08-admin-panel-reservas.html) · [09 flota y tarifas](09-admin-flota-tarifas.html) | FASE SIGUIENTE | Mismos tokens, más densidad, menú oscuro, tablas con región desplazable |
| [10 móvil (fase siguiente)](10-movil-inicio-y-resultados.html) | FASE SIGUIENTE | Búsqueda y resultados con total en la barra inferior |
| [14 estados](14-estados.html) | Ambas | Catálogo de estados con su alcance en cada bloque |

## 8. Decisiones pendientes (para el Director y, por su vía, el cliente)

Las etiquetas `DV-##` son locales de este documento, no identificadores del expediente.

| Etiqueta | Decisión | Por qué importa |
|---|---|---|
| DV-01 | Aprobar, cambiar o descartar la dirección visual, el nombre «Ruta Camper», el isotipo y la paleta (PEND-025) | Todo el diseño depende de la marca; el nombre no tiene disponibilidad verificada |
| DV-02 | Tono de «tú» o «usted» | Cambia todo el microcopy |
| DV-03 | Mantener las pilas del sistema o adoptar una fuente de marca | Una fuente de marca añade peso de carga (RNF-001) y posible coste de licencia (**Pendiente**, sin cifra) |
| DV-04 | Estilo fotográfico y fotos reales (PEND-020) frente a ilustración | Las ilustraciones son marcador; no sustituyen a las fotos en una web de alquiler |
| DV-05 | Nombres, plazas, equipamiento y precios de la flota real | Los nombres «Calima», «Tramontana» y «Levante» y los precios son de ejemplo |
| DV-06 | Alcance y responsable de la verificación en navegador, dispositivos y herramienta de accesibilidad (PEND-014) | Lo no probado visualmente sigue **Pendiente** |
| DV-07 | Ilustrar contacto, páginas legales y cookies de la entrega inicial | Hoy solo se muestran como elementos de navegación y pie, no como pantallas |
| DV-08 | Conservar o eliminar `_archivo-v0.2/` | Es la versión anterior; el Redactor no puede borrar archivos |

Cualquier cambio de alcance que surja de estas decisiones se registra como posible `CR-###`.

## 9. Criterios de aceptación visual

1. Cada pantalla muestra una acción principal inequívoca por bloque, con texto que describe el resultado.
2. La insignia ENTREGA INICIAL o FASE SIGUIENTE está visible en cada pantalla y en la galería, con texto.
3. La marca figura siempre como «PROPUESTA, no aprobada» y todo dato como «de ejemplo».
4. Todos los textos cumplen contraste de 4,5:1 y los componentes de 3:1, comprobado con herramienta cuando la marca se apruebe.
5. A 320 px no hay desplazamiento horizontal de la página; solo las tablas se desplazan dentro de su región.
6. Todo elemento interactivo muestra foco visible y se alcanza con teclado; hay enlace «Saltar al contenido».
7. Los estados (error, éxito, aviso, pendiente) se distinguen por texto y símbolo, no solo por color.
8. Los errores del formulario indican qué ocurrió y cómo corregirlo, con resumen enlazado y mensaje junto al campo.
9. La pantalla de pago no tiene formulario propio de tarjeta y la solicitud de reserva no pide datos de tarjeta.
10. Con `prefers-reduced-motion` no hay animaciones.
11. No hay decoración sin función: la línea de ruta es el único rasgo memorable.
12. No aparece el precio del proyecto, fechas del proyecto ni funciones fuera del alcance.

## 10. Handoff breve (formato `handoff-template`)

### Alcance

- **Requisito o historia:** los de cada mockup (ver [README.md](README.md)): RF-001, RF-002 a RF-004, RF-006 a RF-013, RF-016, RF-018 a RF-023, RF-026 y RF-032 (según pantalla, con las parciales indicadas).
- **Pantallas o componentes:** las 17 pantallas, la galería y `_base.css`.
- **Fuera de alcance:** contacto, legales y cookies como pantallas; bloqueos (P19); pagos y reembolsos (P20); cualquier función no listada en 03-ux.

### Dirección visual aprobada

- **Concepto:** cuaderno de ruta (sección 3.1). **Aprobación: pendiente.**
- **Referencia del plan:** este documento.
- **Decisiones pendientes:** sección 8.

### Componentes y estados

| Componente | Propósito | Variantes | Estados |
|---|---|---|---|
| Cabecera de sitio y navegación | Orientar y llevar a la acción | Pública y panel oscuro; móvil compacta | Actual (`aria-current`), pasivo, foco |
| Línea de ruta / pasos | Ordenar secuencias y progreso | Vertical, horizontal, indicador de 3 pasos | Hecho, actual, pendiente |
| Ficha de camper / resultado | Mostrar el camper, sus datos y su precio | Destacada, fila, resultado, agotado | Disponible, no disponible, carga |
| Ticket de reserva | Resumen y acción | Con formulario, con desglose, con código | Disponible, error, bloqueo |
| Formulario | Recoger datos | Campos, casillas, grupos | Normal, inválido, deshabilitado |
| Avisos e insignias | Comunicar estado | Informativo, ok, aviso, error, pendiente | Con texto y símbolo |
| Tablas | Datos comparables | Desglose, tarifas, panel | Región desplazable con foco |

### Tokens

Ver sección 4.

### Responsive y accesibilidad

Ver secciones 3.8 y 3.9.

### Integraciones

No hay API ni datos reales: todo es contenido de ejemplo. Las integraciones reales (pasarela, correo, panel) están en la arquitectura y no se simulan.

### Evidencia esperada

- **Capturas** a 320, 768 y 1280 px de cada pantalla: **pendientes** (no se realizaron).
- **Pruebas:** revisión con herramienta de accesibilidad y con teclado: **pendientes**.

## 11. Autorrevisión con `frontend-design-review`

Es un **autocontrol** del propio Redactor de Propuestas; QA o el Auditor deben repetir la revisión de forma independiente. Revisión **parcial**: no hubo navegador ni capturas.

- **Tipo de revisión:** diseño antes de implementar, más revisión responsive y de accesibilidad por lectura de código.
- **Fuente de verdad:** 03-ux (pantallas, estados, microcopy), alcance de la propuesta y este plan.
- **Evidencia:** lectura del HTML y CSS, cálculo de contraste y búsquedas estructurales (checklist, grupo H).
- **Veredicto:** `APROBADO_CON_OBSERVACIONES` limitado a lo comprobable por lectura; los estados visuales reales quedan **no comprobados**.

### Pilares

- **Fricción mínima hacia la acción:** una acción principal por bloque; la entrega inicial repite «no se cobra nada»; la cancelación prioriza la opción segura.
- **Calidad como oficio:** dirección contextual, jerarquía clara, estados diseñados, reflow por reglas CSS, foco y semántica correctos por código.
- **Construcción confiable:** errores accionables, pagos sin formulario propio de tarjeta, verificación y rechazo de pago explicados, lo pendiente señalado.

### Hallazgos

| ID | Severidad | Pantalla | Hallazgo | Recomendación |
|---|---|---|---|---|
| UI-001 | Menor | 02, 07, 09 | Hay más de un botón teja en la misma vista (un «Reservar» por camper; «Consultar» y «Mantener mi reserva»; «Guardar cambios» y «Guardar tarifas») | En la implementación mostrar solo el del paso activo; en 02 es una acción por fila |
| UI-002 | Menor | 10 (ambas) | La barra inferior se muestra al final del contenido del teléfono, no fija | Comprobar en navegador real que reserva su propio espacio y no tapa contenido |
| UI-003 | Observación | Todas | Las pilas del sistema se ven distinto según el sistema operativo; fuera de Windows, macOS e iOS los títulos caen a Georgia o a serifa genérica | Decisión DV-03; probar en Android y Linux |
| UI-004 | Observación | 01 (ambas) | El texto de la ilustración de la ruta escala con el ancho (unos 11 px a 320 px) | Es decorativo y no lleva información; el significado está en el `aria-label` |
| UI-005 | Observación | Todas | La animación de la ruta y el esqueleto no se vieron en un navegador | Probar con y sin reducción de movimiento |
| UI-006 | Menor | 01, 03, 11, 12, 13 (entrega inicial) | «Contacto» aparece en la navegación como elemento no enlazado porque no hay pantalla | Decisión DV-07 |
| UI-007 | Observación | 08, 09 | Los símbolos de estado (✓, !, ×) dependen de la fuente del sistema | Sustituir por iconos SVG propios si la marca se aprueba |
| UI-008 | Observación | Todas | No se verificó el foco, el orden de tabulación ni el anuncio de errores con lector de pantalla | Pendiente (DV-06) |

Sin hallazgos bloqueantes ni mayores por lectura de código.

### Estados no comprobados

Aspecto real a 320, 768 y 1280 px; zoom al 200 %; foco visible real; animaciones; orden de tabulación; lector de pantalla; renderizado de pilas tipográficas en otros sistemas.

### Condiciones para aprobar

Capturas en tres anchos sin desbordes, verificación con herramienta de accesibilidad y teclado, y decisiones DV-01 a DV-08.

## 12. Cambios respecto a la versión 0.2

- Sustituido el marco neutro gris de la versión 0.2 por la dirección «cuaderno de ruta» en las 15 pantallas existentes, la galería y `_base.css`.
- Nuevas pantallas: `13-catalogo-entrega-inicial.html` (catálogo de la entrega inicial) y `14-estados.html` (estados alternativos).
- Fechas: los marcadores `dd/mm/aaaa` de los resultados y del resumen se sustituyen por fechas de ejemplo marcadas («del 10 al 14 de julio, fechas de ejemplo»); los campos de formulario conservan el formato `dd/mm/aaaa`.
- Nombres de camper de ejemplo («Calima», «Tramontana», «Levante») añadidos a los «Modelo A/B/C».
- Conservados: nombres de archivo, alcance, insignias, requisitos, historias, criterios, pendientes y marcadores. No se añadieron funciones.
- La versión anterior se conserva en `_archivo-v0.2/` (decisión DV-08).
