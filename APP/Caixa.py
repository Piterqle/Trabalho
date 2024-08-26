import  tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from Gerente import ler, escrever

# Aqui vai ficar a parte de venda dos produtos só adicionando o ID dele como se fosse  Código de barra e salvar em um arquivo
db_produtos = "BancoDeDados/Estoque.json"
db_vendas = "BancoDeDados/Vendas.json"
class janela_Caixa(tk.Tk):
    def __init__(self):
        super().__init__()
        self.produto = ler(db_produtos)
        self.vendas = ler(db_vendas)
        self.carrinho = {}
        self.total = 0
        self.Caixa()


    def Caixa(self):
        self.geometry("1060x600")

        self.red_frame = tk.Frame(self, bg="#e74c3c", width=950, height=80)
        self.red_frame.pack(fill="x", anchor="n")
        self.red_frame.pack_propagate(False)
        
        tk.Label(self.red_frame, text="Mercado Do Bom", font=("Arial", 45, "bold"), fg="White", bg="#e74c3c").pack(pady=10)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.frame_entry = tk.Frame(self.main_frame)
        self.frame_entry.grid(row=0, column=0, sticky="nw", padx=10)

        tk.Label(self.frame_entry, text="ID ou o Nome do Item:", font=("Arial", 15)).pack(anchor="w")
        lista_indicie = []
        for i in self.produto:
            lista_indicie.append(self.produto[i]["ID"])
        self.ID_compra = ttk.Combobox(self.frame_entry, values=lista_indicie, width=28, font=("Arial", 11 ))
        self.ID_compra.pack(anchor="w")

        tk.Label(self.frame_entry, text="Quantidade:", font=("Arial", 15)).pack(anchor="w")
        self.quant_compra = tk.Entry(self.frame_entry, width=30, font=("Arial", 11))
        self.quant_compra.pack(anchor="w")
        
        tk.Label(self.frame_entry, text="Qual a forma de Pagamento?", font=("Arial", 15)).pack(anchor="w")

        self.paga = tk.IntVar(value=0)
        sla = 0
        lista_pagamento = ["Dinheiro", "Débito", "Crédito", "Pix"]
        for i in (lista_pagamento):
            sla += 1
            tk.Radiobutton(self.frame_entry, text=i, value=sla,font=("Arial", 9), variable=self.paga).pack(anchor="w")


        bt_carrinho = tk.Button(self.frame_entry, text="Adicionar", command=self.adicionar_carrinho, width=15, bg="#d4ac0d")
        bt_carrinho.pack(side="top", pady=10)

        self.lista_topico = ["ID", "Nome", "Quantidade", "Valor por Unidade", "Total"]
        self.frame_tree = tk.Frame(self.main_frame, width=300, height=300)
        self.frame_tree.grid(row=0, column=1, padx=10, pady=10)
        self.frame_tree.grid_propagate(False)
        
        self.tree = ttk.Treeview(self.frame_tree, columns=self.lista_topico, show="headings")
        self.tree.pack(expand=True, fill="both", side="left")
        self.tree.grid_propagate(False)

        for coluna in self.lista_topico:
            self.tree.heading(coluna, text=coluna)
            self.tree.column(coluna, width=150)

        self.tree.tag_configure("all", font=("Arial", 12))
        
        scroll = ttk.Scrollbar(self.frame_tree, command=self.tree.yview)
        scroll.pack(side="right", fill="y")
        self.tree.config(yscrollcommand=scroll.set)

        self.label_total = tk.Label(self.main_frame, font=("Arial", 20, "bold"),text="O Valor Total é R$ 0,00")
        self.label_total.grid(column=1, row=1)

        bt_confirm_compra = tk.Button(self.main_frame, text="Cofirmar Comprar", width=20, bg="#2ecc71", command=self.salvar_venda)
        bt_confirm_compra.grid(column=1, row=4, pady=150, sticky="w")

        bt_cancelar_compra = tk.Button(self.main_frame, text="Cancelar", width=20, bg="red", command=self.cancelar_venda)
        bt_cancelar_compra.grid(column=1, row=4, pady=150, sticky="w", padx=170)

        
    
    def adicionar_carrinho(self):
        id_nome = self.ID_compra.get()
        quant_item = (self.quant_compra.get())
        dict_produto = self.produto
        print(self.paga.get())

        if "" in (id_nome, quant_item):
            messagebox.showerror("ERRO", "Preenchar os Espaços para continua a Compra")
        else:
            for index in dict_produto:
                if dict_produto[id_nome]:
                    quant_estoque = float(dict_produto[id_nome]["Quantidade"])
                    valor_estoque = (quant_estoque) - float(quant_item)
                    dict_produto[id_nome]["Quantidade"] = int(valor_estoque)
                    escrever(db_produtos, self.produto)
                    preço_string = str(dict_produto[id_nome]["Preço"])
                    preço_float = float(preço_string.replace("R$", "").replace(",", "."))
                    
                    
                    
                    add_carrinho = preço_float * float(quant_item)
                    self.total += add_carrinho
                    self.carrinho[len(self.carrinho)+1] = {"ID": len(self.carrinho)+1,
                                                        "Nome": dict_produto[id_nome]["Nome"], 
                                                        "Quantidade": quant_item,
                                                        "Valor por Unidade": dict_produto[id_nome]["Preço"],
                                                        "Total": f"R$ {str(add_carrinho).replace(".", ",")}"}
                    break
            
            else:
                messagebox.showerror("ERRO", "Verifique o ID")
            
            for widget in self.tree.get_children():
                self.tree.delete(widget)
            for key, index in self.carrinho.items():
                valores = [index[col] for col in self.lista_topico]
                self.tree.insert("", tk.END, values=valores, tags="all")
            string_total = str(self.total)
            self.label_total.configure(text=f"O Valor Total é R$ {string_total.replace(".", ",")}")
        
    def salvar_venda(self):
        pass 
    
    def cancelar_venda(self):
        for widget in self.tree.get_children():
            self.tree.delete(widget)
        self.label_total.configure(text="O Valor Total é R$ 0,00")



                
                

if __name__ == "__main__":
    app = janela_Caixa()
    app.mainloop()