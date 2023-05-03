#Sistema de secretaria escolar que ira realizar registro dos alunos


def main():
    print("Bem-vindo ao meu programa!")
    # Adicione o código adicional do seu programa aqui

    while True:
     #versao 1 do codigo, para fins de teste
        nome_aluno = input("Digite o nome completo do aluno: ")
        #print("O nome completo do aluno é: " + nome_aluno)

        idade_aluno = int(input("Digite a idade do aluno: "))
        #print("A idade do aluno é: " + idade_aluno)

        pai_aluno = input("Digite o nome do pai completo do aluno: ")
        #print("O nome completo do pai do aluno é: " + pai_aluno)

        mae_aluno = input("Digite o nome da mãe completo do aluno: ")
        #print("O nome completo da mãe do aluno é: " + mae_aluno)

        #if e else caso o aluno seja do ensino medio ou do fundamental

        tipo_ensino_aluno = input("Digite o tipo de ensino do aluno (fundamental, infantil ou medio): ")
        turma_aluno = input("Digite o numero da turma do aluno (obs deve ser um valor inteiro): ")

        if tipo_ensino_aluno == "fundamental":
            tipo_ensino_aluno = "ensino fundamental"
            print("A turma do aluno é: " + turma_aluno + " ano do ensino fundamental")

        elif tipo_ensino_aluno == "infantil":
            tipo_ensino_aluno = "educação mnfantil"
            print("A turma do aluno é: " + turma_aluno + " ano da educação infantil")

        elif tipo_ensino_aluno == "medio":
            tipo_ensino_aluno = "ensino médio"
            print("A turma do aluno é: " + turma_aluno + " ano do ensino médio")

        else:
            print("Tipo de ensino inválido")

        
        
        #embaixo, dicionário de registro de alunos para acumulo de dados.
        aluno = {}
        
        aluno["nome_aluno"] = nome_aluno
        aluno["idade_aluno"] = idade_aluno
        aluno["pai_aluno"] = pai_aluno
        aluno["mae_aluno"] = mae_aluno
        aluno["turma_aluno"] = turma_aluno
        aluno["tipo_ensino_aluno"] = tipo_ensino_aluno
    
    # pergunte ao usuário se deseja continuar adicionando alunos
        continuar = input("Deseja continuar adicionando alunos? (s/n) ")
        if continuar.lower() == "n":
            break  # sai do loop se o usuário não deseja mais adicionar alunos

    print(aluno) #codigo esta retornando apenas o valor do ultimo aluno, descobrir pq
        
    

if __name__ == '__main__':
    main()

