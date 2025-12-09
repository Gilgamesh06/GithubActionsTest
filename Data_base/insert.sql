
-- Insertar datos en la tabla estudiantes
INSERT INTO "ESTUDIANTE" ("NOMBRE", "APELLIDO", "EDAD", "GENERO") VALUES
('Juan', 'Perez', 20, 'Masculino'),
('Maria', 'Garcia', 22, 'Femenino'),
('Pedro', 'Rodriguez', 21, 'Masculino'),
('Ana', 'Martinez', 23, 'Femenino'),
('Luis', 'Gonzalez', 24, 'Masculino');

-- Insertar datos en la tabla asignaturas
INSERT INTO "ASIGNATURA" ("NOMBRE", "CREDITOS") VALUES
('Matematicas', 4),
('Fisica', 3),
('Quimica', 3),
('Historia', 2),
('Geografia', 2);

-- Insertar datos en la tabla profesores
INSERT INTO "PROFESOR" ("NOMBRE", "APELLIDO", "EDAD", "GENERO") VALUES
('Juan', 'Perez', 20, 'Masculino'),
('Maria', 'Garcia', 22, 'Femenino'),
('Pedro', 'Rodriguez', 21, 'Masculino'),
('Ana', 'Martinez', 23, 'Femenino'),
('Luis', 'Gonzalez', 24, 'Masculino');

-- Insertar datos en la tabla cursos
INSERT INTO "CURSO" ("NOMBRE", "FID_ASIGNATURA", "FID_PROFESOR") VALUES
('Matematicas', 1, 1),
('Fisica', 2, 2),
('Quimica', 3, 3),
('Historia', 4, 4),
('Geografia', 5, 5);

-- Insertar datos en la tabla matriculas
INSERT INTO "MATRICULA" ("FID_ESTUDIANTE", "FID_CURSO", "FECHA") VALUES
(1, 1, '2025-12-01'),
(2, 2, '2025-12-02'),
(3, 3, '2025-12-03'),
(4, 4, '2025-12-04'),
(5, 5, '2025-12-05');
