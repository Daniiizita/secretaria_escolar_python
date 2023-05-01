# codigo que ira gerar o acesso e controle do banco de dados pelo proprio python
# 1 - Controle do Banco de dados
"""Comandos que podem vir a ser uteis para manuseio do SQL:
Alguns comandos úteis para você usar no futuro incluem:
    mycursor.execute(sql): Executa uma consulta SQL especificada pela string sql.
    mycursor.fetchall(): Retorna todos os resultados da consulta como uma lista de tuplas.
    mycursor.fetchone(): Retorna o próximo resultado da consulta como uma tupla.
    mycursor.fetchmany(size): Retorna os próximos size resultados da consulta como uma lista de tuplas.
    mycursor.lastrowid: Retorna o ID da última linha inserida na tabela.
"""

import mysql.connector

# Crie uma conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    password="root",
    database="secretaria_escolar",
)

# Crie um cursor para executar consultas SQL
mycursor = mydb.cursor()

# Verifique se a tabela alunos já existe
mycursor.execute("SHOW TABLES LIKE 'alunos'")
resultado = mycursor.fetchone()

# Criação da tabela alunos (se ainda não existir)
if resultado is None:
    mycursor.execute("CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), idade INT, pai VARCHAR(255), mae VARCHAR(255), turma VARCHAR(255), tipo_ensino VARCHAR(255))")
    print("Tabela alunos criada com sucesso!")
else:
    print("A tabela alunos já existe.")

# Fechamento da conexão com o banco de dados
mydb.close()