# Banco de Dados Escolar
<p>Esse codigo foi criado por enzoea link do perfil do github <a href="https://github.com/enzoea/AtividadesPython">Repositorio Original</a></p>

# Como executar
<p>Primeiramente você deve executar o code.sql no seu workebench ou mysql command line</p>

``` 
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
        Cep VARCHAR(50) NOT NULL
    );
    -- Data e salario aleatorios dados em geral aleatorios
    INSERT INTO Professores VALUES(1, "Enzo", 123456, 1.421, "1988-05-05");
    INSERT INTO Turmas VALUES(1, "TurmaAB", 1);
    INSERT INTO Alunos VALUES (1, "Vitor", "2005-10-04", 1);

```
<p>Para você executar você deve utilizar os comandos abaixos</p>

## Windows 
```
    git clone https://github.com/joaovtk/proz-course-database 
    cd proz-course-database\ConectividadeComPython
    pip install -r requirements.txt
    python main.py
```

## Linux 

```
    git clone https://github.com/joaovtk/proz-course-database 
    cd proz-course-database/ConectividadeComPython
    pip install -r requirements.txt
    python main.py
```

### Alerta para alunos do curso 
<p>Por causa de um erro do suporte tecnico o pip não está no path então você deve usar o seguinte codigo abaixo</p>
<p>Comando apenas para usuario de windows e com a instalação padrão sem o path</p>

```
    git clone https://github.com/joaovtk/proz-course-database 
    cd proz-course-database\ConectividadeComPython
    C:\Users\Aluno\AppData\Local\Programs\Python\Python311\Scripts\pip install -r requirements.txt
    python main.py
```