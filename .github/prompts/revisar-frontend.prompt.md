---
name: "revisar-frontend"
description: "Revisa una interfaz de forma independiente contra especificación, sistema de diseño, responsive y accesibilidad."
agent: "QA Engineer"
argument-hint: "Indica la pantalla, componente, flujo o rutas que se deben revisar."
---

Revisa `${input:reviewScope:describe la interfaz o rutas a revisar}`.

Procedimiento:

1. Reúne requisito, criterio de aceptación, handoff, sistema de diseño y evidencia disponible.
2. Aplica la Skill `frontend-design-review` ubicada en `.github/skills/frontend-design-review/`.
3. No modifiques código ni corrijas defectos.
4. Distingue defecto funcional, defecto visual, diferencia autorizada, mejora y falta de especificación.
5. Registra hallazgos `UI-###` con esperado, actual, impacto, evidencia, severidad y recomendación.
6. Declara explícitamente estados, dispositivos o criterios que no pudieron comprobarse.
7. Emite un veredicto sustentado.
