# Contraste y accesibilidad

## Comprobaciones mínimas

- Texto normal: objetivo mínimo 4.5:1.
- Texto grande: objetivo mínimo 3:1.
- Componentes, controles y foco visibles: objetivo mínimo 3:1 frente a colores adyacentes cuando corresponda.
- No comunicar error, éxito, selección o estado únicamente mediante color.

## Proceso

1. Comprobar combinaciones de texto y fondos principales.
2. Comprobar texto de botones y CTA.
3. Comprobar estados hover, active, focus y disabled.
4. Comprobar mensajes semánticos.
5. Registrar excepciones o combinaciones no aptas.

## Herramienta local

```bash
python .github/skills/color-system/scripts/check_contrast.py "#17211B" "#F7F3EB"
```

El script devuelve la relación de contraste y una evaluación orientativa para texto normal, texto grande y componentes.
