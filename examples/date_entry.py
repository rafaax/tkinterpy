import sys
import pymysql
import datetime
sys.path.append('..')
from tkinter import *
from tkcalendar import Calendar, DateEntry
from src import conn


now = datetime.datetime.now()


def grad_date():
    data_formato_db = date_entry.get_date()
    date.config(text = data_formato_db)

app = Tk()
app.title('Gerar Relatorio')
app.geometry('600x400')
app.wm_maxsize(width=600, height=400)
app.wm_minsize(width=600, height=400)


rotulo = Label(app, text="Insira a placa")
rotulo.pack()

campo_texto = Entry(app, width=30)
campo_texto.pack()

date_entry = DateEntry(app, width=12, background='black', foreground='white', borderwidth=2, year=now.year)
date_entry.pack(pady=10)

Button(app, text= "Get Date", command= grad_date).pack()

date = Label(app, text="")
date.pack()

# query = 'SELECT placa, data_atualizacao, observacao, velocidade, pos_id, latitude, longitude FROM sau_posicionamento WHERE placa = "' + placa + '" AND date(data_atualizacao) = "' + data + '" ORDER BY data_atualizacao DESC'
# cursor.execute(query)

app.mainloop()