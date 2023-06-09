import mysql.connector
from datetime import datetime
#import gui

# Chama a função iniciar() do módulo da interface gráfica
#gui.iniciar()

def main():
    
    def inserir_registro ():
        print("Bem-vindo ao sistema de Registro de Alunos!")
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port="3306",
        password="root",
        database="python_secretaria_escolar"
        )
        
        mycursor = mydb.cursor()
        
        alunos = []  # lista de alunos

        while True:
            aluno = {}  # dicionário para cada aluno

            nome_aluno = input("Digite o nome completo do aluno: ")
            data_nascimento_aluno = input("Digite a data de nascimento do aluno no formato dd/mm/aaaa,(exemplo: 01/01/2000): ")
            pai_aluno = input("Digite o nome do pai completo do aluno: ")
            mae_aluno = input("Digite o nome da mãe completo do aluno: ")
            tipo_ensino_aluno = input("Digite o tipo de ensino do aluno (fundamental, infantil ou medio): ")
            turma_aluno = input("Digite o numero da turma do aluno (obs deve ser um valor inteiro): ")
        
            # Converte a string em um objeto datetime
            data_nascimento = datetime.strptime(data_nascimento_aluno, "%d/%m/%Y")

            # Formata a data no formato do SQL (aaaa-mm-dd)
            data_nascimento_aluno = data_nascimento.strftime("%Y-%m-%d")

            if tipo_ensino_aluno == "fundamental":
                tipo_ensino_aluno = "ensino fundamental"
                print("A turma do aluno é: " + turma_aluno + " ano do ensino fundamental")

            elif tipo_ensino_aluno == "infantil":
                tipo_ensino_aluno = "educação infantil"
                print("A turma do aluno é: " + turma_aluno + " ano da educação infantil")

            elif tipo_ensino_aluno == "medio":
                tipo_ensino_aluno = "ensino médio"
                print("A turma do aluno é: " + turma_aluno + " ano do ensino médio")

            else:
                print("Tipo de ensino inválido")
            
            
            #dicionario deve ficar antes da integracao final com banco de dados
            aluno["nome"] = nome_aluno
            aluno["data_nascimento"] = data_nascimento_aluno
            aluno["pai"] = pai_aluno
            aluno["mae"] = mae_aluno
            aluno["turma"] = turma_aluno
            aluno["tipo_ensino"] = tipo_ensino_aluno

            alunos.append(aluno)  # adicione o dicionário do aluno à lista de alunos

            
            # inserindo dados na tabela alunos
            sql = "INSERT INTO alunos (nome, data_nascimento, pai, mae, turma, tipo_ensino) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (aluno["nome"], aluno["data_nascimento"], aluno["pai"], aluno["mae"], aluno["turma"], aluno["tipo_ensino"])
            mycursor.execute(sql, val)

            # fazendo a transação
            mydb.commit()

            # imprimindo a mensagem de confirmação
            print(mycursor.rowcount, "registro inserido.")
        
            #terminar de arrumar codigo, ao inserir nao adicionar aluno o banco de dados não salva os registros inseridos.
            continuar = input("Deseja continuar adicionando alunos? (s/n) ")
            if continuar.lower() == "n":
                break
            
        
            #mostrando select com os valores
            mycursor.execute("SELECT * FROM alunos")
            result = mycursor.fetchall()
            for row in result:
                print(row)
        

        for aluno in alunos:  # imprima todos os alunos
            print(aluno)
            
            inserir_registro()


if __name__ == '__main__':
    main()
    