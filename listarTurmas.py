from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import ttk
import pygame

def lerListaTurmas():
    pygame.init()
    pygame.mixer.music.load('sons\sound-2.mp3')
    pygame.mixer.music.play()
    try:
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        dados_Turma = cursor.execute('select * from turmas;')
        rows = dados_Turma.fetchall()
        for row in rows:
            tree.insert('', END, values = row)
    finally:
        cursor.close()
        cx.close()

janela_lerTurma = Tk()
janela_lerTurma.title('Lista das Turmas Ofertadas - IFCE')
janela_lerTurma.config(bg = 'light green', bd = 10)

tree = ttk.Treeview(janela_lerTurma,
                    column=('c1', 'c2', 'c3'),
                    show ='headings')  
tree.column('#1')
tree.heading('#1', text = 'ID Turma')
tree.column('#2')
tree.heading('#2', text = 'Código Turma')
tree.column('#3')
tree.heading('#3', text = 'Nome da Turma')


tree.pack()

button = Button(janela_lerTurma, text ='Ver lista das turmas',
                bg = 'light green',
                fg = 'green',
                bd = 0,
                command = lerListaTurmas)
button.pack()
button1 = Button(janela_lerTurma, text='Fechar',
                 bg = 'light green',
                 fg = 'green',
                 bd = 0,
                 command= janela_lerTurma.destroy).pack()

janela_lerTurma.mainloop()
