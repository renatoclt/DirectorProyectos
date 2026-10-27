# Revisión de seguridad del diseño: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Reporte del agente Revisor de Seguridad ("Seguridad del diseño campers"), persistido por el Gestor de Documentación sin cambiar su significado.  
> **Tipo de revisión:** estática y documental **de diseño**. **No se ejecutó ninguna prueba de seguridad.**  
> **Aprobación:** NINGUNA. GATE-002 sigue **PENDING**, el alcance **NO está aprobado** y no existe solicitud PLANNING → BUILD ([APPROVALS](../00-control/APPROVALS.md)). BUILD y despliegue están prohibidos.

**Aviso del Gestor:**
- El "veredicto" de la sección final es la valoración del Revisor sobre un borrador de diseño. **No es una aprobación del proyecto, de una puerta ni de un riesgo.** Ninguna aceptación de riesgo ha sido solicitada ni concedida.
- Este documento no es asesoramiento jurídico. Los puntos legales se marcan "validar con asesoría" (PEND-010).
- Los hallazgos SEG-001 a SEG-017 están en estado **ABIERTO** ([RISKS](../00-control/RISKS.md) §4). Esto no indica que el sistema sea seguro ni inseguro: no existe sistema.
- El Revisor leyó el borrador de arquitectura desde un archivo temporal (versión entregada por el agente), no desde [solution-architecture.md](../04-architecture/solution-architecture.md). No indica haber leído la especificación UX/UI.

# Reporte de agente: Revisión de seguridad del diseño, MVP alquiler de campers (España)

- **Agente:** Revisor de Seguridad (independiente, no correctivo)
- **Contrato:** `security-reviewer.contract.json`. Fase DESIGN, solo lectura. No hay conflicto con el contrato. No edité nada ni corregí hallazgos.
- **Archivos consultados:**
  - `DECISIONS.md`: leído completo.
  - `requirements.md`: secciones de reglas de negocio (RN-007 a RN-027), validaciones, RNF y casos de aceptación, más búsquedas por palabra clave. No lo leí entero.
  - `mvp-and-backlog.md`: HU y los CA-002 a CA-025 más relevantes. No lo leí entero.
  - Arquitectura borrador (archivo temporal): leída completa.
- **Archivos modificados:** ninguno.
- **Comandos o pruebas ejecutadas:** ninguna.
- **Resultado:** COMPLETADO_CON_PENDIENTES.

## Alcance y método

Revisión **estática y documental** del diseño. Todas las decisiones (DEC-001 a DEC-032) están en estado PROPUESTA. La arquitectura es un borrador y las tecnologías son recomendaciones. Usé como guía OWASP ASVS y Top 10 y un modelado de amenazas básico (STRIDE) sobre los flujos de reserva, pago, consulta y panel. Los puntos legales (RGPD/LOPDGDD, LSSI-CE, PSD2) los marco como **"validar con asesoría"**, no como asesoramiento jurídico.

## Superficie de ataque

1. **Público anónimo:** búsqueda de disponibilidad, creación de reserva y holds, formulario de contacto y consulta por código + email. La consulta permite cancelar y generar un reembolso.
2. **Webhook de la pasarela:** endpoint entrante, autenticado solo por firma.
3. **Panel `/admin`:** misma aplicación y mismo origen que la parte pública. Rol único con acceso a datos personales, tarifas, bloqueos y reembolsos.
4. **Subida de imágenes**, almacén de objetos y CDN.
5. **Correo saliente (outbox):** contiene el código de reserva y datos personales.
6. **Worker y conciliación:** acceso a la BD y a la API de la pasarela.
7. **Terceros:** hosting, pasarela, correo, CDN, observabilidad, CAPTCHA o analítica.
8. **Cadena de suministro y despliegue:** dependencias, CI, secretos, copias de seguridad.

## Controles verificados (solo en el diseño, nada implementado)

- Exclusión por rango en PostgreSQL contra solapes, con hold en la misma transacción (ADR-003).
- Precio calculado en servidor y congelado (RN-010, VAL-017).
- Confirmación solo por webhook; la redirección no confirma (RN-023, ADR-005).
- Idempotencia con `payment_event` de id único y verificación de importe y moneda (ADR-006).
- Pago alojado, sin datos de tarjeta en la web (RNF-006, CA-031).
- Errores uniformes y límite de intentos en el acceso por código (CA-013, ADR-011).
- Consentimientos versionados y no premarcados (RN-026, VAL-014).
- Cookies no técnicas solo tras el consentimiento (RF-017).
- Documentos del conductor verificados en persona (DEC-010), lo que minimiza datos.
- Hash adaptativo para la contraseña del admin y cookies `HttpOnly/Secure/SameSite`.
- Secretos fuera del repositorio.
- Copias cifradas con restauración probada (como recomendación).

Todo esto es intención de diseño. **Ninguno está verificado en ejecución.**

## Hallazgos

Escala: Alta, Media, Baja. No identifico una Crítica en diseño. Varias Altas deben cerrarse antes de BUILD o de producción.

| ID | Sev. | Ubicación | Riesgo | Requisito que debe cumplirse | Verificación propuesta |
|---|---|---|---|---|---|
| **SEG-001** | Alta | ADR-011, RN-025, DEC-005, HU-012 | El email no es un secreto. Quien conozca o adivine el email y obtenga el código accede a datos personales y puede **cancelar y disparar un reembolso**. No hay mínimo de entropía, política de bloqueo ni definición del código en URL, logs o caché. El enlace mágico solo se menciona como alternativa. | (a) Código de CSPRNG con entropía mínima documentada (≥ 64 bits, valor a fijar). (b) Respuesta, estado y tiempos idénticos en cualquier fallo. (c) Límites por IP, por código y por email, con retardo progresivo. (d) Código y email solo por POST o cuerpo, nunca en query string. (e) `Cache-Control: no-store`, `Referrer-Policy` y `noindex`. (f) Decidir enlace mágico o reautenticación por correo antes de **cancelar**. (g) Mostrar datos mínimos hasta verificar. | Pruebas de enumeración y fuerza bruta (CA-013 ampliado). Comparar respuestas y tiempos. Revisar logs y CDN en busca del código. Test de que una cancelación exige el segundo factor. |
| **SEG-002** | Alta | ADR-005, ADR-006, RN-023, VAL-018 | El webhook es el punto único de confirmación. Riesgos: firma validada sobre el cuerpo ya parseado, replay, confianza en metadatos del cliente, y el "respaldo por consulta directa" confiando en datos de la petición. Redsys y Stripe validan de forma distinta. | (a) Verificar la firma sobre el cuerpo crudo, con comparación en tiempo constante y tolerancia de marca de tiempo. (b) Rechazar cualquier evento sin firma válida (fail-closed). (c) Cruzar referencia, reserva, **importe, moneda y estado** contra la BD, nunca contra metadatos. (d) Máquina de estados que impida retrocesos o duplicados. (e) El respaldo consulta la pasarela solo con la referencia guardada. (f) Secreto de webhook propio por entorno, con rotación. (g) Endpoint sin cookies ni CORS, con límite de tamaño. | Pruebas CA-004: firma inválida, replay, duplicado, desorden, importe o moneda distintos, pago de otra reserva. Prueba de contrato con el sandbox del proveedor. |
| **SEG-003** | Alta | ADR-003, ADR-007, R-ARQ-02, R-ARQ-03 | La concurrencia está bien planteada, pero quedan puntos sin cerrar. (1) El borrado perezoso de holds dentro de la transacción puede competir con un pago en curso. (2) La sesión de pago puede vivir más que el hold de 15 min. (3) Pago tardío con ocupación recreada por el worker. (4) Bloqueo manual del admin frente a reserva. Una resolución defectuosa puede dar **doble reserva o cobro sin servicio**. | (a) La restricción de exclusión es la garantía final, sin filtros por hora. (b) El hold no expira mientras haya un pago en vuelo, o la sesión de pago se expira por API. (c) Transiciones atómicas con bloqueo de fila, y reembolso idempotente al fallar la reserva tardía. (d) Todos los orígenes de ocupación pasan por la misma restricción. | Pruebas de concurrencia contra la BD real: N peticiones simultáneas y carrera hold-expiración-webhook. Prueba directa de la restricción (CA-002, CA-003, CA-007). |
| **SEG-004** | Alta | RF-007, RN-016, VAL-016, RN-018 | **Abuso de negocio.** (1) Un bot crea holds de 15 min sobre toda la flota y bloquea el inventario sin pagar (denegación de disponibilidad). (2) Las sesiones de pago pueden servir para *card testing*, con daño reputacional y de cuenta ante la pasarela. | (a) Límite de holds activos por IP, email y sesión. (b) Anti-bot antes del hold o del pago, que respete la privacidad (valorar CAPTCHA sin cookies de terceros). (c) Verificar el email antes de crear la sesión de pago, o limitar reintentos. (d) 3DS/SCA y reglas antifraude de la pasarela activadas. (e) Alertas por tasa de reservas expiradas y de pagos fallidos. | Prueba de carga y abuso en staging. Revisión de la configuración antifraude. Alertas simuladas. |
| **SEG-005** | Alta | RF-013, RF-025, DEC-024, HU-023, VAL-020 | **Manipulación de importes y reembolsos.** Riesgos: reembolso mayor que lo pagado, doble reembolso por doble clic o cancelación concurrente, cálculo con política errónea (ISS-002), y reembolso a un medio distinto del original. Además VAL-020 admite **precios ≥ 0**: una tarifa 0 o alterada por un admin comprometido genera reservas de importe cero o mínimo. | (a) Reembolso calculado solo en servidor, con tope `pagado − ya reembolsado` y clave de idempotencia. (b) Reembolso solo al medio original. (c) Tarifas > 0 con confirmación de cambios grandes, y flujo definido para importe 0. (d) Reembolsos del admin con reautenticación. (e) Instantánea de la política aplicada guardada en la reserva. | Pruebas de manipulación de importe y fechas. Doble cancelación concurrente. Test de límites del reembolso. Revisión de la regla definitiva de DEC-025. |
| **SEG-006** | Alta | ADR RF-019, HU-017, DEC-014 | **Autenticación del panel insuficiente.** El MFA es solo "se recomienda". El rol es único y potencialmente compartido. No hay política de contraseñas, sesiones ni recuperación de cuenta. El panel comparte origen con la parte pública (un XSS público escala a admin). Tiene acceso a datos personales y reembolsos. Cuenta inicial sin definir. | (a) **MFA obligatorio** (TOTP o WebAuthn) y códigos de recuperación. (b) Contraseñas largas, comprobación contra filtraciones y sin reglas de complejidad arbitrarias. (c) Cuentas nominales, sin compartir ni credenciales por defecto. (d) Sesión con caducidad por inactividad y absoluta, rotación del ID tras login, cierre global. (e) Recuperación con enfriamiento y aviso por correo. (f) Bloqueo con límite que no permita enumerar usuarios. (g) Cookie `__Host-`, CSRF y reautenticación en acciones críticas. (h) Valorar lista de IP permitidas o acceso VPN al panel. | Pruebas de login, fijación y robo de sesión, CSRF, recuperación y enumeración. Revisión del alta de la primera cuenta. |
| **SEG-007** | Alta | DEC-016, RF-029, RNF-009 | **Auditoría del panel aplazada a Fase 2** mientras el admin ya cambia tarifas, bloquea fechas, cancela y reembolsa en el MVP. Sin registro, no hay forma de investigar un abuso interno o una cuenta comprometida. `reservation_status_history` no cubre catálogo ni tarifas. | Registro de auditoría **mínimo en el MVP** (quién, cuándo, qué, valores antes y después) para login, tarifas, bloqueos, cancelaciones, reembolsos y exportaciones. Solo lectura y sin datos personales innecesarios. | Revisión de que cada acción sensible deja huella. Prueba de que el admin no puede borrarla. |
| **SEG-008** | Media | Arquitectura, ADR-010 | **CSRF, XSS, inyección, cabeceras y caché.** Datos del cliente (nombre, mensajes de contacto) se muestran en el panel y en correos: XSS almacenado e inyección HTML o de cabeceras de correo. La caché CDN/ISR puede **exponer páginas personalizadas** (consulta, retorno del pago). CORS, CSP y HSTS no están definidos. | (a) Codificación de salida contextual y plantillas con autoescape (web, panel y correo). (b) Consultas parametrizadas y validación por esquema en el servidor. (c) CSRF en todas las mutaciones, pública y admin. (d) CSP estricta sin `unsafe-inline`, HSTS, `nosniff`, `frame-ancestors` y `Referrer-Policy`. (e) CORS cerrado, sin API para terceros. (f) Sin caché pública en rutas con sesión o código. (g) Neutralizar CSV/fórmulas en exportaciones. | Escáner dinámico (por ejemplo OWASP ZAP) y pruebas manuales. Comprobar cabeceras. Pruebas de caché con CDN. Payloads XSS en contacto y nombre. |
| **SEG-009** | Media | RF-020, VAL-022, RNF-013 | **Subida de imágenes.** La amenaza principal es un admin comprometido o un archivo malicioso (polyglot, SVG, bomba de descompresión, metadatos con GPS). La validación por "tipo y tamaño" es insuficiente. | (a) Lista cerrada de formatos (sin SVG), validación por *magic bytes* y **reprocesado** que elimine EXIF. (b) Límites de bytes y de píxeles. (c) Nombres aleatorios generados por el servidor. (d) Escritura solo desde la app, lectura pública solo de derivados. (e) Servir con `nosniff` y de origen aparte, sin ejecución. | Pruebas con archivos manipulados (extensión falsa, polyglot, imagen enorme). Revisar permisos del almacén y cabeceras servidas. |
| **SEG-010** | Alta (validar legal) | RN-026, RNF-008, PEND-010 | **RGPD sin cerrar.** Falta definir: plazos de retención, supresión y derechos de los interesados, procedimiento de brechas, contratos de encargado con hosting, pasarela, correo, CDN y observabilidad, y transferencias fuera de la UE. `payment_event` guarda la carga bruta y `email_outbox` guarda contenido con datos personales. Se pide fecha de nacimiento para la edad mínima (VAL-011). Las copias conservan datos que debieron suprimirse. | (a) Inventario de datos y finalidades, y mínimos por campo (valorar guardar solo "mayor de edad"). (b) Retención definida y trabajos de anonimizado. (c) Consentimiento con versión, fecha y finalidad, también el de cookies. (d) Cifrado en tránsito y en reposo, con acceso mínimo. (e) Contratos y región UE confirmados. (f) Purga de cargas brutas y del outbox. (g) Política de supresión con las copias. | Revisión por asesoría legal (no la sustituye este reporte). Test de supresión y anonimizado. Revisar qué datos guarda cada tabla. |
| **SEG-011** | Media | Observabilidad, RGPD | **Logs y seguimiento de errores.** "Sin datos personales" es solo una intención. El código de reserva en URLs, las cargas de webhook y el correo del cliente pueden acabar en logs, en el CDN o en un servicio de errores de terceros. | Redacción obligatoria en el registro. Lista de campos prohibidos (código de reserva, email, teléfono, secretos). Retención y acceso limitados a los logs. Contrato con el proveedor de errores. | Inyectar datos de prueba y buscar en logs y errores. Revisar la configuración del CDN y de los registros de acceso. |
| **SEG-012** | Media | Secretos, configuración, despliegue | **Secretos y entornos.** No se define dónde viven, quién accede ni cómo se rotan. Riesgos: staging con datos reales, cuentas de BD con exceso de privilegios, TLS de BD no exigido, modo depuración, origen accesible saltándose el CDN. | (a) Gestor de secretos, claves por entorno y rotación. (b) **Prohibido** usar datos reales fuera de producción. (c) Roles de BD de mínimo privilegio, distintos para la app, el worker y las migraciones. (d) TLS en todas las conexiones. (e) Origen que solo acepta tráfico del CDN. (f) Sin depuración en producción. (g) Detección de secretos en el repositorio. | Escaneo de secretos en repo y CI. Revisión de la configuración de despliegue. Prueba de acceso directo al origen. |
| **SEG-013** | Media | RNF-011 | **Copias y restauración.** RPO/RTO sin definir. No consta el cifrado, el control de acceso ni la inmutabilidad de las copias, ni la cobertura de imágenes y secretos. Riesgo de ransomware y de pérdida de reservas pagadas. | Copias cifradas, aisladas y con acceso separado. Cubrir BD y almacén de imágenes. Restauración probada y documentada con RPO/RTO acordados. Alinear retención de copias con SEG-010. | Prueba de restauración completa en entorno aislado. Revisión de permisos y de la retención. |
| **SEG-014** | Media | Despliegue, CI | **Cadena de suministro.** Solo se menciona "auditoría de dependencias". Falta *lockfile*, versiones fijadas, revisión de SDKs de terceros, control de scripts externos (CSP/SRI), protección de ramas y secretos de CI. | Lockfile y versiones fijadas. SCA y SBOM en CI. Acciones de CI fijadas por hash. Ramas protegidas y revisión obligatoria. Mínimo de scripts de terceros, con SRI. Actualizaciones periódicas con SLA. | Salida del SCA sin vulnerabilidades altas abiertas. Revisión de permisos del CI. |
| **SEG-015** | Media | ADR-009, VAL-009, RN-018 | **Correo.** Se envían correos a direcciones no verificadas, por lo que se puede acosar a terceros o hacer *email bombing*. Sin límites por destinatario. Riesgo de inyección de cabeceras en contacto. Los correos llevan el código de reserva. Falta política DMARC. | Límite por destinatario y por tiempo. Verificación de email antes de enviar enlaces de pago. Sanear cabeceras. SPF, DKIM y DMARC (idealmente en rechazo). Plantillas sin datos innecesarios y correos de aviso al admin sin datos personales completos. | Pruebas de volumen y de inyección. Verificar la alineación DMARC y las cabeceras en staging. |
| **SEG-016** | Media | RF-017, RF-015 | **Cookies y antispam.** Una solución antispam o la propia pasarela pueden poner cookies de terceros. Sin definir el registro del consentimiento ni la carga previa. | Inventario de cookies y scripts. Nada no técnico antes del consentimiento. Rechazar tan fácil como aceptar. Guardar prueba del consentimiento. Antispam compatible con privacidad (validar legal). | Auditoría de cookies en navegador limpio. Prueba de que nada se carga sin consentimiento. |
| **SEG-017** | Baja | RF-019, ADR-004 | **Autorización en servidor.** Con rol único, el riesgo es que el control quede solo en el frontend o que el rol enumerado de Fase 2 se implante después sin pruebas. | Denegar por defecto en todos los endpoints `/admin`. Comprobar la sesión y el rol en servidor en cada operación. Pruebas negativas por endpoint. | Prueba automática de que todo endpoint admin rechaza anónimos y sesiones caducadas. |

## Controles obligatorios para BUILD

Antes de iniciar BUILD (y aún más antes de producción):

1. **Acceso del cliente (SEG-001):** código de CSPRNG, errores uniformes, límites, `no-store`, y el segundo factor decidido para cancelar.
2. **Webhook (SEG-002):** firma sobre cuerpo crudo, tolerancia de tiempo, verificación de importe y moneda, idempotencia y máquina de estados.
3. **Concurrencia (SEG-003):** restricción de exclusión como garantía final y pruebas de concurrencia automatizadas.
4. **Antiabuso (SEG-004):** límites de holds y de sesiones de pago, anti-bot y antifraude de la pasarela activados.
5. **Importes y reembolsos (SEG-005):** cálculo solo en servidor, tope e idempotencia, y reembolso al medio original.
6. **Panel (SEG-006):** MFA obligatorio, política de sesión, recuperación, CSRF y reautenticación.
7. **Auditoría mínima (SEG-007)** en el MVP, no en Fase 2.
8. **Web segura (SEG-008):** CSP, HSTS, CSRF, codificación de salida y consultas parametrizadas.
9. **Imágenes (SEG-009):** formatos cerrados, reprocesado, límites y servido seguro.
10. **Datos (SEG-010):** inventario, retención y consentimientos definidos antes de guardar datos reales.
11. **Logs y secretos (SEG-011, SEG-012):** redacción, gestor de secretos, sin datos reales fuera de producción, roles de BD de mínimo privilegio y TLS.
12. **Copias y dependencias (SEG-013, SEG-014):** copias cifradas con restauración probada, SCA y lockfile en CI.
13. **Pruebas de seguridad en CI:** SAST, SCA y detección de secretos como puertas de calidad.

## Riesgos aceptados o pendientes

**Ningún riesgo ha sido aceptado.** Aceptar uno requiere autoridad del cliente a través del Director. Quedan pendientes:

- **Decisiones del cliente que condicionan la seguridad:** pasarela (PEND-012), titularidad (PEND-011), código + email o enlace mágico, MFA del admin, hosting y región, retención de datos y RPO/RTO (PEND-015).
- **Validación legal** (PEND-010): RGPD/LOPDGDD, LSSI-CE, PSD2/SCA, consumidores y desistimiento. Este reporte no sustituye esa validación.
- **Política de cancelación** (DEC-025, PEND-008) con impacto en SEG-005.
- Revisión de seguridad **de implementación** (código, configuración, pruebas dinámicas) pendiente para la fase QUALITY.

## Pruebas de seguridad ejecutadas

**Ninguna.** No hay código, entorno ni analizadores aplicables. Las verificaciones propuestas en la tabla son **no ejecutadas**. Todo lo anterior se basa en lectura estática de borradores.

## Limitaciones de la revisión

- Solo diseño. Los controles están descritos, no implementados ni probados.
- Los documentos son borradores sin aprobación de alcance y pueden cambiar. No leí por completo `requirements.md` ni `mvp-and-backlog.md`. Pueden existir requisitos no revisados.
- No se eligió pasarela, hosting ni proveedor de correo. Los riesgos específicos de cada uno quedan sin evaluar.
- Los puntos legales son señalamientos para validar con asesoría. No son asesoramiento jurídico.
- La ausencia de hallazgos en un área no implica que sea segura. Falta modelar la amenaza interna del cliente y el impacto de la disponibilidad y de los contracargos (disputas, fuera del MVP).

## Veredicto

**APROBADO CON CONDICIONES** para **continuar el diseño y pasar a PLANNING**. **No** se aprueba iniciar BUILD ni producción mientras no se cumplan los controles obligatorios de la sección anterior y se resuelvan SEG-001 a SEG-007 y SEG-010 (en este último, la parte legal con asesoría). Este veredicto no garantiza la seguridad del sistema. Es una valoración del borrador de diseño con la información disponible.

**Escalado al Director:**
1. Decidir el segundo factor para cancelar y el MFA obligatorio (SEG-001, SEG-006).
2. Mover la auditoría mínima al MVP (SEG-007).
3. Corregir VAL-020 para que el precio sea > 0 o defina el flujo de importe 0 (SEG-005).
4. Ninguna aceptación de riesgo ha sido solicitada ni concedida.

---

## Registro documental (Gestor de Documentación)

- **Estado:** BORRADOR. **Fecha de persistencia:** 2026-10-26.
- **Fuente:** reporte del Revisor de Seguridad entregado por el Director (agente "Seguridad del diseño campers"). Se omitieron solo la línea de metadatos del sistema del agente y el prefijo "[Turn 0]".
- **Hallazgos:** SEG-001 a SEG-017 (7 Altas: SEG-001 a SEG-007; SEG-010 Alta "validar legal"; 8 Medias: SEG-008, 009, 011 a 016; 1 Baja: SEG-017). Registrados en [RISKS](../00-control/RISKS.md) §4 en estado ABIERTO.
- **Decisiones pendientes que se derivan:** PEND-037 a PEND-040 y la relación con PEND-035 en [DECISIONS](../00-control/DECISIONS.md).
- **Trazabilidad:** SEG → ADR/RF/RN en [TRACEABILITY](../00-control/TRACEABILITY.md) §8.
- **Actividad y tarea:** [ACT-007](../00-control/AGENT-ACTIVITY.md), [TASK-015](../00-control/TASKS.md).
- **Inconsistencias nuevas detectadas al persistir:** ver ISS-024 a ISS-033 en [RISKS](../00-control/RISKS.md).

## Enlaces relativos

[Estado del proyecto](../00-control/PROJECT-STATE.md) · [Decisiones](../00-control/DECISIONS.md) · [Riesgos e impedimentos](../00-control/RISKS.md) · [Trazabilidad](../00-control/TRACEABILITY.md) · [Tareas](../00-control/TASKS.md) · [Aprobaciones](../00-control/APPROVALS.md) · [requirements.md](../01-discovery/requirements.md) · [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) · [Especificación UX/UI](../03-ux/ux-specification.md) · [Arquitectura de solución](../04-architecture/solution-architecture.md) · [Plan de implementación](../05-planning/implementation-plan.md)
