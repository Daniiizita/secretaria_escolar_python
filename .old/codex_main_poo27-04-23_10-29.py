"""
Exemplo de código feito usando OpenAI Codex para refatoração ou geração de códigos
"""

class SecretariaEscolar:
    def __init__(self):
        self.aluno = dict()
        self.continuar = None
        
    def main(self):
        print("Bem-vindo ao meu programa!")
        # Adicione o código adicional do seu programa aqui

        while True:
            self.nome_aluno = input("Digite o nome completo do aluno: ")
            #print("O nome completo do aluno é: " + nome_aluno)

            self.idade_aluno = int(input("Digite a idade do aluno: "))
            #print("A idade do aluno é: " + idade_aluno)

            self.pai_aluno = input("Digite o nome do pai completo do aluno: ")
            #print("O nome completo do pai do aluno é: " + pai_aluno)

            self.mae_aluno = input("Digite o nome da mãe completo do aluno: ")
            #print("O nome completo da mãe do aluno é: " + mae_aluno)

            #if e else caso o aluno seja do ensino medio ou do fundamental

            self.tipo_ensino_aluno = input("Digite o tipo de ensino do aluno (fundamental, infantil ou medio): ")
            self.turma_aluno = input("Digite o numero da turma do aluno (obs deve ser um valor inteiro): ")

            if self.tipo_ensino_aluno == "fundamental":
                self.tipo_ensino_aluno = "ensino fundamental"
                print("A turma do aluno é: " + self.turma_aluno + " ano do ensino fundamental")

            elif self.tipo_ensino_aluno == "infantil":
                self.tipo_ensino_aluno = "educação mnfantil"
                print("A turma do aluno é: " + self.turma_aluno + " ano da educação infantil")

            elif self.tipo_ensino_aluno == "medio":
                self.tipo_ensino_aluno = "ensino médio"
                print("A turma do aluno é: " + self.turma_aluno + " ano do ensino médio")

            else:
                print("Tipo de ensino inválido")
        
        #embaixo, dicionário de registro de alunos para acumulo de dados.
            self.aluno["nome_aluno"] = self.nome_aluno
            self.aluno["idade_aluno"] = self.idade_aluno
            self.aluno["pai_aluno"] = self.pai_aluno
            self.aluno["mae_aluno"] = self.mae_aluno
            self.aluno["turma_aluno"] = self.turma_aluno
            self.aluno["tipo_ensino_aluno"] = self.tipo_ensino_aluno
    
    # pergunte ao usuário se deseja continuar adicionando alunos
            self.continuar = input("Deseja continuar adicionando alunos? (s/n) ")
            if self.continuar.lower() == "n":
                break  # sai do loop se o usuário não deseja mais adicionar alunos

    def registro(self):
        print(self.aluno) #codigo esta retornando apenas o valor do ultimo aluno, descobrir pq

if __name__ == '__main__':
    secretaria = SecretariaEscolar()
    secretaria.main()
    secretaria.registro()