DELIMITER //
CREATE TRIGGER 'afterglow'
BEFORE UPDATE ON Celestial_Body
FOR EACH ROW
	IF (new.Is_part_of_G IS NULL) THEN
	SET new.Is_part_of_G = 0;
	END IF//
	DELIMITER ;


