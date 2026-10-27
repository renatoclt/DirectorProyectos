# Opción B (entrega inicial acotada): evaluación y estimación — Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Reporte del Planificador de Proyecto sobre la Opción B, entregado por el Director (transcrito sin cambiar su significado; no hay archivo de origen separado). La instrucción del usuario del 2026-10-26 aporta los datos marcados [C]. Complementa el [plan de implementación](implementation-plan.md) y la [estimación del MVP completo](estimacion-plazo.md).  
> **Naturaleza:** **Recomendación / estimación a confirmar.** No es compromiso ni calendario. El reporte no incluye fechas de calendario ni costos; el valor de 400 USD de la sección 7 lo fijó el usuario y no lo calculó el Planificador.  
> **Aprobación:** NINGUNA. La [solicitud de cambio CR-001](../00-control/CHANGE-REQUESTS.md) está en `WAITING_FOR_APPROVAL`. GATE-001 y GATE-002 siguen **PENDING**, el alcance **NO está aprobado** y no existe solicitud PLANNING → BUILD ([APPROVALS](../00-control/APPROVALS.md)). BUILD sigue prohibido.

## Confirmaciones del usuario (2026-10-26) [C]

Instrucción explícita del usuario trasladada al Gestor. No son aprobación del cliente de España.

1. **[C]** Se elige la **Opción B** (entrega inicial acotada).
2. **[C]** Plazo objetivo: **1 semana**.
3. **[C]** Valor de esta entrega: **400 USD**, fijado por el usuario. La moneda de facturación e IVA quedan **PENDIENTES** (el cliente está en España).
4. **[C]** Hay margen de negociación en la propuesta (sin cifra).

**Avisos del Gestor:**
- **La sección 7 de este documento es INTERNA.** No debe copiarse a documentos destinados al cliente.
- El Planificador **no leyó en detalle** `ux-specification`, `implementation-plan` ni la arquitectura; la coherencia de la pila con 04-architecture queda por verificar (ver R-007 [OPB] y la decisión pendiente 5).
- **Los 7 días D1 a D7 y las 40 h de una semana no son una fecha de calendario:** son días relativos desde el arranque (D1), que no ha ocurrido.
- Los IDs R-001 a R-008 de este documento llevan el calificador **[OPB]** (opción B) porque R-001 a R-008 ya existen en el registro con otros significados (ver ISS-003 en [RISKS](../00-control/RISKS.md)). Las tareas T1 a T10 llevan el mismo calificador.
- Comprobación aritmética del Gestor (no cambia la fuente): la suma de T1 a T10 da 50 h (mínimo) y 70 h (máximo), coincidente con "50–70 h". El valor probable de 60 h es el punto medio. 400 USD / 60 h ≈ 6,7 USD/h; 400 USD / 7,5 días de 8 h ≈ 53 USD/día; 400 USD / 40 h = 10 USD/h: coherente con las cifras de §7. **No verificable por el Gestor:** el desglose del "núcleo B" en 38–42 h no se detalla por tarea en la fuente.
- Observaciones sobre el propio reporte (registradas en ISS-041 en [RISKS](../00-control/RISKS.md); ISS-038 a ISS-045 son las inconsistencias nuevas de esta entrega): el núcleo (38–42 h) supera las "30–35 h con foco real" que el reporte da como capacidad de una semana; D6 y D7 se describen como "colchón no contado" y a la vez se usan como hitos; la publicación aparece en D7 y en D8–D10.

## 1. Veredicto

**Con 1 persona full-stack, la Opción B completa no cabe en 1 semana con holgura.**

- **Capacidad.** Una semana son 5 días hábiles, unas 40 h. Con foco real quedan unas 30–35 h.
- **Esfuerzo.** B completa necesita unas 50–70 h, con 60 h como valor probable. Son 6–9 días hábiles.
- **Plazo realista de B completa con 1 persona:** 1,5–2,5 semanas desde el inicio, contando la latencia del cliente.

**Lo máximo que cabe en 1 semana: un "núcleo B"** (unas 38–42 h, sin holgura, riesgo alto). Para que quepa hay que recortar:
- Máximo 3–4 campers de ejemplo.
- Tarifas y condiciones en una sola página.
- Legales a partir de plantilla, con banner de cookies solo informativo y sin analítica.
- Formulario por servicio de correo o función serverless, sin almacenamiento propio.
- JSON-LD solo de organización y vehículo básico.
- Una única ronda de cambios.

**Condiciones que lo permiten (todas necesarias):**
1. Dedicación de 1 persona al 100 %, o 1 persona más un apoyo parcial de contenido y QA (unas 15–20 h).
2. El cliente entrega todo el contenido el D1.
3. Acceso a dominio/DNS y hosting el D1–D2.
4. Feedback del cliente en ≤1 día hábil.
5. Hosting estático con función para el formulario.

**Opción recomendada:** comprometer en 1 semana la **entrega a revisión (URL de pruebas)** y la publicación en D8–D10. Otra salida es usar 2 personas, con unos 5–6 días hábiles.

**Alternativas:**
- B completa en 1,5–2,5 semanas con 1 persona.
- 2 personas, con unos 5–6 días hábiles.

## 2. Desglose (horas de 1 persona)

Los tamaños son relativos y no son un calendario comprometido. Los IDs T1 a T10 llevan el calificador [OPB] en el registro de control ([TASKS](../00-control/TASKS.md)).

| ID | Tarea | Entrada → Salida / cierre | h (mín–máx) | Dep. |
|---|---|---|---|---|
| T1 [OPB] | Arranque, repo, hosting estático, despliegue, base de mockups | Mockups y marca provisional → sitio vacío en URL de revisión | 4–5 | — |
| T2 [OPB] | Inicio, catálogo, fichas, tarifas, condiciones y contacto (datos en archivo) | Contenido del cliente → páginas navegables | 14–18 | T1, contenido |
| T3 [OPB] | Responsive, accesibilidad básica, imágenes optimizadas | T2 → revisión en móvil sin fallos graves | 5–7 | T2 |
| T4 [OPB] | SEO base: metadatos, sitemap, robots, datos estructurados, URLs limpias | T2 → validado con herramienta | 3–4 | T2 |
| T5 [OPB] | Legales (borrador desde plantilla) y aviso de cookies | Datos legales de la empresa → páginas marcadas "borrador a validar" | 4–6 | datos empresa |
| T6 [OPB] | Formulario de solicitud: fechas, camper, conductor, privacidad; antispam; correo; fecha y versión de la aceptación en el correo | T2 → solicitud recibida en el buzón | 8–12 | T1, correo destino |
| T7 [OPB] | Dominio, HTTPS, SPF/DKIM/DMARC | Acceso DNS → correo no cae en spam | 2–3 (+ espera de DNS) | acceso DNS |
| T8 [OPB] | QA: móvil, formulario, enlaces, rendimiento | T3–T7 → lista de pruebas pasada | 4–6 | T3–T7 |
| T9 [OPB] | Una ronda de ajustes del cliente | Feedback → cambios | 3–5 | T8, cliente |
| T10 [OPB] | Publicación y guía de edición de contenido | Aprobación → sitio en producción | 3–4 | T9 |

**Total:** 50–70 h (valor probable 60 h).

**Ruta crítica:** contenido del cliente (D1) → T2 → T6, junto con acceso DNS → T7 → T8 → feedback del cliente → T9 → T10.

**Supuesto [S] a confirmar:** "contenido editable por el equipo" significa que lo edita el proveedor mediante archivos de datos. Si el cliente debe editar solo, hace falta un CMS ligero (+1–2 días) o pasa a la fase siguiente.

## 3. Equipo y dependencias del cliente

**Equipo, todo como Supuesto [S]:** 1 full-stack al 100 %. Sin QA ni diseñador dedicados. Los mockups sirven de base visual. D1–D5 son hábiles y D6–D7 son colchón no contado. Es viable con 1 persona solo para el núcleo, sin margen.

| Día (relativo) | Dependencia del cliente | Si falla |
|---|---|---|
| D1 | Datos de los campers (plazas, equipamiento, tarifas orientativas) y fotos reales, o aceptar las de ejemplo | Cada día de retraso mueve la entrega 1:1 |
| D1 | Datos legales (razón social, NIF, domicilio), contacto, correo de destino y nombre de marca (PEND-025) | Legales incompletos |
| D1–D2 | Acceso a DNS y hosting, o permiso para usar una URL provisional | Publicación en dominio propio en riesgo |
| D2 | Textos de condiciones, o aceptar un borrador genérico | Se publica un genérico |
| D5→D6 | Feedback en ≤1 día hábil | Se pierde la ronda de ajustes |
| D6–D7 | Aprobación final | Publicación en D8 o después |

**Nota del Gestor:** en la fuente las dependencias del cliente se identifican por el día (D1 a D7) en que se necesitan y no tienen otro ID. Se conserva esa identificación.

## 4. Riesgos y exclusiones

Riesgos propios de esta entrega. Probabilidad e impacto son los del Planificador. Calificador **[OPB]** por colisión con R-001 a R-008 existentes (ISS-003). Estado de todos: OPEN. Registro en [RISKS](../00-control/RISKS.md) §6.

| ID | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R-001 [OPB] | Contenidos y fotos tardíos o de baja calidad | Alta | Alto | Contenido de ejemplo marcado; fecha límite en D1 |
| R-002 [OPB] | Textos legales y de cookies sin validar | Media | Alto | Publicar como borrador; asesoría legal del cliente fuera de alcance |
| R-003 [OPB] | Entregabilidad del correo (spam, DNS tardío) | Media | Alto | SPF/DKIM/DMARC; copia en el servicio de correo; probar con la cuenta real |
| R-004 [OPB] | Solicitudes perdidas al no haber base de datos | Baja | Alto | Registro del proveedor de correo y copia a un segundo buzón |
| R-005 [OPB] | SEO sin garantías de posicionamiento | Alta | Medio | Prometer solo lo técnico, no posiciones |
| R-006 [OPB] | Sin margen: cualquier retraso rompe la semana | Alta | Alto | Núcleo recortado, o ampliar el plazo o el equipo |
| R-007 [OPB] | Rehacer la parte pública al migrar al MVP completo | Media | Medio | Elegir una pila compatible con 04-architecture |
| R-008 [OPB] | Estacionalidad: la web debe estar publicada antes de la temporada alta | Media | Medio | Confirmar con el cliente su temporada |

**NO incluido:**
- Hosting, dominio y correo de terceros, y sus costos.
- Asesoría legal.
- Pago en línea, disponibilidad automática y panel de administración.
- Cuentas, reembolsos, MFA y auditoría.
- Mantenimiento posterior.
- Garantía de Core Web Vitals reales o de posicionamiento.
- Formato de factura, moneda e impuestos (pendiente).

## 5. Hitos relativos (núcleo, variante recomendada)

Días relativos desde el arranque (D1). **No son fechas de calendario.**

- **D1:** arranque, contenido y accesos recibidos.
- **D2:** esqueleto desplegado en URL de revisión, con inicio y una ficha.
- **D3:** catálogo, fichas y contacto completos.
- **D4:** formulario de extremo a extremo, legales en borrador y SEO.
- **D5:** QA y entrega a revisión del cliente.
- **D6:** feedback y ajustes.
- **D7:** publicación, solo si el DNS y la aprobación llegaron. Si no, D8 o después.

## 6. Cobertura de requisitos (insumo para el CR)

Insumo de [CR-001](../00-control/CHANGE-REQUESTS.md). Clasificación del Planificador; el Gestor no la ha contrastado con el texto completo de cada RF, RNF y RN.

**Cubre:** RNF-002 (SEO técnico), RNF-003 (responsive) y RNF-001 (rendimiento como objetivo, sin garantía).

**Cubre parcialmente:**
- **RF-001:** catálogo sin gestión en panel.
- **RF-006:** solicitud, sin resumen ni pago.
- **RF-010:** aviso por correo, sin justificante.
- **RF-015:** contacto; el FAQ ya estaba en Fase 2.
- **RF-016:** legales como borrador.
- **RF-017:** banner informativo, sin categorías.
- **RF-018:** SEO base.
- **RF-026:** aviso por solicitud, no por reserva ni cancelación.
- **RN-026:** fecha y versión solo en el correo.
- **RNF-004, RNF-005, RNF-006, RNF-008, RNF-013, RNF-014:** parciales; la accesibilidad es solo básica, sin auditoría AA.

**No cubre:**
- RF-002 a RF-005 (búsqueda, disponibilidad, precio y extras).
- RF-007 a RF-009 (bloqueo y pago).
- RF-011 a RF-013 (consulta, código y cancelación).
- RF-019 a RF-025 (panel).
- RF-032 (expiración de reservas).
- RN-003 y RN-010.
- RNF-007, RNF-009, RNF-010 y RNF-011.

**Sin clasificar por el Planificador (observación del Gestor, ISS-042):** RF-014, RF-027 a RF-031 y RNF-012. RF-014 y RF-027 a RF-031 ya están en Fase 2 o ampliaciones según [REQUIREMENTS](../00-control/REQUIREMENTS.md). RNF-012 no tiene valores definidos (PEND-015, PEND-021). No se les asigna cobertura en el expediente.

**Desviación a confirmar:** RN-001 y RNF-010. El cliente confirmó flota y sedes configurables desde un panel. En la Opción B pasan a contenido editable por el proveedor, y el panel pasa a la fase siguiente. Registrar como CR: cambio de alcance que sustituye el MVP completo por la entrega inicial acotada. La estimación de 28–36 semanas sigue aplicando al MVP completo ([estimacion-plazo.md](estimacion-plazo.md)).

## 7. Alcance y precio (400 USD) — **SECCIÓN INTERNA: NO COPIAR A DOCUMENTOS PARA EL CLIENTE**

> **INTERNA.** Esta sección contiene aritmética de costo, criterio de negociación y recomendaciones del Planificador para el Director. No debe copiarse, citarse ni resumirse en la propuesta ni en ningún documento para el cliente.

- **Aritmética derivada del precio fijado por el usuario [C], no una tarifa propuesta.** 400 USD sobre 60 h probables equivalen a unos 6–7 USD/h, o unos 50 USD por día de 8 h. Sobre el núcleo de 40 h son unos 10 USD/h.
- **Coherencia.** El repositorio no tiene una tarifa de referencia. El Director debe contrastar esos valores con su costo o tarifa interna. Solo es defendible si el alcance se limita al núcleo, con 1 ronda de cambios y sin costos de terceros.
- **Qué dejar claro al cliente por escrito:**
  - Qué incluye: las páginas, el formulario, el SEO técnico base y el borrador legal.
  - Qué no incluye: la lista de exclusiones de la sección 4.
  - Los plazos dependen de sus entregas el D1 (contenido, accesos).
  - Hay una sola ronda de cambios; lo adicional es otro alcance.
  - Los costos de dominio, hosting, correo y asesoría legal los asume el cliente.
  - La moneda y los impuestos (USD o EUR, IVA) se definen antes de facturar.
- **Negociación.** Si se recorta el precio, hay que recortar alcance (por ejemplo, fichas o ronda de cambios) y no la calidad. No ceder plazo sin ceder alcance.

## Decisiones pendientes para el Director

Registradas en [DECISIONS](../00-control/DECISIONS.md) (DEC-034 y PEND-043 a PEND-047, calificador [OPB]).

1. Elegir entre el núcleo en 1 semana, la B completa en unas 2 semanas, o 2 personas. *(El usuario eligió la Opción B con plazo objetivo de 1 semana [C]; la variante —núcleo en 1 semana, B completa o 2 personas— sigue sin precisar: ver PEND-046 [OPB].)*
2. Quién edita el contenido: el proveedor o el cliente (PEND-045 [OPB]).
3. USD o EUR, e impuestos (PEND-043 [OPB]).
4. Confirmar la desviación de RN-001 y RNF-010, y abrir el CR (CR-001, `WAITING_FOR_APPROVAL`; PEND-044 [OPB]).
5. Compatibilidad de la pila con 04-architecture (PEND-047 [OPB]).

## Enlaces

[Solicitud de cambio CR-001](../00-control/CHANGE-REQUESTS.md) · [Decisiones](../00-control/DECISIONS.md) · [Riesgos](../00-control/RISKS.md) · [Tareas](../00-control/TASKS.md) · [Trazabilidad](../00-control/TRACEABILITY.md) · [Estado del proyecto](../00-control/PROJECT-STATE.md) · [Estimación del MVP completo (28–36 semanas)](estimacion-plazo.md) · [Plan de implementación](implementation-plan.md) · [Requisitos](../00-control/REQUIREMENTS.md)
