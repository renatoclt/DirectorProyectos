---
name: "validar-contratos-agentes"
description: "Comprueba que perfiles, contratos y herramientas estén sincronizados sin ejecutar escenarios conductuales."
agent: "Ingeniero de Testing de Agentes"
---

Ejecuta `python testing/run_tests.py` y enfoca el reporte en:

- perfiles sin contrato;
- contratos sin perfil;
- nombres o herramientas desincronizados;
- visibilidad incorrecta;
- agentes no incluidos en el Director;
- escenarios faltantes;
- cambios respecto al baseline.

No modifiques archivos ni actualices el baseline.
