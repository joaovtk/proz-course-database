CREATe TABLE IF NOT EXISTS Generos (
	GenreCode INTEGER,
    GenreName VARCHAR(40) UNIQUE NOT NULL,
    PRIMARY KEY (GenreCode)
);