# ÍNDICE DE ANEXOS — Web de alquiler de campers (España)

Este documento organiza todo el material de la propuesta (12-propuesta/) para referencia rápida.

---

## DOCUMENTOS DE LA PROPUESTA

| Archivo | Tipo | Para quién | Uso | Tamaño aproximado | Duración de lectura |
|---|---|---|---|---|---|
| **PROPUESTA-EJECUTIVA.md** | Resumen ejecutivo | Cliente + Director | Decisión sobre si avanzar (2–3 min) | 3 KB | 2–3 min |
| **propuesta-comercial.md** | Propuesta comercial completa | Cliente + Director | Detalle de oferta, alcance, plan, inversión, decisiones | ~90 KB | 20–25 min |
| **analisis-consolidado.md** | Análisis técnico consolidado | Director + Equipo | Brief, requisitos, MVP, UX, arquitectura, seguridad, plan, riesgos, decisiones, identificadores | ~120 KB | 30–45 min |
| **perfil-empresa.md** | Identidad y capacidades | Director | Datos de la empresa, equipo, contacto, términos comerciales · **PENDIENTE COMPLETAR** | ~8 KB | 5 min |

---

## MOCKUPS (Galería y pantallas)

| Archivo | Tipo | Pantalla | Alcance | Estado |
|---|---|---|---|---|
| **mockups/index.html** | Galería navegable | Todas las 17 pantallas | Inicio, gestión de pantallas | Interactivo en navegador |
| **mockups/README.md** | Documentación | Mapas y leyenda | Qué son los mockups, matriz pantalla → RF/HU/CA | Referencia |
| **mockups/direccion-visual.md** | Cuaderno de ruta | Sistema de diseño | Marca, tipografía, colores, tokens, decisiones visuales · **PROPUESTA, NO APROBADA** | Guía interna |
| **mockups/_base.css** | Estilos CSS | Compartidos | Estilos autocontenidos (sin recursos remotos) | Producción |

### Pantallas de la entrega inicial

| Archivo | Nombre | Requisitos | Insignia | Estado |
|---|---|---|---|---|
| **01-inicio-entrega-inicial.html** | Inicio con catálogo | RF-001, RF-018 · HU-001, HU-015 | **ENTREGA INICIAL** | Borrador |
| **03-ficha-camper-entrega-inicial.html** | Ficha de camper | RF-001 · HU-001 | **ENTREGA INICIAL** | Borrador |
| **10-movil-entrega-inicial.html** | Inicio y solicitud (móvil) | RNF-003, RF-001, RF-006 · HU-016 | **ENTREGA INICIAL** | Borrador |
| **11-solicitud-reserva.html** | Formulario de solicitud | RF-006, RF-010, RF-026, RN-026 · HU-005 | **ENTREGA INICIAL** | Borrador |
| **12-tarifas-y-condiciones.html** | Tarifas y condiciones | RF-001, RF-016 · HU-001 | **ENTREGA INICIAL** | Borrador |
| **13-catalogo-entrega-inicial.html** | Catálogo (3–4 campers) | RF-001 · HU-001 | **ENTREGA INICIAL** | Borrador |

### Pantallas de la fase siguiente (MVP completo)

| Archivo | Nombre | Requisitos | Insignia | Estado |
|---|---|---|---|---|
| **01-inicio.html** | Inicio con buscador | RF-002, RF-018 · HU-001, HU-002, HU-015 | **FASE SIGUIENTE** | Borrador |
| **02-resultados-busqueda.html** | Resultados con disponibilidad | RF-002, RF-003, RF-004 · HU-002, HU-003, HU-004 | **FASE SIGUIENTE** | Borrador |
| **03-ficha-camper.html** | Ficha completa | RF-001, RF-003 · HU-001, HU-003 | **FASE SIGUIENTE** | Borrador |
| **04-resumen-y-datos-conductor.html** | Resumen y datos del conductor | RF-004, RF-006 · HU-004, HU-005 | **FASE SIGUIENTE** | Borrador |
| **05-pago.html** | Formulario de pago (hosted) | RF-007, RF-008, RF-009 · HU-006, HU-007 | **FASE SIGUIENTE** | Borrador |
| **06-confirmacion.html** | Confirmación de reserva | RF-010, RF-032 · HU-008, HU-009, HU-010 | **FASE SIGUIENTE** | Borrador |
| **07-consulta-reserva.html** | Consulta y cancelación | RF-011, RF-012, RF-013 · HU-011, HU-012 | **FASE SIGUIENTE** | Borrador |
| **08-admin-panel-reservas.html** | Panel: reservas | RF-019, RF-023 · HU-017, HU-021 | **FASE SIGUIENTE** | Borrador |
| **09-admin-flota-tarifas.html** | Panel: flota, sedes, tarifas | RF-020, RF-021, RF-022 · HU-018, HU-019, HU-020 | **FASE SIGUIENTE** | Borrador |
| **10-movil-inicio-y-resultados.html** | Inicio y resultados (móvil) | RF-002, RF-003 · HU-002, HU-016 | **FASE SIGUIENTE** | Borrador |
| **14-estados.html** | Estados alternativos | Errores, confirmación, sin datos | Múltiples | Borrador |

---

## DOCUMENTOS DE CONTROL DEL PROYECTO

(En la carpeta `../00-control/`, no aquí; se enlazan para referencia)

| Archivo | Propósito | Para quién |
|---|---|---|
| **PROJECT-STATE.md** | Estado maestro del proyecto | Director + Equipo |
| **REQUIREMENTS.md** | Requisitos funcionales y no funcionales | Equipo técnico |
| **DECISIONS.md** | Decisiones tomadas o propuestas | Equipo + Director |
| **TASKS.md** | Tareas, estado y asignación | Director + Equipo |
| **RISKS.md** | Riesgos, impedimentos y mitigation | Equipo |
| **TRACEABILITY.md** | Matriz RF → HU → CA → ADR → SEG → TASK → CP | Auditoría |
| **APPROVALS.md** | Aprobaciones y puertas | Director |
| **CHANGE-REQUESTS.md** | Solicitudes de cambio (ej: CR-001, opción B) | Director + Cliente |
| **AGENT-ACTIVITY.md** | Actividad del equipo de agentes | Director + Auditoría |

---

## FUENTES DEL EXPEDIENTE

(En las carpetas del proyecto, no en propuesta; la propuesta las resume o las enlaza)

| Carpeta | Archivo | Propósito |
|---|---|---|
| **00-intake/** | client-brief.md | Brief del cliente |
| **01-discovery/** | requirements.md | Análisis de requisitos |
| **02-product/** | mvp-and-backlog.md | Definición de MVP, historias, criterios |
| **03-ux/** | ux-specification.md | Especificación UX/UI completa |
| **04-architecture/** | solution-architecture.md | Arquitectura técnica |
| **05-planning/** | implementation-plan.md | Plan de implementación (MVP completo) |
| **05-planning/** | estimacion-plazo.md | Estimación de plazo (MVP: 28–36 semanas) |
| **05-planning/** | estimacion-opcion-b.md | Estimación opción B (entrega inicial: 1 semana) |
| **08-security/** | security-review.md | Revisión de seguridad de diseño (estática) |

---

## DOCUMENTOS DE VERIFICACIÓN

| Archivo | Propósito | Para quién |
|---|---|---|
| **checklist-calidad-propuesta.md** | Verificaciones realizadas antes de entregar | Director + Auditoría |

### Grupos de verificación en checklist

- **A. Identidad y presentación**
- **B. Alcance y trazabilidad**
- **C. Estimación y plazo**
- **D. Inversión e impuestos**
- **E. Mockups y dirección visual**
- **F. Marcadores PENDIENTE y bloqueos**
- **G. Documentación interna**
- **H. Rediseño v0.3 (Skills frontend-design + frontend-design-review)**

---

## CÓMO LEER ESTE PAQUETE

### Para el cliente (decisión rápida: sí/no)

1. **PROPUESTA-EJECUTIVA.md** (2–3 min): «Qué, cuándo, cuánto» y decisiones necesarias.
2. **mockups/index.html** (5–10 min): Ver las pantallas en el navegador; las de la entrega inicial llevan insignia «ENTREGA INICIAL».
3. **propuesta-comercial.md** sección 10 (5 min): Preguntas que necesitamos que contesten.

**Tiempo total: 15–20 minutos.**

### Para el Director (revisión de completitud)

1. **PROPUESTA-EJECUTIVA.md** (resumen).
2. **propuesta-comercial.md** completo (todo).
3. **perfil-empresa.md** (identificar qué falta).
4. **checklist-calidad-propuesta.md** (verificaciones).
5. Luego: **analisis-consolidado.md** (detalle técnico si es necesario).

### Para el equipo técnico (implementación futura)

1. **analisis-consolidado.md** (brief, requisitos, MVP, UX, arquitectura, plan).
2. **mockups/README.md** + **mockups/direccion-visual.md** (qué se va a construir).
3. **mockups/01-inicio-entrega-inicial.html** + otras pantallas de entrega inicial (qué entregar en la semana 1).
4. **implementation-plan.md** (tareas y secuencia).

---

## ESTADO DE LOS DOCUMENTOS

- **PROPUESTA-EJECUTIVA.md:** BORRADOR (entregado 2026-10-26).
- **propuesta-comercial.md:** BORRADOR v0.2 (reestructurada para opción B).
- **analisis-consolidado.md:** BORRADOR (incluye análisis de opción B).
- **perfil-empresa.md:** BORRADOR (40 marcadores PENDIENTE).
- **mockups:** BORRADOR v0.3 (rediseño con Skills frontend-design; archivos v0.2 en `_archivo-v0.2/`).
- **checklist-calidad-propuesta.md:** BORRADOR (verificaciones documentadas).

**Ningún documento está aprobado ni autorizado para envío al cliente hasta que:**

1. Se completen los 40 marcadores PENDIENTE de empresa (datos de la empresa, equipo, contacto, términos).
2. Se resuelvan las 10 decisiones de alcance (sección 10 de propuesta-comercial).
3. El Director apruebe y autorice el envío.
4. El cliente responda y firme.

---

## BLOQUEADORES (qué falta para estar listo)

| Bloqueo | Dónde | Impacto | Responsable |
|---|---|---|---|
| Datos de empresa (40 marcadores) | perfil-empresa.md | No se puede presentar al cliente sin identidad, contacto, equipo, términos | Director |
| Decisiones del cliente (OB-01 a OB-14) | propuesta-comercial.md §10 | No se puede finalizar el plan sin sus respuestas | Cliente (coordinado por Director) |
| Aprobación del Director | GATE-001 | No se envía nada al cliente sin revisión y visto bueno | Director |
| Firma del cliente | APPROVALS.md | No se autoriza arranque sin aprobación escrita | Cliente |

---

## NAVEGACIÓN RÁPIDA

### Por audiencia

- **Cliente:** PROPUESTA-EJECUTIVA → mockups/index.html → propuesta-comercial.md §10.
- **Director:** Todo.
- **Equipo técnico:** analisis-consolidado.md → implementation-plan.md → mockups.
- **Auditoría:** TRACEABILITY.md + checklist-calidad-propuesta.md + APPROVALS.md.

### Por tema

- **«¿Cuánto cuesta y cuándo?»** → PROPUESTA-EJECUTIVA §«Inversión confirmada» + propuesta-comercial.md §6 y §8.
- **«¿Qué entra en la entrega inicial?»** → propuesta-comercial.md §3.
- **«¿Y en la fase siguiente?»** → propuesta-comercial.md §11.
- **«¿Qué requisitos cubre?»** → analisis-consolidado.md §2 (opción B) + propuesta-comercial.md §3.2.
- **«¿Cuáles son los riesgos?»** → analisis-consolidado.md §9 + RISKS.md.
- **«¿Cómo es el plan?»** → propuesta-comercial.md §5 + implementation-plan.md.
- **«¿Qué decisiones necesitamos?»** → propuesta-comercial.md §10.
- **«¿Cómo se ve?»** → mockups/index.html (abrir en navegador).

---

## VERSIONES Y CAMBIOS

| Fecha | Versión | Cambio |
|---|---|---|
| 2026-10-26 | Propuesta v0.1 | Creación inicial con MVP completo |
| 2026-10-26 | Propuesta v0.2 | Opción B (entrega inicial) como oferta principal |
| 2026-10-26 | Mockups v0.3 | Rediseño con Skills; pantallas 13 y 14 nuevas; dirección visual |
| 2026-10-26 | **Propuesta-Ejecutiva** | Resumen para decisión en 2–3 minutos |
| 2026-10-26 | **INDICE-ADJUNTOS.md** | Este documento |

---

## Preguntas frecuentes sobre este material

**P: ¿Por qué hay tantos marcadores `{{PENDIENTE: ...}}`?**  
R: La propuesta es honesta sobre qué falta. Antes de enviarla al cliente, el Director completa todos los campos con datos confirmados o marca explícitamente como «no aplica».

**P: ¿Se puede cambiar de verdad o solo es una propuesta?**  
R: Todo es negociable. La opción B es una **Recomendación** que requiere decisión del cliente. Cualquier cambio se registra como CR (solicitud de cambio).

**P: ¿Por qué el MVP completo es fase siguiente y no ahora?**  
R: Porque el plazo de 1 semana no permite pago seguro y disponibilidad automática confiables. La opción B es salir pronto con lo que funciona sin intermediación de pago. Después se añaden los componentes críticos.

**P: ¿Qué pasa si el cliente no aporta contenido el primer día?**  
R: El plazo se pospone. Por eso el plan de contingencia y holgura están en D6–D7.

**P: ¿Quién dirige la propuesta ante el cliente?**  
R: El Director de Proyectos es el único portavoz (regla corporativa del equipo).

---

## Contacto (cuando la propuesta esté lista)

{{PENDIENTE: nombre y correo del Director o portavoz de la empresa}}

---

**Última revisión:** 2026-10-26  
**Creado por:** Gestor de Documentación (verificación de paquete propuesta)  
**Estado:** BORRADOR — Falta completar datos de empresa y confirmar decisiones del cliente
