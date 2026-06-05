import os
from dotenv import load_dotenv

load_dotenv()


# configuración base de datos
class DB:
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    NAME = os.getenv("DB_NAME")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    
    

DATA_PATH = "data/raw/"
DELITOS_ZIPFILE_NAME = "Municipal_Delitos"
INEGI_FILE_NAME = "AGEEML_202510141527415" # sin extensión
MYSQL_CONFIG = {
    "database": "delitos"
}