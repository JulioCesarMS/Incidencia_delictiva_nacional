from src.database.create_star_model import create_dim_entidad, create_dim_municipio, create_dim_tipo_delito
from src.database.create_star_model import create_fact_delitos




def create_dw_tables(db):

    create_dim_entidad(db)
    print("Tabla dim_entidad creada correctamente")
    create_dim_municipio(db) 
    print("Tabla dim_municipio creada correctamente")
    create_dim_tipo_delito(db)
    print("Tabla dim_tipo_delito creada correctamente")
    create_fact_delitos(db)
    print("Tabla fact_delitos creada correctamente")