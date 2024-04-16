import tkinter as tk
from tkinter import messagebox

def button_submit():
    mostrar_mensagem()
    mostrar_texto()

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "botao clicado.")


def mostrar_texto():
    texto_inserido = campo_texto.get()
    if texto_inserido:
        messagebox.showinfo("Texto Inserido", f"Você digitou: {texto_inserido}")
    else:
        messagebox.showwarning("Texto em branco", "Por favor, insira algum texto.")


janela = tk.Tk()
janela.title("Interface simples")



rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.pack()

campo_texto = tk.Entry(janela, width=30)
campo_texto.pack()



botao = tk.Button(janela, text="Enviar", command=button_submit)
botao.config(fg="red")
botao.pack()

janela.mainloop()