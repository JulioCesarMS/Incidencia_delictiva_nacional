


# carga datos a fact delitos 
def load_fact_delitos(db):
    query = """
    INSERT INTO fact_delitos (anio,mes,id_mun,id_tipo_delito,total)
    SELECT
        td.anio,
        td.mes,
        dm.id_mun,
        dtd.id_tipo_delito,
        td.total
    FROM staging_delitos td

    INNER JOIN dim_municipio dm
        ON td.CVE_ENT = dm.cve_ent 
        AND td.CVE_MUN = dm.cve_mun

    INNER JOIN dim_tipo_delito dtd 
        ON td.tipo_delito = dtd.tipo_delito 
        AND td.subtipo_delito = dtd.subtipo_delito
        AND td.modalidad = dtd.modalidad
     
        
    ON DUPLICATE KEY UPDATE
        total = VALUES(total);
    """
    db.execute(query)