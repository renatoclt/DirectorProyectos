# Tokens semánticos

## Principio

Nombrar por función, no por pigmento. Así una dirección cromática puede sustituirse sin reescribir la estructura de la interfaz.

## Tokens mínimos

```css
:root {
  --color-primary: #000000;
  --color-primary-hover: #000000;
  --color-primary-active: #000000;
  --color-secondary: #000000;
  --color-secondary-hover: #000000;
  --color-accent: #000000;
  --color-background: #ffffff;
  --color-background-alt: #ffffff;
  --color-surface: #ffffff;
  --color-surface-elevated: #ffffff;
  --color-text: #000000;
  --color-text-secondary: #000000;
  --color-text-muted: #000000;
  --color-border: #000000;
  --color-border-strong: #000000;
  --color-success: #000000;
  --color-warning: #000000;
  --color-error: #000000;
  --color-info: #000000;
}
```

Los valores son marcadores: sustituirlos por la paleta elegida.

## Escalas

Usar familias `50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950` solo cuando un sistema real lo necesite. No llenar el proyecto de escalas sin uso.

## Estados

Los estados hover, active, disabled y focus deben ser distinguibles sin depender únicamente de cambios mínimos de color.
