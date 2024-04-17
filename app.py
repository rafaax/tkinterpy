import sys
import pymysql
import datetime
import pprint
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from src import conexao
from mysql.connector import connect


def submit():

    conn = pymysql.connect(host=conexao.host, user=conexao.user, password=conexao.passw, database=conexao.db,charset='utf8')
    cursor = conn.cursor()

    data = input_date.get_date()
    placa = input_text.get()
    
    if not placa:
        messagebox.showwarning("Erro", "Por favor insira alguma placa válida.")
        return False

    placa = placa.replace('-', '') # removendo o traço da string para nao haver conflito

    data_hoje = now.strftime("%Y-%m-%d")
    data_input = data.strftime("%Y-%m-%d")
    
    if data_input > data_hoje:
        messagebox.showerror("Erro", "Data inserida não é valida por ser maior que a data atual!")
        return False

    query = 'SELECT * from sau_veiculos where placa = "' + placa + '" limit 1'
    cursor.execute(query)
    results = cursor.fetchone()
    for r in results:
        print(r)
    # print(results)
    #query = 'SELECT placa, data_atualizacao, observacao, velocidade, pos_id, latitude, longitude FROM sau_posicionamento WHERE placa = "' + placa + '" AND date(data_atualizacao) = "' + data_input + '" ORDER BY data_atualizacao DESC'
    # cursor.execute(query)

    # results = cursor.fetchall()
    # pprint.pprint(results)
    


now = datetime.datetime.now()

app = Tk()
app.title('Gerar Relatorio')
app.geometry('600x400')
app.wm_maxsize(width=600, height=400)
app.wm_minsize(width=600, height=400)

text_1 = Label(app, text="Insira a placa")
text_1.pack()

input_text = Entry(app, width=12)
input_text.pack()

input_date = DateEntry(app, width=12, background='black', foreground='white', borderwidth=2, year=now.year, date_pattern="dd/mm/yyyy")
input_date.pack(pady=10)

Button(app, text= "Salvar", command=submit).pack()


app.mainloop()