# Testing del sistema de agentes

Esta carpeta prueba **el equipo de agentes**, no el producto que los agentes construyan.

## Cuatro niveles

1. **Estructura:** YAML, archivos, nombres, visibilidad y referencias.
2. **Contratos:** perfil, contrato y política de herramientas deben coincidir.
3. **Baseline:** detecta cualquier modificación en perfiles o contratos.
4. **Conducta:** escenarios que evalúan si cada agente conserva su función original.

## Ejecutar en Windows

```powershell
python -m pip install -r testing/requirements.txt
python testing/run_tests.py
```

También puedes usar:

```powershell
./testing/run-tests.ps1
```

En VS Code: `Ctrl+Shift+P` → `Tasks: Run Task` → `Validar sistema de agentes`.

## Ejecutar escenarios conductuales

Con Session Target **Local**, ejecuta directamente:

```text
/probar-sistema-agentes mode=smoke
```

El prompt activa al Ingeniero de Testing de Agentes como agente principal. Esto permite que invoque a los agentes evaluados sin habilitar subagentes anidados.

Modos disponibles: `static`, `smoke`, `full` y `agent:<nombre>`.

## Actualizar el baseline

El baseline no se actualiza para ocultar una prueba fallida. Después de revisar y aprobar un cambio intencional:

```powershell
python testing/run_tests.py --update-baseline --confirm-update-baseline
python testing/run_tests.py
```

El Ingeniero de Testing de Agentes tiene prohibido ejecutar esa actualización. La decisión debe ser humana.

## Limitación importante

Las pruebas automáticas validan estructura y coherencia. Las pruebas conductuales usan modelos generativos y pueden variar; por eso se evalúan mediante rúbricas, comportamientos obligatorios y comportamientos prohibidos.
