--Project Querries
--like ; find the planets
SELECT Name FROM Celestial_Body
Where Classification LIKE 'p%';

--aggregate, HAVING and Group by ; find how many CB's per SID and how many do not have a solar system.
SELECT COUNT(CID), Is_part_ofS
FROM Celestial_Body
GROUP BY Is_part_ofS
HAVING COUNT(CID) > 0;

--subquery ; Finds objects discovered after date
SELECT Name, CID FROM Celestial_Body
WHERE CID IN(SELECT CID FROM Discovered WHERE Date_discovered > 17000101);
