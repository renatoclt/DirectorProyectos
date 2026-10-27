# Paquete de propuesta ejecutiva

Estas plantillas separan dos niveles de información:

1. `PROPUESTA-EJECUTIVA.md`: documento breve para que una persona tome una decisión en 2 a 3 minutos.
2. `INDICE-ADJUNTOS.md` y los anexos: detalle funcional, alcance, plan, recursos, plazo, riesgos y mockup.

La propuesta ejecutiva no debe convertirse en un documento técnico extenso. Cuando un dato requiera explicación, se resume y se enlaza al anexo correspondiente.

Estructura esperada por proyecto:

```text
projects/<slug>/
├── 00-propuesta/
│   ├── PROPUESTA-EJECUTIVA.md
│   ├── INDICE-ADJUNTOS.md
│   └── adjuntos/
│       ├── A01-ENTENDIMIENTO-Y-OBJETIVOS.md
│       ├── A02-ALCANCE-Y-ENTREGABLES.md
│       ├── A03-PLAN-DE-TRABAJO-Y-RECURSOS.md
│       ├── A04-PLAZO-DISPONIBILIDAD-Y-COMUNICACION.md
│       ├── A05-SUPUESTOS-RIESGOS-Y-PREGUNTAS.md
│       ├── A06-MOCKUP-Y-DECISIONES-DE-DISENO.md
│       └── A07-DIRECCION-VISUAL-Y-PALETA.md
└── 03-ux/
    └── mockup-conceptual/
        ├── index.html
        ├── styles.css
        ├── script.js
        ├── README.md
        └── MOCKUP-SPECIFICATION.md
```
