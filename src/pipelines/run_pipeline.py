from src.utils.open_zip import open_zipfile
from src.extract.extractor import concat_files, extract_inegi_geo, extract_file
from src.transform.transformer import transform_delitos, transform_inegi_geo
from src.load.loader import load_to_mysql
from src.database.mysql_client import MySQLDatabase
from src.database.create_staging import create_total_delitos_table, create_table_inegi_geo, add_constraint
from src.load.load_dimensions import load_dim_entidad, load_dim_municipio, load_dim_tipo_delito
from src.load.load_fact import load_fact_delitos
from src.load.create_dw import create_dw_tables
from config.settings import MYSQL_CONFIG, DATA_PATH, INEGI_FILE_NAME, DELITOS_ZIPFILE_NAME
from src.utils.getFilenames import get_file_names
import pandas as pd





def run():
    
    
    print("----------------------------------------")
    print("             Base de delitos            ")
    print("----------------------------------------")
    # DB
    db = MySQLDatabase(MYSQL_CONFIG["database"])

    print("\n---      Creación de tablas       ---")
    # crea tablas si no existen
    create_total_delitos_table(db)
    #add_constraint(db)
    create_table_inegi_geo(db)
    # crea modelo star
    create_dw_tables(db)

    # inegi 
    df_geo = extract_inegi_geo(DATA_PATH, INEGI_FILE_NAME)
    # nombre archivos
    file_names = get_file_names()
    print("\n---       Carga de información    ---")
    print(f"Cargando: inegi_geo")

    for file_name in file_names:      
        print(f"Cargando: {file_name}")
        df = extract_file(file_name)
        df_transformed = transform_delitos(df)
        load_to_mysql(db, df_transformed, "staging_delitos")
        
    # transforma
    df_geo_clean = transform_inegi_geo(df_geo)
    # carga a mysql
    load_to_mysql(db, df_geo_clean, "geo_loc")
    print("Creación de tabla staging completada \n")
    
    print("---   Generación de dimensiones   ---")
    # carga de información
    load_dim_entidad(db)
    print("Carga dim_entidad")
    load_dim_municipio(db)
    print("Garga dim_municipio")
    load_dim_tipo_delito(db)
    print("Carga dim_tipo_delito")
    load_fact_delitos(db)
    print("Carga fact_delitos")
    #truncate_staging(db)
    print("Carga completada \n")
    
    db.close()

    print("✅ Pipeline ejecutado correctamente")

