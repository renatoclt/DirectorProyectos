---
name: frontend-design
description: Diseña o rediseña interfaces web distintivas, coherentes, responsive y accesibles sin caer en plantillas genéricas. Usar cuando se necesite definir dirección visual, sistema de tokens, composición, tipografía, contenido de interfaz, componentes o implementar una página, landing, dashboard, aplicación o flujo frontend. No usar para redefinir requisitos, reglas de negocio, APIs, bases de datos o infraestructura.
---

# Frontend Design

Aplicar esta capacidad como un director de diseño que debe dar a cada producto una identidad visual propia, vinculada con su industria, audiencia, propósito y contenido real.

Esta Skill adapta para este proyecto los principios de la Skill pública `frontend-design` de Anthropic. Consultar [UPSTREAM.md](UPSTREAM.md) para origen, licencia y cambios de integración.

## Límites obligatorios

- Respetar el alcance, los requisitos, los criterios de aceptación y el contrato del agente que utiliza la Skill.
- No inventar funcionalidades, roles, datos, reglas de negocio ni integraciones.
- No ampliar herramientas ni permisos del agente.
- No sustituir validaciones de seguridad, accesibilidad, QA o arquitectura.
- Distinguir claramente entre decisión confirmada, supuesto y propuesta visual.
- Si falta información esencial de marca o audiencia, proponer una dirección marcada como pendiente de aprobación.

## Elegir el modo

### Modo A: dirección y especificación

Usar cuando el resultado esperado sea una propuesta visual, una especificación UX/UI, un wireframe, un sistema de diseño o un handoff, sin modificar código.

### Modo B: implementación

Usar cuando exista autorización para modificar frontend y se disponga de alcance aprobado, especificación, restricciones técnicas y rutas permitidas.

## Flujo obligatorio

### 1. Comprender el encargo

Identificar antes de diseñar:

- producto y problema;
- audiencia principal;
- tarea prioritaria;
- personalidad y tono;
- contenido real disponible;
- restricciones de marca, tecnología, rendimiento y accesibilidad;
- sistema de diseño o componentes existentes;
- estados críticos del flujo.

No comenzar por colores o componentes aislados.

### 2. Anclar el diseño en el contexto

Extraer referencias del mundo real del producto: materiales, lenguaje, ambiente, actividad, cultura visual, nivel de confianza requerido y momento de uso.

Una plataforma financiera, una veterinaria y un alquiler de campers no deben compartir automáticamente la misma estética.

### 3. Definir una dirección visual compacta

Antes de construir, completar la plantilla de [plan de diseño](references/design-plan-template.md) con:

- concepto en una frase;
- rasgo memorable principal;
- paleta semántica de 4 a 6 colores;
- tipografía y escala;
- composición y alineación;
- espaciado, radios, bordes y sombras;
- uso de imágenes e iconografía;
- movimiento y reducción de movimiento;
- reglas de contenido y tono;
- criterios responsive y accesibles.

Gastar la audacia en uno o pocos elementos memorables. Mantener el resto disciplinado.

### 4. Revisar contra el brief

Aplicar [anti-generic-checklist.md](references/anti-generic-checklist.md).

Corregir cualquier decisión que podría pertenecer indistintamente a otro proyecto. No usar por costumbre:

- una cuadrícula de tarjetas idénticas para todo;
- un único radio y sombra en todos los componentes;
- gradientes decorativos sin función;
- etiquetas en mayúsculas o numeración sin significado;
- tipografías por defecto sin justificación;
- animaciones repetidas en cada sección;
- textos de relleno o llamadas a la acción ambiguas.

Estos recursos pueden utilizarse cuando el contexto los justifique, no como respuesta automática.

### 5. Diseñar todos los estados

Incluir, cuando apliquen:

- inicial;
- carga y skeleton;
- vacío;
- error recuperable;
- error bloqueante;
- éxito;
- sin permisos;
- sin conexión;
- datos parciales;
- contenido largo;
- interacción por teclado;
- reducción de movimiento;
- móvil, tablet y escritorio.

### 6. Construir o especificar con contenido realista

- Usar nombres, precios, fechas, estados y mensajes coherentes con el producto.
- Nombrar acciones por su resultado: `Guardar cambios`, no `Enviar`.
- Mantener el mismo vocabulario durante todo el flujo.
- Explicar errores indicando qué ocurrió y cómo continuar.
- Tratar los estados vacíos como una oportunidad para orientar la siguiente acción.

### 7. Aplicar calidad técnica

En modo implementación:

- reutilizar componentes y tokens existentes antes de crear otros;
- evitar valores duros cuando exista un token;
- mantener selectores CSS predecibles y sin colisiones;
- asegurar foco visible, navegación por teclado y contraste adecuado;
- respetar `prefers-reduced-motion`;
- optimizar imágenes, fuentes y carga inicial;
- verificar reflow y contenido sin desbordes;
- añadir o actualizar pruebas cuando el contrato lo permita.

### 8. Criticar antes de terminar

Revisar el resultado como si fuera una propuesta externa:

- ¿se reconoce el producto sin leer el nombre?
- ¿la acción principal es obvia?
- ¿la jerarquía explica qué hacer después?
- ¿existe un elemento memorable y contextual?
- ¿hay decoración sin función?
- ¿funciona con contenido extremo y en móvil?
- ¿los estados alternativos están cubiertos?
- ¿cumple el alcance sin inventar funciones?

Si el entorno permite capturas, usarlas para revisar la composición. Corregir antes de presentar.

## Salida en modo dirección

Entregar:

1. contexto comprendido;
2. dirección visual;
3. tokens propuestos;
4. estructura o wireframe;
5. componentes y estados;
6. responsive;
7. accesibilidad;
8. contenido clave;
9. decisiones pendientes;
10. criterios de aceptación visual;
11. handoff basado en [handoff-template.md](references/handoff-template.md).

## Salida en modo implementación

Entregar:

1. plan visual aprobado usado;
2. archivos modificados;
3. componentes y estados implementados;
4. tokens reutilizados o añadidos;
5. comportamiento responsive y accesible;
6. pruebas y comandos ejecutados;
7. capturas o evidencia disponible;
8. diferencias respecto al diseño;
9. riesgos y pendientes.
