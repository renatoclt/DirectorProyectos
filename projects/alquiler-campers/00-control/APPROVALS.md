# Aprobaciones y puertas de fase: Web de alquiler de campers (España)

> **Proyecto:** `alquiler-campers`  
> **Estado del documento:** BORRADOR  
> **Fecha:** 2026-10-26  
> **Fuente:** Instrucciones del Director de Proyectos al Gestor de Documentación; plantilla `templates/project-control/APPROVALS.md`.  
> **Decisiones pendientes:** las tres puertas de este registro.

El silencio no constituye aprobación. Conserva la evidencia textual o documental de cada decisión.

## Estados

`PENDING`, `APPROVED`, `APPROVED_WITH_CONDITIONS`, `REJECTED`, `REVOKED`.

## 1. Registro de puertas

| ID | Transición o decisión | Solicitado | Artefactos evaluados | Criterios | Decisor | Decisión | Condiciones | Evidencia | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| GATE-001 | Autorizar inicio de DISCOVERY | 2026-10-26 | [client-brief.md](../00-intake/client-brief.md) | Objetivo preliminar y autorización para analizar | Usuario | PENDING | — | Sin aprobación registrada | — |
| GATE-002 | DISCOVERY → DESIGN | 2026-10-26 | [requirements.md](../01-discovery/requirements.md), [mvp-and-backlog.md](../02-product/mvp-and-backlog.md) | DISCOVERY: requisitos, reglas y preguntas resueltas (reglas corporativas, "Fases y puertas de aprobación") | Usuario | PENDING | — | Sin aprobación registrada | — |

**Nota sobre GATE-002:** el identificador `GATE-002` lo asigna el Gestor de Documentación como siguiente número secuencial. El Director pidió registrar la puerta DISCOVERY → DESIGN como pendiente sin indicar su identificador. El Director debe confirmar el ID.

## 2. Transición PLANNING → BUILD

**No solicitada.** No existe puerta registrada ni aprobación para pasar de PLANNING a BUILD.

- No existe alcance aprobado.
- No se ha autorizado ningún desarrollo.
- Según las reglas corporativas, no se avanza de PLANNING a BUILD sin aprobación humana explícita registrada en este archivo.

**Nota del Gestor (2026-10-26):** el Planificador entregó un plan de implementación en BORRADOR ([implementation-plan.md](../05-planning/implementation-plan.md)), con una tarea (TASK-013 del plan) para "aprobación del plan y solicitud PLANNING → BUILD". Eso **no es una solicitud**: el Gestor no ha registrado ninguna puerta nueva ni aprobación. El Revisor de Seguridad indica que no aprueba BUILD mientras no se cumplan sus controles obligatorios y se resuelvan SEG-001 a SEG-007 y SEG-010 ([security-review.md](../08-security/security-review.md)). Las decisiones B1 a B9 y las del Director siguen pendientes ([DECISIONS](DECISIONS.md) §4). GATE-001 y GATE-002 siguen PENDING. Ningún artefacto de UX, arquitectura, seguridad ni plan está aprobado. No se modifica ninguna puerta ni condición de este archivo.

**Nota del Gestor (2026-10-26, opción B):** **CR-001** ([CHANGE-REQUESTS](CHANGE-REQUESTS.md)) está en `WAITING_FOR_APPROVAL`: lo solicitó el usuario y está **pendiente de aprobación formal del cliente** (PEND-044). La elección de la opción B, el plazo objetivo de 1 semana y el valor de 400 USD son [C] del usuario (DEC-034 [OPB]) y **no constituyen una aprobación registrada en este archivo**. **No hay solicitud PLANNING → BUILD** ni se registra ninguna aprobación, puerta ni condición nueva. GATE-001 y GATE-002 siguen PENDING.

## 3. Observación del Gestor de Documentación

El análisis de negocio y la definición de producto se realizaron mientras GATE-001 figura como PENDING. El Gestor no atribuye aprobación a ese trabajo. Se registra como **borrador sin aprobación**. El Director decide cómo regularizar la secuencia de puertas.

## 4. Condiciones abiertas

| Gate | Condición | Responsable | Fecha objetivo | Estado | Evidencia de cierre |
|---|---|---|---|---|---|
| — | Ninguna (no hay puertas aprobadas con condiciones) | — | — | — | — |

## 5. Aprobaciones revocadas o sustituidas

| Gate | Motivo | Revocada por | Fecha | Nueva referencia |
|---|---|---|---|---|
| — | Ninguna | — | — | — |

## Enlaces

[Estado del proyecto](PROJECT-STATE.md) · [Decisiones](DECISIONS.md) · [Requisitos](REQUIREMENTS.md) · [Riesgos e impedimentos](RISKS.md) · [Solicitudes de cambio](CHANGE-REQUESTS.md)
