# Sistema de color: por qué existe y cómo usarlo

## Por qué separar color del diseño general

`frontend-design` resuelve la dirección visual completa. `color-system` aísla una decisión sensible: convertir contexto de marca en colores reutilizables, accesibles y sustituibles sin reescribir UX.

## Por qué tres alternativas

Una sola paleta hace difícil distinguir entre decisión razonada y primera ocurrencia del modelo. Tres direcciones obligan a comparar posicionamiento, claridad, confianza, diferenciación y accesibilidad. El sistema recomienda una para no bloquear el flujo, pero las tres quedan como propuestas.

## Tokens semánticos

`--color-primary` describe función. `--green` describe pigmento. Los tokens semánticos permiten cambiar identidad cromática sin cambiar el significado de componentes ni reglas.

## Accesibilidad

El contraste se revisa antes del mockup. La Skill incluye `scripts/check_contrast.py` para validar combinaciones HEX de forma determinista. El color nunca debe ser el único indicador de estado.

## Flujo

```text
contexto → color-system → A/B/C → comparación → recomendación → tokens → frontend-design → mockup/implementación → frontend-design-review
```

## Cambiar de paleta sin cambiar UX

Si el cliente prefiere B en lugar de A, conservar navegación, jerarquía, contenido y componentes. Sustituir tokens y revisar contraste. Solo cambiar estructura si existe una razón UX independiente del color.

## QA y auditoría

QA comprueba contraste y uso de tokens, pero no diseña una identidad nueva. Auditor de Entrega verifica que la implementación coincida con la dirección aprobada o declarada.

## Modificar sin romper

1. Editar `.github/skills/color-system/`.
2. Actualizar `governance/skills-lock.json` si cambia metadata o uso.
3. Actualizar escenarios afectados.
4. Ejecutar `python testing/run_tests.py`.
5. Revisar `SKILLBASE-002`.
6. Solo tras aprobación humana, actualizar baseline.
