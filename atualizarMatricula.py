from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import messagebox
import pygame

def atualizar_Matricula():
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
        cursor.execute('''UPDATE matriculas set id_aluno=?, id_turma=?, ano=?, periodo=? where cod_matricula = ?''',
    (alunoMat, turmaMat, anoMat, periodoMat, codigoMat))
        cx.commit()  
        messagebox.showinfo('Cadastro', f'A matrícula {alunoMat} foi atualizada com sucesso na Turma {turmaMat}!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'A matrícula do aluno não foi atualizada')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()     
  
janela_atualizarMatricula = Tk()
janela_atualizarMatricula.title('Cadastro de Novos Alunos - IFCE')
janela_atualizarMatricula.config(bg = 'black')
janela_atualizarMatricula.geometry('230x340')

label1 = Label(janela_atualizarMatricula,
               bg = 'black',
               fg = 'white',  
               text = '  Informe o código de matrícula do aluno:')
label1.grid(row=0, column=0)
codigo_matricula = Entry(janela_atualizarMatricula)
codigo_matricula.grid(row= 1, column=0, pady=10, padx=10)

label2 = Label(janela_atualizarMatricula,
               bg = 'black', 
               fg = 'white', 
               text= 'Informe novo ID do aluno:')
label2.grid(row= 2, column=0) 
id_aluno = Entry(janela_atualizarMatricula)
id_aluno.grid(row= 3, column=0, pady=10, padx=10)

label3 = Label(janela_atualizarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe novo ID da Turma:')
label3.grid(row= 4, column=0)
id_Turma = Entry(janela_atualizarMatricula)
id_Turma.grid(row= 5, column=0)    

label4 = Label(janela_atualizarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o Ano:')
label4.grid(row= 6, column=0)
ano = Entry(janela_atualizarMatricula)
ano.grid(row= 7, column=0)

label5 = Label(janela_atualizarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Informe o período:\n(M, T ou N)')
label5.grid(row= 8, column=0)
periodo = Entry(janela_atualizarMatricula)
periodo.grid(row= 9, column=0)

botao = Button(janela_atualizarMatricula,
               bg = 'black',
               fg = 'white', 
               text= 'Atualizar Matrícula',
               command= atualizar_Matricula)
botao.grid(row= 13, column=0, pady = 10)

botao2 = Button(janela_atualizarMatricula,
                bg = 'black',
                fg = 'white', 
                text = 'Fechar',
                command = janela_atualizarMatricula.destroy)
botao2.grid(row=14, column=0)


janela_atualizarMatricula.mainloop()