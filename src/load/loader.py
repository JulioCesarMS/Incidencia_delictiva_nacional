

# carga a mysql
def load_to_mysql(db, df, table_name, batch_size=5000):
    db.insert_to_db(df, tabla=table_name, batch_size=batch_size)