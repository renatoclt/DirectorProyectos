---
name: "Mantenimiento seguro de Skills"
description: "Se aplica al crear o modificar Skills; exige origen, licencia, lock, referencias, escenarios y baseline revisado."
applyTo: ".github/skills/**/*"
---

# Mantenimiento seguro de Skills

Toda modificación de una Skill debe conservar:

1. `SKILL.md` con `name` igual a la carpeta y descripción con activadores claros.
2. `LICENSE.txt`.
3. `UPSTREAM.md` con origen, revisión y cambios locales.
4. `agents/openai.yaml`.
5. Referencias locales existentes.
6. Registro sincronizado en `governance/skills-lock.json`.
7. Escenarios conductuales de los agentes que la utilizan.
8. Pruebas automáticas ejecutadas.
9. Baseline actualizado solo después de revisión humana explícita.

Una Skill no puede conceder herramientas, ampliar rutas, redefinir alcance ni debilitar el contrato del agente.
