# Gobierno del sistema de agentes y Skills

Esta carpeta contiene controles externos a los prompts.

## Agentes

Cada agente tiene tres capas:

1. **Contrato de alcance** en `contracts/*.contract.json`.
2. **Restricción técnica** mediante herramientas, visibilidad y rutas.
3. **Pruebas de regresión** en `testing/`.

`tool-policies.json` mantiene herramientas esperadas y `phase-gates.json` formaliza transiciones que requieren evidencia o aprobación humana.

## Skills

`skills-lock.json` registra para cada Skill:

- carpeta local;
- repositorio y ruta de origen;
- revisión de referencia;
- licencia;
- modo de integración;
- agentes autorizados;
- propósito.

Las Skills no conceden permisos. El contrato del agente sigue siendo el límite superior.

## Regla de mantenimiento de un agente

1. Actualiza `.agent.md`.
2. Actualiza su contrato.
3. Añade o modifica escenarios.
4. Ejecuta pruebas.
5. Revisa el cambio.
6. Actualiza baseline solo con aprobación humana.
7. Repite la suite.

## Regla de mantenimiento de una Skill

1. Revisa upstream y licencia.
2. Compara con la adaptación local.
3. Actualiza `SKILL.md`, referencias o metadata.
4. Conserva `LICENSE.txt` y documenta cambios en `UPSTREAM.md`.
5. Actualiza `skills-lock.json`.
6. Actualiza escenarios si cambia conducta.
7. Ejecuta pruebas.
8. Revisa `SKILLBASE-002`.
9. Actualiza baseline solo con aprobación humana.

## Propuesta y mockup

- El Director coordina la propuesta, pero no escribe directamente.
- Gestor de Documentación solo escribe bajo `projects/<slug>/`.
- Prototipador UX solo escribe bajo `projects/<slug>/03-ux/mockup-conceptual/`.
- El Planificador puede estimar por rangos con supuestos visibles.
- Ninguna fecha tentativa equivale a compromiso contractual.
- Las afirmaciones comerciales deben provenir de `company/COMPANY-PROFILE.md`.
