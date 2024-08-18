import tkinter as tk
from tkinter import messagebox
import json


arquivo = "APP/DataBase_login.json"

def ler(a):
        try:
            with open(a, mode="r", encoding="utf-8") as file:
                dados = json.load(file)
        except:
            dados = {}
        return dados

def escrever(a):
    with open(a, mode="w", encoding="utf-8") as file:
        json.dump(data_base, file)

# gerente_nome = "Pedro"
# ID_gerente = 0
# genero_gerente = "Masculino"
senha_gerente = "123"
# cargo_gerente = "Gerente"
# data_base[ID_gerente] = {"Nome": gerente_nome,"Gênero": genero_gerente,"Cargo":cargo_gerente,  "Senha": senha_gerente}


data_base = ler(arquivo)

class Cadastro_janela(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.geometry("350x580")
        self.title("Cadastro")
        self.cargo = tk.IntVar()
        self.genero_var = tk.IntVar()
        self.display()
        
    def display(self):
        self.frame_cadastro = tk.Frame(self, width=200, height=100)
        self.frame_cadastro.pack(anchor="w", padx=20, pady=20)
        
        tk.Label(self.frame_cadastro, text="Nome do Funcionario:", font=("Arial", 11)).pack(anchor="w")
        self.nome_cadastro = tk.Entry(self.frame_cadastro, width=50, bd=4)
        self.nome_cadastro.pack(anchor="w", pady=10)

        tk.Label(self.frame_cadastro, text="Gênero:", font=("Arial", 11) ).pack(anchor="w", pady=10)
        tk.Radiobutton(self.frame_cadastro, text="Masculino", font=("Arial", 8), variable=self.genero_var, value=1).pack(anchor="w")
        tk.Radiobutton(self.frame_cadastro, text="Feminino", font=("Arial", 8), variable=self.genero_var, value=2).pack(anchor="w")
        tk.Radiobutton(self.frame_cadastro, text="Outro", font=("Arial", 8), variable=self.genero_var, value=3).pack(anchor="w")

        tk.Label(self.frame_cadastro, text="Cargo:", font=("Arial", 12) ).pack(anchor="w", pady=10)
        tk.Radiobutton(self.frame_cadastro, text="Gerente", font=("Arial", 8), variable=self.cargo, value=1).pack(anchor="w")
        tk.Radiobutton(self.frame_cadastro, text="Funcionário", font=("Arial", 8), variable=self.cargo, value=2).pack(anchor="w")

        tk.Label(self.frame_cadastro, text="Senha:", font=("Arial", 11)).pack(anchor="w", pady=10)
        self.senha_cadastro = tk.Entry(self.frame_cadastro, width=50, bd=4, show="*")
        self.senha_cadastro.pack(anchor="w", pady=10)
        tk.Label(self.frame_cadastro, text="Confirmar Senha:", font=("Arial", 11)).pack(anchor="w", pady=10)
        self.confirm_cadastro = tk.Entry(self.frame_cadastro, width=50, bd=4, show="*")
        self.confirm_cadastro.pack(anchor="w", pady=10)

        self.bt_cadastro = tk.Button(self.frame_cadastro, text="Salvar", command=self.salvar,width=10,  bg="#2ecc71")
        self.bt_cadastro.pack(side="top", pady=5)
        self.bt_cancelar = tk.Button(self.frame_cadastro, text="Cancelar", command=self.destroy, width=10, bg="#e74c3c")
        self.bt_cancelar.pack(side="bottom", pady=5)
        
    def salvar(self, event=None):
        nome = self.verif_nome()
        genero = self.select_genero()
        cargo = self.select_cargo()
        senha = self.senha_cadastro.get()
        confir_senha = self.confirm_cadastro.get()
        if senha == confir_senha:
            if cargo == "Gerente":
                if  senha == senha_gerente:
                    data_base[len(data_base)] = {"Nome": nome,"Gênero": genero, "Cargo": cargo, "Senha":senha}
                    escrever(arquivo)
                else:
                    messagebox.showerror("ERRO", "Você não tem Permissão para cadastrar como Gerente")
            else:
                data_base[len(data_base)] = {"Nome": nome,"Gênero": genero, "Cargo": cargo, "Senha":senha}
                escrever(arquivo)
        else:
            messagebox.showerror("ERRO", "Senhas não se Coincidem")

    def verif_nome(self):
        nome = self.nome_cadastro.get()
        return nome
            
    def select_genero(self):
        genero = None
        if self.genero_var.get() == 1:
            genero = "Masculino"
        elif self.genero_var.get() == 2:
            genero = "Feminino"
        elif self.genero_var.get() == 3:
            genero = "Outro"
        return genero
    
    def select_cargo(self):
        cargo = None
        if self.cargo.get() == 1:
            cargo = "Gerente"
        elif self.cargo.get() == 2:
            cargo = "Funário"
        return cargo
    

if __name__ == "__main__":
    root = Cadastro_janela()
    root.mainloop()