from tkinter import messagebox
import tkinter as tk
import json



data_base ={}

gerente_nome = "Pedro"
ID_gerente = "00"
senha_gerente = "123"
data_base[ID_gerente] = {"Nome": gerente_nome, "Senha": senha_gerente}



class App(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.geometry("500x600")
        self.title("Supermercado")
    
        self.login()

    
    def login(self):
        tk.Label(self, text="Tela de Login", font=("Arial", 16)).pack(pady=10)

        
        frame_login = tk.Frame(self, width=100, height=100)
        frame_login.pack(padx=105, pady=50)

        tk.Label(frame_login, font=("Arial", 11), text="Nome:").pack(padx=0, pady=0, anchor="w")
        self.txb_nome = tk.Entry(frame_login, width=100)
        self.txb_nome.pack(padx=0, pady=10, anchor="w")

        tk.Label(frame_login, font=("Arial", 11), text="Senha:").pack(padx=0, pady=0, anchor="w")
        self.txb_senha = tk.Entry(frame_login, width=100)
        self.txb_senha.pack(padx=0, pady=10, anchor="w")

        bt_confirm = tk.Button(frame_login, text="Confirmar", width=10, command=self.confirm)
        bt_confirm.pack(anchor="w", padx=0, pady=10)

        bt_cancelar = tk.Button(frame_login, text="Cancelar", width=10, command=self.cancelar)
        bt_cancelar.pack(padx=0, pady=0, anchor="w")
        
    def cancelar(self):
        self.destroy()
    def confirm(self):
        nome = self.txb_nome.get()
        senha = self.txb_senha.get()
        for i in data_base:
            if nome == data_base[i]["Nome"]:
                if senha == data_base[i]["Senha"]:
                    messagebox.showinfo("Acesso Aceito", f"Bem-vindo: {nome}")
            else:
                messagebox.showerro("Acesso Negado", "Verfique se sua senha ou nome")

        


if __name__ == "__main__":
    Aplicativo = App()
    Aplicativo.mainloop()