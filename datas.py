from tkinter import *
from tkinter import messagebox
import sshtunnel
import mysql.connector

root = Tk()

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='xxxxxxxxxxx', ssh_password='xxxxxxxxxxx',
    remote_bind_address=('xxxxxxxxxxxxxxxxxxxx', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='xxxxxxxxxxxxx', password='xxxxxxxxxxxxxx',
        host='xxxxxxxxxxxx', port=tunnel.local_bind_port,
        database='xxxxxxxxxxxxxxx',
    )

    ##Use this commands in the first time you run and then delete this
    c = connection.cursor()
    c.execute("CREATE TABLE provas (name VARCHAR(250), day VARCHAR(250), cont VARCHAR(250))")
    ###########################################################################################


    def add():

        materia = clicked.get()

        c = connection.cursor()

        ins = "INSERT INTO provas (name, day, cont) VALUES (%s, %s, %s)"
        val = (materia, data.get(), trabalho.get())
        c.execute(ins, val)

        connection.commit()

        messagebox.showinfo('Suceeso', 'Adicionado com Sucesso!')
        trabalho.delete(0, 'end')
        data.delete(0, 'end')


    lMat = Label(root, text="Matéria:")

    options = [

        'Química',
        'Biologia',
        'Matemática',
        'Português',
        'Literatura',
        'Espanhol',
        'Inglês',
        'Geografia',
        'Filosofia',
        'Sociologia',
        'Ed. Física',
        'Física',
        'História'

    ]

    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(root, clicked, *options)


    lTrab = Label(root, text="Conteúdo:")
    trabalho = Entry(root, width=30)

    lData = Label(root, text="Data:")
    data = Entry(root, width=30)

    btn = Button(root, text='Adicionar', command=add)

    lMat.pack()
    drop.pack()
    lTrab.pack()
    trabalho.pack()
    lData.pack()
    data.pack()
    btn.pack()


    root.mainloop()
    connection.close()


