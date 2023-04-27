class Aluno:
    def __init__(self, nome, idade, pai, mae, tipo_ensino, turma):
        self.nome = nome
        self.idade = idade
        self.pai = pai
        self.mae = mae
        self.tipo_ensino = tipo_ensino
        self.turma = turma
    
    def main():
        print("Bem-vindo ao meu programa!")
    
    alunos = []  # lista vazia para armazenar as instâncias da classe Aluno
    
    while True:
        nome = input("Digite o nome completo do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        pai = input("Digite o nome do pai completo do aluno: ")
        mae = input("Digite o nome da mãe completo do aluno: ")
        tipo_ensino = input("Digite o tipo de ensino do aluno (fundamental, infantil ou medio): ")
        turma = input("Digite o numero da turma do aluno (obs deve ser um valor inteiro): ")
        
        aluno = Aluno(nome, idade, pai, mae, tipo_ensino, turma)  # cria uma instância da classe Aluno
        
        alunos.append(aluno)  # adiciona a instância do aluno à lista de alunos
        
        continuar = input("Deseja continuar adicionando alunos? (s/n) ")
        if continuar.lower() == "n":
            break
    
    for aluno in alunos:  # percorre a lista de alunos e exibe as informações de cada um
        print(aluno.get_info_aluno())


    def get_turma_ensino(self):
        if self.tipo_ensino == "fundamental":
            return f"{self.turma} ano do ensino fundamental"
        elif self.tipo_ensino == "infantil":
            return f"{self.turma} ano da educação infantil"
        elif self.tipo_ensino == "medio":
            return f"{self.turma} ano do ensino médio"
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

