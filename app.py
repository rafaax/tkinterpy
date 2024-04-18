import sys
import pymysql
import datetime
import pprint
from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar, DateEntry
from src import conexao
from mysql.connector import connect


def submit():

    conn = connect(user=conexao.user, password=conexao.passw, host=conexao.host, database=conexao.db)
    
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

    cursor = conn.cursor()

    query = 'SELECT equi_id from sau_veiculos where placa = %s limit 1'
    cursor.execute(query, (placa, ))

    result = cursor.fetchone()

    if result:
        equipament_id = result[0]
        
        def close_loading():
            loading_page.destroy()
            
        loading_page = Tk()
        loading_page.title("Loading Page")
        loading_page.geometry("300x200")
        loading_page.resizable(False, False)

        loading_label = ttk.Label(loading_page, text="Carregando...", font=("Arial", 14))
        loading_label.pack(pady=50)

        progress_bar = ttk.Progressbar(loading_page, length=200, mode='indeterminate')
        progress_bar.pack()
        
        loading_page.after(5000, close_loading)
        progress_bar.start(10)

        

        # query = 'SELECT placa, data_atualizacao, observacao, velocidade, pos_id, latitude, longitude FROM sau_posicionamento WHERE placa = "' + placa + '" AND date(data_atualizacao) = "' + data_input + '" ORDER BY data_atualizacao DESC'
        # cursor.execute(query)
        
    else:
        messagebox.showerror("Erro", "Placa não é valida!")


    

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