import tkinter as tk
from tkinter import messagebox
import json


# Aki vai ficar uma deashboard que dê para adicionar Produtos 
# Controle de Vendas com uma tabela de vendas
# Controle de Estoque q tenha as vendas do porduto e vai avisar a quantidade dele
db_produtos = "BancoDeDados/Estoque.json"

class Janela_Gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Gerente()

    def Gerente(self):
        self.geometry("950x600")
        
        frame_dash = tk.Frame(self, width=200 , height=600, bg="Black")
        frame_dash.grid(column=0 ,row=0, rowspan=7, columnspan=2)

        tk.Label(frame_dash, text="Menu do Gerente", bg="white", font=("Arial", 11)).pack(padx=10, pady=15)
        bt_AddProtudo = tk.Button(frame_dash, text="Adicionar Items", bg="white")
        bt_AddProtudo.pack(padx=10 , pady=200)
        
        



if __name__ == "__main__":
    root = Janela_Gerente()
    root.mainloop()