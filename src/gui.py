# Importa a biblioteca tkinter
import tkinter as tk

# Importa as funções do módulo main
from main import main, inserir_registro

# Define a função inserir_registro_gui, que é chamada pelo botão Inserir
def inserir_registro_gui():
    # Obtém os valores dos campos da interface gráfica
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    pai = entry_data_nascimento.get()
    mae = entry_mae.get()
    turma = entry_turma.get()
    tipo_ensino = entry_tipo_ensino.get()

    # Chama a função inserir_registro do módulo main para inserir os valores no banco de dados
    inserir_registro(nome, data_nascimento, pai, mae, turma, tipo_ensino)

# Define a função iniciar, que cria a interface gráfica
def iniciar():
    # Cria uma janela
    janela = tk.Tk()

    # Cria os campos de entrada e os rótulos
    label_nome = tk.Label(janela, text="Nome Completo: ")
    entry_nome = tk.Entry(janela)

    label_data_nascimento = tk.Label(janela, text="Data de Nascimento dd/mm/aa: ")
    entry_data_nascimento = tk.Entry(janela)
    
    label_pai = tk.Label(janela, text="Nome do Pai: ")
    entry_pai = tk.Entry(janela)
    
    label_mae = tk.Label(janela, text="Nome da Mãe: ")
    entry_mae = tk.Entry(janela)
    
    label_turma = tk.Label(janela, text="Turma: ")
    entry_turma = tk.Entry(janela)
    
    label_tipo_ensino = tk.Label(janela, text="Tipo de Ensino (infantil, fundamental, medio): ")
    entry_tipo_ensino = tk.Entry(janela)   

    # Cria o botão Inserir
    button_inserir = tk.Button(janela, text="Inserir", command=inserir_registro_gui)

    # Adiciona os campos e rótulos à janela
    label_nome.pack()
    entry_nome.pack()

    label_data_nascimento.pack()
    entry_data_nascimento.pack()
    
    label_pai.pack()
    entry_pai.pack()
    
    label_mae.pack()
    entry_mae.pack()
    
    label_turma.pack()
    entry_turma.pack()
    
    label_tipo_ensino.pack()
    entry_tipo_ensino.pack()

    button_inserir.pack()

    # Inicia a janela
    janela.mainloop()
