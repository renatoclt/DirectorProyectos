---
name: frontend-design-review
description: Revisa interfaces frontend, PRs, componentes, páginas y flujos contra calidad visual, sistema de diseño, responsive, accesibilidad y confianza. Usar para auditorías de UI, comparación con especificaciones o Figma, revisión de tokens, estados, jerarquía, contenido y comportamiento. Puede orientar creación visual, pero en este proyecto se usa principalmente como control independiente. No usar para backend, datos, infraestructura o lógica sin interfaz.
---

# Frontend Design Review

Aplicar una revisión sistemática de interfaces sin modificar la implementación cuando el agente actúe como QA o auditor.

Esta Skill adapta para este proyecto la Skill pública `frontend-design-review` de Microsoft. Consultar [UPSTREAM.md](UPSTREAM.md) para origen, licencia y cambios.

## Límites obligatorios

- La Skill no concede herramientas ni permisos adicionales.
- Respetar el contrato del agente que la utiliza.
- En modo auditoría o QA, no editar código, diseño, baseline ni evidencia.
- No aceptar afirmaciones sin archivo, captura, prueba o especificación verificable.
- No convertir recomendaciones visuales en alcance aprobado.
- No revisar backend, base de datos, infraestructura o reglas de negocio salvo su efecto visible en la interfaz.

## Elegir el tipo de revisión

Consultar [review-type-modifiers.md](references/review-type-modifiers.md) y seleccionar uno:

- revisión de diseño antes de implementar;
- revisión de componente;
- revisión de PR o implementación;
- revisión responsive;
- revisión de accesibilidad;
- revisión de flujo crítico;
- revisión final para entrega.

## Preparar contexto

Reunir, según exista:

- objetivo del usuario;
- requisito, historia y criterio de aceptación;
- especificación UX/UI;
- sistema de diseño y tokens;
- Figma o referencia visual;
- implementación y rutas;
- estados esperados;
- breakpoints;
- capturas o entorno ejecutable;
- restricciones de accesibilidad y rendimiento.

Si falta una fuente de verdad, declarar la revisión como parcial y no inventarla.

## Proceso de revisión

### 1. Identificar la tarea

Responder:

- ¿qué intenta lograr el usuario?
- ¿cuál es la acción principal?
- ¿qué confirma que terminó?
- ¿qué errores o alternativas puede encontrar?

### 2. Comparar con el sistema de diseño

Comprobar:

- reutilización de componentes;
- variantes correctas;
- tokens en lugar de valores arbitrarios;
- tipografía, color, espaciado y forma;
- consistencia entre vistas;
- excepción documentada cuando corresponda.

### 3. Evaluar tres pilares

#### Fricción mínima hacia la acción

- La siguiente acción es evidente.
- No compiten múltiples acciones principales.
- No existen callejones sin salida.
- El flujo pide solo información necesaria.
- Volver, cancelar o corregir es posible cuando corresponde.

#### Calidad como oficio

- La dirección estética es contextual, no genérica.
- La jerarquía visual ayuda a comprender.
- Responsive y reflow funcionan.
- Los estados están completos.
- El foco es visible y la navegación por teclado funciona.
- Contraste, etiquetas y semántica son adecuados.
- Movimiento e imágenes no degradan rendimiento o accesibilidad.

#### Construcción confiable

- Los errores son transparentes y accionables.
- Pagos, datos sensibles y acciones irreversibles muestran confirmación y estado.
- La interfaz no promete algo que el sistema no puede garantizar.
- El contenido generado por IA se identifica cuando el producto lo requiere.
- El usuario comprende consecuencias, progreso y resultado.

### 4. Revisar estados y extremos

Comprobar:

- carga;
- vacío;
- error;
- éxito;
- deshabilitado;
- sin permisos;
- sin conexión;
- contenido largo;
- traducciones;
- zoom;
- móvil estrecho;
- teclado;
- reducción de movimiento.

### 5. Clasificar hallazgos

Usar:

- **Bloqueante:** impide completar la tarea, incumple seguridad/accesibilidad crítica o invalida el criterio.
- **Mayor:** afecta significativamente comprensión, consistencia o uso.
- **Menor:** refinamiento que no bloquea la tarea.
- **Observación:** recomendación sin incumplimiento demostrado.

Cada hallazgo debe incluir:

- identificador;
- pantalla o componente;
- fuente de verdad;
- esperado;
- actual;
- impacto;
- evidencia;
- recomendación;
- severidad.

### 6. Emitir veredicto

Usar uno:

- `APROBADO`;
- `APROBADO_CON_OBSERVACIONES`;
- `RECHAZADO`;
- `BLOQUEADO_POR_FALTA_DE_EVIDENCIA`.

Aplicar [review-output-format.md](references/review-output-format.md) y [quick-checklist.md](references/quick-checklist.md).

## Uso junto a `frontend-design`

- Usar `frontend-design` para proponer o construir una dirección visual.
- Usar `frontend-design-review` para evaluar el resultado de forma independiente.
- El mismo agente puede hacer autocontrol durante construcción, pero QA o Auditor deben repetir la revisión sin asumir que la autocorrección es evidencia suficiente.

## Patrones

Consultar [pattern-examples.md](references/pattern-examples.md) para ejemplos de hallazgos y diferencias entre defecto, mejora y falta de especificación.
