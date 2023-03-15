import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()    #crea un oggetto in python che simula un comando in SQL

mycursor.execute("CREATE DATABASE mydatabase")