# 1. Mapa general

## Problema

Con muchos agentes es fácil perder qué hizo cada uno, por qué lo hizo y quién puede cambiar archivos.

## Solución

El sistema separa responsabilidades:

```text
Cliente
  -> Director
      -> especialistas de descubrimiento
      -> especialistas de construcción
      -> QA y Seguridad
      -> Auditor de Trazabilidad
      -> Auditor de Entrega
```

Alrededor del equipo existen controles independientes:

```text
Contratos + herramientas + pruebas + trazabilidad + aprobaciones
```

## Regla central

El Director coordina, pero no implementa ni se audita a sí mismo. Los agentes especializados reciben el mínimo contexto y permisos necesarios.

## Entrada comercial de la versión 5

```text
Descripción
→ Propuesta ejecutiva
→ Adjuntos detallados
→ Mockup conceptual
→ Validación del cliente
→ Descubrimiento y planificación
```

La propuesta facilita la decisión; los adjuntos mantienen el detalle y la trazabilidad.
