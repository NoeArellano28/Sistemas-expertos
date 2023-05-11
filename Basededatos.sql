CREATE DATABASE Base;
USE Base;
CREATE TABLE deportes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255),
  pelota BOOLEAN,
  equipo BOOLEAN,
  campo BOOLEAN,
  agua BOOLEAN,
  invierno BOOLEAN
);

INSERT INTO deportes (nombre, pelota, equipo, campo, agua, invierno)
VALUES
  ("Futbol", true, true, true, false, false),
  ("Natacion", false, false, false, true, false),
  ("Esqui", false, false, false, false, true),
  ("Golf", false, false, true, false, false),
  ("Hockey", false, true, false, false, true),
  ("Ciclismo", false, false, false, false, false),
  ("WaterPolo", true, true, false, true, false),
  ("Tenis", True, False, True, False, False);


SELECT DATABASE();
SELECT * FROM deportes