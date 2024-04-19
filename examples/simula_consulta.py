import tkinter as tk
from tkinter import ttk
import threading
import time
import pymysql

def consulta():
    time.sleep(5)

    # query = ...
    # cursor.execute(query, ...)

    # dps q a consulta acabar, remover a barra de progresso
    progress_bar.stop()

def iniciar_consulta():
    consulta_thread = threading.Thread(target=consulta)
    consulta_thread.start()

    progress_bar.start(10)

root = tk.Tk()
root.title("Consulta com Barra de Progresso")

loading_page = ttk.Frame(root)
loading_page.pack(pady=50)

progress_bar = ttk.Progressbar(loading_page, length=200, mode='indeterminate')
progress_bar.pack()

start_button = ttk.Button(loading_page, text="Iniciar Consulta", command=iniciar_consulta)
start_button.pack(pady=10)

root.mainloop()
