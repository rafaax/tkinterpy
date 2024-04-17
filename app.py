import sys
import pymysql
import datetime
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from src import conn


now = datetime.datetime.now()

def submit():
    data = input_date.get_date()
    placa = input_text.get()

    if not placa:
        messagebox.showwarning("Erro", "Por favor insira alguma placa válida.")
    else:    
        print(data)
        print(placa)


conn = pymysql.connect(host=conn.host, user=conn.user, password=conn.passw, database=conn.db,charset='utf8')
cursor = conn.cursor()

app = Tk()
app.title('Gerar Relatorio')
app.geometry('600x400')
app.wm_maxsize(width=600, height=400)
app.wm_minsize(width=600, height=400)

text_1 = Label(app, text="Insira a placa")
text_1.pack()

input_text = Entry(app, width=30)
input_text.pack()

input_date = DateEntry(app, width=12, background='black', foreground='white', borderwidth=2, year=now.year)
input_date.pack(pady=10)

Button(app, text= "Salvar", command= submit).pack()


app.mainloop()