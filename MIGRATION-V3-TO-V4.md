# Migración de la versión 3 a la versión 4

La versión 4 integra Skills reutilizables de diseño y amplía testing, contratos y documentación.

## Antes de copiar

1. Haz una copia del repositorio actual.
2. Guarda o cierra archivos abiertos en VS Code.
3. Si VS Code muestra `The content of the file is newer`, compara o usa `File: Revert File`; no sobrescribas a ciegas.
4. Conserva cualquier personalización propia para compararla después.

## Instalación con el paquete completo

Extrae el contenido en la raíz del repositorio, de modo que `.github/` quede directamente en esa raíz.

## Instalación con el parche

Extrae el parche sobre la versión 3 y acepta únicamente los reemplazos incluidos. El parche contiene baselines ya sincronizados con la versión 4 oficial del paquete.

## Validación

```powershell
python -m pip install -r testing/requirements.txt
python testing/run_tests.py
```

Resultado esperado:

```text
Errores: 0 | Advertencias: 0
RESULTADO: APROBADO
```

Después, en una conversación nueva con Local:

```text
/skills
/probar-sistema-agentes mode=smoke
```

## Si aparece BASE-002 o SKILLBASE-002

No actualices el baseline de inmediato.

1. Revisa qué archivo personalizado difiere.
2. Decide si conservar tu cambio o la versión 4.
3. Sincroniza perfil, contrato, Skill, lock y escenarios según corresponda.
4. Ejecuta pruebas.
5. Solo con aprobación humana explícita, actualiza baselines.

## Nuevos comandos

```text
/disenar-frontend
/revisar-frontend
```

## Nuevas rutas

```text
.github/skills/
governance/skills-lock.json
testing/baselines/skill-manifest.json
SKILL-CATALOG.md
THIRD-PARTY-NOTICES.md
aprendizaje/12-skills-reutilizables.md
```
