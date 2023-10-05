import sqlite3
from datetime import datetime
import random

class User():
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year
        self.con = sqlite3.Connection("Extra/main.db")
        self.cursor = self.con.cursor()
    
    def checkAge(self):
        if (int(datetime.now().year) - int(self.year)) < 16:
            print("Você não está apto para logar")
    def RegisterUser(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INT AUTO_INCREMENT, name STRING, year INT, ammount FLOAT)")
        data = self.cursor.execute(f"SELECT * FROM Users WHERE name = '{self.name}'")
        data = data.fetchone()
        if not data:
            self.cursor.execute(f"INSERT INTO Users VALUES (0, '{self.name}', {self.year}, {random.randint(0, 1000)})")
        else:
            print("Esse usuario já existe")
    def FetchDatabase(self):
        data = self.cursor.execute("SELECT * FROM Users")
        print(data.fetchall())
        
name = str(input("Digite seu nome: "))
year = str(input("Digite o ano da sua data de nascimento: "))
user = User(name, year)
user.checkAge()
user.RegisterUser()
user.FetchDatabase()
user.con.commit()

        
    