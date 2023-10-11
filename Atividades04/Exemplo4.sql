CREATE TABLE IF NOT EXISTS Livros (
	BookCode INT UNIQUE NOT NULL,
    BookName VARCHAR(50) NOT NULL,
    Author INT NOT NULL,
    Editor INT NOT NULL,
    DataPub DATE,
    Genre INT NOT NULL,
    Price FLOAT, 
    FOREIGN KEY (Author) REFERENCES Autores (AuthorCode) ON DELETE CASCADE,
    PRIMARY KEY (BookCOde)
);