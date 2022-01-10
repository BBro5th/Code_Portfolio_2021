--Trigger
CREATE TRIGGER afterglow
BEFORE INSERT
ON Celestial_Body
FOR EACH ROW

BEGIN

IF NEW.CID EXISTS (SELECT CID FROM Celestial_Body)
THEN 
DELETE FROM Celestial_Body WHERE OLD.Celestial_Body 
INSERT INTO Celestial_Body
SELECT * FROM inserted
END IF;


-- An example case

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_part_of_G)
VALUES (13, 'Polaris', 108100000000 , 70000000, 'Star', 89.1550, 02.3149, 27190000, 0);