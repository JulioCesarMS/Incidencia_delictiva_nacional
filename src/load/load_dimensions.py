

# carga datos a dimensión estado
def load_dim_entidad(db):
    query = """
    INSERT INTO dim_entidad (cve_ent,nom_ent,nom_abr)
    SELECT DISTINCT
        cve_ent,
        nom_ent,
        nom_abr
    FROM geo_loc
    """
    db.execute(query)


# carga datos a dimensión municipio    
def load_dim_municipio(db):
    query = """
    INSERT INTO dim_municipio (cve_ent,nom_ent,cve_mun,nom_mun,latitud,longitud,poblacion)
    SELECT
        g.cve_ent,
        g.nom_ent,
        g.cve_mun,
        g.nom_mun,
        AVG(g.lat_decimal),
        AVG(g.lon_decimal),
        SUM(g.pob_total)
    FROM geo_loc g
    GROUP BY
        g.cve_ent,
        g.nom_ent,
        g.cve_mun,
        g.nom_mun;
    """
    db.execute(query)
    
# carga datos a dimensión tipo delito   
def load_dim_tipo_delito(db):
    query = """
    INSERT INTO dim_tipo_delito (tipo_delito,subtipo_delito,modalidad)
    SELECT DISTINCT
        tipo_delito,
        subtipo_delito,
        modalidad
    FROM staging_delitos;
    """
    db.execute(query)
    
    
