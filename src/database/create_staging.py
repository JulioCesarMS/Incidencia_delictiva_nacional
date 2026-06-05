


# crea tabla de delitos en caso de no existir
def create_total_delitos_table(db):
    query = """
    CREATE TABLE IF NOT EXISTS staging_delitos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Anio INT,
        Mes CHAR(2),
        CVE_ENT CHAR(2) NOT NULL,
        CVE_MUN CHAR(3) NOT NULL,
        Tipo_delito VARCHAR(100),
        Subtipo_delito VARCHAR(100),
        Modalidad VARCHAR(100),
        Total INT
    );
    """
    db.execute(query)
    print("Tabla staging_delitos creada correctamente")

# protege de duplicados
def add_constraint(db):
    query = """  
        ALTER TABLE staging_delitos 
        ADD CONSTRAINT unique_delito 
        UNIQUE (
            Anio, 
            Mes, 
            CVE_ENT, 
            CVE_MUN, 
            Tipo_delito, 
            Subtipo_delito, 
            Modalidad
        );
    
    """
    db.execute(query)
    print("Se agregó restricción para evitar duplicados")

# crea tabla de inegi en caso de no existir
def create_table_inegi_geo(db):
    
    query = """
        CREATE TABLE IF NOT EXISTS geo_loc (
            CVEGEO VARCHAR(9) PRIMARY KEY NOT NULL,
            Estatus VARCHAR(10),
            CVE_ENT CHAR(2),
            NOM_ENT VARCHAR(100),
            NOM_ABR VARCHAR(10),
            CVE_MUN CHAR(3),
            NOM_MUN VARCHAR(100),
            CVE_LOC CHAR(4),
            NOM_LOC VARCHAR(100),
            AMBITO CHAR(1),
            LATITUD VARCHAR(20),
            LONGITUD VARCHAR(20),
            LAT_DECIMAL DECIMAL(10,6),
            LON_DECIMAL DECIMAL(10,6),
            ALTITUD INT,
            CVE_CARTA VARCHAR(10),
            POB_TOTAL INT,
            POB_MASCULINA INT,
            POB_FEMENINA INT,
            TOTAL_VIVIENDAS_HABITADAS INT,
            UNIQUE INDEX idx_ent_mun_loc (CVE_ENT, CVE_MUN, CVE_LOC),
            INDEX idx_ent_mun (CVE_ENT, CVE_MUN)
        );

    """
    db.execute(query)
    print("Tabla geo_loc creada correctamente")
    
    
    
    
    