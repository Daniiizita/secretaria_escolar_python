CREATE TABLE alunos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255),
  idade INT,
  pai VARCHAR(255),
  mae VARCHAR(255),
  turma VARCHAR(255),
  tipo_ensino VARCHAR(255)
);

select * from alunos;