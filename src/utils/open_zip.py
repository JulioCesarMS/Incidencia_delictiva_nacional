from zipfile import ZipFile
import os
from config.settings import  DATA_PATH

# busca el zip en el directorio  DATA_PATH y lo extrae importante antes de actualizar eliminar el anterior
def open_zipfile(folder_path):
    # buscar archivos .zip en la carpeta
    zip_files = [f for f in os.listdir(folder_path) if f.endswith(".zip")]

    # validaciones
    if len(zip_files) == 0:
        raise FileNotFoundError("No se encontró ningún archivo .zip en la carpeta")

    if len(zip_files) > 1:
        raise ValueError(f"Se encontraron múltiples .zip: {zip_files}")

    # si encuentra varios toma el primero
    zip_file = zip_files[0]
    zip_path = os.path.join(folder_path, zip_file)

    # extracción en la misma carpeta
    with ZipFile(zip_path, 'r') as zip_ref:
        #zip_ref.printdir()
        #print(f"Extrayendo {zip_file}...")
        zip_ref.extractall(folder_path)
        print(f"Extracción completada")

    return zip_path