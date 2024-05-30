

 # Predicción de Precio de Ticket de Avión - Fase 3

## Descripción
En esta fase, nos centramos en la implementación del modelo predictivo en una aplicación web utilizando Flask. Esta fase incluye la creación del modelo, la configuración del servidor web y la interfaz de usuario para realizar predicciones.

## Estructura del Proyecto

**Dockerfile:** Archivo para la construcción de la imagen Docker.

**entrypoint.sh:** Script de entrada para ejecutar los procesos de creación del modelo y el servidor Flask.

**predict.html:** Archivo HTML que sirve como interfaz de usuario para realizar predicciones.

**createModel.py:** Script para crear y guardar el modelo predictivo.

**myrestapi.py:** Script que define la API REST con Flask para realizar las predicciones.

**dataframe.csv:** Dataset utilizado para crear el modelo.

**30_predict.csv:** Archivo con las predicciones generadas.

**requirements.txt:** Lista de dependencias necesarias para el proyecto.

# Instalación

## Clona el repositorio y navega a la carpeta de la fase-2:

**git clone https://github.com/cripto26/Prediccion_precio_de_ticket_de_avion.git**

**cd Prediccion_precio_de_ticket_de_avion/fase-2**

# Uso

## Construye la imagen de Docker:

**docker build -t prediccion_precio_ticket .**

## Ejecuta el contenedor:

**docker run --rm prediccion_precio_ticket**

