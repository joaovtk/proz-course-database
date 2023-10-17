import mysql.connector as connect
from dotenv import dotenv_values

env = dotenv_values(".env")


def GetRegister():
    print("Forneça seu cadastro\nNome e Senha")
    register = {
        "name": "",
        "password": ""
    }

    register["name"] = str(input("Digite seu nome: "))
    register["password"] = str(input("Digite sua senha de acesso: "))

    return register

userProps = "(id int(4) AUTO_INCREMENT PRIMARY KEY, name varchar(30), password varchar(30))"
taskProps = "(id int(4) AUTO_INCREMENT PRIMARY KEY, name varchar(20), desc varchar(50), userId INT, FOREIGN KEY (userId) REFERENCES users(id)"

con = connect.MySQLConnection(user="root", password=f'{env["DB_PASS"]}', database="todo")
con.e(f"CREATE TABLE IF NOT EXISTS users {userProps}")
con._execute_query(f"CREATE TABLE IF NOT EXISTS tasks {taskProps}")
