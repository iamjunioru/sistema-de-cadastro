# Sistemas de Informação
# POO - Programação Orientada a Objetos
# Equipe:
# - Raimundo Gonçalves de Sousa Júnior
# - José Gabriel de Oliveira Lima
# - Miqueias Alencar Oliveira
# - Pedro Oliveira Diniz campos

# (inicie o programa por aqui para ter a experiência completa.) :)
# * Menu Principal *

import tkinter # biblioteca usada para desenvolver a interface.
from tkinter import *
import pygame # biblioteca de jogos, usada para colocar a música de fundo no menu.

def menu():
    pygame.init()
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import main
def sobre():
    pygame.mixer.music.load('sons\sound-1.mp3')
    pygame.mixer.music.play()
    import equipe

menu_principal = Tk()
menu_principal.iconbitmap('imagens/ifce.ico') # icone no topo da janela
menu_principal.title('IFCECAD - Menu Principal') # texto do topo da janela
# menu_principal.wm_attributes('-fullscreen','true') # deixa tela em fullcreen sem bordas
# menu_principal.overrideredirect(True) # tira a tira barra de titulo
menu_principal.geometry('400x350') # dimensão da janela
menu_principal.resizable(False, False) # não maximizar janela

menu_principal.config(background = "#054900") # cor do frame do background

# logo
logo = PhotoImage(file="imagens/logo.png")
logo = logo.subsample(5, 5)
figura1 = Label(image = logo, bg = "#054900")



botao1 =  Button(menu_principal,
                 text = "● ENTRAR ●",
                 font = ("Arial Black", 15),
                 bg = "#054900",
                 fg = 'white',
                 bd = 0,
                 highlightthickness = 0,
                 command = menu,) # font = ("Georgia", 18)
botao2 =  Button(menu_principal, text = "SOBRE NÓS",
                 font = ("Arial", 13),
                 bg = '#054900',
                 fg = 'white',
                 bd = 0,
                 highlightthickness = 0,
                 command = sobre)
figura1.grid(row = 0, column = 0, padx = (50,0))
botao1.grid(row = 1, column= 0, padx = (50, 0), pady = (10,0))
botao2.grid(row = 2, column= 0, padx = (50, 0), pady = (10,0))


pygame.init()
pygame.mixer.music.load('sons\konohapeace.mp3')
pygame.mixer.music.play()

print('POO - PROJETO FINAL')
print('''Equipe:
- Raimundo Gonçalves de Sousa Júnior
- José Gabriel de Oliveira Lima
- Miqueias Alencar Oliveira
- Pedro Oliveira Diniz campos''')
print('')
print('▶▶▶\n[A música está tocando]')
print('')
print('▶▶▶\n[Feche a janela para parar a música]')

menu_principal.mainloop()
