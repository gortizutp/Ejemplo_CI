# Usar la imagen oficial liviana de Python 3.11
FROM python:3.11-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos de la carpeta local al contenedor
COPY . .

# Ejecutar la prueba unitaria durante la construcción de la imagen
RUN python -m unittest discover -s tests

# Comando por defecto al iniciar el contenedor
CMD ["python", "operaciones.py"]