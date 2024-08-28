import tkinter as tk
from tkinter import messagebox
import json
from tkinter import ttk
from datetime import *

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
# Kore wa ikumasu deashboard que dê para adicionar Produtos 
# Controle de Vendas com uma tabela de vendas
# Controle de Estoque q tenha as vendas do porduto e vai avisar a quantidade dele
db_produtos = "BancoDeDados/Estoque.json"



class Janela_Gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.produto = ler(db_produtos)
        self.gerente()

    def gerente(self):
        self.geometry("950x600")
        self.produto = ler(db_produtos)
        self.title("Poderoso Chefinho")
        
        frame_dash = tk.Frame(self, width=500 , height=100, bg="Black") #Frame Dashboard
        frame_dash.pack(anchor="w")

        tk.Label(frame_dash, text="Menu do Gerente", bg="Black", fg="white",font=("Arial", 15, "bold")).pack(padx=10)

        frame_buttons = tk.Frame(frame_dash, bg="Black")
        frame_buttons.pack(anchor="center", padx= 400, pady=5)
        bt_AddProtudo = tk.Button(frame_buttons, text="🗃️ Adicionar Items", bg="white", width=20, command=self.on_add)
        bt_AddProtudo.pack(pady=5)
        bt_Vendas = tk.Button(frame_buttons, text="Vendas", bg="White", width=20)
        bt_Vendas.pack()
        bt_Edit= tk.Button(frame_buttons, text="Editar Item", bg="White", width=20, command=self.on_edit )
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
        
        

        for key, item in self.produto.items():
            valores = [item[col] for col in column]
            item_id = tree.insert("", tk.END, values=valores,)
            data_item = datetime.strptime(item["Validade"], "%d/%m/%Y" )
            
            if data_item < datetime.now():
                tree.item(item_id, tags=("yellow_bg"))
            else:
                if int(item["Quantidade"]) <= 15:
                    tree.item(item_id, tags=("vermelho_bg",))
                else:
                    tree.item(item_id, tags=("verde_bg", ))
        
        tree.tag_configure("yellow_bg", foreground="#f1c40f", font=("Arial", 11))
        tree.tag_configure("verde_bg", foreground="green", font=("Arial", 11))
        tree.tag_configure("vermelho_bg", foreground="red", font=("Arial", 11))

        scroll = tk.Scrollbar(tree_frame, command=tree.yview)
        scroll.pack(side="right", fill="y")
        tree.config(yscrollcommand=scroll.set)
        
    def add_produto(self):
        self.geometry("950x600")

        frame_addP = tk.Frame(self, width=200, height=100 )
        frame_addP.pack(padx=10 , pady=10)
        
        tk.Label(frame_addP, text="Nome do Produto:", font=("Arial", 11)).pack( anchor="w")
        self.entry_nomeP = tk.Entry(frame_addP, width=50, bd=4)
        self.entry_nomeP.pack(pady=10, anchor="w")

        tk.Label(frame_addP, text="Preço por KG", font=("Arial", 11) ).pack(anchor="w")
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
     
    def screen_editar(self):
        self.geometry("950x600")
        self.produto = ler(db_produtos)
        
        edit_frame = tk.Frame(self)
        edit_frame.pack(anchor="center", expand=True, pady=10)

        tk.Label(edit_frame, text="Digite o ID do item:", font=("Arial", 11)).pack( anchor="w")
        self.entry_item = tk.Entry(edit_frame, width=50, bd=4)
        self.entry_item.pack(pady=10, anchor="w")

        tk.Label(edit_frame, text="Editar Qual Tópico:", font=("Arial", 11)).pack( anchor="w")
        self.combo_topico = ttk.Combobox(edit_frame, values=("Nome", "Preço", "Quantidade", "Lote", "Validade", "Categoria"),
                                         width=41, font=("Arial", 10))
        self.combo_topico.pack(pady=10, anchor="w")

        tk.Label(edit_frame, text="Qual será o Novo valor:", font=("Arial", 11)).pack( anchor="w")
        self.entry_valor = tk.Entry(edit_frame, width=50, bd=4)
        self.entry_valor.pack(pady=10, anchor="w")

        bt_salvar = tk.Button(edit_frame, width=15, text="Salvar Alteração", bg="#2ecc71", command=self.editar)
        bt_salvar.pack(side="top", pady=10)

        bt_cancelar = tk.Button(edit_frame, width=15, text="Cancelar", bg="#e74c3c",command=self.on_main)
        bt_cancelar.pack(side="bottom")


    def on_add(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.add_produto()
    
    def on_main(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.gerente()
    
    def on_edit(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.screen_editar()
    
    def editar(self):
        ID = self.entry_item.get()
        topico = self.combo_topico.get()
        valor = self.entry_valor.get()
        
        if "" in (ID, topico, valor):
            messagebox.showerror("ERRO", "Preencha os Espaços")
        else:
            if topico == "Preço":
                valor = f"R$ {float(valor.replace(",", ".")):.2f}"
                valor = str(valor).replace(".", ",")
            elif topico == "Validade":
                valor = self.data(valor)
            
            if valor == None:
                messagebox.showerror("ERRO", "Verifique a Data o Produto pode estar Vencido")
            else:
                for item in self.produto:
                    if ID in self.produto:
                        if topico in self.produto[item]:
                            self.produto[ID][topico] = valor
                            escrever(db_produtos, self.produto)
                            self.on_main()
                            break
                        else:
                            messagebox.showerror("ERRO", "Tópico Inexistente")
                            break
                else:
                    messagebox.showerror("ERRO", "Verifique o ID")

    def salvar_produto(self):
        nome_produto = self.entry_nomeP.get().capitalize()
        preço = self.entry_preçokg.get()
        quantidade =self.entry_quantP.get()
        lote = self.entry_loteP.get()
        validade = self.data(self.entry_validadeP.get())
        categoria = self.entry_categoriaP.get().capitalize()
        
        if "" in (nome_produto, preço, quantidade, lote, validade, categoria):
            messagebox.showerror("ERRO", "Preencha os espaços")
        else:
            if nome_produto.isnumeric() or categoria.isnumeric():
                messagebox.showerror("ERRO", "Verifique os espaços Preenchidos (Números no Espaço de Letras)")
            else:
                if preço.isalpha() or quantidade.isalpha():
                    messagebox.showerror("ERRO", "Verifique os espaços Preenchidos (Letras no Espaço de Numeros)")
                else:
                    for i in self.produto:
                        if nome_produto in self.produto[i]["Nome"]:
                            messagebox.showerror("ERRO", "Esse produto já está cadastrado")
                            break
                    else:
                        if validade == None:
                            messagebox.showerror("ERRO", "Verfique a Data o produto pode estar vencido")
                            
                        else:
                            self.produto[len(self.produto)+1] = {
                                                        "ID": len(self.produto)+1,
                                                        "Nome": nome_produto, 
                                                        "Preço": f"R$ {preço}", 
                                                        "Quantidade": int(quantidade), 
                                                        "Lote": lote, 
                                                        "Validade": validade,
                                                        "Categoria": categoria}
                            escrever(db_produtos, self.produto)
                            self.on_main()

    def data(self, string):
        data_atual = datetime.now()
        
        try:
            data_objt = datetime.strptime(string, "%d%m%Y")
        except:
            data_objt = datetime.strptime(string, "%d/%m/%Y")
        data_real = data_objt.strftime("%d/%m/%Y")
        if data_objt > data_atual:
            return data_real
        else:
            return None
        
    def historico_vendas(self):
        pass

if __name__ == "__main__":
    janela = Janela_Gerente()
    janela.mainloop()
