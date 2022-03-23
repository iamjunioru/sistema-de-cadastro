from tkinter import *
from sqlite3 import dbapi2
from tkinter import *
from tkinter import messagebox
import sqlite3
import pygame

def deletar_Matricula():
    pygame.init()
    pygame.mixer.music.load('sons\sound-2.mp3')
    pygame.mixer.music.play()
    try:
        codmat = codigo_Matricula.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute(f'''delete from matriculas where cod_matricula = {codmat};''')
        cx.commit()          
        messagebox.showinfo('Cadastro deletado!', f'O cadastro de {codmat} foi deletado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do aluno não foi deletado.')
        cx.rollback()
    finally:
        cursor.close()       
        cx.close()  

janela_deletarMatricula = Tk()
janela_deletarMatricula.title('Deletar Matrícula')
janela_deletarMatricula.geometry('250x100')
janela_deletarMatricula.config(bg = 'black')

label = Label(janela_deletarMatricula,
              bg = 'black',
              fg = 'white', 
              text='Informe o código da matrícula para deletar')
label.pack()
codigo_Matricula = Entry(janela_deletarMatricula)
codigo_Matricula.pack()

botao = Button(janela_deletarMatricula,
               text= 'Deletar Matrícula',
               bg = 'black',
               fg = 'white', 
               command= deletar_Matricula)
botao.pack()

botao2 = Button(janela_deletarMatricula,
                text = 'Fechar',
                bg = 'black',
                fg = 'white', 
                command = janela_deletarMatricula.destroy)
botao2.pack()

janela_deletarMatricula.mainloop()