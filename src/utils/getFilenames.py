from pathlib import Path
from config.settings import DATA_PATH


ruta = Path(F"{DATA_PATH}/Municipal_Delitos")

# obtiene nombre archivos desde la carpeta 
def get_file_names():
    file_names = [archivo.name for archivo in ruta.glob("*.xlsx")]
    return file_names