import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()    

mycursor.execute("CREATE TABLE bommo(name VARCHAR(255), address VARCHAR(255))")