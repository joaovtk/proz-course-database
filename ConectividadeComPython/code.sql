DROP DATABASE BDEscolar;
CREATE DATABASE BDEscolar;
USE BDEscolar;

CREATE TABLE Professores (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    cnpj int NOT NULL, 
    salario float,
    dataNasc date    
);

CREATE TABLE Turmas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeTurma VARCHAR(20) NOT NULL,
    ProfessorID INT,
    FOREIGN KEY (ProfessorID) REFERENCES Professores(ID)
);

CREATE TABLE Alunos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    DataNascimento DATE,
    TurmaID INT,
    FOREIGN KEY (TurmaID) REFERENCES Turmas(ID)
);

CREATE TABLE Disciplinas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeDisciplina VARCHAR(30) NOT NULL,
    TurmaID INT,
    FOREIGN KEY (TurmaID) REFERENCES Turmas(ID)
);

CREATE TABLE UnidadesEscolares (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeUnidade VARCHAR(50) NOT NULL,
    Endereco VARCHAR(100)
);