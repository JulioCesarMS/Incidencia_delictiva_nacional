import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ecobici.cdmx.gob.mx/"
DATA_URL = "https://ecobici.cdmx.gob.mx/en/open-data/"

DATA_PATH = "data/raw/"
DELITOS_ZIPFILE_NAME = "Municipal-Delitos-2015-2025_feb2026"
INEGI_FILE_NAME = "AGEEML_202510141527415" # sin extensión
MYSQL_CONFIG = {
    "database": "delitos"
}