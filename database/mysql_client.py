import mysql.connector
from mysql.connector import Error
import pandas as pd

# Clase 
class MySQLDatabase():
    def __init__(self, database):
        self.host = "localhost"
        self.user = "root"
        self.password = "astro123"
        self.database = database
        self.connection = None

    # método para establecer conexión
    def connect(self):
        host = self.host
        database = self.database
        username = self.user
        password = self.password
        try:
            self.connection = mysql.connector.connect(host=host, 
                                            database=database, 
                                            user=username, 
                                            password=password)
            print("✅ Conexión exitosa")
        except Error as e:
            print("Error: ",e)
            self.connection = None
    
    # método para ejecutar escript, no retorna nada
    def execute(self, query):
        """Ejecuta queries tipo DDL (CREATE, DROP, ALTER)."""
        self.connect()
        conn = self.connection
        cursor = conn.cursor()

        try:
            cursor.execute(query)
            conn.commit()
            print("✅ Query ejecutado correctamente")
        except Error as e:
            print(f"❌ Error ejecutando query: {e}")
        finally:
            cursor.close()
    
    # método para ejecutar un query
    def execute_query(self, query, values=None):
        """Ejecuta una consulta SQL y retorna un DataFrame."""
        self.connect()
        try:
            df = pd.read_sql(query, con=self.connection, params=values)
            return df
        except Error as e:
            print(f"Error ejecutando query: {e}")
            return None

    # método par cargar datos a una tabla
    # def insert_to_db(self, df, tabla, batch_size=5000):
    #     """
    #     Inserta un DataFrame en una tabla MySQL por lotes.
        
    #     Parámetros:
    #         df : pd.DataFrame
    #             DataFrame a insertar.
    #         tabla : str
    #             Nombre de la tabla destino.
    #         batch_size : int
    #             Tamaño del lote para inserciones masivas.
    #     """
    #     # Conexión a MySQL
    #     self.connect()
    #     conn = self.connection
    #     cursor = conn.cursor()
    #     # Reemplazar NaN con None para evitar errores
    #     df = df.where(pd.notnull(df), None)
    #     # Convertir DataFrame a lista de tuplas
    #     values = [tuple(row) for row in df.itertuples(index=False, name=None)]
    #     # Crear placeholders dinámicamente
    #     placeholders = ", ".join(["%s"] * len(df.columns))
    #     cols = ", ".join(df.columns)
    #     insert_query = f"INSERT INTO {tabla} ({cols}) VALUES ({placeholders})"

    #     # Inserción por lotes
    #     for start in range(0, len(values), batch_size):
    #         end = start + batch_size
    #         cursor.executemany(insert_query, values[start:end])
    #         conn.commit()
    #     # Cerrar conexión
    #     cursor.close()
    def insert_to_db(self, df, tabla, batch_size=5000):
        """
        Inserta un DataFrame en MySQL evitando duplicados (UPSERT).
        """

        self.connect()
        conn = self.connection
        cursor = conn.cursor()

        # Reemplazar NaN con None
        df = df.where(pd.notnull(df), None)

        # Convertir DataFrame a lista de tuplas
        values = [tuple(row) for row in df.itertuples(index=False, name=None)]

        # Columnas
        cols = ", ".join(df.columns)

        # Placeholders
        placeholders = ", ".join(["%s"] * len(df.columns))

        # Construir UPDATE dinámico (excluyendo id si existiera)
        update_cols = ", ".join([
            f"{col}=VALUES({col})"
            for col in df.columns
        ])

        # Query tipo UPSERT
        insert_query = f"""
        INSERT INTO {tabla} ({cols})
        VALUES ({placeholders})
        ON DUPLICATE KEY UPDATE
        {update_cols}
        """

        # Inserción por lotes
        for start in range(0, len(values), batch_size):
            end = start + batch_size
            cursor.executemany(insert_query, values[start:end])
            conn.commit()

        cursor.close()


    def close(self):
        """Cierra la conexión."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔒 Conexión cerrada")
            self.connection = None