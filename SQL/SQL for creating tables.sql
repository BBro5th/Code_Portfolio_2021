--DONE BY Bradley B

CREATE TABLE Galaxy (
GID int NOT NULL,
Gname VarChar(225),
GDEC double(12,5), 
GRA double(12,5),
DistG double(12,12),
PRIMARY KEY (GID)
);
CREATE TABLE Solar_System (
SID int NOT NULL,
Sname Varchar(225),
SDEC double(12,5),
SRA double(12,5),
DistS double(12,12),
Is_part_of int, 
PRIMARY KEY (SID),
FOREIGN KEY (Is_part_of) REFERENCES Galaxy(GID)
);
CREATE TABLE Celestial_Body(
CID int NOT NULL,
Name VarChar (225),
Mass BIGINT(225),
Diameter int,
Classification VarChar (225),
Declination double(12,5),
Right_Ascension double(12,5), 
Distance BIGINT(225),
Is_part_ofS int,
Is_Star_of int,
Is_part_of_G int,
PRIMARY KEY (CID),
FOREIGN KEY (Is_part_ofS) REFERENCES Solar_System(SID),
FOREIGN KEY (Is_Star_of) REFERENCES Solar_System(SID),
FOREIGN KEY (Is_part_of_G) REFERENCES Galaxy(GID)
);
CREATE TABLE Researcher(
ReID int NOT NULL,
firstName VarChar(225),
lastName VarChar(225),
PRIMARY KEY (ReID)
);
Create TABLE Discovered(
CID int, 
ReID int,
Date_discovered DATE,
FOREIGN KEY (CID) REFERENCES Celestial_Body(CID),
FOREIGN KEY (ReID) REFERENCES Researcher(ReID)
);

