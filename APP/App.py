from tkinter import messagebox
import tkinter as tk
import json
from Gerente import Janela_Gerente, ler, escrever

arquivo = "BancoDeDados/DataBase_login.json"
db_produtos = "BancoDeDados/Estoque.json"



# gerente_nome = "Pedro"
# ID_gerente = 0
# genero_gerente = "Masculino"
senha_gerente = "123"
# cargo_gerente = "Gerente"
# data_base[ID_gerente] = {"Nome": gerente_nome,"Gênero": genero_gerente,"Cargo":cargo_gerente,  "Senha": senha_gerente}

produto = ler(db_produtos)
data_base = ler(arquivo)
class App_Super(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)        
        self.login()

    #Àrea do Login
    def login(self):
        self.geometry("500x600")
        self.title("Supermercado")
        tk.Label(self, text="Tela de Login", font=("Arial", 16)).pack(pady=10)

        
        frame_login = tk.Frame(self, width=100, height=100)
        frame_login.pack(padx=105, pady=50)

        tk.Label(frame_login, font=("Arial", 11), text="Nome:").pack(padx=0, pady=0, anchor="w")
        self.txb_nome = tk.Entry(frame_login, width=100)
        self.txb_nome.pack(padx=0, pady=10, anchor="w")

        tk.Label(frame_login, font=("Arial", 11), text="Senha:").pack(padx=0, pady=0, anchor="w")
        self.txb_senha = tk.Entry(frame_login, width=100, show="*")
        self.txb_senha.pack(padx=0, pady=10, anchor="w")

        bt_confirm = tk.Button(frame_login, text="Confirmar", width=10, command=self.confirm)
        bt_confirm.pack(side="top", padx=0, pady=10)

        bt_cancelar = tk.Button(frame_login, text="Cancelar", width=10, command=self.cancelar)
        bt_cancelar.pack(padx=0, pady=0, side="bottom")

        tk.Label(self, text="Você é novo aqui?", font=("Arial", 10)).place(x=140, y=500)
        label_cadastro = tk.Label(self, text="Cadastre-se", font=("Arial", 10), fg="#3498db" )
        label_cadastro.place(x=250, y=500)
        label_cadastro.bind("<Button-1>", self.open_cadastro)

    def cancelar(self):
        self.destroy()
    
    def confirm(self):
        nome = self.txb_nome.get()
        senha = self.txb_senha.get()
        for i in data_base:
            if nome == data_base[i]["Nome"]:
                if senha == data_base[i]["Senha"]:
                    messagebox.showinfo("Acesso Aceito", f"Bem-vindo: {nome}")
                    if data_base[i]["Cargo"] == "Gerente":
                        self.open_gerente()
                    else:
                        self.open_funcionario()
                    break
        else:
            messagebox.showerror("Acesso Negado", "Verfique se sua senha ou nome")


    #Àrea do Cadastro
    def Cadastro(self):
        self.geometry("500x600")
        
        self.genero_var = tk.IntVar(value=0)
        self.cargo = tk.IntVar(value=0)
        
        
        self.frame_cadastro = tk.Frame(self, width=200, height=100)
        self.frame_cadastro.pack(padx=20, pady=20)
        
        tk.Label(self.frame_cadastro, text="Nome do Funcionario:", font=("Arial", 11)).pack(anchor="w")
        self.nome_cadastro = tk.Entry(self.frame_cadastro, width=50, bd=4)
        self.nome_cadastro.pack(anchor="w", pady=10)

        tk.Label(self.frame_cadastro, text="Gênero:", font=("Arial", 11) ).pack(anchor="w", pady=10)
        tk.Radiobutton(self.frame_cadastro, text="Masculino", font=("Arial", 8), variable=self.genero_var, value=1).pack(anchor="w")
        tk.Radiobutton(self.frame_cadastro, text="Feminino", font=("Arial", 8), variable=self.genero_var, value=2).pack(anchor="w")
        tk.Radiobutton(self.frame_cadastro, text="Outro", font=("Arial", 8), variable=self.genero_var, value=3).pack(anchor="w")

        tk.Label(self.frame_cadastro, text="Cargo:", font=("Arial", 12) ).pack(anchor="w", pady=10)
        tk.Radiobutton(self.frame_cadastro, text="Gerente", font=("Arial", 8), variable=self.cargo, value=1).pack(anchor="w")
        tk.Radiobutton(self.frame_cadastro, text="Caixa", font=("Arial", 8), variable=self.cargo, value=2).pack(anchor="w")
        tk.Radiobutton(self.frame_cadastro, text="Repositor", font=("Arial", 8), variable=self.cargo, value=3).pack(anchor="w")

        tk.Label(self.frame_cadastro, text="Senha:", font=("Arial", 11)).pack(anchor="w", pady=10)
        self.senha_cadastro = tk.Entry(self.frame_cadastro, width=50, bd=4, show="*")
        self.senha_cadastro.pack(anchor="w", pady=10)
        tk.Label(self.frame_cadastro, text="Confirmar Senha:", font=("Arial", 11)).pack(anchor="w", pady=10)
        self.confirm_cadastro = tk.Entry(self.frame_cadastro, width=50, bd=4, show="*")
        self.confirm_cadastro.pack(anchor="w", pady=10)

        self.bt_cadastro = tk.Button(self.frame_cadastro, text="Salvar", command=self.salvar,width=10,  bg="#2ecc71")
        self.bt_cadastro.pack(side="top", pady=5)
        self.bt_cancelar = tk.Button(self.frame_cadastro, text="Cancelar", command=self.open_login, width=10, bg="#e74c3c")
        self.bt_cancelar.pack(side="bottom", pady=5)
    
    def verif_nome(self):
        nome = self.nome_cadastro.get()
        if nome == "":
            nome = None
        return nome
            
    def select_genero(self):
        genero = self.genero_var.get()
        if genero == 1:
            genero = "Masculino"
        elif genero == 2:
            genero = "Feminino"
        elif genero == 3:
            genero = "Outro"
        else:
            genero = None
        return genero
    
    def select_cargo(self):
        cargo = None
        if self.cargo.get() == 1:
            cargo = "Gerente"
        elif self.cargo.get() == 2:
            cargo = "Caixa"
        elif self.cargo.get() == 3:
            cargo = "Repositor"
        return cargo
        
    def salvar(self, event=None):
        nome = self.verif_nome()
        genero = self.select_genero()
        cargo = self.select_cargo()
        senha = self.senha_cadastro.get()
        confir_senha = self.confirm_cadastro.get()
        if senha == confir_senha:
            if None in (nome, genero, cargo):
                messagebox.showerror("ERRO", "Preencha todas os Espaços")
            else:
                if cargo == "Gerente":
                    if  senha == senha_gerente:
                        data_base[len(data_base)+1] = {"Nome": nome,"Gênero": genero, "Cargo": cargo, "Senha":senha}
                        escrever(arquivo, data_base)
                        self.open_login()
                    else:
                        messagebox.showerror("ERRO", "Você não tem Permissão para cadastrar como Gerente")
                else:
                    data_base[len(data_base)+1] = {"Nome": nome,"Gênero": genero, "Cargo": cargo, "Senha":senha}
                    escrever(arquivo, data_base)
                    self.open_login()
        else:
            messagebox.showerror("ERRO", "Senhas não se Coincidem")

    
    #Àrea de Reescrever o app de acordo com a Necessidade
    def open_cadastro(self,event=None):
        for widget in self.winfo_children():
            widget.destroy()
        self.Cadastro()
    
    def open_login(self, event=None):
        for widget in self.winfo_children():
            widget.destroy()
        widget.destroy()

        self.login()
         
    def open_gerente(self, event=None):
        self.destroy()
        gerente =Janela_Gerente()
        gerente.mainloop()
    
    def open_funcionario(self, envent=None):
        print("teste")

if __name__ == "__main__":
    Aplicativo = (App_Super())
    Aplicativo.mainloop()