from tkinter import *
from sqlite3 import dbapi2
from tkinter import *
from tkinter import messagebox
import sqlite3
import pygame

def deletar_Aluno():
    pygame.init()
    pygame.mixer.music.load('sons\sound-2.mp3')
    pygame.mixer.music.play()
    try:
        nid = numero_id.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute(f'''delete from alunos where id = {nid};''')
        cx.commit()          
        messagebox.showinfo('Cadastro deletado!', f'O cadastro de {nid} foi deletado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do aluno não foi deletado.')
        cx.rollback()
    finally:
        cursor.close()       
        cx.close()  

janela_deletar = Tk()
janela_deletar.title('Deletar Aluno')
janela_deletar.geometry('250x100')
janela_deletar.config(bg = 'black')

label = Label(janela_deletar,
              bg = 'black',
              fg = 'white', 
              text='Informe o ID do aluno para deletar')
label.pack()
numero_id = Entry(janela_deletar)
numero_id.pack()

botao = Button(janela_deletar,
               text = 'Deletar Aluno',
               bg = 'black',
               fg = 'white', 
               command = deletar_Aluno)
botao.pack()

botao2 = Button(janela_deletar,
                text = 'Fechar',
                bg = 'black',
                fg = 'white', 
                command = janela_deletar.destroy)
botao2.pack()

janela_deletar.mainloop()