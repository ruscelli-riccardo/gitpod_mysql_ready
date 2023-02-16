import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="animali",
)

mycursor = mydb.cursor()    

mycursor.execute("CREATE TABLE Mammiferi(ID int, Nome_proprio varchar(255), Razza varchar(255), Peso int, Età int)")