import tkinter as tk
from tkinter import messagebox
import json


# Aki vai ficar uma deashboard que dê para adicionar Produtos 
# Controle de Vendas com uma tabela de vendas
# Controle de Estoque q tenha as vendas do porduto e vai avisar a quantidade dele
db_produtos = "BancoDeDados/Estoque.json"

produto = {}

class Janela_Gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.add_produto()

    def Gerente(self):
        self.geometry("950x600")
        self.title("'PODER ILIMITADO MORRA!!'")
        
        frame_dash = tk.Frame(self, width=500 , height=100, bg="Black")
        frame_dash.pack(anchor="w")

        tk.Label(frame_dash, text="Menu do Gerente", bg="Black", fg="white",font=("Arial", 15)).pack(padx=10)

        frame_buttons = tk.Frame(frame_dash, bg="Black")
        frame_buttons.pack(anchor="center", padx= 400, pady=5)
        bt_AddProtudo = tk.Button(frame_buttons, text="Adicionar Items", bg="white", width=20)
        bt_AddProtudo.pack(pady=5)
        bt_Vendas = tk.Button(frame_buttons, text="Vendas", bg="White", width=20)
        bt_Vendas.pack()

    
    def add_produto(self):
        self.geometry("350x580")

        frame_addP = tk.Frame(self, width=200, height=100 )
        frame_addP.pack(padx=10 , pady=10, anchor="w")
        
        tk.Label(frame_addP, text="Nome do Produto:", font=("Arial", 11)).pack( anchor="w")
        entry_nomeP = tk.Entry(frame_addP, width=50, bd=4)
        entry_nomeP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Preço Por Kg", font=("Arial", 11) ).pack(anchor="w")
        entry_preçokg = tk.Entry(frame_addP, width=50, bd=4)
        entry_preçokg.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Quantidade", font=("Arial", 11)).pack(anchor="w")
        entry_quantP = tk.Entry(frame_addP, width=50, bd=4)
        entry_quantP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Lote", font=("Arial", 11)).pack(anchor="w")
        entry_loteP = tk.Entry(frame_addP, width=50, bd=4)
        entry_loteP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Validade", font=("Arial", 11)).pack(anchor="w")
        entry_validadeP = tk.Entry(frame_addP, width=50, bd=4)
        entry_validadeP.pack(pady=10, anchor="w")

        



if __name__ == "__main__":
    root = Janela_Gerente()
    root.mainloop()