from src import conexao, functions, tkinter

## main

validarDir('files/')
validarDir('files/csv')
validarDir('files/xlsx')

now = datetime.datetime.now()
func = functions.Functions()

app = Tk()
app.title('Gerar Relatorio')
app.geometry('300x150')
app.wm_maxsize(width=600, height=400)
app.wm_minsize(width=300, height=150)

text_1 = Label(app, text="Insira a placa")
text_1.pack()

input_text = Entry(app, width=12)
input_text.pack()

input_date = DateEntry(app, width=12, background='black', foreground='white', borderwidth=2, year=now.year, date_pattern="dd/mm/yyyy")
input_date.pack(pady=10)

Button(app, text= "Salvar", command=submit).pack()


app.mainloop()