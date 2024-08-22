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
        self.produto = ler(db_produtos)
        red_frame = tk.Frame(self, bg="#e74c3c", width=1920, height=80)
        red_frame.pack( expand=True, anchor="n")
        red_frame.pack_propagate(False)
        
        tk.Label(red_frame, text="Mercado Do Bom", font=("Arial", 45), fg="White", bg="#e74c3c").pack()

        frame_entry = tk.Frame(self)
        frame_entry.place(x=10, y=150)
        
        tk.Label(frame_entry, text="ID ou o Nome do Item:", font=("Arial", 15)).pack(anchor="w")
        self.ID_compra = tk.Entry(frame_entry, width=50, bd=4)
        self.ID_compra.pack(anchor="w")

        tk.Label(frame_entry, text="Quantidade:", font=("Arial", 15)).pack(anchor="w")
        self.quant_compra = tk.Entry(frame_entry, width=50, bd=4)
        self.quant_compra.pack(anchor="w")

        bt_carrinho = tk.Button(frame_entry, text="Adicionar", command=self.adicionar_carrinho, width=15, bg="#d4ac0d")
        bt_carrinho.pack(side="top", pady=10)

        frame_tree = tk.Frame(self, bg="red", width=100, height=100)
        frame_tree.pack()

    def adicionar_carrinho(self):
        id_nome = self.ID_compra.get()
        quant_item = int(self.quant_compra.get())
        dict_produto = self.produto

        if "" in (id_nome, quant_item):
            messagebox.showerror("ERRO", "Preenchar os Espaços para continua a Compra")
        else:
            for index in dict_produto:
                if dict_produto[id_nome]:
                    valor_estoque = int(dict_produto[id_nome]["Quantidade"]) - quant_item
                    dict_produto[id_nome]["Quantidade"] = valor_estoque
                    escrever(db_produtos, self.produto)
                    preço_string = dict_produto[id_nome]["Preço"]
                    preço_float = float(preço_string.replace("R$", ""))
                    add_carrinho = float(preço_float * quant_item)
                    self.carrinho[len(self.carrinho)]

            else:
                messagebox.showerror("ERRO", "Verifique o ID")
                

if __name__ == "__main__":
    app = janela_Caixa()
    app.mainloop()