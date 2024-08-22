import  tkinter as tk
from tkinter import messagebox
import json
from Gerente import ler, escrever

# Aqui vai ficar a parte de venda dos produtos só adicionando o ID dele como se fosse  Código de barra e salvar em um arquivo
db_produtos = "BancoDeDados/Estoque.json"
vendas = "BancoDeDados/Vendas.json"
class janela_Caixa(tk.Tk):
    def __init__(self):
        super().__init__()
        self.produto = ler(db_produtos)
        self.Caixa()


    def Caixa(self):
        self.geometry("950x600")
        red_frame = tk.Frame(self, bg="#e74c3c", width=2000, height=100)
        red_frame.pack(side="top", expand=True, anchor="n")
        red_frame.pack_propagate(False)
        
        tk.Label(red_frame, text="Mercado Do Bom", font=("Arial", 45), fg="White", bg="#e74c3c").pack()
        
if __name__ == "__main__":
    app = janela_Caixa()
    app.mainloop()