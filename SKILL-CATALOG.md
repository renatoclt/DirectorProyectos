# Catálogo de Skills reutilizables

Las Skills viven en `.github/skills/`. Enseñan procedimientos reutilizables; no son agentes ni conceden herramientas.

| Skill | Origen | Uso principal | Agentes autorizados |
|---|---|---|---|
| `color-system` | Original del proyecto | Tres paletas, comparación, recomendación, tokens y contraste | Diseñador UX UI, Desarrollador Frontend, QA Engineer, Auditor de Entrega |
| `frontend-design` | Adaptación de Anthropic | Crear o rediseñar interfaces web contextuales | Diseñador UX UI, Desarrollador Frontend, Prototipador UX |
| `frontend-design-review` | Adaptación de Microsoft | Revisar calidad visual, sistema de diseño, responsive y accesibilidad | Diseñador UX UI, Desarrollador Frontend, QA Engineer, Auditor de Entrega |

## Flujo recomendado

```text
brief → color-system → A/B/C → recomendación + tokens → frontend-design → mockup/implementación → frontend-design-review
```

## Regla de prioridad

```text
Requisito aprobado → Contrato del agente → Marca y decisiones del proyecto → Skill reusable → Recomendación general
```

Una Skill nunca puede reemplazar una decisión aprobada ni permitir escritura fuera de las rutas del agente.

## Actualización segura

1. Revisar origen/licencia o declarar Skill original.
2. Actualizar `UPSTREAM.md` y `governance/skills-lock.json`.
3. Actualizar escenarios.
4. Ejecutar `python testing/run_tests.py`.
5. Revisar `SKILLBASE-002`.
6. Solo tras aprobación humana, actualizar baseline.
