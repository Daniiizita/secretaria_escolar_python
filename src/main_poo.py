# Refatoração do código original para a Orientação a Objetos, data_versão: 27-04-2023_10-07

class Aluno:
    def __init__(self, nome, idade, pai, mae, tipo_ensino, turma):
        self.nome = nome
        self.idade = idade
        self.pai = pai
        self.mae = mae
        self.tipo_ensino = tipo_ensino
        self.turma = turma
    
    def get_turma_ensino(self):
        if self.tipo_ensino == "fundamental":
            return f"{self.turma}º ano do ensino fundamental"
        elif self.tipo_ensino == "infantil":
            return f"{self.turma}º ano da educação infantil"
        elif self.tipo_ensino == "medio":
            return f"{self.turma}º ano do ensino médio"
        else:
            return "Tipo de ensino inválido"
        
    def get_info_aluno(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "pai": self.pai,
            "mae": self.mae,
            "tipo_ensino": self.tipo_ensino,
            "turma": self.get_turma_ensino(),
        }


def main():
    print("Bem-vindo ao meu programa!")
    
    alunos = [] # cria uma lista vazia fora do loop para armazenar todos os objetos da classe Aluno

    while True:
        # coleta informações do aluno a ser criado
        nome = input("Digite o nome completo do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        pai = input("Digite o nome do pai completo do aluno: ")
        mae = input("Digite o nome da mãe completo do aluno: ")
        tipo_ensino = input("Digite o tipo de ensino do aluno (fundamental, infantil ou medio): ")
        turma = input("Digite o numero da turma do aluno (obs deve ser um valor inteiro): ")
        
        # cria um objeto Aluno com as informações coletadas e adiciona o objeto à lista de alunos
        aluno = Aluno(nome, idade, pai, mae, tipo_ensino, turma)  # cria uma instância da classe Aluno
        alunos.append(aluno)

        #if da turma do aluno
        if aluno.tipo_ensino == "fundamental":
            print(f"{aluno.nome} tem {aluno.idade} anos e está no {aluno.turma}º ano do ensino fundamental.")
        elif aluno.tipo_ensino == "infantil":
            print(f"{aluno.nome} tem {aluno.idade} anos e está no {aluno.turma}º ano da educação infantil.")
        elif aluno.tipo_ensino == "medio":
            print(f"{aluno.nome} tem {aluno.idade} anos e está no {aluno.turma}º ano do ensino médio.")
        else:
            print("Tipo de ensino inválido.")
        
        continuar = input("Deseja continuar adicionando alunos? (s/n) ")
        if continuar.lower() == "n":
            break
    
    # exibe informações dos alunos criados
    for aluno in alunos:
        print(aluno.get_info_aluno())

if __name__ == '__main__':
    main()