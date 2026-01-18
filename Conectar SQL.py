"""
MySQL Database Connection and Data Management Module.

This module provides functionality to connect to a MySQL database (Sakila sample database),
extract data using pandas, and export DataFrames back to the database using SQLAlchemy.

Required packages:
    - mysql-connector-python
    - pandas
    - sqlalchemy
"""

# pip install mysql-connector-python

import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# Información de la base de datos
config = {
    'user': 'root',
    'password': 'ipsdatax',
    'host': 'localhost',
    'database': 'sakila',
    'raise_on_warnings': True
}


# Conexión
connection = mysql.connector.connect(**config) #** es para desempaquetar el diccionario y pasarlo como argumento a la función


# 1 Extraer información (con pandas)
CONSULTA = "SELECT * FROM actor"
df = pd.read_sql_query(CONSULTA, connection)



# 2 Exportar DataFrame a MySQL (con pandas)
## Nombre de la tabla
engine = create_engine("mysql+mysqlconnector://root:ipsdatax@localhost/sakila")
df.to_sql('actors_2', con=engine, if_exists='append', index=False)
