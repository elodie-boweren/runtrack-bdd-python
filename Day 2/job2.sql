CREATE TABLE etage(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

CREATE TABLE salle(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT
);

 INSERT INTO etage(nom, numero, superficie) VALUES
    ('RDC',0,500),
    ('R+1',1,500);

INSERT INTO salle(nom, id_etage, capacite) VALUES ('Lounge', 1, 100), ('Studio Son', 1, 5), ('Broadcasting', 2, 50), ('Bocal Peda', 2, 4), ('Coworking', 2, 80), ('Studio Video', 2, 5);

CREATE TABLE employee(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(150),
    prenom VARCHAR(150),
    salaire FLOAT,
    id_service INT
    );