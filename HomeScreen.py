import tkinter as tk
from tkinter import messagebox
import ScreenManager

class HomeScreen(tk.Frame):

    def __init__(self, parent, controller) -> None:
        super().__init__(parent)

        self.configure(bg="#f2f2f2")

        # Rótulo do título
        label_titulo = tk.Label(
            self, 
            text="Stock Control", 
            font=("Arial", 24, "bold"), 
            bg="#f2f2f2", 
            fg="#333"
        )
        label_titulo.pack(side='top', anchor='center', pady=50)

        # Botão de Login
        botao_login = tk.Button(
            self, 
            text="Login", 
            font=("Arial", 14), 
            bg="#4CAF50", 
            fg="white", 
            width=10, 
            command=lambda:controller.show("LoginScreen")
        )
        botao_login.pack(side='top', anchor='center', pady=15)

        # Botão de Sair
        botao_sair = tk.Button(
            self, 
            text="Sair", 
            font=("Arial", 14), 
            bg="#f44336", 
            fg="white", 
            width=10, 
            command=lambda:controller.destroy()
        )
        botao_sair.pack(side='top', anchor='center', pady=15)
