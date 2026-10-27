# 12. Skills reutilizables y por qué se integraron así

## Qué problema resuelven

Los agentes definen **quién** trabaja y qué permisos tiene. Las Skills definen **cómo** ejecutar una capacidad repetible. Separarlas evita inflar los prompts de los agentes y permite actualizar una práctica común sin duplicarla.

```text
Agente: Diseñador UX UI
Contrato: solo lectura
Skill: frontend-design
Resultado: especificación visual, no código
```

La Skill no cambia el contrato. Si un agente no tiene `edit`, cargar una Skill de diseño no le concede edición.

## Por qué se reutilizaron bases externas

Diseñar desde cero otra guía universal habría duplicado conocimiento ya trabajado públicamente. Se eligieron dos fuentes:

- `frontend-design` de Anthropic para dirección visual contextual y control contra resultados genéricos.
- `frontend-design-review` de Microsoft para revisión estructurada de interfaz, responsive, accesibilidad y sistema de diseño.

No se copiaron como cajas negras. Se adaptaron al español y a las reglas corporativas, se conservaron licencias y se registró la revisión de origen.

## Por qué existen dos Skills

### `frontend-design`

Sirve para crear o rediseñar. La usan principalmente UX/UI y Frontend.

### `frontend-design-review`

Sirve para evaluar. QA y Auditor la usan sin editar; Frontend puede usarla como autocontrol, pero eso no reemplaza la revisión independiente.

## Archivos de una Skill

```text
.github/skills/<nombre>/
├── SKILL.md
├── LICENSE.txt
├── UPSTREAM.md
├── agents/openai.yaml
└── references/
```

- `SKILL.md`: activadores y flujo.
- `LICENSE.txt`: permisos y obligaciones legales.
- `UPSTREAM.md`: origen, revisión y modificaciones.
- `agents/openai.yaml`: nombre visible.
- `references/`: plantillas y checklists cargados cuando hacen falta.

## Por qué existe `skills-lock.json`

`governance/skills-lock.json` documenta:

- nombre local;
- repositorio y ruta de origen;
- revisión usada;
- licencia;
- modo de integración;
- agentes autorizados.

Así no dependemos de recordar de dónde apareció una carpeta meses después.

## Baseline de Skills

`testing/baselines/skill-manifest.json` guarda hashes de:

- `SKILL.md`;
- referencias;
- licencia;
- metadata;
- `UPSTREAM.md`;
- lock.

Si alguno cambia, aparece `SKILLBASE-002`. Esto no significa automáticamente que el cambio sea malo; significa que debe revisarse antes de aceptarlo.

## Flujo de creación y revisión

```text
Brief aprobado
      ↓
Diseñador UX UI + frontend-design
      ↓
Handoff y criterios visuales
      ↓
Desarrollador Frontend + frontend-design
      ↓
Autorrevisión con frontend-design-review
      ↓
QA + frontend-design-review
      ↓
Corrección
      ↓
Auditor de Entrega + evidencia
```

## Regla contra dependencia ciega

Una Skill pública puede cambiar, contener supuestos incompatibles o recomendar prácticas que no corresponden al proyecto. Por eso:

1. se versiona localmente;
2. se revisa su licencia;
3. se adapta a los contratos;
4. se prueba;
5. no se actualiza automáticamente desde Internet.

## Ejercicio

1. Abre `.github/skills/frontend-design/SKILL.md`.
2. Localiza los límites obligatorios.
3. Abre `governance/skills-lock.json`.
4. Identifica los agentes autorizados.
5. Cambia una palabra en una copia temporal de una referencia.
6. Ejecuta las pruebas y observa `SKILLBASE-002`.
7. Revierte el cambio; no actualices el baseline para ocultarlo.
