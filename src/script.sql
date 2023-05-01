# Não executar o CREATE TABLE abaixo, ele serve apenas de precaução caso
# o código data_base.py não funcione corretamente.

CREATE TABLE alunos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255),
  data_nascimento DATE,
  pai VARCHAR(255),
  mae VARCHAR(255),
  turma VARCHAR(255),
  tipo_ensino VARCHAR(255)
);

select * from alunos;

# DROP TABLE alunos;