# Sistemas de Informação
# POO - Programação Orientada a Objetos
# Equipe:
# - Raimundo Gonçalves de Sousa Júnior
# - José Gabriel de Oliveira Lima
# - Miqueias Alencar Oliveira
# - Pedro Oliveira Diniz campos

from tkinter import *
from tkinter import ttk
import tkinter
import pygame


def cadAlunos():
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import cadastrarAlunos
def cadMat():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import cadastrarMatricula
def cadTurma():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import cadastrarTurma
def atualizarAluno():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import atualizarAluno
def atualizarMat():
    import atualizarMatricula
def atualizarTurma():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import atualizarTurma
def listarAlunos():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import listarAlunos
def listarMat():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import listarMatriculas
def listarTurmas():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import listarTurmas
def deletarAlunos():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import deletarAluno
def deletarMat():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import deletarMatricula
def deletarTurma():    
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import deletarTurma

menuprincipal = Tk()
menuprincipal.iconbitmap('imagens/ifce.ico')
menuprincipal.title('IFCAD - Projeto Final')
# menuprincipal.iconbitmap('C:/Users/dream/Documents/Projetos PYTHON/PROJETO FINAL - POO/imagens/ifce.ico')
menuprincipal.geometry("860x250")
menuprincipal.resizable(False, False)
menuprincipal.config(bg = '#141514')

eqp = Label(menuprincipal, text='Equipe:\n- Junior\n- Gabriel\n- Miqueias\n- Pedro',
                      width=0,
                      height=5,
                      bg='#141514',
                      fg='white')
eqp.place(x = 730, y= 70)


'''label = Label(menuprincipal, text = 'teste', bg = "pink", bd = 5, justify = RIGHT, padx = 10, pady = 10)  
label.grid(row=0, column = 0, pady=10, padx=10)'''

botao = Button(menuprincipal,
               text='SISTEMA DE CADASTRO',
               bg = '#141514',
               fg = 'white',
               borderwidth = 1,
               width='20',
               height='2',
               bd = 0,
               pady=1)
botao.grid(row=0, column=0, pady = 10, padx = 10)

botao1 = Button(menuprincipal,
               text='Cadastrar Novo Aluno',
               bg = 'black',
               fg = 'white',
               borderwidth = 1,
               width='20',
               height='2',
               command=cadAlunos,
               pady=1)
botao1.grid(row=1, column=0, pady = 10, padx = 10)

botao2 = Button(menuprincipal, text='Atualizar Cadastro Aluno',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20',
                height='2',
                command=atualizarAluno)
botao2.grid(row=2, column=0, pady = 10, padx = 10)

botao3 = Button(menuprincipal, text='Listar Alunos Cadastrados',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20',
                height='2',
                command=listarAlunos)
botao3.grid(row=4, column=0, pady=10, padx= 10)

botao4 = Button(menuprincipal, text='Cadastrar Nova Turma',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20', 
                height='2',
                command=cadTurma)
botao4.grid(row=1, column=1, pady=10, padx= 10)

botao5 = Button(menuprincipal, text='Atualizar Cadastro Turma',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20', 
                height='2',
                command=atualizarTurma)
botao5.grid(row=2, column=1, pady=10, padx= 10)

botao6 = Button(menuprincipal, text='Listar Turmas Cadastrados',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20',
                height='2',
                command=listarTurmas)
botao6.grid(row=4, column=1, pady=10, padx= 10)

botao7 = Button(menuprincipal, text='Cadastrar Nova Matrícula',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20',
                height='2',
                command=cadMat)
botao7.grid(row=1, column=2, pady=10, padx= 10)

botao8 = Button(menuprincipal, text='Atualizar Matrícula',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20',
                height='2',
                command=atualizarMat)
botao8.grid(row=2, column=2, pady=10, padx= 10)

botao9 = Button(menuprincipal, text='Listar Matrículas',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20',
                height='2',
                command=listarMat)
botao9.grid(row=4, column=2, pady=10, padx= 10)

botao10 = Button(menuprincipal, text='Deletar Aluno',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                 width='20',
                 height='2',
                 command=deletarAlunos)
botao10.grid(row=1, column=3, pady=10, padx= 10)

botao11 = Button(menuprincipal, text='Deletar Turma',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                 width='20',
                 height='2',
                 command=deletarTurma)
botao11.grid(row=2, column=3, pady=10, padx= 10)

botao12 = Button(menuprincipal, text='Deletar Matrícula',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                 width='20',
                 height='2',
                 command=deletarMat)
botao12.grid(row=4, column=3, pady=10, padx= 10)

botao_fechar = Button(menuprincipal, text='Fechar',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                      width='20',
                      height='2', 
                      command= menuprincipal.destroy)
botao_fechar.grid(row=4, column= 5, pady=10, padx= 10)

menuprincipal.mainloop()



# numero mat do aluno lim = 20 numeros
# matricula nao aceita caso for memso num
# mas n importa o nome e data, podem ser os mesmos, o mesmo vale pra sexo.



