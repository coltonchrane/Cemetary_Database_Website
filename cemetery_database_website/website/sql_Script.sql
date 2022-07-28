-- SQLite
CREATE TABLE Directory(
    id INTEGER NOT NULL,
    section varchar(25) NOT NULL,
    lot int NOT NULL,
    first_name varchar(20),
    middle_name varchar(20),
    last_name varchar(20),
    date_of_birth varchar(15),
    date_of_death varchar(15),
    reserved number(1) ,
    phone_number varchar(20),
    address varchar(50),
    notes varchar(50)
);

INSERT INTO Directory (section,lot,first_name,middle_name,last_name,date_of_birth,reserved,phone_number,address,notes)
VALUES ("South",1,"Colton","Carl","Chrane","1-18-1996",1,"5405555555","123 road","swag");

INSERT INTO Directory (section,lot,first_name,middle_name,last_name,date_of_birth, date_of_death,phone_number,address,notes)
VALUES ("South",3,"Rae","","Liota","5-18-1940", "4-20-2022","5409311364","123 road","swag");

INSERT INTO Directory (section,lot)
VALUES ("South",2);

INSERT INTO Directory (section,lot)
VALUES ("South",4);

INSERT INTO Directory (section,lot)
VALUES ("South",5);

INSERT INTO Directory (section,lot,first_name,middle_name,last_name,date_of_birth, date_of_death,phone_number,address,notes)
VALUES ("South",6,"Oscar","","Maddox","5-18-1940", "4-20-2022","5405555555","123 road","swag");

INSERT INTO Directory (section,lot,first_name,middle_name,last_name,date_of_birth, date_of_death,phone_number,address,notes)
VALUES ("South",7,"Albert","","Wilson","5-18-1940", "4-20-2022","5405555555","123 road","swag");

INSERT INTO Directory (section,lot,first_name,middle_name,last_name,date_of_birth, date_of_death,phone_number,address,notes)
VALUES ("South",9,"Ryan","","Morton","5-18-1940", "4-20-2022","5405555555","123 road","swag");


DROP TABLE Directory;

SELECT * FROM Directory;

SELECT * FROM Directory WHERE last_name

SELECT section AS Section, lot AS Lot , first_name || ' ' || middle_name || ' ' || last_name AS Name, date_of_birth|| ' ~ ' ||date_of_death AS Date, phone_number AS [Phone Number], address AS Address FROM Directory;