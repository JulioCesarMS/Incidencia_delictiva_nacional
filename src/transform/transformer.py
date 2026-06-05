import pandas as pd

MESES = {
    'Enero':'01', 'Febrero':'02', 'Marzo':'03', 'Abril':'04', 
    'Mayo':'05', 'Junio':'06','Julio':'07', 'Agosto':'08', 
    'Septiembre':'09', 'Octubre':'10', 'Noviembre':'11', 'Diciembre':'12'
    }


# linpieza y transformación de la base de delitos
def transform_delitos(df):
    # reshape
    dfm = df.melt(
        id_vars=df.columns[:9],
        var_name="Mes",
        value_name="Total"
    )
    # agregación
    dfm = dfm.groupby([
        'Año','Mes','Clave_Ent','Entidad','Cve. Municipio',
        'Municipio','Tipo de delito','Subtipo de delito','Modalidad'
    ], as_index=False).agg({'Total':'sum'})
    
    dfm['Total'] = pd.to_numeric(dfm["Total"], errors="coerce").astype('int')
    # códigos
    dfm['Cve. Municipio'] = [str(x[-3:]) for x in dfm['Cve. Municipio'].astype('str')]
    dfm["CVE_ENT"] = dfm["Clave_Ent"].astype(str).str.zfill(2)
    dfm["CVE_MUN"] = dfm["Cve. Municipio"].astype(str).str.zfill(3)
    dfm["NOM_ENT"] = dfm["Entidad"].astype(str)
    dfm["NOM_MUN"] = dfm["Municipio"].astype(str)
    dfm = dfm.drop(columns=['Entidad','Municipio','Clave_Ent','Cve. Municipio', 'NOM_ENT','NOM_MUN'])
    # meses
    dfm["Mes"] = dfm["Mes"].map(MESES)
    # rename
    dfm  = dfm.rename(columns={
        'Año':'Anio', 
        'Tipo de delito':'Tipo_delito',
        'Subtipo de delito':'Subtipo_delito'})
    
    dfm = dfm[['Anio','Mes','CVE_ENT','CVE_MUN', 'Tipo_delito','Subtipo_delito','Modalidad','Total']]

    return dfm

# limpieza y transformación de base INEGI
def transform_inegi_geo(df):
    
    df = df.copy()
    # limpieza
    df['CVEGEO'] = df['CVEGEO'].str.zfill(9)
    df['CVE_ENT'] = df['CVE_ENT'].str.zfill(2)
    df['CVE_MUN'] = df['CVE_MUN'].str.zfill(3)
    df['CVE_LOC'] = df['CVE_LOC'].str.zfill(4)
    df['LAT_DECIMAL'] = df['LAT_DECIMAL'].astype('float')
    df['LON_DECIMAL'] = df['LON_DECIMAL'].astype('float')
    df['ALTITUD'] = pd.to_numeric(df["ALTITUD"], errors="coerce", downcast='integer')
    df['CVE_CARTA'] = df['CVE_CARTA'].astype('str')
    df['POB_TOTAL'] = pd.to_numeric(df["POB_TOTAL"], errors="coerce", downcast='integer')
    df['POB_MASCULINA'] = pd.to_numeric(df["POB_MASCULINA"], errors="coerce", downcast='integer')
    df['POB_FEMENINA'] = pd.to_numeric(df["POB_FEMENINA"], errors="coerce", downcast='integer')
    df['TOTAL_VIVIENDAS_HABITADAS'] = pd.to_numeric(df["TOTAL DE VIVIENDAS HABITADAS"], errors="coerce", downcast='integer')
    df = df.drop(columns=['TOTAL DE VIVIENDAS HABITADAS'])

    return df