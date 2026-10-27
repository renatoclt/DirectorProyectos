# Migración v5 → v6

La versión 6 añade una capa reusable de dirección cromática antes del mockup.

## Nuevo

- `.github/skills/color-system/`
- `templates/proposal/adjuntos/A07-DIRECCION-VISUAL-Y-PALETA.md`
- `aprendizaje/14-sistema-de-color.md`
- escenarios DIR-006, UX-003, FE-003, QA-003, AUDIT-003 y AGTTEST-004

## Flujo nuevo

```text
brief → color-system → A/B/C → recomendación → tokens → frontend-design → mockup → frontend-design-review
```

La recomendación permite continuar sin bloquear el mockup, pero permanece como `PROPUESTA` hasta validación humana.

## Instalación

Copiar el parche v5→v6 en la raíz y ejecutar:

```powershell
python testing/run_tests.py
```

No actualizar baseline automáticamente si aparece una regresión inesperada.
