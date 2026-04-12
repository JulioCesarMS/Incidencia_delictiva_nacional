import pandas as pd

# concatena archivos extraidos del zip
def concat_files(path, file_names):
    files = []
    for name in file_names:
        file_path = f"{path}/{name}.xlsx"
        df = pd.read_excel(file_path)
        files.append(df)

    return pd.concat(files, axis=0, ignore_index=True)


# extrae archivo INEGI
def extract_inegi_geo(path, filename):
    
    # nombre de archivo
    dic_convert = {
                'CVEGEO':str,
                'CVE_ENT':str,
                'NOM_ENT': str,
                'CVE_MUN':str,
                'NOM_MUN': str,
                'CVE_LOC':str,
                'NOM_LOC': str,
                'AMBITO': str,
                'LATITUD':str,
                'LONGITUD':str,
                'ALTITUD':str,
                'CVE_CARTA':str
            }
    # path
    
    try: 
        file = f"{path}/{filename}.csv"
        df = pd.read_csv(
            file,
            skiprows=0,
            header=0,
            dtype=dic_convert,
            encoding="latin1",
            low_memory=False
        )
      
    except:
        file = f"{path}/{filename}.xlsx"
        df = pd.read_excel(
            file,
            skiprows=0,
            header=0,
            converters=dic_convert,
            engine="openpyxl"
        )
    
    return df