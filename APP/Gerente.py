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
    
def lista_join(lista):
    lista_certa = []
    for tupla in lista:
        separada = ", ".join(tupla)
        lista_certa.append(separada)
    return lista_join(lista_certa)
# Kore wa ikumasu deashboard que dê para adicionar Produtos 
# Controle de Vendas com uma tabela de vendas
# Controle de Estoque q tenha as vendas do porduto e vai avisar a quantidade dele
db_produtos = "BancoDeDados/Estoque.json"
db_vendas = "BancoDeDados/Vendas.json"


class Janela_Gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.produto = ler(db_produtos)
        self.vendas = ler(db_vendas)
        self.dict_produtos_vendas = {}
        self.gerente()
        #Messabox de acordo com os Estorque 
        messagebox.showerror("Vencidos", f"IDs: {lista_join(self.lista_id_vencido)}")
        messagebox.showwarning("Acabando", f"IDs: {lista_join(self.lista_id_acabando)}", )
    
    def gerente(self): #layout do Menu
        self.geometry("950x600")
        self.produto = ler(db_produtos)
        self.title("Área do Gerente")

        #Frames aléatorios 
        frame_dash = tk.Frame(self, width=1920 , height=160, bg="Black") #Frame Dashboard
        frame_dash.pack(anchor="w")
        frame_dash.propagate(False)

        tk.Label(frame_dash, text="Menu do Gerente", bg="Black", fg="white",font=("Arial", 15, "bold")).pack(padx=10)

        frame_pesquisa = tk.Frame(frame_dash, bg="Black")
        frame_pesquisa.pack(anchor="e", side="bottom")
        
        #Botão de Pesquisa no Estoque
        bt_pesquisa = tk.Button(frame_pesquisa, text="🔎", command=self.pesquisar, width=3)
        bt_pesquisa.grid(column=1, row=0)

        #Entry de pesquisa
        self.txb_pesquisa = tk.Entry(frame_pesquisa, width=25, bd=4)
        self.txb_pesquisa.grid(column=0, row=0)

        #Frame dos Buttons
        frame_buttons = tk.Frame(frame_dash, bg="Black")
        frame_buttons.pack(anchor="center", padx= 400, side="top")
       
        #Botão para abrir o Painel de Adicionar Produtos
        bt_AddProtudo = tk.Button(frame_buttons, text="🗃️ Adicionar Items", bg="white", width=20, command=self.add_produto)
        bt_AddProtudo.pack(pady=5)
       
        #Botão Para abrir o Painel de Vendas
        bt_Vendas = tk.Button(frame_buttons, text="Vendas", bg="White", width=20, command=self.historico_vendas)
        bt_Vendas.pack()
        
        #Botão para abrir o Painel de edição de Items
        bt_Edit= tk.Button(frame_buttons, text="Editar Item", bg="White", width=20, command=self.screen_editar )
        bt_Edit.pack(pady=5)
        
        
        
        #Códigos da TreeView
        tree_frame = tk.Frame(self)
        tree_frame.pack(fill="both", expand=True)
        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Arial", 10))
        column = ("ID", "Nome", "Preço", "Quantidade", "Lote", "Validade", "Categoria")
        self.tree_menu = ttk.Treeview(tree_frame, columns= column, show="headings",)
        self.tree_menu.pack(expand=True, fill="both", side="left")
        self.lista_atributos = ["ID", "Nome", "Preço", "Quantidade", "Lote", "Validade", "Categoria"]        

        for coluna, atri in zip(column, self.lista_atributos):
            self.tree_menu.heading(coluna, text=atri)
            self.tree_menu.column(coluna, width=100)
        
        self.lista_id_vencido = []
        self.lista_id_acabando = []

        for key, item in self.produto.items():
            valores = [item[col] for col in column]
            item_id = self.tree_menu.insert("", tk.END, values=valores,)
            data_item = datetime.strptime(item["Validade"], "%d/%m/%Y" )
            
            if data_item < datetime.now():
                self.tree_menu.item(item_id, tags=("yellow_bg", "all"))
                self.lista_id_vencido.append((str(item["ID"]), str(item["Nome"])))
            else:
                if int(item["Quantidade"]) <= 15:
                    self.tree_menu.item(item_id, tags=("vermelho_bg", "all"))
                    self.lista_id_acabando.append((str(item["ID"]), str(item["Nome"])))
                else:
                    self.tree_menu.item(item_id, tags=("verde_bg", "all"))
        
        self.tree_menu.tag_configure("yellow_bg", foreground="#f1c40f")
        self.tree_menu.tag_configure("verde_bg", foreground="green")
        self.tree_menu.tag_configure("vermelho_bg", foreground="red")
        self.tree_menu.tag_configure("all", font=("Arial", 11))

        scroll = tk.Scrollbar(tree_frame, command=self.tree_menu.yview)
        scroll.pack(side="right", fill="y")
        self.tree_menu.config(yscrollcommand=scroll.set)
        
    def add_produto(self): #Layout do Painel de Registro
        for widget in self.winfo_children():
            widget.destroy()
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
     
    def screen_editar(self): #Layout de Edição
        root = tk.Tk()
        root.geometry("450x600")
        root.title("Edição")
        self.produto = ler(db_produtos)
        
        deco_frame = tk.Frame(root, bg="Black",width=1920, height=100)
        deco_frame.pack(anchor="n", expand=True)
        deco_frame.propagate(False)

        tk.Label(deco_frame, text="Menu de Edição", font=("Arial", 17,"bold"), fg="#FFFFFF", bg="Black").pack(anchor="center", expand=True)
        
        edit_frame = tk.Frame(root)
        edit_frame.pack(anchor="n", expand=True, pady=10)

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

        bt_salvar = tk.Button(edit_frame, width=15, text="Salvar Alteração", bg="#2ecc71", command=lambda:self.editar(root))
        bt_salvar.pack(side="top", pady=10)

        bt_cancelar = tk.Button(edit_frame, width=15, text="Cancelar", bg="#e74c3c",command=lambda: self.off_windowns(root))
        bt_cancelar.pack(side="bottom")
    
    def historico_vendas(self): #Layout de Histórico de Vendas
        for widget in self.winfo_children():
            widget.destroy()
        
        self.title("Histórico de Vendas")
        
        top_frame = tk.Frame(self, width=1920, height=100, bg="#566573")
        top_frame.pack(anchor="n", expand=True)
        top_frame.propagate(False)

        tk.Label(top_frame, text="Hitórioco de Vendas", font=("Arial", 17, "bold"), fg="White", bg="#566573").pack(padx=10, pady=10, side="left")

        bt_voltar = tk.Button(top_frame, text="Voltar", width=15, font=("Arial", 9, "bold"),command=self.on_main)
        bt_voltar.pack(side="right", padx=15)

        frame_tree = tk.Frame(self, width=1920, height=980)
        frame_tree.pack(anchor="n", expand=True)
        frame_tree.propagate(False)

        lista_topico = ["ID da Venda", "Data", "Forma de Pagamento", "Total"]
        self.tree_vendas = ttk.Treeview(frame_tree, columns=lista_topico,  show="headings")
        self.tree_vendas.pack(anchor="n", expand=True, fill="both")
        self.tree_vendas.propagate(False)
        for topico in lista_topico:
            self.tree_vendas.heading(topico, text=topico)
            self.tree_vendas.column(topico, width=100)

        for key, items in self.vendas.items():
            valores = [items[col] for col in lista_topico]
            self.tree_vendas.insert("", "end", values=valores)
        
        self.tree_vendas.bind("<<TreeviewSelect>>", self.item_selecionado)
          
    def on_main(self): #Comando Para retornar para o Menu
        for widget in self.winfo_children():
            widget.destroy()
        
        self.gerente()
    
    def off_windowns(self, root): #Comando para apagar a janela
        root.destroy()
    
    def editar(self, root): #Comando para Edição de Item 
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
                            root.destroy()
                            self.on_main()
                            break
                        else:
                            messagebox.showerror("ERRO", "Tópico Inexistente")
                            break
                else:
                    messagebox.showerror("ERRO", "Verifique o ID")

    def salvar_produto(self): #Comando para salvar no Dicionário o Item
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

    def item_selecionado(self, event=None): #Pegar o item Selecionado e Mostrar o Historico
        selecionado = self.tree_vendas.selection()
        if selecionado:
            valores = self.tree_vendas.item(selecionado, "values")
            vendas_selecionada = valores[0]
            if self.vendas[vendas_selecionada]:
                self.dict_produtos_vendas = self.vendas[vendas_selecionada]["Venda"]
        root = tk.Tk()
        root.geometry("700x500")
        
        deco_frame = tk.Frame(root, width=1920, height=100, bg="#34495e")
        deco_frame.pack(anchor="n", expand=True)
        deco_frame.propagate(False)

        tk.Label(deco_frame, text="Informações dos Produtos Vendidos", font=("Arial", 17, "bold"), bg="#34495e", fg="White").pack(anchor="center", fill="both", pady=35)

        frame_tree = tk.Frame(root, width=1920, height=980)
        frame_tree.pack(anchor="n", expand=True)
        frame_tree.propagate(False)

        produto_venda = ["ID", "Nome", "Quantidade", "Valor por Unidade", "Total" ]
        self.tree_produto = ttk.Treeview(frame_tree, show="headings", columns=produto_venda)
        self.tree_produto.pack(side="left", expand=True, fill="both")
        self.tree_produto.propagate(False)

        for top in produto_venda:
            self.tree_produto.heading(top, text=top)
            self.tree_produto.column(top, width=100)
        
        for index, items in self.dict_produtos_vendas.items():
            valores = [items[col] for col in produto_venda]
            self.tree_produto.insert("", "end", values=valores)
        
        scroll = tk.Scrollbar(frame_tree, command=self.tree_produto.yview)
        scroll.pack(side="right", fill="y")
        self.tree_produto.config(yscrollcommand=scroll.set)
    
    def pesquisar(self): #Função para pesquisa e colocar na tree o item
        item_ID = self.txb_pesquisa.get()
        dict_pesquisa = {}
        try:
            if self.produto[item_ID]:
                self.pesqui_reut(item_ID)
        except:
            for key, item in self.produto.items():
                if item["Nome"] == item_ID.capitalize():
                    self.pesqui_reut(key)
            else:
                messagebox.showerror("ERRO", "ID ou Nome não Existem")

    def delete_tree(self): #Funçaõ para excluir a tree_menu
        for item in self.tree_menu.get_children():
            self.tree_menu.delete(item)
            
    def data(self, string): #Função de verificação e formatação da Data
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
        
    def pesqui_reut(self, ID_nome): #Reeutiliza o codigo Para da insert
        dict_pesquisa = self.produto[ID_nome]
        self.delete_tree()
        valores = [dict_pesquisa[col] for col in self.lista_atributos]
        item_tree =self.tree_menu.insert("", "end", values=valores, tags=("all"))
        data_item = datetime.strptime(dict_pesquisa["Validade"], "%d/%m/%Y" )
        #Colore de Acordo com a condição
        if data_item < datetime.now():
            self.tree_menu.item(item_tree, tags=("yellow_bg", "all"))
        else:
            if int(dict_pesquisa["Quantidade"]) <= 15:
                self.tree_menu.item(item_tree, tags=("vermelho_bg", "all"))
            else:
                self.tree_menu.item(item_tree, tags=("verde_bg", "all"))
    

if __name__ == "__main__":
    janela = Janela_Gerente()
    janela.mainloop()
