# Propuesta ejecutiva y mockup conceptual

## Por qué se separa la información

Un cliente necesita decidir rápido, mientras el equipo necesita conservar detalle suficiente para ejecutar y auditar. Un solo documento intenta cumplir ambos objetivos y termina siendo demasiado largo o demasiado superficial.

Por eso la versión 5 utiliza dos niveles:

```text
PROPUESTA EJECUTIVA
→ lectura de 2 a 3 minutos
→ objetivo, solución, alcance, plazo, disponibilidad y próximo paso

ADJUNTOS
→ requisitos, entregables, recursos, estimación, riesgos y diseño
```

## Presentación sin afirmaciones inventadas

La sección “Presentación” debe explicar por qué el enfoque y las capacidades encajan con el proyecto. No debe inventar años de experiencia, clientes, certificaciones ni casos de éxito.

La fuente autorizada es:

`company/COMPANY-PROFILE.md`

Cuando un dato no esté confirmado, se marca como `POR CONFIRMAR`.

## Plan de trabajo

El plan ejecutivo muestra pocas fases y el resultado de cada una. El desglose completo vive en el anexo A03.

## Disponibilidad

La disponibilidad debe provenir del perfil comercial. Cuando todavía no está definida, se presenta como propuesta sujeta a confirmación, no como compromiso.

## Plazo estimado

Una estimación responsable necesita:

- alcance considerado;
- capacidad o equipo asumido;
- fecha de inicio;
- tiempo esperado para feedback;
- rango de duración;
- ventana tentativa de entrega;
- nivel de confianza;
- condiciones que pueden cambiarla.

Una fecha tentativa no es un compromiso contractual.

## Mockup conceptual

El mockup permite validar visualmente lo entendido antes de desarrollar. Se crea con datos ficticios en:

`projects/<slug>/03-ux/mockup-conceptual/`

No tiene backend, pagos, autenticación ni integraciones reales.

## Roles

- Director de Proyectos: consolida y presenta.
- Analista de Negocio: aclara problema y reglas.
- Product Manager: define MVP y exclusiones.
- Diseñador UX UI: define flujo, pantallas y dirección.
- Planificador de Proyecto: sustenta plan y estimación.
- Prototipador UX: crea el mockup estático.
- Gestor de Documentación: guarda propuesta y anexos.

## Comando recomendado

```text
/propuesta-con-mockup
```
