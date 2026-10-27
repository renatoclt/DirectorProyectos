---
name: color-system
description: Define, compare and validate reusable color systems for digital products before visual implementation. Use when a web or app project needs a brand-aligned palette, three differentiated color directions, semantic design tokens, accessible contrast, UI state colors, or a documented color recommendation that must feed frontend-design, mockups, implementation, QA, or delivery review. Do not use to redefine product scope, business rules, brand facts, or agent permissions.
---

# Color System

Definir la dirección cromática como una decisión de producto y marca, no como decoración. Producir alternativas comparables, recomendar una y convertirla en tokens semánticos que puedan cambiar sin alterar UX ni lógica.

## Límites

- Respetar brief, requisitos, marca confirmada y contrato del agente.
- No inventar colores corporativos como si fueran aprobados.
- No redefinir funcionalidades, reglas de negocio ni arquitectura.
- No conceder herramientas, rutas ni permisos.
- Marcar toda dirección no aprobada como `PROPUESTA`.
- No usar popularidad o tendencia como única justificación.

## Flujo obligatorio

### 1. Comprender el contexto

Identificar:

- industria y modelo de negocio;
- audiencia principal;
- posicionamiento;
- personalidad deseada;
- contexto y frecuencia de uso;
- nivel de confianza requerido;
- acción principal que debe destacar;
- marca, colores o restricciones existentes;
- accesibilidad y modos de visualización aplicables.

Si falta información, continuar con supuestos visibles en vez de inventar decisiones aprobadas.

### 2. Generar tres direcciones realmente diferentes

Crear exactamente tres propuestas iniciales: A, B y C. No deben ser variaciones mínimas del mismo hue.

Para cada una indicar:

- nombre y concepto;
- personalidad;
- colores base con HEX;
- primary, secondary, accent, background, surface, text y muted;
- público o posicionamiento que favorece;
- fortalezas;
- debilidades y riesgos;
- percepción de marca;
- comportamiento esperado de CTA;
- observaciones de contraste.

Consultar [palette-generation.md](references/palette-generation.md) y [anti-generic-colors.md](references/anti-generic-colors.md).

### 3. Comparar

Crear una tabla comparativa con criterios relevantes al proyecto, por ejemplo:

- confianza;
- claridad;
- diferenciación;
- energía o calma;
- sensación premium;
- adecuación a la industria;
- visibilidad de CTA;
- accesibilidad;
- escalabilidad del sistema.

No declarar una ganadora sin explicar el criterio.

### 4. Recomendar una dirección

Elegir una como `RECOMENDADA` y explicar:

- qué objetivo de negocio ayuda a comunicar;
- por qué encaja con la audiencia;
- por qué es más adecuada que las otras dos;
- qué riesgos conserva;
- qué elementos siguen pendientes de aprobación.

El flujo puede continuar con la recomendada sin esperar selección humana, siempre que permanezca marcada como propuesta.

### 5. Convertir la dirección en tokens semánticos

No definir el sistema final con nombres físicos como `--green` o `--orange`. Utilizar tokens semánticos. Consultar [semantic-tokens.md](references/semantic-tokens.md).

Mínimo:

- `--color-primary`
- `--color-primary-hover`
- `--color-primary-active`
- `--color-secondary`
- `--color-secondary-hover`
- `--color-accent`
- `--color-background`
- `--color-background-alt`
- `--color-surface`
- `--color-surface-elevated`
- `--color-text`
- `--color-text-secondary`
- `--color-text-muted`
- `--color-border`
- `--color-border-strong`
- `--color-success`
- `--color-warning`
- `--color-error`
- `--color-info`

Cuando el sistema lo necesite, definir escalas `50` a `950` para familias relevantes. No generar tonos mecánicamente si degradan la percepción o el contraste.

### 6. Validar contraste y estados

Consultar [contrast-rules.md](references/contrast-rules.md).

Comprobar, cuando apliquen:

- texto sobre fondo;
- texto sobre primary y accent;
- CTA normal, hover, active y disabled;
- foco visible;
- bordes y controles;
- success, warning, error e info;
- información que no dependa exclusivamente del color.

Usar `scripts/check_contrast.py` cuando se requiera una comprobación determinista entre dos colores HEX.

### 7. Preparar la salida

Utilizar [palette-presentation.md](references/palette-presentation.md) como formato de referencia.

Entregar:

1. contexto de marca;
2. Paleta A;
3. Paleta B;
4. Paleta C;
5. tabla comparativa;
6. paleta recomendada y justificación;
7. tokens semánticos;
8. escalas relevantes;
9. contraste y accesibilidad;
10. usos correctos e incorrectos;
11. alternativas y cómo cambiar entre ellas sin alterar UX.

## Integración con otras Skills

Orden recomendado:

`color-system` → `frontend-design` → mockup/implementación → `frontend-design-review`

`frontend-design` debe usar la paleta recomendada o aprobada, no volver a inventar una distinta sin justificar el cambio.

`frontend-design-review` debe comprobar consistencia, contraste y uso de tokens; en QA o auditoría no debe rediseñar.
