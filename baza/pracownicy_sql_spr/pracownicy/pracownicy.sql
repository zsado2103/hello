DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy (
    id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    kod INTEGER,
    miasto_z TEXT,
    ulica TEXT,
    data_u DATE,
    miasto_u TEXT
    
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska (
    id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT    
    
);

DROP TABLE IF EXISTS place;
CREATE TABLE place (
    id_p INTEGER,
    id_s INTEGER,
    placa DECIMAL,
    data_z  DATE,
    
    FOREIGN KEY (id_p) REFERENCES kontakty(id_pracownika)
    FOREIGN KEY (id_s) REFERENCES stanowiska(id_stanowiska)
);

DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty (
    id_pracownika INTEGER,
    typ_k BOOLEAN,
    kontakt INTEGER,
    uwagi TEXT,
    
    FOREIGN KEY (id_pracownika) REFERENCES pracownicy(id_pracownika) ON DELETE NO ACTION ON UPDATE NO ACTION
);
