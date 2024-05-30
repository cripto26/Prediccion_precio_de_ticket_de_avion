

 # Predicción de Precio de Ticket de Avión - Fase 2

## Descripción
En esta fase, configuramos un contenedor de Docker con todas las librerías necesarias para correr el modelo de predicción.

## Estructura del Proyecto

**Dockerfile:**  Archivo para la construcción de la imagen Docker.

**entrypoint.sh:**  Script de entrada para ejecutar los procesos de entrenamiento y predicción.

**predict.py:**  Script para realizar las predicciones utilizando el modelo entrenado.

**train.py:**  Script para entrenar el modelo de predicción.

**30_predict.csv:**  Archivo con las predicciones generadas.

**Data_Train.xlsx:**  Dataset utilizado para el entrenamiento.

**requirements.txt:**  Lista de dependencias necesarias para el proyecto.

# Instalación

## Clona el repositorio y navega a la carpeta de la fase-2:

**git clone https://github.com/cripto26/Prediccion_precio_de_ticket_de_avion.git**

**cd Prediccion_precio_de_ticket_de_avion/fase-2**

# Uso

## Construye la imagen de Docker:

**docker build -t prediccion_precio_ticket .**

## Ejecuta el contenedor:

**docker run --rm prediccion_precio_ticket**

