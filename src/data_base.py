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

# Execute uma consulta SQL
mycursor.execute("SELECT * FROM alunos")

# Obtenha os resultados da consulta
resultados = mycursor.fetchall

# Imprima os resultados
for resultado in resultados:
    print(resultado)
