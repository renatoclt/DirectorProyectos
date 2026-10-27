# Ejemplos de clasificación

## Defecto funcional

**Situación:** el botón `Confirmar reserva` no envía la operación.

**Clasificación:** defecto funcional, no solo visual.

**Recomendación:** registrar en QA y vincular al criterio de aceptación.

## Defecto visual

**Situación:** el precio total usa un estilo secundario aunque es la decisión principal de compra.

**Clasificación:** defecto visual mayor si contradice la especificación aprobada.

## Diferencia autorizada

**Situación:** el equipo sustituyó un componente de Figma por uno equivalente del sistema de diseño y existe decisión aprobada.

**Clasificación:** diferencia autorizada, no defecto.

## Mejora propuesta

**Situación:** una animación podría reforzar el cambio de estado, pero no existe requisito ni problema de comprensión.

**Clasificación:** observación o mejora, no incumplimiento.

## Falta de especificación

**Situación:** no existe definición para el estado de pago pendiente.

**Clasificación:** bloqueo de diseño o requisito; no inventar el comportamiento durante la revisión.

## Hallazgo bien formado

### UI-004 — Acción principal compite con acción secundaria

- Pantalla: resumen de reserva móvil.
- Fuente de verdad: diseño aprobado `RES-UX-03`.
- Esperado: `Pagar reserva` como única acción primaria.
- Actual: `Pagar reserva` y `Guardar para después` tienen igual peso.
- Impacto: aumenta duda en el punto de conversión.
- Evidencia: captura `checkout-mobile-02.png`.
- Severidad: Mayor.
- Recomendación: convertir la acción secundaria en enlace y conservar un único botón primario.
