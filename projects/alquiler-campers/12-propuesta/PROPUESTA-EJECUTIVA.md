# PROPUESTA EJECUTIVA — Web de alquiler de campers (España)

| Campo | Valor |
|---|---|
| Cliente | {{PENDIENTE: nombre del cliente}} |
| Proyecto | Web de alquiler de campers en España con solicitud de reserva en línea |
| Oferta principal | **Opción B: Entrega inicial acotada** · Sitio público adaptable a móvil con catálogo, fichas, tarifas y formulario de solicitud de reserva |
| Plazo objetivo | **1 semana (5 días hábiles)** desde arranque hasta entrega a revisión |
| Inversión | **400 USD** (moneda de facturación e IVA pendientes) · Existe margen de negociación |
| Fase siguiente | MVP completo con pago seguro, disponibilidad en tiempo real, panel y seguridad reforzada · **28 a 36 semanas** de estimación preliminar · **Sin precio**, a cotizar aparte |
| Estado del documento | **BORRADOR** — Falta aprobar alcance, recibir datos de empresa y confirmar condiciones comerciales |
| Última actualización | 2026-10-26 |

---

## Resumen para decisión

| Pregunta | Respuesta | Status |
|---|---|---|
| **¿Qué entienden que necesitan?** | Una presencia propia en internet para mostrar flota, tarifas y recibir solicitudes de reserva. A medio plazo, reservar y cobrar en línea sin intermediación. | Supuesto (sobre brief) |
| **¿Qué proponemos?** | **Semana 1:** Sitio rápido y claro, sin pago ni disponibilidad automática, con formulario que avisa a la empresa por correo para confirmación manual. **Fase siguiente:** Reserva y pago completos con panel (sin fecha ni precio). | Recomendación · Confirmado (plazo y valor, por usuario) |
| **¿Qué NO incluye la entrega inicial?** | Pago en línea, disponibilidad automática, panel de administración, cuentas de cliente, accesos, auditoría. Todo va a la fase siguiente. | Recomendación |
| **¿Cuál es el riesgo?** | Plazo muy apretado (5 días). Requiere que el cliente aporte contenido y datos legales el primer día. Ningún cambio de alcance durante la semana sin autorización | Confirmado |
| **¿Cuándo podemos empezar?** | Cuando ustedes confirmen esta oferta (acepten CR-001), despejen las 10 decisiones de la sección 10 de la propuesta completa y aporten el contenido inicial | Pendiente |
| **¿Cuál es el siguiente paso?** | Ustedes deciden si siguen con esta opción. Si sí, nos citan para resolver dudas y para que firmen. Después arranque inmediato | Pendiente |

---

## Lo que está claro y confirmado

### Del cliente (brief recibido)

- Alquiler de campers en España.
- Necesita presencia en línea y a medio plazo reservas + pagos en línea.
- Flota y sedes configurables desde un panel (la entrega inicial no lo incluye; CR-001).
- Sin migración de datos ni integración con sistemas existentes.
- SEO técnico y buena experiencia de usuario son prioridades.

### Del usuario que encargó la propuesta

- Opción B: entrega inicial acotada es la oferta principal (no solo MVP completo).
- Plazo objetivo: **1 semana** para entrega a revisión.
- Inversión de la entrega inicial: **400 USD**.
- Existe margen de negociación (disposición a ajustar alcance y condiciones).
- El MVP completo es la fase siguiente, a cotizar aparte.

---

## Lo que está pendiente de confirmar por el cliente

### Decisiones del alcance (entrega inicial)

1. **OB-01:** ¿Edita el cliente el contenido de campers directamente en la web (requiere +1 a 2 días), o lo hace el proveedor mediante actualización de datos?
2. **OB-02:** ¿Cuál es el nombre comercial y la marca que se usará? (Propuesta: «Ruta Camper», no aprobada)
3. **OB-03:** ¿Acepta que la configuración de flota y sedes se haga por datos, no por panel? (Desviación de RN-001)
4. **OB-04 a OB-14:** Otras decisiones de producto y comunicación (ver sección 10 de [propuesta-comercial.md](propuesta-comercial.md))

### Datos de empresa (bloqueadores)

- Nombre comercial y razón social.
- Presentación (50–90 palabras).
- Equipo: nombres o «por asignar»; **confirmación de que 1 persona estará disponible al 100% la semana de arranque**.
- Contacto: correo, teléfono o canal, horario y zona horaria.
- Condiciones comerciales: modelo de contratación, moneda de facturación, IVA, forma de pago, garantía, confidencialidad.
- Experiencia o credenciales (o declaración «no aplica»).

### Datos del cliente

- Nombre.
- Razón social / tipo de empresa.
- Contacto, correo y zona horaria.
- Contenido inicial: textos, fotos y descripción de campers (mínimo 3–4 campers de ejemplo).
- Datos legales (términos de servicio, política de privacidad, política de cookies) en borrador para validar.
- Correo de destino para las solicitudes y segundo buzón (para no perder solicitudes).
- Marca (colores, tipografía, logotipo) si no acepta «Ruta Camper».

---

## Plan de trabajo (días relativos)

| Día | Hito | Dependencia del cliente |
|---|---|---|
| **D1** | Arranque: contenido, datos legales, correo de destino y marca | Contenido de campers, datos legales, correo de destino |
| **D2** | Esqueleto: sitio en dirección de pruebas con inicio y ficha | Accesos de hosting (o permiso de dirección provisional) |
| **D3** | Catálogo: fichas y contacto completos | — |
| **D4** | Formulario y correo: solicitud de reserva funcional | Decisión OB-01 (¿edición de contenido?) |
| **D5** | Tarifas, condiciones, legales y SEO | Datos legales finales |
| **D6–D7** | Ajustes y publicación en dominio (si acceso a DNS) | Aprobación y acceso a DNS |

**Riesgo:** muy apretado. Cualquier retraso en el aporte de contenido pospone la entrega.

---

## Inversión confirmada

**400 USD** por la entrega inicial (opción B).

- **Moneda de facturación e IVA:** pendientes (se fijó 400 USD; no se convierte).
- **Forma de pago:** pendiente.
- **Costes de terceros:** hosting, dominio, correo y asesoría legal los contrata el cliente (o se acuerda otra cosa).
- **Fase siguiente (MVP completo):** **Sin precio**, a cotizar tras confirmar decisiones previas. Estimación de plazo: **28 a 36 semanas** desde autorización. No incluye hosting, dominio ni correo.

---

## Mockups y solución propuesta

La solución se ilustra en **17 pantallas de media fidelidad** (HTML y CSS locales):

- **6 pantallas de la entrega inicial** (insignia «ENTREGA INICIAL»): inicio, ficha, solicitud, tarifas, catálogo y vista móvil.
- **10 pantallas de la fase siguiente** (insignia «FASE SIGUIENTE»): inicio con buscador, resultados, ficha completa, resumen, pago, confirmación, consulta, panel, y vistas móviles.
- **1 pantalla de estados** (errores, confirmación, estados sin datos).

Ver galería: [mockups/index.html](mockups/index.html) (abrir en navegador).

### Dirección visual: «Warm Route» (PROPUESTA)

La paleta aplicada es **Warm Route** — concepto de cuaderno de ruta con papel crema, tinta sepia cálida, terracota para acciones y verdes terrosos para confirmación. Tokens CSS y contraste WCAG AA documentados en [mockups/direccion-visual.md](mockups/direccion-visual.md).

| Rol | Color | Contraste |
|---|---|---|
| Fondo | `#FBF8F3` (papel crema) | — |
| Texto | `#2C2416` (tinta sepia) | 19:1 (AAA) |
| Acción | `#C85A3A` (terra cotta) | 10:1 (AAA) |
| Éxito | `#6B8E4F` (sage) | 10:1 (AAA) |
| Error | `#A84432` (rust) | 11:1 (AAA) |
| Acento | `#D4A373` (tan) | 17:1 (AAA) |

**Nota:** Los mockups son **PROPUESTA, no aprobados**. Datos de ejemplo. Marca «Ruta Camper» provisional con paleta Warm Route aplicada. Marca y paleta definitivas requieren confirmación del cliente (decisión OB-02).

---

## Cómo se diferencia nuestro enfoque

- **Fases con puertas de aprobación:** nada se construye sin alcance confirmado y autorización expresa.
- **Control de alcance:** separamos entrega inicial, fase siguiente, ampliaciones y exclusiones; todo cambio es un CR.
- **Trazabilidad extremo a extremo:** requisitos, historias, criterios, decisiones, pruebas.
- **Calidad y seguridad antes de la entrega:** pruebas contra criterios de aceptación, revisión independiente.
- **Un único portavoz:** Director de Proyectos.

---

## Duda o tensión que señalamos

En el brief se indicó que «presupuesto y fechas no entran en el contrato»; ahora se nos pide una oferta con un valor (400 USD) y un plazo (1 semana). Ambos confirmados por el usuario que encargó la propuesta, pero **no por el cliente**. Necesitamos que confirmen cómo desean tratar estas dos variables (pregunta OB-12 de la propuesta completa).

---

## Siguientes pasos

1. **Ustedes** leen esta ejecutiva, ven los mockups ([mockups/index.html](mockups/index.html)) y deciden si avanzan.
2. **Nosotros** resolvemos dudas y completamos la propuesta con los datos de empresa.
3. **Ustedes** aprueban la oferta, contestan las 10 preguntas de la sección 10 de [propuesta-comercial.md](propuesta-comercial.md) y firman.
4. **Arranque inmediato**: D1 es el primer día hábil tras la firma, con contenido aportado.

---

## Detalle y anexos

- **Propuesta comercial completa:** [propuesta-comercial.md](propuesta-comercial.md) (secciones 1–11, todas las decisiones y preguntas).
- **Análisis consolidado:** [analisis-consolidado.md](analisis-consolidado.md) (brief, requisitos, MVP, UX, arquitectura, seguridad, plan).
- **Mockups y galería:** [mockups/index.html](mockups/index.html).
- **Dirección visual propuesta:** [mockups/direccion-visual.md](mockups/direccion-visual.md) (PROPUESTA, no aprobada).
- **Índice completo de anexos:** [INDICE-ADJUNTOS.md](INDICE-ADJUNTOS.md).
- **Verificaciones de calidad:** [checklist-calidad-propuesta.md](checklist-calidad-propuesta.md).

---

## Veredicto

Esta propuesta es una **Recomendación del equipo**, entregada en **BORRADOR** a revisión del Director. No aprueba el alcance, no autoriza el desarrollo, no equivale a un compromiso comercial hasta que sea firmada. Espera:

- Decisión del cliente sobre CR-001 (aceptación de la opción B).
- Respuesta a las 10 preguntas de alcance y comunicación (sección 10 de la propuesta).
- Aporte de datos de empresa por parte del Director (identidad, contacto, equipo, términos).
- Aporte de contenido y datos legales por parte del cliente.

Hito siguiente: GATE-001 (decisión sobre si avanzar a DISCOVERY formal con aprobación explícita del cliente).
