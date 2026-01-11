import random
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


def gerar_mira():
    tamanho = random.randint(1, 5)
    espessura = round(random.uniform(0.5, 2.0), 1)
    espaçamento = random.randint(-3, 3)
    cor = random.choice([1, 2, 3, 4, 5])
    alpha = random.randint(150, 250)

    mira = f"""
cl_crosshairsize {tamanho}
cl_crosshairthickness {espessura}
cl_crosshairgap {espaçamento}
cl_crosshaircolor {cor}
cl_crosshairalpha {alpha}
cl_crosshairdot 0
cl_crosshair_drawoutline 0
"""
    return mira

    

def gerar_mira_interface():
    texto.delete("1.0", tk.END)
    texto.insert(tk.END, gerar_mira())

    messagebox.showinfo("Sucesso!", "Mira gerada com sucesso!")



janela = ctk.CTk()
janela.geometry("400x350")
janela.title("Gerador de miras pro CS2")
janela.resizable(False, False)

titulo = ctk.CTkLabel(janela, text="Gerador de miras pro CS2", font=("Arial", 12))
titulo.pack(pady=10)


texto = tk.Text(janela, height=12, width=45)
texto.pack(pady=10, padx=10)

botao = ctk.CTkButton(janela, text="Gerar mira", command=gerar_mira_interface, font=("Arial", 12))
botao.pack(pady=5)

janela.mainloop()
