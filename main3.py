import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (ID, Nome_proprio, Razza, Peso, Età) VALUES (%s, %s, %s, %s, %s)"
val = [
  ( 1, 'Bommo', 'Capra', 50, 19),
  ( 2, 'Pippo', 'Lupo', 34, 5),
  ( 3, 'Pluto', 'Leone', 100, 34),
  ( 4, 'Luca', 'Elefante', 500, 2),
  ( 5, 'Gianni', 'Scimmia', 20, 98)
]

mycursor.executemany(sql, val)

mydb.commit()

