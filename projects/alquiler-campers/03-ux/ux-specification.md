# Especificación UX/UI: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Reporte del agente Diseñador UX/UI ("Especificación UX campers"), persistido por el Gestor de Documentación sin cambiar su significado.  
> **Aprobación:** NINGUNA. GATE-002 (DISCOVERY → DESIGN) sigue **PENDING** y el alcance **NO está aprobado** ([APPROVALS](../00-control/APPROVALS.md)). BUILD está prohibido.

**Aviso del Gestor:** este documento es un **borrador de diseño** y no es válido como especificación hasta que se aprueben el alcance y la puerta. La propuesta de marca no aprueba ninguna marca. No se han aprobado las decisiones pendientes de las secciones 16 y 17.

# Reporte de agente

- **Agente:** Diseñador UX/UI
- **Objetivo:** Diseñar la experiencia del MVP de la web de alquiler de campers (España) según la propuesta del PM (DEC-029).
- **Contrato aplicado:** `ux-ui-designer.contract.json` (solo lectura). **Conflicto, devuelto al Director:** el contrato limita el trabajo a la fase DESIGN y al "alcance aprobado". Hoy GATE-002 está PENDING y el alcance no está aprobado. Este documento es un **BORRADOR de diseño** y no es válido como especificación hasta que se aprueben el alcance y la puerta. La propuesta de marca no aprueba ninguna marca (acción prohibida). Toda pantalla fuera del MVP del PM figura solo como nota.
- **Elementos relacionados:** RF-001 a RF-026 y RF-032, RNF-001 a RNF-005 y RNF-013, HU-001 a HU-024, CA-001 a CA-034, DEC-001 a DEC-032, PEND-001 a PEND-024, ISS-002.
- **Archivos consultados:** PROJECT-STATE, DECISIONS, requirements, mvp-and-backlog, el contrato, `copilot-instructions.md`, la plantilla de reporte y el escenario UX-001.
- **Archivos modificados:** ninguno. **Pruebas ejecutadas:** ninguna.
- **Evidencia:** solo documentos en BORRADOR. No hay usuarios, analítica ni pruebas de usabilidad. Todo lo que aparece es inferencia de diseño.

**Leyenda:** [C] Confirmado · [S] Supuesto · [R] Recomendación · [P] Pendiente.

## 0. Base de diseño

- **[C]** Web de campers en España, con flota y sedes configurables. La empresa crea marca, logotipo y textos. Las fotos reales no están confirmadas. Rendimiento y SEO son importantes.
- **[R]** Diseño según el PM (DEC-001, 003, 005, 011, 012, 014, 018, 019, 009, 027). Es decir:
  - Pago total con tarjeta.
  - Acceso por código + email.
  - Un solo rol (admin).
  - Misma sede de recogida y devolución.
  - Sin extras ni FAQ.
  - Solo español y EUR.
  - Bloqueo de fechas durante el pago.
- **Contradicción abierta (ISS-002):** el momento de la política de cancelación. El PM dice "al cancelar" y el Director recomienda "al reservar" (DEC-025). **El diseño no elige.** La pantalla de cancelación muestra el reembolso que calcula el servidor y la versión de política aplicada.

## 1. Tipos de usuario y objetivos

| Usuario | Objetivo | Estado |
|---|---|---|
| Visitante / cliente particular (móvil u ordenador) | Ver campers, comprobar disponibilidad y precio total, reservar y pagar sin llamar. Consultar y cancelar su reserva | [S] particular; perfil, nacionalidad y volumen [P] |
| Administrador (único rol) | Mantener flota, sedes y tarifas. Gestionar reservas, bloqueos, pagos y reembolsos sin ayuda técnica | [S] / DEC-014 |
| Operador de sede | No existe en el MVP | Fase 2 (HU-034) |

## 2. Recorridos principales

**R1 · Reserva feliz (HU-002 a HU-010).**
1. Inicio.
2. Búsqueda con fechas y, si hay varias, sede.
3. Resultados.
4. Ficha.
5. Resumen de precio.
6. Datos del conductor y aceptaciones.
7. Pago con 3-D Secure.
8. "Verificando pago", mientras el servidor espera la notificación de la pasarela.
9. Confirmación con código.
10. Correo con justificante.

**R2 · Pago fallido (CA-006).** En el pago se rechaza la tarjeta o falla la autenticación. Se muestra un error y el tiempo restante del bloqueo. El cliente reintenta mientras el bloqueo siga vigente. Si el bloqueo vence, pasa al flujo R3.

**R3 · Pago pendiente o expirado (CA-004, 005, 007).**
- *Pendiente de verificación:* el navegador vuelve, pero la pasarela aún no ha notificado. Se muestra "en verificación" y no se confirma.
- *Expirada:* se informa, se liberan las fechas y se ofrece una nueva búsqueda con las mismas fechas.
- *Pago tardío:* se confirma por correo si las fechas siguen libres. Si no, se reembolsa y se avisa.

**R4 · Consulta y cancelación (HU-011, HU-012).**
1. "Mi reserva", con código + email.
2. Detalle.
3. Cancelar.
4. Ver el reembolso calculado y confirmar.
5. Pantalla de resultado y correo.

**R5 · Administrador.**
1. Acceso.
2. Alta de sedes, flota (con imágenes), tarifas y temporadas.
3. Seguimiento de reservas.
4. Bloqueos manuales (HU-022). Cubren las reservas telefónicas mientras no exista alta manual.
5. Pagos y reembolsos.

## 3. Mapa del sitio y navegación

**Público.** Cabecera: Campers · Sedes · Mi reserva · Contacto · botón "Buscar". Pie: legales, cookies, contacto.

```
/ ........................ Inicio (indexable)
/campers/ ................ Catálogo (indexable)
/campers/{slug} .......... Ficha (indexable, datos estructurados)
/sedes/{slug} ............ Página de sede (indexable, RF-018)
/buscar?... .............. Resultados (noindex)
/reserva/{resumen|datos|pago|estado} (noindex)
/mi-reserva .............. Consulta y cancelación (noindex)
/contacto
/legal/{aviso-legal|privacidad|cookies|condiciones-alquiler|politica-cancelacion}
```

**Admin (noindex, autenticado).** `/admin/` (acceso) → Reservas · Flota · Sedes · Tarifas y temporadas · Bloqueos · Pagos y reembolsos.

- **[R]** Las URLs son una propuesta, y el SEO se define en arquitectura. El código de reserva no debe ir en una URL adivinable.
- **[R]** Si hay una sola sede, se oculta el selector de sede y no se genera una página de sede duplicada del inicio. Decisión [P].

## 4. Inventario de pantallas y wireframes

**Convención de permisos.** Públicas = visitante. Las del panel requieren admin autenticado (CA-021). La salida esperada de cada pantalla está en su wireframe.

### P01 Inicio (RF-001, 002, 018 · HU-001, 002, 015)
- **Datos:** hero, destacados de flota activa y sedes.
- **Acciones:** buscar, ir a ficha o sede.
- **Salida:** resultados o ficha.

```
[Cabecera]
H1: Alquila tu camper en España
[Sede ▾*] [Recogida: dd/mm/aaaa] [Devolución: dd/mm/aaaa] [Buscar]
 *solo si hay varias sedes
Campers destacados: [card][card][card] -> /campers/
Sedes: [card sede] -> /sedes/{slug}
Cómo funciona: 1 Elige · 2 Paga · 3 Recibe tu código
[Pie]
```

### P02 Catálogo (RF-001 · HU-001, CA-016)
- **Datos:** campers activos con foto, plazas, precio orientativo "desde" y sede base.
- **Acciones:** abrir ficha, filtrar por sede.
- **Salida:** ficha.
- **Nota:** el precio orientativo ("desde") es [P]; el cálculo final es del servidor.

```
H1 Nuestros campers   [Filtro sede]
[foto][Nombre · N plazas · Sede][Desde X €/noche*][Ver ficha]
```

### P03 Ficha (RF-001, 003 · HU-001, CA-016)
- **Datos:** galería, descripción, plazas, equipamiento, sede, fianza informativa y condiciones configuradas.
- **Acciones:** elegir fechas, "Reservar".
- **Permisos:** un camper desactivado no aparece (404 o redirección, [P]).
- **Salida:** resumen de precio.

```
Migas: Inicio > Campers > {Nombre}
[Galería]  H1 {Nombre}  [Plazas][Equipamiento]
Panel de reserva: [Recogida][Devolución] -> disponible/no disponible
 Total: X € (desglose) [Reservar]
Fianza: {importe/texto P}, se gestiona en la entrega
Políticas: [Cancelación] [Condiciones]
```

### P04 Resultados (RF-002, 003 · HU-002, 003, CA-001, 009, 015)
- **Datos:** campers disponibles con precio total del periodo.
- **Acciones:** cambiar fechas, ver ficha, "Reservar".
- **Salida:** ficha o resumen.
- **Vacío:** "Sin disponibilidad". Las sugerencias automáticas de fechas o vehículos son Fase 2 [R]. En el MVP solo se ofrece cambiar fechas y contactar.

```
Resumen búsqueda (editable) · N resultados
[card: foto, nombre, plazas, Total X € por N noches, [Reservar]]
```

### P05 Resumen de precio (RF-004 · HU-004, CA-017, 034)
- **Datos:** camper, sede, fechas, noches, desglose por temporada, impuestos (tratamiento [P], PEND-010), total a pagar hoy, fianza informativa y política de cancelación.
- **Acciones:** editar fechas, continuar.
- **Salida:** datos del conductor.
- **Notas:** stepper "1 Resumen · 2 Tus datos · 3 Pago". No incluye paso de extras (Fase 2, DEC-018).

```
{Camper} · Sede · Recogida/Devolución (mismas sede)
Alquiler: N noches (temp. X: a €, temp. Y: b €)   Subtotal
IVA/impuestos: {P}        TOTAL A PAGAR AHORA: X €
Fianza (informativa, se gestiona en la entrega): {P}
Cancelación: {resumen de política} [Ver política completa]
[Continuar]
```

### P06 Datos del conductor (RF-006 · HU-005, CA-010, 018)
- **Datos:** nombre y apellidos, email (con confirmación), teléfono, fecha de nacimiento (edad mínima configurable, [P] PEND-019), ocupantes y aceptaciones.
- **Acciones:** continuar al pago, que crea el bloqueo temporal.
- **Salida:** pago.
- **Notas:** no se piden documentos en la web; se verifican en persona (DEC-010).

```
Nombre* Apellidos* Email* Repite email* Teléfono* F.nacimiento* Ocupantes*
[ ] Acepto condiciones de alquiler y privacidad* (enlaces, sin premarcar)
[ ] Quiero recibir novedades (opcional, aparte, sin premarcar)
Aviso: "Verificaremos tu carnet y DNI en la recogida."
[Volver] [Ir al pago]
```

### P07 Pago (RF-007 a 009 · HU-006, 007, CA-003, 006, 031)
- **Datos:** resumen, temporizador del bloqueo y área de pago de la pasarela.
- **Acciones:** pagar, reintentar, volver.
- **Salida:** pantalla de estado.
- **Notas:** integración alojada o embebida [P] (PEND-012). Nunca se piden datos de tarjeta fuera de la pasarela.

```
Tus fechas están reservadas durante {mm:ss}  (aviso accesible, no solo visual)
Total: X €   [Área de pago seguro]   [Pagar X €]
Texto: "Pago seguro procesado por {pasarela}. No guardamos tu tarjeta."
```

### P08 Estado y confirmación (RF-010, 032 · HU-008 a HU-010, CA-004, 005, 007, 019)
- **Datos:** estado, código de reserva, resumen, y próximos pasos (qué llevar, fianza, dirección y horario de la sede).
- **Acciones:** descargar o ver justificante, ir a "Mi reserva", contactar.
- **Permisos:** accesible solo con el contexto de la sesión de pago. Después, usar el código y el email.
- **Salida:** correo de confirmación.

```
[Variante confirmada] H1 Reserva confirmada · Código: XXXX [Copiar]
 Hemos enviado el justificante a {email}. Guarda tu código.
[Variantes] Verificando pago / Pago rechazado (reintentar) / Reserva expirada (nueva búsqueda)
```

### P09 Consulta de reserva (RF-011, 012 · HU-011, CA-013, 020)
- **Datos:** código + email, y luego el detalle con estados de reserva y de pago, importes, sede y justificante.
- **Acciones:** cancelar si procede, contactar, reenviar correo.
- **Permisos:** ninguno si los datos son correctos. El error es genérico (CA-013).
- **Salida:** detalle o cancelación.

```
[Código*] [Email*] [Consultar]  ¿Perdiste tu código? -> reenviar correo / contacto
-- Detalle: estado (texto + icono), camper, fechas, sede, importe, [Justificante] [Cancelar reserva]
```

### P10 Cancelación (RF-013 · HU-012, CA-008)
- **Datos:** reserva, tramo y versión de política aplicados, y reembolso calculado por el servidor.
- **Acciones:** confirmar o volver.
- **Salida:** pantalla de resultado, con importe y plazo de reembolso [P, PEND-009].
- **Notas:** botón destructivo con confirmación explícita. El importe sale solo del servidor. Los valores de la política están por validar (P-001).

```
Cancelar reserva {código}
Según la política {versión}: reembolso X € (de Y € pagados). {Resumen del tramo}
[ ] Entiendo que la cancelación es inmediata y no se puede deshacer
[Mantener mi reserva] [Cancelar y solicitar reembolso]
```

### P11 Contacto (RF-015 · HU-013, CA-029)
- **Datos:** datos de contacto, y un formulario con nombre, email, motivo, mensaje y aceptación de privacidad.
- **Salida:** confirmación del envío. El formulario lleva antispam (VAL-016).

### P12 Páginas legales y política de cancelación (RF-016 · HU-014, CA-027)
- **Datos:** texto con título, fecha y versión.
- **Salida:** solo lectura, enlazadas desde el pie y desde los pasos de reserva.
- **Notas:** el contenido es [P] hasta que lo valide la asesoría legal (PEND-010, PEND-022).

### P13 Cookies (RF-017 · HU-014, CA-026)
- **Datos:** banner en el primer acceso y centro de preferencias.
- **Acciones:** aceptar, rechazar, configurar (con la misma prominencia) y modificar después desde el pie.
- **Notas:** sin cookies no técnicas hasta consentir. El detalle legal está pendiente de validación.

### P14 a P20 Panel admin (RF-019 a 026 · HU-017 a 024)
**P14 Acceso (RF-019, CA-021).** Usuario y contraseña, límite de intentos, error genérico. La recuperación de contraseña es [P].

**P15 Reservas (RF-023, CA-022, 032).**
- **Lista:** filtros por estado, fechas, camper y código.
- **Detalle:** cliente, camper, fechas, importes, estados de reserva y de pago, y notas.
- **Acciones:** cancelar, anotar.

```
[Filtros] [Tabla: código|cliente|camper|fechas|estado reserva|estado pago|importe]
Detalle: datos, línea de tiempo de eventos, [Cancelar] [Añadir nota]
```

**P16 Flota (RF-020, CA-011).** Alta, edición y desactivación. Modelo, plazas, equipamiento, fianza, sede base e imágenes (con texto alternativo obligatorio). Si hay reservas futuras, se desactiva y se avisa del impacto, sin eliminar (VAL-021, DEC-028).

**P17 Sedes (RF-021).** Alta, edición y desactivación. Dirección, horarios y contacto. Misma regla de desactivación.

**P18 Tarifas y temporadas (RF-022, CA-012, 034).**
- Precio por noche por vehículo y temporada.
- Temporadas sin solapes (VAL-020).
- Mínimo de noches.
- Aviso permanente: "los cambios no afectan a reservas ya creadas".

**P19 Bloqueos (RF-024, CA-023).** Selección de camper y rango, y motivo. Si hay conflicto, se rechaza y se muestran las reservas en conflicto.

**P20 Pagos y reembolsos (RF-025, CA-024).**
- Transacciones con estado.
- Reembolso total o parcial con confirmación del importe.
- Los reembolsos fallidos aparecen marcados "gestión manual".

**P21 Aviso por correo al admin (RF-026, CA-025).** No es una pantalla. Solo se necesita un campo para configurar el correo de aviso. Su ubicación es [P].

## 5. Flujos críticos paso a paso

**Reserva y pago (R1).**
1. El cliente indica fechas.
2. El servidor valida y revalida la disponibilidad en cada paso (VAL-007).
3. El resumen se muestra con el precio calculado en el servidor.
4. Los datos y las aceptaciones deben ser válidos.
5. Al pulsar "Ir al pago" se crea el bloqueo. Si alguien lo obtuvo antes, aparece el aviso "Estas fechas se acaban de reservar" con enlace a nueva búsqueda (CA-003).
6. El cliente paga y se autentica con 3-D Secure.
7. Vuelve a la web, donde el estado es "verificando" hasta recibir la notificación válida (CA-004).
8. Confirmada: se muestran el código y el correo con justificante.

**Cancelación (R4).**
1. Acceso con código y email.
2. El servidor calcula el reembolso.
3. El cliente confirma explícitamente.
4. La reserva queda cancelada y las fechas se liberan.
5. Se muestra el resultado y se envía un correo.
6. Si el reembolso falla, el cliente ve "estamos procesando tu reembolso" y el admin lo gestiona.

## 6. Estados de interfaz

| Pantalla | Carga | Vacío | Éxito | Error | Sin permisos | Sin conexión |
|---|---|---|---|---|---|---|
| Resultados | Esqueleto con altura reservada | Sin disponibilidad, con "cambiar fechas" y "contacto" | Lista | Fechas inválidas (en el campo) o fallo de servidor con reintento | n/a | Aviso y reintento, sin perder los datos |
| Ficha y catálogo | Esqueleto | Sin campers activos | Contenido | 404 si está desactivado | n/a | Aviso |
| Resumen y datos | Cálculo en curso | n/a | Total mostrado | Fechas ya no disponibles. Mínimo de noches. Edad mínima | n/a | Conserva los campos |
| Pago | "Preparando pago seguro" | n/a | Pasa a estado | Rechazo o 3DS fallido (reintento mientras dure el bloqueo). Bloqueo vencido | Sin bloqueo → volver | El pago puede estar en curso: no reenviar, consultar estado |
| Estado | "Verificando tu pago" | n/a | Confirmada | Expirada. Fallida | Sin contexto → ir a "Mi reserva" | "No podemos comprobar tu pago ahora. Si ya pagaste, recibirás un correo" |
| Mi reserva | Cargando | n/a | Detalle | Datos no coinciden (mensaje genérico). Límite de intentos | n/a | Aviso |
| Cancelación | Calculando reembolso | n/a | Cancelada | No cancelable. Fallo de reembolso (gestión manual) | Sin sesión de reserva → volver a consulta | Aviso, sin enviar dos veces |
| Panel (listas) | Esqueleto | "Aún no hay {flota/sedes/reservas}" con acción de alta | Guardado con aviso | Validación de campo. Conflicto de fechas. Desactivar con reservas | Sesión caducada → acceso | Cambios no guardados |

## 7. Formularios y validaciones visibles

- **Principios [R]:**
  - Etiquetas siempre visibles.
  - El error aparece junto al campo y en un resumen.
  - El texto explica cómo corregir.
  - Los datos escritos se conservan.
- **Búsqueda:** VAL-001 a 004. Formato dd/mm/aaaa, con campo de texto alternativo al calendario. Recogida no anterior a hoy más la antelación (valor [P], PEND-017). Devolución posterior. Mínimo de noches de la temporada.
- **Conductor:** VAL-008 a 011, 013, 014, 016. Nombre y apellidos. Email con doble entrada. Teléfono, que admite +34. Edad mínima [P]. Ocupantes ≤ plazas. Aceptación obligatoria y sin premarcar. Marketing opcional y aparte.
- **Consulta:** código + email, límite de intentos y error genérico.
- **Contacto:** campos obligatorios, aceptación de privacidad y antispam sin CAPTCHA inaccesible [R].
- **Panel:** VAL-020 a 022. Precios ≥ 0. Mínimo de noches ≥ 1. Imágenes con formato y peso validados, y con texto alternativo.

## 8. Comportamiento responsive

- **[R]** Diseño mobile-first. Los puntos de quiebre se definen en implementación y no se fijan aquí.
- **Cabecera:** menú compacto en móvil, con "Buscar" y "Mi reserva" siempre accesibles.
- **Búsqueda:** una columna en móvil, y en línea en escritorio.
- **Resumen:** el total y el botón principal quedan visibles (barra inferior fija en móvil). Los pasos se muestran en una sola columna.
- **Panel:** usable en escritorio y tableta. Las tablas se convierten en tarjetas o scroll con cabeceras fijas.
- **Objetivos táctiles:** amplios (buena práctica, [R]).
- **Calendario:** selector nativo o accesible, con alternativa de texto.

## 9. Accesibilidad (objetivo WCAG 2.1 AA [R], alcance de la revisión [P], PEND-014)

- **Estructura:** un H1 por página, jerarquía de encabezados, landmarks, "saltar al contenido" y títulos de página únicos (1.3.1, 2.4.1, 2.4.2).
- **Teclado:** todo operable con teclado, con foco visible y orden lógico (2.1.1, 2.4.3, 2.4.7). El banner de cookies y los modales atrapan el foco y lo devuelven al cerrarse.
- **Formularios:** etiquetas, `autocomplete` (1.3.5), errores asociados al campo, identificados por texto y no solo por color (3.3.1, 3.3.3), y mensajes anunciados (4.1.3).
- **Pago y cancelación:** acciones reversibles o con confirmación (3.3.4).
- **Temporizador del bloqueo (2.2.1):** se avisa antes de vencer con un aviso accesible. Si se puede extender el tiempo o no, es [P], porque afecta a la disponibilidad.
- **Contraste:** 4.5:1 para texto y 3:1 para elementos de interfaz (1.4.3, 1.4.11). Se verificará con herramienta cuando la marca se apruebe.
- **Zoom y reflow:** sin pérdida al ampliar el texto ni al ajustar el ancho (1.4.4, 1.4.10).
- **Estados:** nunca solo por color. Siempre texto e icono. Cada imagen tiene texto alternativo (1.1.1), con campo obligatorio en el panel.
- **Calendario y galería:** operables sin ratón.
- **Pendiente:** si la accesibilidad es obligatoria legalmente (PEND-010).

## 10. Microcopy clave [R] (tono "tú" propuesto, pendiente, ver §11)

| Momento | Texto propuesto |
|---|---|
| Búsqueda vacía | "No hay campers libres del {fecha} al {fecha}. Prueba con otras fechas o escríbenos." |
| Fechas inválidas | "La devolución debe ser posterior a la recogida." / "Para estas fechas el mínimo es {n} noches." |
| Bloqueo | "Tus fechas están reservadas durante {mm:ss}." |
| Pérdida de fechas | "Estas fechas se acaban de reservar. Busca otras fechas." |
| Pago rechazado | "No hemos podido completar el pago. Revisa los datos o prueba otra tarjeta." |
| Verificando | "Estamos verificando tu pago. No lo repitas: te avisaremos por correo." |
| Expirada | "Tu reserva ha expirado y las fechas se han liberado. Si pagaste, te lo reembolsaremos." |
| Acceso fallido | "No encontramos una reserva con esos datos." (sin confirmar existencia) |
| Cancelación | "Se te reembolsarán {X €}. Esta acción no se puede deshacer." |
| Fianza | "La fianza se gestiona en la recogida. No se cobra ahora." |
| Consentimiento | "He leído y acepto las condiciones de alquiler y la política de privacidad." |

## 11. Propuesta de identidad de marca (PROPUESTA, no aprobada; la define la empresa)

- **Nombre provisional (propuesta):** "Ruta Camper". No se ha comprobado disponibilidad de marca ni de dominio. [P]
- **Concepto [R]:** viaje, libertad y confianza. Una empresa cercana y fiable.
- **Paleta propuesta** (contrastes calculados de forma aproximada y a verificar con herramienta):

| Rol | Valor propuesto | Uso |
|---|---|---|
| Primario (bosque) | #1F4D3F | Cabecera, botones y enlaces, con texto blanco |
| Acento (terracota) | #A64B20 | Llamadas a la acción secundarias |
| Fondo cálido | #F6F1E7 | Secciones alternas |
| Texto | #1E2420 | Cuerpo de texto |
| Error | #B3261E | Mensajes de error, siempre con texto e icono |

- **Tipografía propuesta:** una familia sans-serif legible, y para el cuerpo la pila de fuentes del sistema. Si se usa una fuente de marca, que sea una sola con pocos pesos.
- **Tono:** cercano, claro y tranquilizador, de "tú". Transparente en precios y políticas. Sin jerga. Decisión de tú/usted [P].
- **Logotipo:** a crear por la empresa. No se diseña aquí.
- **Pendientes de marca (escalado al Director):** nombre, logotipo, paleta, tipografía, tono, estilo fotográfico e iconografía.

## 12. Rendimiento visual (RNF-001, objetivo CWV de CA-014, protocolo [P])

- **Imágenes:** formatos modernos con alternativa, tamaños responsivos (`srcset`) y dimensiones declaradas para evitar saltos (CLS). La imagen principal de la página se carga con prioridad y el resto con carga diferida.
- **Panel de flota:** redimensiona y comprime al subir (RNF-013).
- **Fotos de ejemplo:** sustituibles sin desarrollo. No se mezclan con fotos reales en una misma ficha.
- **Tipografía:** fuente de sistema por defecto. Si hay fuente propia, se sirve en el mismo dominio, en WOFF2, con subconjunto y `font-display: swap`. Se precarga solo la imprescindible.
- **Estados de carga:** esqueletos con la altura final reservada.
- **Otros:** el pie y las tarjetas no usan efectos pesados. Los scripts de terceros (analítica y mapa) solo se cargan con consentimiento, y el mapa de sede es opcional.
- **Pasarela:** el componente de pago se carga solo en la pantalla de pago.

## 13. Fase 2 (solo nota, sin diseñar)

- **Extras en el resumen (HU-025):** añadiría un paso al flujo.
- **FAQ (HU-026).**
- **Modificar reserva (HU-027).**
- **Cuentas de cliente (HU-032):** sustituyen a "Mi reserva".
- **Depósito + saldo (HU-030):** añade estado de pago parcial y recordatorios.
- **Factura y clientes empresa (HU-031).**
- **Otra sede de devolución (HU-036):** cambiaría los formularios de búsqueda y resumen.
- **Panel:** reservas manuales (HU-028), plantillas de correo (HU-029), informes y auditoría (HU-033), roles (HU-034) y centro de avisos (HU-035).

## 14. Matriz pantalla → requisito

| Pantalla | RF | HU | CA |
|---|---|---|---|
| P01 Inicio | RF-002, 018 | HU-001, 002, 015 | CA-028 |
| P02 Catálogo / P03 Ficha | RF-001, 003 | HU-001, 003 | CA-016 |
| P04 Resultados | RF-002, 003 | HU-002, 003 | CA-001, 009, 015 |
| P05 Resumen | RF-004 | HU-004 | CA-017, 034 |
| P06 Datos conductor | RF-006 | HU-005 | CA-010, 018 |
| P07 Pago | RF-007, 008, 009 | HU-006, 007 | CA-003, 006, 031 |
| P08 Estado y confirmación | RF-010, 032 | HU-008, 009, 010 | CA-004, 005, 007, 019 |
| P09 Consulta | RF-011, 012 | HU-011 | CA-013, 020 |
| P10 Cancelación | RF-013 | HU-012 | CA-008 |
| P11 Contacto | RF-015 | HU-013 | CA-029 |
| P12 Legales / P13 Cookies | RF-016, 017 | HU-014 | CA-026, 027 |
| P14 Acceso admin | RF-019 | HU-017 | CA-021 |
| P15 Reservas admin | RF-023 | HU-021 | CA-022, 032 |
| P16 Flota / P17 Sedes | RF-020, 021 | HU-018, 019 | CA-011, 033 |
| P18 Tarifas | RF-022 | HU-020 | CA-012, 034 |
| P19 Bloqueos | RF-024 | HU-022 | CA-023, 002 |
| P20 Pagos y reembolsos | RF-025 | HU-023 | CA-024 |
| P21 Aviso admin | RF-026 | HU-024 | CA-025 |
| Transversal | RNF-001 a 005 | HU-015, 016 | CA-014, 030 |

## 15. Riesgos de experiencia

1. **ISS-002:** el momento de la política de cancelación cambia el texto y el cálculo de P05 y P10.
2. **Pago total al reservar:** puede aumentar el abandono (R-005 [PM]). Se mide.
3. **Fotos de ejemplo:** reducen la confianza y la conversión. El plan de sustitución es previo a la publicación.
4. **Sin cuentas:** si el cliente pierde el código, depende del reenvío del correo y del contacto (R-004 [PM]). Hay que mostrarlos con claridad.
5. **El bloqueo vence mientras el cliente autentica el pago:** frustración y pagos tardíos. Los avisos del temporizador son clave.
6. **Estado "verificando":** puede generar consultas si la pasarela tarda. El mensaje debe tranquilizar y explicar el correo posterior.
7. **Textos legales sin validar** en el pie y en los pasos de reserva (PEND-010).
8. **Reservas por teléfono:** solo con bloqueo manual (R-003 [PM]), con riesgo de error del admin.
9. **Fianza informativa:** el cliente puede esperar que se cobre en la web. El texto debe ser muy explícito.
10. **Marca:** tipografía y paleta provisionales. Cambiarlas tarde implica rehacer componentes.

> Nota del Gestor: estos 10 riesgos están numerados por el agente en esta sección. En [RISKS](../00-control/RISKS.md) se registran como R-UX-01 a R-UX-10 (ID provisional del Gestor; el número de origen es el de esta lista).

## 16. Pendientes de decisión del cliente (vía Director)

- **Marca:** nombre, logotipo, paleta, tipografía, tono (tú/usted) y estilo de imagen.
- **Flujo y reglas:**
  - Política de cancelación y su momento de aplicación (PEND-008, ISS-002).
  - Quién asume las comisiones de reembolso (PEND-009).
  - Importe y texto de la fianza (PEND-018).
  - Edad mínima (PEND-019).
  - Duración del bloqueo y posibilidad de ampliarlo (DEC-027).
  - Antelación mínima y máxima (PEND-017).
  - Definición de "noche" y horarios (PEND-013).
  - Tratamiento del IVA en la presentación de precios (PEND-010).
- **Integración:**
  - Proveedor y tipo de integración de la pasarela, alojada o embebida (PEND-012).
  - Qué correos se envían en el MVP más allá de la confirmación (DEC-023). En concreto: reenvío de código, enlace para reintentar un pago y aviso de expiración.
- **Panel:**
  - Recuperación de contraseña del admin.
  - Dónde se configura el correo de aviso al admin.
- **Producto:**
  - Si hay una o varias sedes y cuál es la cobertura SEO por sede.
  - Qué pasa con el precio orientativo "desde" en el catálogo.
  - Comportamiento de las fichas desactivadas.
  - Cliente sin acceso a su email (PEND-023).
- **Verificación:** protocolo de medición y alcance de accesibilidad (PEND-014).

## 17. Preguntas abiertas para el Director

1. ¿Se activa el diseño formal (DESIGN) pese a que GATE-002 y el alcance siguen sin aprobar? Este reporte quedaría como borrador hasta entonces.
2. ¿Cuál de las dos políticas de cancelación (ISS-002) se refleja en P05 y P10?
3. ¿Se acepta el mensaje "verificando pago" y la ampliación o no del bloqueo (2.2.1)?
4. ¿Se desea una pantalla de inicio en el panel, o basta con que "Reservas" sea la entrada? (No se ha inventado una.)
5. ¿Hay material de marca existente, o se parte de cero?

## Resultado

**COMPLETADO_CON_PENDIENTES.**

El diseño cubre todos los flujos críticos y los estados alternativos. Sigue condicionado por las decisiones de las secciones 16 y 17, por la validación legal y por la aprobación del alcance.

**Siguiente acción recomendada:** el Director decide la pregunta 1 y las de marca. Con el alcance aprobado, el diseño se formaliza en `03-ux/ux-specification.md`. Esa tarea corresponde al Gestor de Documentación.

---

## Registro documental (Gestor de Documentación)

- **Estado:** BORRADOR. **Fecha de persistencia:** 2026-10-26.
- **Fuente:** reporte del Diseñador UX/UI entregado por el Director (agente "Especificación UX campers"). Se omitió solo la línea de metadatos del sistema del agente.
- **Decisiones pendientes:** ver §16 y §17, registradas como PEND-025 a PEND-033 y PEND-012, PEND-013, PEND-017 a PEND-019, PEND-023 en [DECISIONS](../00-control/DECISIONS.md).
- **Riesgos:** R-UX-01 a R-UX-10 en [RISKS](../00-control/RISKS.md).
- **Trazabilidad:** matriz de §14 incorporada a [TRACEABILITY](../00-control/TRACEABILITY.md) §6.
- **Actividad y tarea:** [ACT-004](../00-control/AGENT-ACTIVITY.md), [TASK-010](../00-control/TASKS.md).

## Enlaces relativos

[Estado del proyecto](../00-control/PROJECT-STATE.md) · [Decisiones](../00-control/DECISIONS.md) · [Riesgos e impedimentos](../00-control/RISKS.md) · [Trazabilidad](../00-control/TRACEABILITY.md) · [Tareas](../00-control/TASKS.md) · [Aprobaciones](../00-control/APPROVALS.md) · [requirements.md](../01-discovery/requirements.md) · [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) · [Arquitectura de solución](../04-architecture/solution-architecture.md)
