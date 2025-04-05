# PlantFriends-Django-Vue
# Pasos para iniciar el proyecto:

1. Crear el entorno virtual con el comando.
```bash
python -m venv venv
```
2. Activar el entorno virtual.
```bash
cd venv\Scripts\activate
```
3. Con el entorno virtual activado, entren a la carpeta backend mediante la consola. ¡Cuidado con ejecutar los comandos de ahora sin eso! 
4. Una vez ahí en esa carpeta, usen el comando para instalar las dependencias.
```bash
pip install -r requirements.txt
```
5. Habiendo hecho eso, lo siguiente es aplicar las migraciones. Primero ejecuten el comando para crear las migraciones y luego el comando para aplicarlas.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
