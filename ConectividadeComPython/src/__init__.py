import mysql.connector
import os 
import platform
import time

def clear():
    # limpando a tela usando o respectivo comando nos sistemas
    if platform.system() == "Windows":
        time.sleep(0.5)
        os.system("cls")
    elif platform.system() == "Linux":
        time.sleep(0.5)
        os.system("clear")

def pause():
    if platform.system() == "Windows":
        os.system("pause")
    elif platform.system() == "Linux":
        os.system("read -rsp $'Press enter to continue...\n'")

# Conectando ao banco de dados
db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="aluno",
    database="BDEscolar"
)

# Criando um cursor
cursor = db.cursor(buffered=True)

# Classe Aluno
class Aluno:
    def __init__(self, nome, data_nascimento, turma_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.turma_id = turma_id

    def salvar(self):
        sql = f"SELECT * FROM Turmas WHERE ID = {self.turma_id}"
        data = cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("Crie uma turma primeiro por favor")
            pause()
        else:
            query = "INSERT INTO Alunos (Nome, DataNascimento, TurmaID) VALUES (%s, %s, %s)"
            values = (self.nome, self.data_nascimento, self.turma_id)
            cursor.execute(query, values)
            db.commit()
            print("Aluno cadastrado com sucesso!")

    @staticmethod
    def listar():
        query = "SELECT * FROM Alunos"
        data = cursor.execute(query)
        data = cursor.fetchall()
        if not data:
            print("Não há nenhum aluno cadastrado digite 1 para cadastrar um aluno")
        else:
            for aluno in data:
                print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Data de Nascimento: {aluno[2]}, Turma ID: {aluno[3]}")

    @staticmethod
    def alterar(aluno_id, novo_nome):
        query = "UPDATE Alunos SET Nome = %s WHERE ID = %s"
        values = (novo_nome, aluno_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(aluno_id):
        query = "DELETE FROM Alunos WHERE ID = %s"
        values = (aluno_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Professor (semelhante ao Aluno)
class Professor:
    def __init__(self, nome, cnpj, salario, data):
        self.nome = nome
        self.cnpj = cnpj
        self.salario = salario
        self.data = data

    def salvar(self):
        query = "INSERT INTO Professores (Nome, cnpj, salario, dataNasc) VALUES (%s, %s, %s, %s)"
        values = (self.nome, self.cnpj, self.salario, self.data)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM Professores"
        cursor.execute(query)
        result = cursor.fetchall()
        for professor in result:
            print(f"ID: {professor[0]}, Nome: {professor[1]}, Cnpj: {professor[2]}, Salario: {professor[3]}, Data de Nascimento: {professor[4]}")

    @staticmethod
    def alterar(professor_id, novo_nome):
        query = "UPDATE Professores SET Nome = %s WHERE ID = %s"
        values = (novo_nome, professor_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(professor_id):
        query = "DELETE FROM Professores WHERE ID = %s"
        values = (professor_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Turma (semelhante ao Aluno)
class Turma:
    def __init__(self, nome_turma, professor_id):
        self.nome_turma = nome_turma
        self.professor_id = professor_id

    def salvar(self):
        query = "INSERT INTO Turmas (NomeTurma, ProfessorID) VALUES (%s, %s)"
        sql = "SELECT * FROM Professores"
        cursor.execute(sql)

        data = cursor.fetchall()

        if not data:
            print("Crie um professor por favor")
            pause()
        else:
            values = (self.nome_turma, self.professor_id)
            cursor.execute(query, values)
            db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM Turmas"
        cursor.execute(query)
        result = cursor.fetchall()
        for turma in result:
            print(f"ID: {turma[0]}, Nome da Turma: {turma[1]}, Professor ID: {turma[2]}")

    @staticmethod
    def alterar(turma_id, novo_nome):
        query = "UPDATE Turmas SET NomeTurma = %s WHERE ID = %s"
        values = (novo_nome, turma_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(turma_id):
        query = "DELETE FROM Turmas WHERE ID = %s"
        values = (turma_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Disciplina (semelhante ao Aluno)
class Disciplina:
    def __init__(self, nome_disciplina, turma_id):
        self.nome_disciplina = nome_disciplina
        self.turma_id = turma_id

    def salvar(self):
        query = "INSERT INTO Disciplinas (NomeDisciplina, TurmaID) VALUES (%s, %s)"
        values = (self.nome_disciplina, self.turma_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM Disciplinas"
        cursor.execute(query)
        result = cursor.fetchall()
        for disciplina in result:
            print(f"ID: {disciplina[0]}, Nome da Disciplina: {disciplina[1]}, Turma ID: {disciplina[2]}")

    @staticmethod
    def alterar(disciplina_id, novo_nome):
        query = "UPDATE Disciplinas SET NomeDisciplina = %s WHERE ID = %s"
        values = (novo_nome, disciplina_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(disciplina_id):
        query = "DELETE FROM Disciplinas WHERE ID = %s"
        values = (disciplina_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Unidade Escolar (semelhante ao Aluno)
class UnidadeEscolar:
    def __init__(self, nome_unidade, cep):
        self.nome_unidade = nome_unidade
        self.cep = cep

    def salvar(self):
        query = "INSERT INTO UnidadesEscolares (NomeUnidade, Cep) VALUES (%s, %s)"
        values = (self.nome_unidade, self.cep)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM UnidadesEscolares"
        cursor.execute(query)
        result = cursor.fetchall()
        for unidade in result:
            print(f"ID: {unidade[0]}, Nome da Unidade: {unidade[1]}, CEP: {unidade[2]}")

    @staticmethod
    def alterar(unidade_id, novo_nome, novo_cep):
        query = "UPDATE UnidadesEscolares SET NomeUnidade = %s, Cep = %s WHERE ID = %s"
        values = (novo_nome, novo_cep, unidade_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(unidade_id):
        query = "DELETE FROM UnidadesEscolares WHERE ID = %s"
        values = (unidade_id,)
        cursor.execute(query, values)
        db.commit()
