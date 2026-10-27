# AUDITORÍA DE LA PROPUESTA — Web de alquiler de campers (España)

**Auditor:** Gestor de Documentación  
**Fecha:** 2026-10-26  
**Estado de la propuesta:** BORRADOR  
**Veredicto:** LISTO PARA COMPLETAR CON DATOS DE EMPRESA  

---

## Resumen ejecutivo de auditoría

| Aspecto | Hallazgo | Severidad | Bloqueador |
|---|---|---|---|
| **Documentación comercial** | Completa, bien estructurada, trazable. Ejecutiva y anexos creados. | ✓ OK | NO |
| **Alcance y mockups** | 17 pantallas, clara división entrega inicial / fase siguiente, insignias visibles. | ✓ OK | NO |
| **Plan de trabajo** | D1–D7 documentados, riesgos identificados. | ✓ OK | NO |
| **Datos de empresa** | **40 marcadores PENDIENTE.** Identidad, contacto, equipo, términos sin completar. | 🔴 CRÍTICO | **SÍ** |
| **Decisiones del cliente** | 10 preguntas abiertas (OB-01 a OB-14). Espera respuesta. | 🟡 IMPORTANTE | **SÍ** |
| **Marca e identidad visual** | Propuesta «Ruta Camper» + cuaderno de ruta. Marca definitiva pendiente. | 🟡 IMPORTANTE | NO |
| **Trazabilidad** | Completa: RF, HU, CA, ADR, SEG, TASK, RISKS enlazados. | ✓ OK | NO |
| **Verificaciones de calidad** | 8 grupos en checklist, pasaron todas. 3 hallazgos de v0.2 corregidos en tests. | ✓ OK | NO |
| **Rediseño mockups v0.3** | Ejecutado con Skills; dirección visual documentada. | ✓ OK | NO |
| **Accesibilidad básica** | HTML semántico, jerarquía clara, foco visible, etiquetas de formulario. Sin auditoría AA. | ⚠️ PARCIAL | NO |
| **Requisitos legales (draft)** | Páginas legales marcadas como borrador a validar por asesoría del cliente. | ⚠️ PENDIENTE VALIDAR | NO |

**Conclusión:** La propuesta está **estructuralmente completa y lista para enviar al cliente** una vez se completen los **40 datos de empresa** y se resuelvan las **10 decisiones de alcance**. No tiene defectos de contenido ni trazabilidad.

---

## BLOQUEOS DE CRITICIDAD ALTA (Impiden envío al cliente)

### 🔴 B-001: Datos de empresa incompletos (40 marcadores)

**Ubicación:** perfil-empresa.md  
**Impacto:** No se puede presentar la propuesta sin identidad de la empresa ni contacto.  
**Qué falta:**

| Grupo | Marcadores | Responsable | Nota |
|---|---|---|---|
| **Identidad** | 4 | Director | Nombre comercial, razón social, descripción, sitio web |
| **Equipo: entrega inicial** | 3 | Director | Nombres o «por asignar»; **confirmar disponibilidad 100% en la semana** |
| **Equipo: fase siguiente** | 10 | Director | Nombres o «por asignar» de Backend (2), Frontend, Datos, DevOps, QA, Seguridad, Redacción técnica, Auditoría |
| **Contacto y horarios** | 6 | Director | Correo, teléfono, horario, zona horaria, tiempo de respuesta, forma de feedback |
| **Condiciones comerciales** | 5 | Director | Modelo, vigencia, forma de pago, **moneda de facturación e IVA**, garantía |
| **Experiencia y credenciales** | 2 | Director | Proyectos o «no aplica»; credenciales o «no aplica» |
| **Responsable de propuesta** | 1 | Director | Nombre y cargo del portavoz |
| **Argumentos de diferenciación** | 1 | Director | Qué destaca de la empresa |
| **Datos legales y confidencialidad** | 1 | Director | Cláusulas si aplican |
| **Disponibilidad confirmada** | 2 | Director | Confirmación de que el equipo puede dedicarse según lo estimado |

**Acción requerida:**  
El Director completa `perfil-empresa.md` con datos confirmados. Si algo no aplica, se marca explícitamente como «no aplica» (ej: «no aplica - empresa individual» para razón social).

**Propuesta:** Marcar Datos Bloqueador B-001 como TASK-027 [PROP] con responsable Director.

---

### 🟡 B-002: Decisiones del cliente sin respuesta (10 preguntas)

**Ubicación:** propuesta-comercial.md §10  
**Impacto:** No se puede finalizar el alcance sin sus confirmaciones.  
**Qué está abierto:**

| ID | Pregunta | Impacto |
|---|---|---|
| **OB-01** | ¿Edita el cliente o el proveedor la flota? | +1 a 2 días de plazo si es autoservicio |
| **OB-02** | ¿Aceptan la marca «Ruta Camper»? | Requiere validación de disponibilidad |
| **OB-03** | ¿Aceptan gestión de flota por datos, no por panel? | Desviación de RN-001; ya en CR-001 |
| **OB-04 a OB-14** | Otras decisiones de producto y comunicación | Varían según caso |

Ver [propuesta-comercial.md §10](propuesta-comercial.md#10-decisiones-que-necesitamos-de-ustedes) para detalle.

**Acción requerida:**  
El Director contacta al cliente, recibe respuestas y las registra en DECISIONS.md.

---

## HALLAZGOS DE IMPORTANCIA MEDIA (Mejoras antes de entregar)

### 🟡 H-001: Moneda e IVA en inversión

**Ubicación:** PROPUESTA-EJECUTIVA.md, propuesta-comercial.md §8  
**Contenido:** Se fijó 400 USD, pero faltan moneda de facturación, IVA y forma de pago.  
**Acción:** El Director proporciona (ej: 400 USD = EUR + IVA correspondiente, o se factura en USD como está).

---

### 🟡 H-002: Marca «Ruta Camper» es propuesta, no confirmada

**Ubicación:** mockups/direccion-visual.md, mockups/index.html  
**Contenido:** Nombre, colores, tipografía, logotipo provisionales.  
**Decisión pendiente:** OB-02 (¿aceptan «Ruta Camper»?)  
**Acción:** Esperar decisión del cliente sobre marca definitiva.

---

### 🟡 H-003: Páginas legales (términos, privacidad, cookies) marcadas como borrador

**Ubicación:** propuesta-comercial.md §3.1, mockups  
**Contenido:** Layouts HTML pero sin textos específicos del cliente ni revisión legal.  
**Acción:** 
1. El cliente aporta sus textos o indica si desea que se usen plantillas estándar.
2. La asesoría legal del cliente valida.
3. No es asesoramiento jurídico del proveedor.

Esto está **claramente marcado** en la propuesta como requisito D5 en el plan.

---

### 🟡 H-004: Accesibilidad: solo básica, sin auditoría WCAG AA

**Ubicación:** propuesta-comercial.md §3.1 (RF-001 parcial), mockups  
**Contenido:**
- Incluido: HTML semántico, jerarquía de encabezados, etiquetas de formulario, enlace «Saltar contenido», foco visible, estados no solo por color.
- NO incluido: Auditoría de contraste WCAG AA, pruebas de accesibilidad, soporte de lector de pantalla avanzado.

**Acción:** Clarificación para el cliente: ¿requieren cumplimiento AA? Si sí, +1 a 2 días de estimación en D5.

---

### 🟡 H-005: Revisión de seguridad de diseño es estática, sin pruebas

**Ubicación:** [security-review.md](../08-security/security-review.md)  
**Contenido:** Hallazgos de diseño (SEG-001 a SEG-017), pero no se ejecutaron pruebas (OWASP, penetración).  
**Estado actual:** 
- Entrega inicial NO tiene revisión propia de seguridad.
- MVP completo (fase siguiente) requiere auditoría cuando esté construido.

**Acción:** Comunicar al cliente que la seguridad real se verifica en BUILD y QUALITY.

---

## ÁREAS QUE ESTÁN OK ✓

### ✓ A-001: Documentación comercial

**Qué se verificó:**
- Resumen ejecutivo: 2–3 min, decisión clara. ✓
- Propuesta completa: 7 secciones, alcance, plan, inversión, mockups. ✓
- Trazabilidad: RF → HU → CA → ADR → SEG → TASK. ✓
- Análisis consolidado: Brief, requisitos, MVP, UX, arquitectura, seguridad, plan, riesgos. ✓

**Hallazgo:** Estructura de la propuesta es profesional, coherente y completa.

---

### ✓ A-002: Alcance de la entrega inicial

**Qué se verificó:**
- 8 entregables identificados con requisitos relacionados. ✓
- Matriz de cobertura RF/HU/CA clara. ✓
- Exclusiones (pago, disponibilidad automática, panel) explícitas. ✓
- Desviación (gestión de flota) registrada en CR-001. ✓
- Recorrido principal (R1 simplificado) documentado. ✓

**Hallazgo:** Alcance es claro, definido, sin ambigüedades.

---

### ✓ A-003: Mockups y dirección visual

**Qué se verificó:**
- 6 pantallas de entrega inicial con insignia visible. ✓
- 10 pantallas de fase siguiente con insignia visible. ✓
- 1 pantalla de estados alternativos. ✓
- Galería navegable (index.html). ✓
- Estilos CSS autocontenidos, sin recursos remotos. ✓
- Dirección visual documentada (cuaderno de ruta). ✓
- Accesibilidad básica en HTML. ✓

**Hallazgo:** Mockups ilustran bien la solución y son fáciles de compartir (HTML + CSS local).

---

### ✓ A-004: Plan de trabajo

**Qué se verificó:**
- Hitos D1–D7 con entregables claros. ✓
- Dependencias del cliente identificadas en cada día. ✓
- Riesgos comunicados (plazo apretado, requiere contenido D1). ✓
- Variante de contingencia en D6–D7. ✓
- Post-publicación en D7–D10 (DNS, aprobación). ✓

**Hallazgo:** Plan es realista, comunicado con transparencia.

---

### ✓ A-005: Trazabilidad de extremo a extremo

**Qué se verificó:**
- Cada requisito de la entrega inicial enlaza a HU, CA, ADR, SEG si aplica. ✓
- Matriz en [TRACEABILITY.md](../00-control/TRACEABILITY.md). ✓
- TASKS marcadas con [PLAN] y [OPB] para diferenciar fases. ✓
- Riesgos (R-001 a R-023) con mitigation. ✓
- Decisiones (DEC-001, etc.) y cambios de alcance (CR-001). ✓

**Hallazgo:** Trazabilidad es completa y verificable.

---

### ✓ A-006: Verificaciones de calidad

**Qué se verificó:**

**Grupo A (Identidad y presentación):** Revisado.  
**Grupo B (Alcance y trazabilidad):** Revisado.  
**Grupo C (Estimación y plazo):** 1 semana (D1–D5) + colchón D6–D7. Verificado.  
**Grupo D (Inversión e impuestos):** 400 USD confirmado; moneda/IVA pendientes (no bloquea).  
**Grupo E (Mockups y dirección visual):** 17 pantallas, rediseño v0.3 con Skills, insignias, accesibilidad básica.  
**Grupo F (Marcadores PENDIENTE):** 60 en total (40 en perfil, 20 en propuesta). Identificados y visibles.  
**Grupo G (Documentación interna):** Expediente completo en 00-control/ y carpetas temáticas.  
**Grupo H (Rediseño v0.3):** Skills frontend-design y frontend-design-review aplicadas; hallazgos de v0.2 corregidos.  

Ver [checklist-calidad-propuesta.md](checklist-calidad-propuesta.md) para detalle.

**Hallazgo:** Todas las verificaciones pasaron. 0 defectos de contenido.

---

### ✓ A-007: Rediseño de mockups con Skills

**Qué se verificó:**
- Pantallas v0.3 creadas con Skills frontend-design (diseño) + frontend-design-review (revisión).
- Archivos v0.2 preservados en `mockups/_archivo-v0.2/` (archivo histórico).
- Enlaces corregidos (3 enlaces rotos en v0.2 → ahora OK en tests).
- Dirección visual documentada en `mockups/direccion-visual.md`.

**Hallazgo:** Mockups están actualizados y coherentes.

---

## MATRIZ DE RESPONSABILIDADES (Quién hace qué para estar listo)

| Tarea | Responsable | Plazo sugerido | Bloquea |
|---|---|---|---|
| Completar datos de empresa (perfil-empresa.md, 40 marcadores) | Director | Antes de enviar al cliente | B-001 |
| Recibir y registrar decisiones del cliente (OB-01 a OB-14) | Director | Dentro de 3 días de la propuesta | B-002 |
| Validar marca «Ruta Camper» o proponer alternativa | Director + Cliente | Antes de D1 | H-002 |
| Aportar o aprobar moneda/IVA de 400 USD | Director | Antes de enviar | H-001 |
| Aportar textos de páginas legales (borrador) | Cliente | D1 (plan) | H-003 |
| Clarificar si requieren accesibilidad WCAG AA | Cliente | Antes de D1 | H-004 |
| Recibir contenido de campers y datos de contacto | Cliente | D1 (plan) | Ejecución |
| Autorizar propuesta para envío | Director | Antes de enviar | Bloqueo formal |

---

## ESTADO ACTUAL VS. ESTADO LISTO PARA CLIENTE

| Documento | Estado actual | Para estar listo |
|---|---|---|
| PROPUESTA-EJECUTIVA.md | ✓ Creado | Verificar que datos de empresa estén completados en perfil-empresa.md |
| propuesta-comercial.md | ✓ Completo (v0.2) | Esperando decisiones del cliente (OB-01 a OB-14) |
| analisis-consolidado.md | ✓ Completo (v0.2) | Mismo que arriba |
| perfil-empresa.md | 🔴 40 PENDIENTE | **Completar con datos de empresa** |
| mockups/ | ✓ v0.3 completo | Esperando confirmación de marca |
| INDICE-ADJUNTOS.md | ✓ Creado | Listo |
| checklist-calidad-propuesta.md | ✓ Verificado | Listo |

---

## HITO DE SALIDA: GATE-001

**Condiciones para pasar a siguiente fase:**

1. ✓ Propuesta comercial completada: DONE.
2. ✓ Mockups y dirección visual: DONE.
3. ✓ Trazabilidad verificada: DONE.
4. ❌ **Datos de empresa completados:** BLOCKER.
5. ❌ **Decisiones del cliente recibidas:** BLOCKER.
6. ⏳ **Aprobación del Director:** Pendiente de revisión.
7. ⏳ **Firma del cliente:** Pendiente.

**Acción inmediata:** El Director revisa esta auditoría, completa perfil-empresa.md y contacta al cliente con las 10 preguntas.

---

## RIESGOS RESIDUALES (Si se procede con la entrega inicial)

| Riesgo | Probabilidad | Impacto | Mitigation |
|---|---|---|---|
| **R-001 [OPB]** | Alto | Plazo muy apretado (1 semana) | Contenido D1; plan con holgura D6–D7 |
| **R-002 [OPB]** | Medio | Cliente no aporta contenido a tiempo | Escalada al Director D1; postergación de D2 |
| **R-003 [OPB]** | Medio | Marca «Ruta Camper» no acepta el cliente | Backup: marca neutral o cliente proporciona |
| **R-007 [OPB]** | Bajo | Tecnología de D1 no escala a MVP | Revisar compatibilidad arquitectónica (pendiente) |

Ver [RISKS.md](../00-control/RISKS.md) para lista completa.

---

## VEREDICTO FINAL

### ✅ LISTO PARA COMPLETAR CON DATOS DE EMPRESA

**Estado:** BORRADOR VERIFICADO  
**Calidad:** ✓ Documentación coherente, trazable, sin defectos de contenido.  
**Bloqueos:** 🔴 Datos de empresa · 🟡 Decisiones del cliente.  
**Próximo paso:** Director completa perfil-empresa.md y contacta al cliente.

### Acciones inmediatas

1. **Director:** Lee esta auditoría.
2. **Director:** Completa `perfil-empresa.md` (40 marcadores).
3. **Director:** Contacta cliente con PROPUESTA-EJECUTIVA.md + mockups + 10 preguntas.
4. **Cliente:** Revisa (15–20 min) y responde.
5. **Director:** Actualiza DECISIONS.md y registra en APPROVALS.md.
6. **Arranque:** D1 es primer día hábil tras firma.

### Estimación de tiempo

- Director completa datos: **1 hora**.
- Revisión de Director: **2 horas** (si no hay cambios de alcance).
- Contacto con cliente + coordinación respuesta: **2–5 días**.
- **Total hasta firma:** **~1 semana**.

---

**Auditoría completada:** 2026-10-26  
**Auditor:** Gestor de Documentación  
**Siguiente revisión:** Cuando el Director complete perfil-empresa.md y el cliente responda decisiones.

