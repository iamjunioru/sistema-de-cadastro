from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import *
from tkinter import messagebox
import pygame

def criar_Turma():
    pygame.init()
    pygame.mixer.music.load('sons\sound-2.mp3')
    pygame.mixer.music.play()
    try:
        idturma = id_turma.get()
        codturma = codigo.get()
        nturma = nome.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute('''insert into turmas (id, codigo_turma, nome_turma) values (?,?,?)''',(idturma, codturma, nturma))
        cx.commit()  
        messagebox.showinfo('Cadastro Turma', f'O cadastro da turma {nturma} foi realizado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro da turma não foi realizado.')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()  


Janela_criarTurma = Tk()
Janela_criarTurma.title('Criar Nova Turma')
Janela_criarTurma.geometry('260x210')
Janela_criarTurma.config(bg = 'black')


label = Label(Janela_criarTurma,
              bg = 'black',
              fg = 'white', 
              text='Informe o ID da turma')
label.pack()
id_turma = Entry(Janela_criarTurma)
id_turma.pack()

label2 = Label(Janela_criarTurma,
               bg = 'black',
               fg = 'white', 
               text='Informe o código da turma')
label2.pack()
codigo = Entry(Janela_criarTurma)
codigo.pack()

label3 = Label(Janela_criarTurma,
               bg = 'black',
               fg = 'white', 
               text='Informe o nome da turma')
label3.pack()
nome = Entry(Janela_criarTurma)
nome.pack()

botao = Button(Janela_criarTurma,
               bg = 'black',
               fg = 'white', 
               text= 'Criar Nova Turma',
               command= criar_Turma)
botao.pack(pady = 10)

botao2 = Button(Janela_criarTurma,
                bg = 'black',
                fg = 'white', 
                text = 'Fechar',
                command = Janela_criarTurma.destroy)
botao2.pack()

Janela_criarTurma.mainloop()