import mysql.connector

def main():
    print("Bem-vindo ao meu programa!")

    alunos = []  # lista de alunos

    while True:
        aluno = {}  # dicionário para cada aluno

        nome_aluno = input("Digite o nome completo do aluno: ")
        idade_aluno = int(input("Digite a idade do aluno: "))
        pai_aluno = input("Digite o nome do pai completo do aluno: ")
        mae_aluno = input("Digite o nome da mãe completo do aluno: ")
        tipo_ensino_aluno = input("Digite o tipo de ensino do aluno (fundamental, infantil ou medio): ")
        turma_aluno = input("Digite o numero da turma do aluno (obs deve ser um valor inteiro): ")

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

        aluno["nome_aluno"] = nome_aluno
        aluno["idade_aluno"] = idade_aluno
        aluno["pai_aluno"] = pai_aluno
        aluno["mae_aluno"] = mae_aluno
        aluno["turma_aluno"] = turma_aluno
        aluno["tipo_ensino_aluno"] = tipo_ensino_aluno

        alunos.append(aluno)  # adicione o dicionário do aluno à lista de alunos

        continuar = input("Deseja continuar adicionando alunos? (s/n) ")
        if continuar.lower() == "n":
            break

    for aluno in alunos:  # imprima todos os alunos
        print(aluno)


if __name__ == '__main__':
    main()