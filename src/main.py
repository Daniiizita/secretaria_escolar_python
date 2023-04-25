#Sistema de secretaria escolar que ira realizar registro dos alunos


def main():
    print("Bem-vindo ao meu programa!")
    # Adicione o código adicional do seu programa aqui

    while True:
     #versao 1 do codigo, para fins de teste
        nome_aluno = input("Digite o nome completo do aluno: ")
        print("O nome completo do aluno é: " + nome_aluno)

        idade_aluno = input("Digite o nome completo do aluno: ")
        print("O nome completo do aluno é: " + nome_aluno)

        pai_aluno = input("Digite o nome completo do aluno: ")
        print("O nome completo do aluno é: " + nome_aluno)

        mae_aluno = input("Digite o nome completo do aluno: ")
        print("O nome completo do aluno é: " + nome_aluno)
    
    # pergunte ao usuário se deseja continuar adicionando alunos
        continuar = input("Deseja continuar adicionando alunos? (s/n) ")
        if continuar.lower() == "n":
            break  # sai do loop se o usuário não deseja mais adicionar alunos

    

if __name__ == '__main__':
    main()

