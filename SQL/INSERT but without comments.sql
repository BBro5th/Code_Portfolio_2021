INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (1, 'Earth', 59722, 12742, 'Planet', 0, 0, 0, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (2, 'Venus', 48700, 12104, 'Planet', -11.1537, 14.0958, 0.28, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (3, 'Mercury', 3285, 4879, 'Planet', -16.2029, 15.0829, 0.61, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (4, 'Mars', 63900, 6779, 'Planet', 05.4317, 00.5647, 0.52, 1, 0);
INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (5, 'Jupiter', 18980000, 139820, 'Planet', -21.3714, 19.4710, 4.2, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (6, 'Saturn', 5683000, 116460, 'Planet', -21.0117, 19.5759, 8.52, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (7, 'Uranus', 868100, 50724, 'Planet', 13.3750, 02.2154, 18.21, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (8, 'Neptune', 1024000, 49244, 'Planet', -05.4826, 23.1705, 29.09, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_part_of_G)
VALUES (9, 'Pluto', 131, 2377, 'Dwarf-Planet', -22.3836, 19.3928, 34.79, 1, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_Star_of, Is_part_of_G)
VALUES (10, 'The Sun', 19890000000, 1392000, 'Star', -20.4338, 16.0309, 1, 1, 1, 0);

INSERT INTO Solar_System (SID, Sname, SDEC, SRA, DistS)
VALUES (2, "Alpha Centaru", -60.50, 14.39, 276364);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_Star_of, Is_part_of_G)
VALUES (11, 'Alpha Centauri A', 22000000000, 1392000, 'Star', -60.5002, 14.3936, 276174, 2, 2, 0);
INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_Star_of, Is_part_of_G)
VALUES (12, 'Alpha Centauri B', 18140000000, 1392000, 'Star', -60.5015, 14.3905, 276364, 2, 2, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_part_of_G)
VALUES (13, 'Polaris', 108000000000 , 70000000, 'Star', 89.1550, 02.3149, 27190000, 0);

INSERT INTO Celestial_Body (CID, Name, Mass, Diameter, Classification, Declination, Right_Ascension, Distance, Is_Part_ofS, Is_Star_of, Is_part_of_G)
VALUES (14, 'Sirius', 460000000 , 23806854, 'Star', -16.4258, 06.4509, 544569, null, null, 0);


INSERT INTO Researcher (ReID, firstName, lastName)
Values (1, 'Galileo', 'Galilei') ;


INSERT INTO Researcher (ReID, firstName, lastName)
Values (2, 'William', 'Herschel') ;

INSERT INTO Researcher (ReID, firstName, lastName)
Values (3, 'Johann', 'Galle') ;
-- Clyde Tombaugh ; pluto
INSERT INTO Researcher (ReID, firstName, lastName)
Values (4, 'Clyde', 'Tombaugh') ;

INSERT INTO Researcher (ReID, firstName, lastName)
Values (5, 'Robert', 'Innes') ;

INSERT INTO Researcher (ReID, firstName, lastName)
Values (6, 'Friedrich', 'Bessel') ;


INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(2, 1, 1610-01-01);
INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(3, 1, 1610-01-01);
INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(4, 1, 1610-01-01);
INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(5, 1, 1610-01-01);
INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(6, 1, 1610-01-01);

INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(7, 2, 17810313);

INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(8, 3, 18460923);

INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(9, 4, 19300218);

INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(11, 5, 19150101);
INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(12, 5, 19150101);

INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(13, 2, 17800101);

INSERT INTO Discovered (CID, ReID, Date_discovered)
Values(14, 6, 18620131);