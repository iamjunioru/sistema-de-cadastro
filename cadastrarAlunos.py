from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import messagebox
import pygame

def executar():
    pygame.init()
    pygame.mixer.music.load('sons\sound-2.mp3')
    pygame.mixer.music.play()
    try:
        nid = numero_id.get()
        naluno = nome_aluno.get()
        dnasc = data_nascimento.get()
        saluno = sexo_aluno.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute('''insert into alunos (id, nome, nascimento, sexo) values (?,?,?,?)''', (nid, naluno, dnasc, saluno))
        cx.commit()  
        messagebox.showinfo('Cadastro', f'O cadastro do(a) aluno(a) {naluno} foi realizado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do aluno não foi realizado.')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()     
  
janela_adicionar = Tk()
janela_adicionar.title('Cadastro de Novos Alunos - IFCE')
janela_adicionar.geometry('230x280')
janela_adicionar.config(bg = 'black')


label1 = Label(janela_adicionar,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o número de matrícula do aluno:')
label1.grid(row=0, column=0,) # padx = (50, 0)
numero_id = Entry(janela_adicionar)
numero_id.grid(row= 1, column=0)
label2 = Label(janela_adicionar,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o nome do aluno:')
nome_aluno = Entry(janela_adicionar)
label2.grid(row= 2, column=0) 
nome_aluno.grid(row= 3, column=0)

label3 = Label(janela_adicionar,
               bg = 'black',
               fg = 'white', 
               text= 'Informe a data de nascimento:\n(DD/MM/AAAA)')
label3.grid(row= 4, column=0)
data_nascimento = Entry(janela_adicionar)
data_nascimento.grid(row= 5, column=0)    

label4 = Label(janela_adicionar,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o sexo do aluno:\n(M/F/O)')
label4.grid(row= 6, column=0)
sexo_aluno = Entry(janela_adicionar)
sexo_aluno.grid(row= 7, column=0)

botao = Button(janela_adicionar,
               bg = 'black',
               fg = 'white', 
               text= 'Adicionar Aluno', command= executar)
botao.grid(row= 13, column=0, pady = 10)

botao2 = Button(janela_adicionar,
                bg = 'black',
                fg = 'white', 
                text = 'Fechar',
                command = janela_adicionar.destroy)
botao2.grid(row=14, column=0)



janela_adicionar.mainloop()