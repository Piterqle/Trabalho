import tkinter as tk
from tkinter import messagebox
import json
from tkinter import ttk

def ler(a):
        try:
            with open(a, mode="r", encoding="utf-8") as file:
                dados = json.load(file)
        except:
            dados = {}
        return dados

def escrever(a,b):
    with open(a, mode="w", encoding="utf-8") as file:
        json.dump(b, file, indent=2, ensure_ascii=False)
# Aki vai ficar uma deashboard que dê para adicionar Produtos 
# Controle de Vendas com uma tabela de vendas
# Controle de Estoque q tenha as vendas do porduto e vai avisar a quantidade dele
db_produtos = "BancoDeDados/Estoque.json"

produto = ler(db_produtos)

class Janela_Gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Gerente()

    def Gerente(self):
        self.geometry("950x600")
        self.title("Poderoso Chefinho")
        
        frame_dash = tk.Frame(self, width=500 , height=100, bg="Black") #Frame Dashboard
        frame_dash.pack(anchor="w")

        tk.Label(frame_dash, text="Menu do Gerente", bg="Black", fg="white",font=("Arial", 15)).pack(padx=10)

        frame_buttons = tk.Frame(frame_dash, bg="Black")
        frame_buttons.pack(anchor="center", padx= 400, pady=5)
        bt_AddProtudo = tk.Button(frame_buttons, text="🗃️ Adicionar Items", bg="white", width=20, command=self.on_add)
        bt_AddProtudo.pack(pady=5)
        bt_Vendas = tk.Button(frame_buttons, text="Vendas", bg="White", width=20)
        bt_Vendas.pack()
        bt_Edit= tk.Button(frame_buttons, text="Editar Quantidade", bg="White", width=20, command=self.on_edit )
        bt_Edit.pack(pady=5)

        tree_frame = tk.Frame(self)
        tree_frame.pack(fill="both", expand=True)
        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Arial", 10))
        column = ("ID", "Nome", "Preço", "Quantidade", "Lote", "Validade", "Categoria")
        tree = ttk.Treeview(tree_frame, columns= column, show="headings",)
        tree.pack(expand=True, fill="both", side="left")
        lista_atributos = ["ID", "Nome", "Preço", "Quantidade", "Lote", "Validade", "Categoria"]        

        for coluna, atri in zip(column, lista_atributos):
            tree.heading(coluna, text=atri)
            tree.column(coluna, width=100)
        
        

        for key, item in produto.items():
            valores = [item[col] for col in column]
            item_id = tree.insert("", tk.END, values=valores,)
            if int(item["Quantidade"]) <= 15:
                tree.item(item_id, tags=("vermelho_bg",))
            else:
                tree.item(item_id, tags=("verde_bg", ))
            
        tree.tag_configure("verde_bg", foreground="green")
        tree.tag_configure("vermelho_bg", foreground="red")

        scroll = tk.Scrollbar(tree_frame, command=tree.yview)
        scroll.pack(side="right", fill="y")
        tree.config(yscrollcommand=scroll.set)
        
                
    def editar(self):
        self.geometry("950x600")
        edit_frame = tk.Frame(self)
        tk.Label(edit_frame, text="Editar Topico:", font=("Arial", 11)).pack( anchor="w")
        self.entry_edit = tk.Entry(edit_frame, width=50, bd=4)
        self.entry_edit.pack(pady=10, anchor="w")

    def on_add(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.add_produto()
    
    def on_main(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.Gerente()
    
    def on_edit(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.editar()

    def add_produto(self):
        self.geometry("950x600")

        frame_addP = tk.Frame(self, width=200, height=100 )
        frame_addP.pack(padx=10 , pady=10)
        
        tk.Label(frame_addP, text="Nome do Produto:", font=("Arial", 11)).pack( anchor="w")
        self.entry_nomeP = tk.Entry(frame_addP, width=50, bd=4)
        self.entry_nomeP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Preço Unitário", font=("Arial", 11) ).pack(anchor="w")
        self.entry_preçokg = tk.Entry(frame_addP, width=50, bd=4)
        self.entry_preçokg.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Quantidade", font=("Arial", 11)).pack(anchor="w")
        self.entry_quantP = tk.Entry(frame_addP, width=50, bd=4)
        self.entry_quantP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Lote", font=("Arial", 11)).pack(anchor="w")
        self.entry_loteP = tk.Entry(frame_addP, width=50, bd=4)
        self.entry_loteP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Validade", font=("Arial", 11)).pack(anchor="w")
        self.entry_validadeP = tk.Entry(frame_addP, width=50, bd=4)
        self.entry_validadeP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Categoria", font=("Arial", 11)).pack(anchor="w")
        self.entry_categoriaP = tk.Entry(frame_addP, width=50, bd=4)
        self.entry_categoriaP.pack(pady=10, anchor="w")

        bt_salvar = tk.Button(frame_addP, width=15, text="Salvar Produto", bg="#2ecc71", command=self.salvar_produto)
        bt_salvar.pack(side="top", pady=10)

        bt_cancelar = tk.Button(frame_addP, width=15, text="Cancelar", bg="#e74c3c",command=self.on_main)
        bt_cancelar.pack(side="bottom")

    def salvar_produto(self):
        nome_produto = self.entry_nomeP.get()
        preço = float(self.entry_preçokg.get())
        quantidade = int(self.entry_quantP.get())
        lote = self.entry_loteP.get()
        validade = self.entry_validadeP.get()
        categoria = self.entry_loteP.get()
        if "" in (nome_produto, preço, quantidade, lote, validade, categoria):
            messagebox.showerror("ERRO", "Preencha os espaços")
        else:
            produto[len(produto)+1] = {"ID": len(produto )+1,
                                       "Nome": nome_produto, 
                                        "Preço": f"R$ {preço:.2f}", 
                                        "Quantidade": quantidade, 
                                        "Lote": lote, 
                                        "Validade":validade,
                                        "Categoria": categoria}
            escrever(db_produtos, produto)
            self.on_main()

if __name__ == "__main__":
    janela = Janela_Gerente()
    janela.mainloop()
