# Explorador de Memoria USB

Este proyecto contiene un script de Python que explora una memoria USB especificada por la etiqueta de la unidad y exporta la información de los archivos y carpetas en un archivo de Excel. La información extraída incluye el nombre, la ruta completa, la fecha y hora de modificación, el tipo y el tamaño de cada archivo y carpeta.

## Requisitos

- Python 3.9
- Anaconda o Miniconda (recomendado para gestionar entornos)

## Instalación

### Paso 1: Crear y activar el entorno Conda

1. Abre una terminal y crea un nuevo entorno Conda con Python 3.9:

   ```bash
   conda create -n usb_env python=3.9

2. Activa el entorno recién creado:
    ```bash
    conda activate usb_env

### Paso 2: Instalar las dependencias

1. Navega al directorio del proyecto donde se encuentra requirements.txt.

2. Instala las dependencias utilizando pip:
    ```bash
    pip install -r requirements.txt

## Uso
Para ejecutar el script y explorar una memoria USB, sigue estos pasos:
1. Navega al directorio del proyecto:
    ```bash
    cd path/to/your/project

2. Ejecuta el script pasando la etiqueta de la unidad USB como argumento:
    ```bash
    python main.py D

Reemplaza D con la letra de la unidad USB que deseas explorar.

## Notas
- Asegúrate de que la unidad USB esté conectada y que la etiqueta proporcionada sea correcta.
- El archivo de salida se generará en el mismo directorio donde se ejecuta el script, con el nombre usb_file_info.xlsx.