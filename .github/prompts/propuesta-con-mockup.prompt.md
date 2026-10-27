---
name: "propuesta-con-mockup"
description: "Convierte una descripción breve en una propuesta ejecutiva concisa, anexos detallados y un mockup conceptual navegable."
agent: "Director de Proyectos"
argument-hint: "Describe el proyecto, el usuario, el resultado esperado y, si existe, la fecha de inicio deseada."
---

Prepara una propuesta comercial inicial para:

`${input:projectDescription:describe el proyecto, el problema y quién lo utilizará}`

Usa el slug:

`${input:projectSlug:indica un slug corto en minúsculas}`

Fecha de inicio deseada o supuesto de inicio:

`${input:proposedStartDate:indica AAAA-MM-DD o escribe "siguiente día hábil después de la aprobación"}`

Procedimiento:

1. Lee `company/COMPANY-PROFILE.md`.
2. Interpreta la necesidad sin inventar requisitos.
3. Coordina un análisis ligero con Analista de Negocio y Product Manager.
4. Si existe interfaz, solicita a Diseñador UX UI el flujo, pantallas y dirección visual mediante `frontend-design`.
5. Solicita a Planificador de Proyecto un plan y una estimación preliminar sustentada.
6. Si existe interfaz, solicita a Prototipador UX crear un mockup estático en `projects/<slug>/03-ux/mockup-conceptual/`.
7. Solicita a Gestor de Documentación crear el paquete bajo `projects/<slug>/00-propuesta/`.
8. No implementes producto real, backend, base de datos, autenticación, pagos ni integraciones.
9. Presenta en el chat una versión ejecutiva de máximo 700 palabras.
10. Indica expresamente que todo el detalle se encuentra en los adjuntos.

La respuesta ejecutiva debe incluir:

## Resumen para decisión
## Presentación
## Lo que entendimos
## Solución propuesta
## Plan de trabajo
## Plazo estimado
## Disponibilidad y comunicación
## Mockup conceptual
## Documentos adjuntos
## Próximo paso

Reglas:

- Explica por qué el enfoque del equipo encaja con el proyecto sin inventar trayectoria o credenciales.
- La disponibilidad debe provenir del perfil comercial o quedar como propuesta por confirmar.
- Incluye una fecha o ventana tentativa solo con un supuesto de inicio visible.
- Indica duración, nivel de confianza y factores que pueden cambiar el plazo.
- Marca propuesta, anexos y mockup como BORRADOR.
- El mockup debe usar datos ficticios y no tener integraciones reales.

# Dirección cromática obligatoria

Cuando exista interfaz, antes del mockup invoca al Diseñador UX UI para aplicar `color-system`: generar Paleta A, B y C, compararlas, recomendar una, producir tokens semánticos y validar contraste. El mockup usa la recomendada como `PROPUESTA`; no esperar selección humana para continuar. Guardar el detalle en `projects/<slug>/00-propuesta/adjuntos/A07-DIRECCION-VISUAL-Y-PALETA.md`. Luego aplicar `frontend-design` y finalmente `frontend-design-review`.
