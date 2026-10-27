# Empresa de agentes para VS Code y GitHub Copilot

Versión **6.0.0**. Este repositorio convierte una descripción breve en un flujo empresarial controlado: descubrimiento, diseño, planificación, construcción, pruebas, seguridad, trazabilidad y entrega.

La versión 6 añade `color-system`: tres direcciones cromáticas comparables, recomendación, tokens semánticos, contraste y el anexo A07 antes de generar mockups, conservando propuestas ejecutivas, Skills y controles anteriores.

## Qué incluye

- **22 agentes** con contratos y herramientas restringidas.
- **3 Skills reutilizables** para color, creación y revisión de interfaces.
- **Contrato de alcance por agente** fuera del prompt.
- **Restricciones técnicas verificables** mediante herramientas, visibilidad y rutas.
- **Testing automático y conductual** con baseline de agentes y Skills.
- **Carpeta `aprendizaje/`** que explica por qué existe cada pieza.
- **Control y trazabilidad por proyecto** mediante `projects/<slug>/00-control/`.
- **Avisos y licencias de terceros** para las Skills adaptadas.

## Inicio rápido

1. Copia todo en la raíz del repositorio.
2. Abre VS Code y selecciona **Session Target: Local**.
3. Ejecuta `Chat: Open Customizations` y revisa diagnósticos.
4. Selecciona **Director de Proyectos**.
5. Instala y ejecuta las pruebas:

```powershell
python -m pip install -r testing/requirements.txt
python testing/run_tests.py
```

Resultado esperado:

```text
RESULTADO: APROBADO
```

## Primer uso recomendado

Completa primero `company/COMPANY-PROFILE.md` con información comercial verificable.

Después ejecuta:

```text
/propuesta-con-mockup
```

El sistema solicitará la descripción, un slug y una fecha de inicio o supuesto. Entregará:

- propuesta ejecutiva para lectura de 2 a 3 minutos;
- anexos con el detalle completo;
- plan de trabajo y recursos;
- plazo preliminar y disponibilidad;
- tres direcciones cromáticas y recomendación cuando exista interfaz;
- mockup conceptual navegable usando la dirección recomendada;
- preguntas y próximo paso.

No se implementa producto real durante esta etapa.

## Comandos disponibles

```text
/iniciar-control-proyecto
/estado-proyecto
/registrar-cambio
/cerrar-fase
/auditar-trazabilidad
/validar-contratos-agentes
/probar-sistema-agentes
/disenar-frontend
/revisar-frontend
/propuesta-con-mockup
```

Los prompt files funcionan en sesiones **Local**.

## Estructura principal

```text
.github/
├── agents/             # 22 perfiles
├── skills/             # Skills reutilizables versionadas
├── instructions/       # gobierno, mantenimiento, testing y diseño
├── prompts/            # procedimientos invocables con /
├── workflows/          # validación en GitHub Actions
└── copilot-instructions.md

governance/
├── contracts/          # un contrato JSON por agente
├── skills-lock.json    # origen, licencia y agentes autorizados
├── tool-policies.json
└── phase-gates.json

testing/
├── run_tests.py
├── baselines/          # agentes y Skills
├── scenarios/
├── manual/
└── reports/

aprendizaje/            # explicación paso a paso
company/                # identidad, capacidades y disponibilidad confirmadas
projects/               # proyectos administrados
templates/              # control, reportes y propuestas
```

Consulta [MAPA-DEL-SISTEMA.md](MAPA-DEL-SISTEMA.md), [AGENT-CATALOG.md](AGENT-CATALOG.md), [SKILL-CATALOG.md](SKILL-CATALOG.md) y [aprendizaje/README.md](aprendizaje/README.md). Para actualizar desde v5, consulta [MIGRATION-V5-TO-V6.md](MIGRATION-V5-TO-V6.md). Para la migración anterior, consulta [MIGRATION-V4-TO-V5.md](MIGRATION-V4-TO-V5.md). La migración histórica v3 a v4 se conserva en [MIGRATION-V3-TO-V4.md](MIGRATION-V3-TO-V4.md).

## Capas de control

### Por agente

1. **Contrato de alcance:** `governance/contracts/<agente>.contract.json`.
2. **Restricciones técnicas:** `tools`, visibilidad y rutas.
3. **Pruebas de regresión:** perfil, contrato y escenarios.

### Por Skill

1. **Instrucción reusable:** `.github/skills/<skill>/SKILL.md`.
2. **Origen y licencia:** `UPSTREAM.md`, `LICENSE.txt` y `THIRD-PARTY-NOTICES.md`.
3. **Lock:** `governance/skills-lock.json`.
4. **Baseline:** `testing/baselines/skill-manifest.json`.
5. **Escenarios conductuales:** UX, Frontend, QA, Auditor y Testing de Agentes.


## Propuesta ejecutiva, adjuntos y mockup

La salida comercial se divide en dos niveles.

### 1. Propuesta ejecutiva

`projects/<slug>/00-propuesta/PROPUESTA-EJECUTIVA.md`

Debe poder leerse en 2 a 3 minutos e incluir:

- resumen para decisión;
- presentación verificable;
- entendimiento del proyecto;
- solución y MVP;
- plan de trabajo;
- plazo preliminar;
- disponibilidad y comunicación;
- mockup;
- próximo paso.

La propuesta indica claramente que el detalle completo se encuentra en los adjuntos.

### 2. Adjuntos detallados

`projects/<slug>/00-propuesta/adjuntos/`

Contienen:

- entendimiento y objetivos;
- alcance y entregables;
- plan, recursos y responsabilidades;
- plazo, disponibilidad y comunicación;
- supuestos, riesgos y preguntas;
- decisiones y limitaciones del mockup.

### 3. Mockup conceptual

`projects/<slug>/03-ux/mockup-conceptual/`

Lo crea **Prototipador UX** con `frontend-design`. Usa datos ficticios, abre localmente y no contiene servicios reales.

### Reglas comerciales

- Las afirmaciones sobre la empresa provienen de `company/COMPANY-PROFILE.md`.
- No se inventan años, clientes, certificaciones, casos de éxito ni disponibilidad.
- El plazo se expresa como rango, fecha o ventana tentativa, nivel de confianza y condiciones.
- Una fecha tentativa no es un compromiso contractual.
- La propuesta y el mockup nacen como BORRADOR.

## Skills de diseño integradas

### `frontend-design`

Adaptación local de una Skill pública de Anthropic. Se usa para crear o rediseñar interfaces web con una dirección visual específica del producto, evitando respuestas visuales genéricas.

Agentes autorizados:

- Diseñador UX UI.
- Desarrollador Frontend.

### `frontend-design-review`

Adaptación local de una Skill pública de Microsoft. Se usa para revisar sistema de diseño, jerarquía, responsive, accesibilidad, estados y confianza.

Agentes autorizados:

- Diseñador UX UI.
- Desarrollador Frontend.
- QA Engineer.
- Auditor de Entrega.

Una Skill **no concede permisos adicionales**. Por ejemplo, QA continúa sin poder editar aunque use una Skill relacionada con código o diseño.

## Flujo de diseño

```text
Alcance aprobado
      ↓
Diseñador UX UI + frontend-design
      ↓
Dirección visual + handoff
      ↓
Desarrollador Frontend + frontend-design
      ↓
Autorrevisión con frontend-design-review
      ↓
QA + frontend-design-review, sin editar
      ↓
Correcciones
      ↓
Auditor de Entrega + evidencia
```

### Diseñar sin código

```text
/disenar-frontend
```

### Revisar sin editar

```text
/revisar-frontend
/propuesta-con-mockup
```

### Ver Skills disponibles

Con Local seleccionado:

```text
/skills
```

## QA versus testing del sistema

| Rol | Qué prueba | Puede editar |
|---|---|---|
| QA Engineer | El producto construido para el cliente, incluida UI cuando aplique | No |
| Ingeniero de Testing de Agentes | Perfiles, contratos, Skills y conducta del equipo | No |
| Auditor de Trazabilidad | Coherencia del mapa y evidencias | No |
| Auditor de Entrega | Preparación final del producto | No |

## Control de un proyecto

Ejecuta:

```text
/iniciar-control-proyecto
```

Se crea:

```text
projects/<slug>/00-control/
├── PROJECT-STATE.md
├── REQUIREMENTS.md
├── DECISIONS.md
├── TASKS.md
├── AGENT-ACTIVITY.md
├── RISKS.md
├── TRACEABILITY.md
├── APPROVALS.md
└── CHANGE-REQUESTS.md
```

`PROJECT-STATE.md` es el panel ejecutivo. Los demás archivos contienen evidencia detallada. El registro de actividad incluye las Skills aplicadas.

## Flujo y aprobaciones

```text
INTAKE -> DISCOVERY -> DESIGN -> PLANNING
                                 |
                           aprobación humana
                                 v
BUILD -> QUALITY -> OPERATIONS/DOCUMENTATION -> DELIVERY -> CLOSED
```

No existe desarrollo sin aprobación explícita, ni despliegue sin autorización específica, ni entrega sin evidencia.

## Probar el sistema

### Pruebas automáticas

```powershell
python testing/run_tests.py
```

Comprueban agentes, contratos, herramientas, prompts, instrucciones, Skills, referencias, licencias, lock, enlaces y baselines.

### Prueba rápida de conducta

```text
/probar-sistema-agentes mode=smoke
```

El prompt activa al Ingeniero de Testing de Agentes como agente principal y evita depender de subagentes anidados.

### Suite completa

```text
/probar-sistema-agentes mode=full
```

### Después de cambiar un agente o una Skill

1. Actualiza la fuente de verdad correspondiente.
2. Actualiza contratos, lock, referencias o escenarios cuando aplique.
3. Ejecuta pruebas.
4. Revisa la diferencia.
5. Solo con aprobación humana, actualiza los dos baselines:

```powershell
python testing/run_tests.py --update-baseline --confirm-update-baseline
python testing/run_tests.py
```

No actualices el baseline para convertir un error accidental en comportamiento aceptado.

## Actualizar una Skill externa

1. Revisa el cambio upstream y su licencia.
2. Compara con la adaptación local.
3. Conserva los límites corporativos.
4. Actualiza `UPSTREAM.md` y `governance/skills-lock.json`.
5. Actualiza escenarios si cambia la conducta.
6. Ejecuta pruebas y revisa `SKILLBASE-002`.
7. Aprueba humanamente la nueva baseline.

No existe actualización automática desde Internet.

## Diagnóstico

Cuando un agente o Skill no aparezca:

- confirma `.github/agents/*.agent.md` o `.github/skills/<nombre>/SKILL.md`;
- revisa YAML y que el `name` coincida con la carpeta;
- selecciona Local;
- abre `Chat: Open Customizations`;
- ejecuta `/skills` para revisar descubrimiento;
- crea una conversación nueva;
- ejecuta `python testing/run_tests.py`.

## Aprendizaje

La carpeta [aprendizaje](aprendizaje/README.md) explica agentes, prompts, instructions, contratos, permisos, testing, trazabilidad, Skills reutilizables y la forma segura de modificar el sistema.
