import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="animali"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (ID, Nome_proprio, Razza, Peso, Età) VALUES (%s, %s, %s, %s, %s)"

x = 1

for x in range(5):


    ID = input("ID: ") 
    Nome_proprio = input("Nome_proprio: ") 
    Razza = input("Razza: ") 
    Peso = input("Peso: ") 
    Età = input("Età: ")
    val = (ID, Nome_proprio, Razza, Peso, Età)
    mycursor.execute(sql, val)


mydb.commit()

