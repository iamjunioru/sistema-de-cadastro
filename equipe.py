import tkinter
from tkinter import *
from tkinter import ttk
import tkinter
# from webbrowser import Chrome


'''def callback():
    Chrome.open_new("https://www.google.com")'''
    
sobre = Tk()
sobre.iconbitmap('imagens/ifce.ico')
sobre.title("Sobre nós  :)")
sobre.geometry("390x300")
sobre.config(background="#054900")
sobre.resizable(False, False)

botao1 =  Button(sobre, text = "EQUIPE",
                 font = ("Arial Black", 15),
                 bg = "#054900",
                 fg = 'white',
                 bd = 0,
                 highlightthickness = 0) # font = ("Georgia", 18)
botao2 =  Button(sobre, text = '''●●●●●●●●●●
Raimundo Gonçalves de Sousa Júnior
José Gabriel de Oliveira Lima
Miqueias Alencar Oliveira
Pedro Oliveira Diniz campos
●●●●●●●●●●''',
                 font = ("Arial", 13),
                 bg = "#054900",
                 fg = 'white',
                 bd = 0,
                 highlightthickness = 0)

'''botao3 = Button(text="Repositório no GitHub",
                bg = 'white',
                fg = '#054900',
                bd = 0,
                command=callback)
botao3.grid(column=0, row=14, padx = (52, 0), pady = (15,0))'''

botao3 =  Button(sobre, text = "\nProgramação Orientada a Objetos\nProfessor da Disciplina:\nManoel Marisergio",
                 font = ("Arial", 10),
                 bg = "#054900",
                 fg = 'white',
                 bd = 0,
                 highlightthickness = 0)
botao3.grid(row = 3, column= 0, padx = (52, 0), pady = (15,0))

botao1.grid(row = 1, column= 0, padx = (52, 0), pady = (15,0))
botao2.grid(row = 2, column= 0, padx = (50, 0), pady = (15,0))


sobre.mainloop()