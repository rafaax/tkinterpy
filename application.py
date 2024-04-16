from tkinter import *
from tkcalendar import Calendar
import src.conn as conn
import pymysql

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())


conn = pymysql.connect(host=conn.host, user=conn.user, password=conn.passw, database=conn.db,charset='utf8')
cursor = conn.cursor()

app = Tk()
app.title('Gerar Relatorio')
app.geometry('600x400')
app.wm_maxsize(width=600, height=400)
app.wm_minsize(width=600, height=400)

cal = Calendar(app, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)

cal.pack(pady = 20)


Button(app, text = "Get Date",
       command = grad_date).pack(pady = 20)

date = Label(app, text = "")

rotulo = Label(app, text="Insira a placa")
rotulo.pack()

campo_texto = Entry(app, width=30)
campo_texto.pack()
# query = 'SELECT placa, data_atualizacao, observacao, velocidade, pos_id, latitude, longitude FROM sau_posicionamento WHERE placa = "' + placa + '" AND date(data_atualizacao) = "' + data + '" ORDER BY data_atualizacao DESC'
# cursor.execute(query)

app.mainloop()