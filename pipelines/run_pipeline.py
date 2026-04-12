from utils.open_zip import open_zipfile
from src.extract import concat_files, extract_inegi_geo
from src.transform import transform_delitos, transform_inegi_geo
from src.load import load_to_mysql
from database.mysql_client import MySQLDatabase
from database.create_table import create_total_delitos_table, create_table_inegi_geo, add_constraint
from config.settings import MYSQL_CONFIG, DATA_PATH, INEGI_FILE_NAME, DELITOS_ZIPFILE_NAME



def run():

    # DB
    db = MySQLDatabase(MYSQL_CONFIG["database"])

    # crea tablas si no existen
    create_total_delitos_table(db)
    add_constraint(db)
    create_table_inegi_geo(db)
    # unzip
    open_zipfile(DATA_PATH)
    # ----------------
    #     extract
    # ----------------
    file_names = [str(year) for year in range(2015, 2026)]

    # delitos
    NEW_DATA_PATH = DATA_PATH + DELITOS_ZIPFILE_NAME
    df = concat_files(NEW_DATA_PATH, file_names)
    # inegi 
    df_geo = extract_inegi_geo(DATA_PATH, INEGI_FILE_NAME)
    print("✅ extracción completada")
    # ----------------
    #    transform
    # ----------------
    df_delitos_clean = transform_delitos(df)
    df_geo_clean = transform_inegi_geo(df_geo)
    #print(df_delitos_clean.columns)
    #print(df_clean.head())
    #print(df_geo_clean.columns)
    
    print("✅ transformación completada")
     # ----------------
    #    Load
    # ----------------
    load_to_mysql(db, df_delitos_clean, "total_delitos2")
    #db.insert_to_db(df_clean, tabla="delitos2", batch_size=5000)
    load_to_mysql(db, df_geo_clean, "geo_loc2")
    #db.insert_to_db(df_geo_clean, tabla="geo_loc2", batch_size=5000)
    print("✅ carga a base de datos completada \n")
    db.close()

    print("✅ Pipeline ejecutado correctamente")

