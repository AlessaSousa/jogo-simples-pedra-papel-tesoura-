import random
from tkinter import *


def jogar(jogador):
    opcoes = ["pedra","papel","tesoura"]
    computador = random.choice(opcoes)
    resultado = ""
    
    if jogador == computador:
        resultado = "Empate!"
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
         resultado = "Você venceu"  
    else:
        resultado = "O computador venceu"   
        
    textoResult.config(text=resultado)
    
janela = Tk()
janela.title("Jan Ken Po")
janela.geometry("400x400")

texto = Label(janela, text="Clique em um dos botôes")
texto.config(bg='lightgray', font=('Arial',14))
texto.grid(column = 0, row = 0, padx = 10, pady = 10)

botao = Button(janela, text = "pedra", command = lambda: jogar("pedra"))
botao.config(bg='white', font=('Arial',14))
botao.grid(column = 0, row = 1, padx = 10, pady = 10)


botao2 = Button(janela, text = "papel", command = lambda: jogar("papel"))
botao2.config(bg='white', font=('Arial',14))
botao2.grid(column = 0, row = 2, padx = 10, pady = 10)

botao3 = Button(janela, text = "tesoura", command = lambda: jogar("tesoura"))
botao3.config(bg='white', font=('Arial',14))
botao3.grid(column = 0, row = 3, padx = 10, pady = 10)

textoResult = Label(janela, text="", bg='lightgray', font=('Arial', 14, 'italic'))
textoResult.grid(column = 0, row = 4, padx=10, pady=10)

janela.mainloop()
