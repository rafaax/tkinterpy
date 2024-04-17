from tkinter import *
from tkcalendar import Calendar
import src.conn as conn
import pymysql
import datetime

now = datetime.datetime.now()


def grad_date():
    data_formatada = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y").strftime("%Y-%m-%d")
    date.config(text = "Selected Date is: " + data_formatada)


conn = pymysql.connect(host=conn.host, user=conn.user, password=conn.passw, database=conn.db,charset='utf8')
cursor = conn.cursor()

app = Tk()
app.title('Gerar Relatorio')
app.geometry('600x400')
app.wm_maxsize(width=600, height=400)
app.wm_minsize(width=600, height=400)


rotulo = Label(app, text="Insira a placa")
rotulo.pack()

campo_texto = Entry(app, width=30)
campo_texto.pack()

cal = Calendar(app, selectmode = 'day',
               year = now.year, month = now.month,
               day = now.day)
cal.pack(pady=10)

Button(app, text = "Get Date", command = grad_date).pack()

date = Label(app)
date.pack()
# query = 'SELECT placa, data_atualizacao, observacao, velocidade, pos_id, latitude, longitude FROM sau_posicionamento WHERE placa = "' + placa + '" AND date(data_atualizacao) = "' + data + '" ORDER BY data_atualizacao DESC'
# cursor.execute(query)

app.mainloop()