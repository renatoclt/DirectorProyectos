# Checklist de calidad de la propuesta — Web de alquiler de campers (España)

| Campo | Valor |
|---|---|
| Proyecto | `alquiler-campers` |
| Revisión realizada por | Redactor de Propuestas |
| Fecha | 2026-10-26 |
| Versión revisada | 0.3 (mockups rediseñados con las Skills `frontend-design` y `frontend-design-review`; oferta principal: opción B, entrega inicial acotada, CR-001) |
| Estado de la propuesta | BORRADOR |

Marca cada fila con `Cumple`, `No cumple`, `No aplica` o `Pendiente` (verificación no realizable por el Redactor o solo parcial) y deja evidencia. No se marca `Cumple` si la verificación no se realizó. Las verificaciones se ejecutaron con búsquedas de texto y scripts de lectura sobre los archivos de esta carpeta el 2026-10-26. Los grupos A a D, F y G se ejecutaron **después de las últimas ediciones de la versión 0.2**, y en la versión 0.3 se volvieron a ejecutar sobre los mockups y los documentos que los enlazan (filas A1, A2, D3, E1 a E5 y G1, y el nuevo grupo H); los resultados citados son los obtenidos en esa ejecución. **Ninguna verificación se hizo en un navegador**: lo que requiere navegador o herramienta de accesibilidad figura como `Pendiente`.

## A. Integridad de datos

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| A1 | No hay fechas inventadas; toda fecha proviene del cliente o de un registro del expediente | Cumple | Búsqueda de `AAAA-MM-DD`, `dd/mm/aaaa` numérico, nombres de mes y de día de la semana en `*.md`, `*.html` y `_base.css` (sin este checklist ni `_archivo-v0.2/`): la única fecha ISO es 2026-10-26 (fecha de elaboración); los nombres de mes aparecen solo en las fechas ficticias del producto de los mockups («del 10 al 14 de julio», «1 jun – 15 jul»), y en los 12 archivos que los contienen todas las líneas con mes incluyen la palabra «ejemplo» (0 líneas sin ella). Son datos de ejemplo del producto, no fechas del proyecto; los campos de formulario conservan el formato `dd/mm/aaaa` como marcador |
| A2 | No hay costos ni cifras inventadas; la inversión es el valor aportado por el Director o PENDIENTE | Cumple | Búsqueda de cifras con moneda (`USD`, `EUR`, `€`, `$`, «dólares», «euros») en los `.md` de la carpeta: la única cifra monetaria es **400 USD** (valor fijado por el usuario) en la propuesta, el análisis, el README y el perfil; `mockups/README.md` y `mockups/direccion-visual.md` no contienen cifras monetarias. Los importes de los mockups son datos ficticios: en las 17 pantallas, 37 líneas con `€` y 0 sin la palabra «ejemplo» en la misma línea; `USD` y `400` = 0 en los mockups |
| A3 | No hay clientes previos, certificaciones, casos de éxito ni credenciales que no estén en `perfil-empresa.md` | Cumple | `perfil-empresa.md` no contiene datos de empresa: identidad, experiencia y credenciales son marcadores `{{PENDIENTE: ...}}`. La sección 1 de la propuesta describe solo la forma de trabajo (respaldada por las reglas del equipo), marcada «Recomendación (práctica de trabajo)» |
| A4 | Disponibilidad, canales y horarios provienen del perfil de empresa | Cumple | Canales, horario, tiempo de respuesta, formato y canal de feedback son marcadores `{{PENDIENTE: ...}}` en la propuesta (sección 7) y en el perfil (sección 6). Lo que se propone (revisión por hitos D1, D2, D5, D6 y D7; feedback en un día hábil; un único portavoz) está marcado «Recomendación» |
| A5 | La fecha calendario solo existe si el cliente confirmó la fecha de inicio; si no, dice PENDIENTE | Cumple | Propuesta, secciones 6 y 11.4: «Fecha de inicio: PENDIENTE» y fecha de entrega «PENDIENTE»; la tabla 6.2 «Día relativo → fecha» muestra la fórmula (D1 + n días hábiles) y «PENDIENTE» en las 7 filas de fecha |

## B. Plazo

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| B1 | El plazo proviene de la estimación sustentada del Planificador | Cumple | Opción B: «1 semana (5 días hábiles) para entrega a revisión; publicación en D7–D10», hitos D1 a D7, supuestos y condiciones, tal como figuran en `05-planning/estimacion-opcion-b.md`. Fase siguiente: 28–36 semanas (probable 30–31), tal como figuran en `05-planning/estimacion-plazo.md` (ya persistida; la versión 0.1 pedía persistirla). Los extremos del método (22 y 45) no se comunican como oferta |
| B2 | Se muestran supuestos de equipo y capacidad, condiciones y holgura | Cumple | Propuesta, secciones 5.2, 6 (riesgo alto y sin holgura), 6.1 (5 condiciones necesarias), 6.3 (supuestos) y 6.4 (condiciones que mueven el plazo); para la fase siguiente, 11.4 (supuestos, contingencia del 15 al 20 %, un solo backend +25–40 %) |
| B3 | Está marcado como Recomendación a confirmar y no como compromiso | Cumple | Sección 6: «Recomendación a confirmar, no un compromiso» (el objetivo de 1 semana figura como Confirmado por el usuario, su calificación como entrega a revisión como Recomendación); sección 11: «Es una Recomendación a confirmar, no un compromiso» |
| B4 | Los hitos son relativos al inicio | Cumple | Tabla 5.1 (D1 a D7), tabla 6.2 (fórmula y «PENDIENTE») y 11.4 (S0 a ~S30); sin fechas |

## C. Alcance y consistencia

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| C1 | El alcance coincide con requisitos y MVP; no se agregó nada nuevo | Cumple | Script: los 25 RF de la sección 11.1 de la propuesta (MVP completo) coinciden exactamente con los RF del MVP del Product Manager (RF-001 a RF-004, RF-006 a RF-013, RF-015 a RF-026 y RF-032; sin sobrantes ni faltantes). La cobertura de la entrega inicial (3.2 y análisis B.3) se comparó con la fila de CR-001 en `00-control/CHANGE-REQUESTS.md`: 3 RNF cubiertos, 8 RF + RN-026 + 6 RNF parciales y 18 RF + RN-003 + RN-010 + 4 RNF no cubiertos, igual en ambos. Los cambios de seguridad se presentan como **cambios recomendados pendientes de decisión** |
| C2 | Se separan entrega inicial, MVP completo, segunda fase, ampliaciones y exclusiones | Cumple | Propuesta: 3.1 (incluido), 3.3 (no incluido), 11.1 (MVP completo), 11.2 (segunda fase, ampliaciones y exclusiones); análisis: secciones B.2 y 3 |
| C3 | Cada afirmación relevante está marcada Confirmado, Supuesto, Recomendación o Pendiente | Pendiente | Verificación solo estructural: las tablas de alcance, solución, plan, equipo, comunicación, inversión, riesgos y decisiones tienen columna Estado; las que no la tienen son datos de control (cabeceras, fórmula, costes, aceptación, anexos). La revisión semántica de cada afirmación queda para el Director |
| C4 | Ningún supuesto se presenta como requisito confirmado | Cumple | Los RF «Confirmado» en la 11.1 (RF-001, 002, 003, 008, 011, 018 y RF-020 a RF-022) son los que las fuentes marcan [C]; RF-012 y RF-019 figuran como Supuesto. La opción B, la semana y los 400 USD figuran como Confirmado **solo** por instrucción del usuario; la aceptación del cliente figura Pendiente (OB-03, 12.3). Las respuestas delegadas («pon tu las reglas», etc.) se tratan como Recomendación |
| C5 | Las contradicciones entre fuentes están señaladas, no resueltas en silencio | Cumple | Análisis, sección 9.4 (ISS-001 a ISS-033); propuesta, sección 2: tensión «presupuesto y fechas fuera del contrato» frente a un valor y un plazo ofertados (OB-12); sección 3.4: desviación de RN-001 y RNF-010; sección 11: 28–36 semanas y 1 semana son alcances distintos (ISS-040) |
| C6 | La sección 10 lista las preguntas que cambian alcance, plazo o inversión | Cumple | Propuesta, sección 10: 14 preguntas de la entrega inicial (OB-01 a OB-14) y 37 de la fase siguiente (grupos B.1 a B.5), cada una con «por qué importa» e impacto |

## D. Trazabilidad y fuentes

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| D1 | Los identificadores RF, RNF, RN, HU, CA, R, ADR, DEC y CR se conservan sin renumerar | Cumple | Script: ningún identificador fuera de rango en propuesta y análisis (RF ≤ 032, RNF ≤ 014, RN ≤ 027, HU ≤ 036, CA ≤ 034, DEC ≤ 032, ADR ≤ 012, SEG ≤ 017, ISS ≤ 033, PEND ≤ 040, CR = 001). Los riesgos de la opción B usan el calificador **[OPB]** (igual que `00-control/RISKS.md`); las etiquetas OB-01 a OB-14 son locales de la propuesta y no identificadores del expediente. Las referencias PEND-043 a PEND-047 y DEC-034 se tomaron de `00-control/` (no verificadas una por una en esta revisión salvo las citadas) |
| D2 | Cada requisito del MVP aparece en la tabla de trazabilidad del análisis | Cumple | Script: los 25 RF del MVP aparecen en la tabla 10.1 del análisis (sin cambios) |
| D3 | Todas las fuentes están citadas con enlace relativo a un archivo existente | Cumple | Script sobre todos los enlaces relativos de los `.md` y `.html` de la carpeta (sin este checklist ni `_archivo-v0.2/`): 622 enlaces en 24 archivos, 0 rotos y 0 fragmentos (`#id`) que no existan en la página de destino |
| D4 | El análisis está en un único archivo: `analisis-consolidado.md` | Cumple | La carpeta contiene un único archivo de análisis; la opción B es una sección dentro de él |

## E. Mockups

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| E1 | Cada mockup está enlazado desde `mockups/index.html` y desde la sección 4 de la propuesta | Cumple | Script: las 17 pantallas (`01-` a `14-`, incluidas las 3 variantes `-entrega-inicial`, el catálogo `13` y los estados `14`) aparecen en `index.html`, en `mockups/README.md` y en la sección 4 de la propuesta (tablas 4.1 y 4.2 y texto bajo 4.1, para `14`); `direccion-visual.md` está enlazado desde la galería, el README, la propuesta y el análisis |
| E2 | Cada mockup indica sus RF, HU o pantalla UX de origen | Cumple | Búsqueda: 17 de 17 pantallas incluyen «Origen:» en su cabecera; el mapa está en `mockups/README.md`. Los mockups 11, 12 y 13 indican que derivan de P05/P06, P03/P12 y P02 y de la opción B (no figuran en la matriz de 03-ux); el 14 indica las pantallas de las que toma los estados |
| E3 | Los mockups declaran ser ilustrativos y no diseño final | Cumple | Búsqueda: «MOCKUP ILUSTRATIVO» (o «MOCKUPS ILUSTRATIVOS» en la galería) y «No es diseño final aprobado» (o «No son diseño final aprobado») en las 17 pantallas y la galería. La marca «Ruta Camper» está rotulada «PROPUESTA, no aprobada» en las 18 páginas (sello en la cabecera de las pantallas con sitio; texto en la galería y en la pantalla 14) |
| E4 | No hay scripts ni recursos remotos (`http`, CDN, fuentes o imágenes externas) | Cumple | Búsquedas sin distinguir mayúsculas en `mockups/*.html` y `_base.css` (19 archivos): `http` = 0; `<script` = 0; atributos `on…=` = 0; `url(`, `@import`, `<img`, `<iframe`, `<object`, `<embed` = 0; `style=` (CSS en línea) = 0; `gradient` = 0. El único recurso enlazado es `_base.css` local; las imágenes son SVG en línea con referencias internas `<use href="#…">`; las fuentes son pilas del sistema. La pantalla de pago sigue sin formulario propio de tarjeta; la solicitud de reserva (11) no pide datos de tarjeta |
| E5 | Cada pantalla declara si pertenece a la entrega inicial o a la fase siguiente con una insignia visible | Cumple | Búsqueda y script: «ENTREGA INICIAL» o «FASE SIGUIENTE» como insignia (`class="fase"`) en las 17 pantallas y en `index.html` (18 de 18 archivos); el texto de la insignia informa y el color solo refuerza. Entrega inicial: 01 y 03 (variantes), 10 (variante móvil), 11, 12 y 13. Fase siguiente: 01, 02, 03, 04, 05, 06, 07, 08, 09 y 10 originales. `14` y la galería muestran ambas, y cada bloque de `14` indica la suya |

Verificaciones adicionales de los mockups (script, 17 pantallas más la galería, versión 0.3): un `<h1>` y un `<main>` por página; sin saltos en la jerarquía de encabezados; 51 campos (`input`, `select`, `textarea`), todos con `<label for>`; 0 identificadores duplicados; 0 anclas, referencias `<use>` y `aria-labelledby` o `aria-describedby` apuntando a un id inexistente; `lang="es"`, `<title>`, `viewport` y enlace «Saltar al contenido» en todas; todo SVG significativo con `role="img"` y `aria-label` y los decorativos con `aria-hidden`; foco visible definido con `:focus-visible` en `_base.css`. **No se verificó con herramienta de accesibilidad ni en un navegador** (ver H7).

## F. Marcadores y estado

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| F1 | Los marcadores `{{PENDIENTE: ...}}` están visibles y listados en la entrega | Cumple | Conteo por búsqueda (sin contar ejemplos de sintaxis): 40 en `perfil-empresa.md` y 20 en `propuesta-comercial.md` (60 en total), más 18 «PENDIENTE» sin llaves en la propuesta (fecha de inicio y de entrega, tabla día → fecha, aceptación y menciones en la vista rápida y el resumen). Listados por grupo en `README.md` |
| F2 | Estado declarado: BORRADOR, EN REVISIÓN o APROBADO; APROBADO solo con aprobación humana registrada | Cumple | «BORRADOR» declarado en `README.md`, `propuesta-comercial.md`, `analisis-consolidado.md`, `perfil-empresa.md`, este checklist, `mockups/README.md` y los HTML; no se declara APROBADO |
| F3 | Se aclara que la propuesta no equivale a aprobar el alcance ni CR-001 | Cumple | Aviso de estado al inicio de la propuesta («No equivale a aprobar el alcance» ni CR-001); `README.md`; secciones 12.1 y 12.3 (aceptación sin firma presunta) |
| F4 | Solo se escribió en `projects/alquiler-campers/12-propuesta/` | Cumple | Revisión de marcas de tiempo desde el inicio de esta actualización: los archivos modificados fuera de `12-propuesta/` son los de `00-control/` y `05-planning/estimacion-opcion-b.md`, escritos por el Director y otros agentes en la misma ventana de tiempo (no por este agente, que solo escribió en la carpeta); dentro de `12-propuesta/` los modificados son los listados en `README.md`. En la versión 0.3 el Redactor de Propuestas solo creó, editó o movió archivos dentro de `12-propuesta/` (incluida la copia `mockups/_archivo-v0.2/`) |
| F5 | El texto usa lenguaje claro para el cliente | Pendiente | Verificación objetiva parcial: los términos técnicos residuales (MFA, 3-D Secure, SPF/DKIM/DMARC, RPO/RTO, WCAG) se explican en el texto o se limitan a la fase siguiente. La claridad es un juicio humano: queda para la revisión del Director |

## G. Opción B (verificaciones específicas de la versión 0.2)

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| G1 | No aparece la aritmética precio/hora ni consejos de negociación | Cumple | Búsqueda en todos los `.md` y `.html` (sin este checklist) de patrones de tarifa por hora o por día, «por hora», cifras seguidas de «h», «horas de», «aritm…», «ceder» y «recortar el precio»: 0 coincidencias relacionadas con precio (en los `.md`, las únicas con «horas de» son «horas de recogida y devolución», de los requisitos del MVP). En la versión 0.3 se repitió sobre los 17 mockups y los 2 `.md` nuevos de `mockups/` (también con `×`, `NxN` y `= N`): las únicas coincidencias son falsos positivos («width=» del `viewport`, «acceder» y el símbolo «×» de estado de error en `direccion-visual.md`); los mockups no muestran multiplicaciones de precio, solo líneas de desglose con su importe de ejemplo. La sección interna de `estimacion-opcion-b.md` no se copió; el esfuerzo se expresa en días de plazo, nunca en horas ni en tarifa. La palabra «negociación» aparece solo en el título y el texto del margen de negociación (sección 8.2, sin cifras ni descuentos) |
| G2 | El precio solo es 400 USD | Cumple | Búsqueda de cifras con moneda (ver A2): única cifra `400 USD`, 7 menciones en la propuesta; ninguna conversión; 0 menciones de «descuento» con cifra; la fase siguiente no tiene cifra |
| G3 | Moneda de facturación e IVA marcados pendientes | Cumple | Propuesta, secciones «Qué está confirmado», 8.1 (filas «Moneda de facturación» e «IVA e impuestos»: Pendiente) y OB-04; perfil, sección 7 (`{{PENDIENTE: moneda de facturación e IVA ...}}`) |
| G4 | No hay fechas calendario | Cumple | Ver A1 y A5; la fórmula usa «fecha de inicio confirmada» (PENDIENTE) |
| G5 | El plazo de 1 semana está calificado como entrega a revisión y con condiciones | Cumple | Propuesta: 10 menciones de «entrega a revisión»; sección 6 («1 semana (5 días hábiles) para la entrega a revisión; publicación en D7–D10 según DNS y aprobación», riesgo alto, sin holgura) y 6.1 (condiciones necesarias) |
| G6 | La fase siguiente no tiene precio | Cumple | Propuesta, secciones 8.3 y 11 («Sin precio … Se cotizará aparte») y 11.6; la sección 11 no contiene cifras monetarias (búsqueda) |
| G7 | La propuesta mantiene separados los alcances de 1 semana y de 28–36 semanas | Cumple | Resumen ejecutivo y sección 11: la estimación 28–36 se declara del MVP completo y no se reestimó (ISS-040); no se suman |
| G8 | La desviación de RN-001 y RNF-010 se presenta al cliente como decisión a aceptar, no como aceptada | Cumple | Propuesta, sección 3.4 y OB-03; análisis, B.4 |

## H. Diseño con Skills (versión 0.3)

Se aplicaron `frontend-design` (Modo A: dirección y especificación) y `frontend-design-review` (autocontrol) de `.github/skills/`. Todo lo que exige navegador o herramienta de accesibilidad queda `Pendiente`.

| # | Verificación | Resultado | Evidencia |
|---|---|---|---|
| H1 | `frontend-design` aplicada con plan de diseño | Cumple | [mockups/direccion-visual.md](mockups/direccion-visual.md) contiene el flujo obligatorio de la Skill: comprensión del encargo (sección 1), anclaje en el mundo real (2), plan de diseño con concepto, rasgo memorable, paleta de 6 colores, tipografía y escala, forma y espacio, composición, imagen e iconografía, movimiento, contenido, responsive, accesibilidad y revisión de singularidad (3), tokens (4), estados (5), decisiones pendientes (8), criterios de aceptación visual (9) y handoff (10). Marcado BORRADOR y PROPUESTA, no aprobada. La calidad del diseño es un juicio que corresponde al Director y al cliente |
| H2 | Checklist anti-genérico revisado | Cumple | Sección 3.10 de `direccion-visual.md`: decisiones genéricas detectadas y corregidas (rejilla de tarjetas iguales sustituida por ficha destacada y filas; un único radio y sombra sustituidos por cuatro formas con función; sin gradientes: `gradient` = 0 en `_base.css`; mayúsculas solo en las insignias de alcance; CTA por resultado). Revisión por lectura del código; el aspecto real queda en H7 |
| H3 | Estados cubiertos | Cumple | `14-estados.html` incluye sin disponibilidad, errores del formulario (resumen, campos y envío), enviando y solicitud enviada, pago rechazado, en verificación y reserva expirada, vacío del panel, esqueleto de carga, sin conexión, contenido largo y foco de teclado; cada pantalla describe sus estados y la sección 5 de `direccion-visual.md` los mapea. Salvedad: «sin permisos» se describe en notas, no se diseña como pantalla |
| H4 | `frontend-design-review` ejecutada como autocontrol | Cumple | Sección 11 de `direccion-visual.md`: veredicto `APROBADO_CON_OBSERVACIONES`, parcial y sin navegador, con 8 hallazgos (UI-001 a UI-008: 3 menores y 5 observaciones; 0 bloqueantes y 0 mayores) y estados no comprobados. Es un autocontrol: QA o el Auditor deben repetir la revisión de forma independiente |
| H5 | Contraste calculado | Cumple | Cálculo con la fórmula de luminancia relativa de WCAG sobre los tokens de `_base.css`: 31 pares de texto (mínimo 5,88:1, umbral 4,5) y 18 de componentes (mínimo 3,24:1, umbral 3), 0 fallos; muestra en la sección 6 de `direccion-visual.md`. Es un cálculo, no una medición en pantalla |
| H6 | Reflow a 320 px verificado por reglas CSS | Cumple | Lectura y búsqueda en `_base.css`: diseño de una columna por defecto y ampliación con `min-width: 40em` y `56em`; sin anchos fijos de 320 px o más (la única cifra de tres dígitos es el radio de 999 px de las pastillas); 22 usos de `minmax(0, …)` y 12 de `min-width: 0` en elementos de rejilla; `overflow-wrap` en `body`; tablas dentro de regiones con `overflow-x: auto`; `.movil` con `min(100%, 22rem)`; cabeceras y botones con `flex-wrap`; reglas `max-width: 30em` para botones a ancho completo. Verificación **por reglas, no por pantalla** (ver H7) |
| H7 | Verificación visual y con herramienta: capturas a 320, 768 y 1280 px; foco real y orden de tabulación; animaciones con y sin `prefers-reduced-motion`; zoom al 200 %; herramienta de accesibilidad y lector de pantalla; renderizado de las pilas tipográficas en Windows, macOS, Android y Linux | Pendiente | No se dispuso de navegador ni de herramienta de capturas en esta revisión; no se afirma que se haya probado visualmente. Decisión DV-06 de `direccion-visual.md` |

## Resultado

| Concepto | Valor |
|---|---|
| Verificaciones que cumplen | 41 de 44 (E5 y G1 a G8 son de la versión 0.2; H1 a H6 son de la versión 0.3) |
| Verificaciones que no cumplen | 0 |
| Verificaciones pendientes | 3 (C3, F5 y H7): las dos primeras por requerir juicio humano y la última por requerir navegador o herramienta de accesibilidad |
| Marcadores PENDIENTE abiertos | 60 con llaves (40 perfil + 20 propuesta) y 18 sin llaves en la propuesta |
| Enlaces relativos verificados | 622 en 24 archivos (md y html, sin contar este checklist, que no contiene enlaces, ni `_archivo-v0.2/`), 0 rotos |
| Conclusión | Lista para revisión del Director como **BORRADOR**. **No está lista para entregar al cliente** mientras existan marcadores PENDIENTE de datos de empresa, moneda, IVA, forma de pago y fecha de inicio, ni mientras CR-001 no sea aprobado, ni mientras la dirección visual y la marca sigan sin aprobar y sin verificar en navegador (H7). Pasa a EN REVISIÓN al entregarla al Director; APROBADO solo con aprobación humana explícita |
