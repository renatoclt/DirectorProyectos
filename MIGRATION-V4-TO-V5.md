# Migración de v4 a v5

La versión 5 añade propuestas ejecutivas, anexos detallados, perfil comercial reutilizable y mockups conceptuales.

## Cambios principales

- Nuevo comando `/propuesta-con-mockup`.
- Nuevo agente interno `Prototipador UX`.
- Nuevo perfil reutilizable `company/COMPANY-PROFILE.md`.
- Nuevas plantillas bajo `templates/proposal/`.
- Nueva estructura por proyecto:
  - `projects/<slug>/00-propuesta/`
  - `projects/<slug>/03-ux/mockup-conceptual/`
- El Planificador puede emitir estimaciones preliminares sustentadas.
- El Director presenta una síntesis gerencial y deriva el detalle a adjuntos.
- Nuevos escenarios de regresión para propuesta, estimación, documentación y mockup.

## Instalación

1. Haz una copia del repositorio.
2. Cierra archivos de agentes abiertos en VS Code.
3. Copia el parche de v4 a v5 en la raíz.
4. Completa `company/COMPANY-PROFILE.md`.
5. Ejecuta:

```powershell
python testing/run_tests.py
```

6. Abre una conversación nueva en Local.
7. Ejecuta:

```text
/propuesta-con-mockup
```

## Compatibilidad

La versión 5 conserva los agentes, contratos, Skills y controles de v4. El nuevo agente solo puede escribir dentro de `projects/*/03-ux/mockup-conceptual/`.
