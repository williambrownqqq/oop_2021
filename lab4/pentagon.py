import mysql.connector
from pentagonConfig import host, user, password, dataBaseName


""" connection to pentagon database """

connectort = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=dataBaseName,
)
MyCursor = connectort.cursor()
