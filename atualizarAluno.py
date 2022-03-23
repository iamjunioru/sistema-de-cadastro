from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import messagebox
import pygame


def atualizarAluno():
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
        cursor.execute('''UPDATE alunos SET nome = ?, nascimento = ?, sexo = ? where id = ?''',  (naluno, dnasc, saluno, nid))
        cx.commit()  
        messagebox.showinfo('Atualizar Cadastro', f'O cadastro do(a) aluno(a) {naluno} foi atualizado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do aluno não foi atualizado')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()

janela_atualizar = Tk()
janela_atualizar.title('Area de Cadastro de Novos Alunos - IFCE')
janela_atualizar.geometry('280x250')
janela_atualizar.config(bg = 'black')

label1 = Label(janela_atualizar,
               text= 'Informe o número do aluno para alterar:',
               fg='white',
               bg='black')
label1.grid(row=0, column=0)
numero_id = Entry(janela_atualizar,
                  bg='white',
                  fg='green')
numero_id.grid(row= 1, column=0)
label2 = Label(janela_atualizar,
               text= 'Informe o novo nome do aluno:',
               fg='white',
               bg='black')
nome_aluno = Entry(janela_atualizar,
                   fg = 'green',
                   bg = 'white')
label2.grid(row= 2, column=0) 
nome_aluno.grid(row= 3, column=0)

label3 = Label(janela_atualizar,
               text= 'Informe a nova data de nascimento(dd/mm/aaaa):',
               fg='white',
               bg='black')
label3.grid(row= 4, column=0)
data_nascimento = Entry(janela_atualizar,
                        fg = 'green',
                        bg = 'white')
data_nascimento.grid(row= 5, column=0)    

label4 = Label(janela_atualizar,
               text= 'Informe o novo sexo do aluno(F/M/O):',
               fg='white',
               bg='black')
label4.grid(row= 6, column=0)
sexo_aluno = Entry(janela_atualizar,
                   fg = 'green',
                   bg = 'white')
sexo_aluno.grid(row= 7, column=0)

botao = Button(janela_atualizar,
               text= 'Atualizar Aluno', 
               fg='white', 
               bg='black',
               command= atualizarAluno)
botao.grid(row = 13, column = 0, pady = 10)

botao2 = Button(janela_atualizar,
                text = 'Fechar',
                fg='white',
                bg='black',
                command = janela_atualizar.destroy)
botao2.grid(row=14, column=0)



janela_atualizar.mainloop()