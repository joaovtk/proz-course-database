DROP DATABASE BDEscolar;
CREATE DATABASE IF NOT EXISTS BDEscolar;
USE BDEscolar;
CREATE TABLE Professores (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL
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
INSERT INTO Professores VALUES (1, "Gleison");
INSERT INTO Turmas VALUES (1, "Turma Ab1", 1);
INSERT INTO Turmas VALUES (2, "Turma Ac1", 1);
INSERT INTO Alunos VALUES (1, "João Vitor", "2005-10-04", 1);
INSERT INTO Alunos (Nome) VALUES ("Gabriel");


SELECT * FROM Alunos WHERE id = 1;
SELECT TurmaID FROM Alunos WHERE nome = "João Vitor";
SELECT * FROM Alunos;

UPDATE Alunos SET DataNascimento = "2006-05-05" WHERE ID = 2;
UPDATE Alunos SET TurmaID = 2 WHERE id = 2;
UPDATE Alunos SET TurmaID = 2 WHERE id = 1;

DELETE FROM Alunos WHERE id = 2;
	

