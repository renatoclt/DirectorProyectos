# Empresa de agentes para VS Code y GitHub Copilot

Versión **3.0.0**. Este repositorio convierte una descripción breve en un flujo empresarial controlado: descubrimiento, diseño, planificación, construcción, pruebas, seguridad, trazabilidad y entrega.

## Qué se añadió en esta versión

- **21 agentes**: los 19 anteriores, un Auditor de Trazabilidad y un Ingeniero de Testing de Agentes.
- **Contrato de alcance por agente** fuera del prompt.
- **Restricciones técnicas verificables** mediante herramientas y visibilidad.
- **Testing automático y conductual** con baseline de regresión.
- **Carpeta `aprendizaje/`** que explica por qué existe cada pieza.
- **Control y trazabilidad por proyecto** mediante `projects/<slug>/00-control/`.

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

## Primer uso

```text
Quiero crear un nuevo proyecto.

Descripción breve:
[Escribe la idea]

Primero responde como una empresa: explica qué entendieron, da un ejemplo, propone un MVP, separa supuestos y realiza solo las preguntas necesarias. No programes todavía.
```

## Comandos disponibles

```text
/iniciar-control-proyecto
/estado-proyecto
/registrar-cambio
/cerrar-fase
/auditar-trazabilidad
/validar-contratos-agentes
/probar-sistema-agentes
```

Los prompt files funcionan en sesiones **Local**.

## Estructura principal

```text
.github/
├── agents/             # 21 perfiles
├── instructions/       # gobierno, mantenimiento y testing
├── prompts/            # procedimientos invocables con /
├── workflows/          # validación en GitHub Actions
└── copilot-instructions.md

governance/
├── contracts/          # un contrato JSON por agente
├── tool-policies.json
└── phase-gates.json

testing/
├── run_tests.py
├── baselines/
├── scenarios/
├── manual/
└── reports/

aprendizaje/            # explicación paso a paso
projects/               # proyectos administrados
templates/              # plantillas de control y reportes
```

Consulta [MAPA-DEL-SISTEMA.md](MAPA-DEL-SISTEMA.md) para el mapa completo y [aprendizaje/README.md](aprendizaje/README.md) para entender las decisiones.

## Tres capas por agente

### 1. Contrato de alcance

`governance/contracts/<agente>.contract.json` establece acciones, rutas, entradas, salidas, prohibiciones y escenarios.

### 2. Restricciones técnicas

Cada `.agent.md` declara `tools`, `user-invocable`, `disable-model-invocation` y `target`. Solo el Director aparece en el selector.

### 3. Pruebas de regresión

`testing/run_tests.py` valida estructura y baseline. Los escenarios de `testing/scenarios/` prueban la conducta mediante rúbricas.

## QA versus testing de agentes

| Rol | Qué prueba | Puede editar |
|---|---|---|
| QA Engineer | El producto construido para el cliente | No |
| Ingeniero de Testing de Agentes | Perfiles, contratos y conducta del equipo | No |
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

`PROJECT-STATE.md` es el panel ejecutivo. Los demás archivos contienen evidencia detallada.

## Flujo y aprobaciones

```text
INTAKE -> DISCOVERY -> DESIGN -> PLANNING
                                 |
                           aprobación humana
                                 v
BUILD -> QUALITY -> OPERATIONS/DOCUMENTATION -> DELIVERY -> CLOSED
```

No existe desarrollo sin aprobación explícita, ni despliegue sin autorización específica, ni entrega sin evidencia.

## Probar el sistema de agentes

### Pruebas automáticas

```powershell
python testing/run_tests.py
```

### Prueba rápida de conducta

Ejecuta el prompt directamente desde el chat en una sesión Local:

```text
/probar-sistema-agentes mode=smoke
```

No lo delegues desde el Director para la suite conductual: el prompt activa al Ingeniero de Testing de Agentes como agente principal y evita depender de subagentes anidados.

### Suite completa

```text
/probar-sistema-agentes mode=full
```

### Después de cambiar un agente

1. Actualiza perfil y contrato.
2. Actualiza escenarios.
3. Ejecuta pruebas.
4. Revisa la diferencia.
5. Solo con aprobación humana, actualiza el baseline:

```powershell
python testing/run_tests.py --update-baseline --confirm-update-baseline
python testing/run_tests.py
```

## Agentes incluidos

Consulta [AGENT-CATALOG.md](AGENT-CATALOG.md). La regla general es usar el equipo mínimo. Un proyecto pequeño usa generalista; una web mediana puede usar Backend + Frontend; Móvil, Datos y DevOps solo se activan cuando el alcance lo requiere.

## Diagnóstico

Cuando un agente no aparezca:

- confirma `.github/agents/*.agent.md`;
- revisa YAML y nombres exactos;
- selecciona Local;
- abre `Chat: Open Customizations`;
- verifica herramientas;
- crea una conversación nueva;
- ejecuta `python testing/run_tests.py`.

## Documentación de aprendizaje

La carpeta [aprendizaje](aprendizaje/README.md) explica agentes, prompts, instructions, contratos, permisos, testing, trazabilidad y la forma segura de modificar el equipo.
