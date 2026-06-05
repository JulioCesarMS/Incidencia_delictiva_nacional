



# crea tabla de delitos en caso de no existir
def create_dim_entidad(db):
    query = """
    CREATE TABLE IF NOT EXISTS dim_entidad (
        id_ent INT AUTO_INCREMENT PRIMARY KEY,
        cve_ent CHAR(2) NOT NULL,
        nom_ent VARCHAR(100),
        nom_abr VARCHAR(10),
        UNIQUE(cve_ent)
    );
    """
    db.execute(query)
    #print("Tabla total_delitos creada o verificada correctamente")
    

# crea dimensión municipio    
def create_dim_municipio(db):
    query = """
    CREATE TABLE IF NOT EXISTS dim_municipio (
        id_mun INT AUTO_INCREMENT PRIMARY KEY,
		cve_ent CHAR(2),
        nom_ent VARCHAR(100),
		cve_mun CHAR(3),
		nom_mun VARCHAR(100),
		latitud DECIMAL(10,6),
		longitud DECIMAL(10,6),
		poblacion INT,
		UNIQUE(cve_ent,cve_mun)
	);
    """
    db.execute(query)
    
    
# crea dimensión municipio    
def create_dim_tipo_delito(db):
    query = """
    CREATE TABLE IF NOT EXISTS dim_tipo_delito (

        id_tipo_delito INT AUTO_INCREMENT PRIMARY KEY,
        tipo_delito VARCHAR(100) NOT NULL,
        subtipo_delito VARCHAR(100) NOT NULL,
        modalidad VARCHAR(100) NOT NULL,
        UNIQUE(
            tipo_delito,
            subtipo_delito,
            modalidad
        )
    );
    """
    db.execute(query)



# crea fact delitos    
def create_fact_delitos(db):
    query = """
    CREATE TABLE IF NOT EXISTS fact_delitos (
        id_fact BIGINT AUTO_INCREMENT PRIMARY KEY,
        anio int DEFAULT NULL,
        mes char(2) DEFAULT NULL,
        id_mun INT NOT NULL,
        id_tipo_delito INT NOT NULL,
        total INT NOT NULL,

        CONSTRAINT fk_fact_mun
            FOREIGN KEY (id_mun)
            REFERENCES dim_municipio(id_mun),

        CONSTRAINT fk_fact_tipo
            FOREIGN KEY (id_tipo_delito)
            REFERENCES dim_tipo_delito(id_tipo_delito),
            
        CONSTRAINT uk_fact_delitos
        UNIQUE (
            anio,
            mes,
            id_mun,
            id_tipo_delito
        )
    );
    """
    db.execute(query)
    
    
    
