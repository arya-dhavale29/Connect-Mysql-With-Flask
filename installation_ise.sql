CREATE DATABASE Animal_05;
CREATE TABLE Animal_05.animals 
(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    animal_type varchar(50) NOT NULL,
    animal_breed varchar(50) NOT NULL,
    age integer NOT NULL,
    email varchar(50) NOT NULL,
    phone varchar(50) NOT NULL
);
