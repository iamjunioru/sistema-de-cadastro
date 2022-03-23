from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import messagebox
import pygame

def matricular_Aluno():
    pygame.init()
    pygame.mixer.music.load('sons\sound-2.mp3')
    pygame.mixer.music.play()
    try:
        codigoMat = codigo_matricula.get()
        alunoMat = id_aluno.get()
        turmaMat = id_Turma.get()
        anoMat = ano.get()
        periodoMat = periodo.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute('''insert into matriculas (cod_matricula, id_aluno, id_turma, ano, periodo) values (?,?,?,?,?)''',
    (codigoMat, alunoMat, turmaMat, anoMat, periodoMat))
        cx.commit()  
        messagebox.showinfo('Cadastro', f'A matrícula {alunoMat} foi realizado com sucesso na turma {turmaMat}!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'A matrícula do aluno não foi realizada.')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()     
  
janela_cadastrarMatricula = Tk()
janela_cadastrarMatricula.title('Matricular Aluno - IFCE')
janela_cadastrarMatricula.geometry('230x300')
janela_cadastrarMatricula.config(bg = 'black')

label1 = Label(janela_cadastrarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o código de matrícula do aluno:')
label1.grid(row=0, column=0)
codigo_matricula = Entry(janela_cadastrarMatricula)
codigo_matricula.grid(row= 1, column=0)

label2 = Label(janela_cadastrarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe ID do aluno:')
label2.grid(row= 2, column=0) 
id_aluno = Entry(janela_cadastrarMatricula)
id_aluno.grid(row= 3, column=0)

label3 = Label(janela_cadastrarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe ID da turma:')
label3.grid(row= 4, column=0)
id_Turma = Entry(janela_cadastrarMatricula)
id_Turma.grid(row= 5, column=0)    

label4 = Label(janela_cadastrarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o ano:')
label4.grid(row= 6, column=0)
ano = Entry(janela_cadastrarMatricula)
ano.grid(row= 7, column=0)

label5 = Label(janela_cadastrarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o período:\n(M)Manhã - (T)Tarde - (N)Noite')
label5.grid(row= 8, column=0)
periodo = Entry(janela_cadastrarMatricula)
periodo.grid(row= 9, column=0)

botao = Button(janela_cadastrarMatricula,
               text= 'Matricular Aluno',
               bg = 'black',
               fg = 'white',
               command= matricular_Aluno)
botao.grid(row = 13, column = 0, pady = 10)

botao2 = Button(janela_cadastrarMatricula,
                text = 'Fechar',
                bg = 'black',
                fg = 'white',
                command = janela_cadastrarMatricula.destroy)
botao2.grid(row = 14, column = 0)


janela_cadastrarMatricula.mainloop()