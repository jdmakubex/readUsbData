import os
import platform
import pandas as pd
from datetime import datetime
import magic
import mimetypes

def get_file_info(root_dir):
    file_info_list = []
    for root, dirs, files in os.walk(root_dir):
        for name in files + dirs:
            file_path = os.path.join(root, name)
            if os.path.exists(file_path):
                try:
                    stat = os.stat(file_path)
                    mod_time = datetime.fromtimestamp(stat.st_mtime)

                    # Obtener el tipo de archivo
                    if os.path.isdir(file_path):
                        file_type = 'Carpeta de archivos'
                    else:
                        try:
                            mime = magic.Magic(mime=True)
                            file_type = mime.from_file(file_path)
                        except magic.MagicException:
                            mime_type, _ = mimetypes.guess_type(file_path)
                            file_type = mime_type if mime_type else 'Archivo desconocido'

                    file_info = {
                        'Nombre': name,
                        'Ruta Completa': file_path,
                        'Fecha de Modificación': mod_time.date(),
                        'Hora de Modificación': mod_time.time(),
                        'Tipo': file_type,
                        'Tamaño': stat.st_size
                    }
                    file_info_list.append(file_info)
                except Exception as e:
                    print(f"Error al procesar el archivo {file_path}: {e}")
    return file_info_list

def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

def get_usb_path(label):
    system = platform.system()
    if system == "Windows":
        return f'{label}:\\'
    elif system == "Linux":
        user = os.getenv("USER")
        return f'/media/{user}/{label}'
    else:
        print(f'Sistema operativo no soportado: {system}')
        exit(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Explorar una memoria USB y exportar información a un archivo de Excel.')
    parser.add_argument('usb_label', type=str, help='Etiqueta de la unidad USB a explorar')
    args = parser.parse_args()

    usb_label = args.usb_label
    root_dir = get_usb_path(usb_label)

    if not os.path.exists(root_dir):
        print(f'La unidad con la etiqueta {usb_label} no se encontró.')
        exit(1)

    file_info_list = get_file_info(root_dir)
    output_file = 'usb_file_info.xlsx'
    save_to_excel(file_info_list, output_file)
    print(f'Información de archivos guardada en {output_file}')
