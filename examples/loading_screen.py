import tkinter as tk
from tkinter import messagebox, ttk



def button_submit():
    
    def close_loading():
        root.destroy()
        
    root = tk.Tk()
    root.title("Loading Page")
    root.geometry("300x200")
    root.resizable(False, False)

    # Create a label for the loading message
    loading_label = ttk.Label(root, text="Loading...", font=("Arial", 14))
    loading_label.pack(pady=50)

    # Create a progress bar
    progress_bar = ttk.Progressbar(root, length=200, mode='indeterminate')
    progress_bar.pack()

    # Schedule closing the loading window after 5 seconds
    root.after(5000, close_loading)

    # Start the progress bar animation
    progress_bar.start(10)


janela = tk.Tk()
janela.title("Interface simples")
janela.geometry('700x400')


rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.pack()

campo_texto = tk.Entry(janela, width=30)
campo_texto.pack()



botao = tk.Button(janela, text="Enviar", command=button_submit)
botao.config(fg="red")
botao.pack()

janela.mainloop()