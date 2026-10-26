3. Instala las dependencias de testing

python -m pip install -r testing/requirements.txt

4. Ejecuta la validación
python testing/run_tests.py

El resultado esperado es:
Errores: 0
Advertencias: 0
RESULTADO: APROBADO

5. Abre una conversación nueva en VS Code
Selecciona:
Session Target: Local
Agente: Director de Proyectos

6. Prueba primero el sistema de agentes
Ejecuta directamente:
/probar-sistema-agentes mode=smoke

7. Inicia un proyecto
/iniciar-control-proyecto

Después puedes utilizar:
/estado-proyecto
/registrar-cambio
/cerrar-fase
/auditar-trazabilidad
/validar-contratos-agentes
/probar-sistema-agentes

La secuencia recomendada de primera instalación es:
1. Extraer el paquete
2. Ejecutar testing estático
3. Ejecutar smoke test conductual
4. Revisar aprendizaje/README.md
5. Seleccionar Director de Proyectos
6. Crear el primer proyecto
7. Consultar /estado-proyecto regularmente