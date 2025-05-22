#roleta russa 
########################
import random
import time
from time import sleep
import os
import random
from pygame import mixer
########################
#audios do jogo 
def audio0():
    mixer.init()
    mixer.music.load("Py-Roulette/suspense.mp3")
    mixer.music.play(-1)
def audio1():
    mixer.init()
    mixer.music.load("Py-Roulette/roleta.mp3")
    mixer.music.play(2)
def audio2():
    mixer.init()
    mixer.music.load("Py-Roulette/shot.mp3")
    mixer.music.play()
def audio3():
    mixer.init()
    mixer.music.load("Py-Roulette/cock.mp3")
    mixer.music.play()
def audio4():
    mixer.init()
    mixer.music.load("Py-Roulette/happy.mp3")
    mixer.music.play(-4)
########################
#atalhos
def limpa():
    os.system("cls")
def p(*texto):
    print(*texto)    
def rand0n():
    return random.randint(1,6)
########################
#Codigos do Game

def jogo():
    limpa()
    audio0()
    p("-" * 10 , "Bem-Vindo ao Jogo" , "-" * 10)
    p("\n")
    p("O jogo consiste em uma roleta russa,voce escolhe um numero,")
    p("e se ele for sorteando você vai de vasco")
    p("\n")
    num = int(input("Escolha um numero ( 1 / 6 ) : "))
    if num <1 or num > 6:
        limpa()
        p("Numero invalido tente novamente")
        sleep(2)
        jogo()
    sleep(2)
    limpa()
    audio1()
    print("Girando tambor.")
    sleep(1)
    limpa()
    print("Girando tambor..")
    sleep(1)
    limpa()
    print("Girando tambor...")
    limpa()
    print("Girando tambor...")
    sleep(1)
    limpa()
    print("Girando tambor..")
    sleep(1)
    limpa()
    print("Girando tambor.")
    sleep(3)
    limpa()
    print("Puxando o gatilho...")
    audio3()
    sleep(2)
    limpa()
    disparo = rand0n()
    p("\n")
    p(f"Numero escolhido : 💀 {num} 💀")
    if num == disparo:
        audio2()
        p(f"💥 SE FUDEU OTÁRIO 💀, o disparo deu {disparo}")
        sleep(5)
        limpa()
        repetir()
    else:
        p(f"😅 Você se safou! O tambor parou no {disparo}")
        audio4()
        sleep(6)
        limpa()
        repetir()
def repetir():
    while True:
        resposta = input("Deseja jogar novamente? (S/N): ").lower()

        if resposta == "s":
            jogo()
            return True
        elif resposta == "n":
            limpa()
            p("Obrigado por jogar, vejo você em breve.")
            sleep(2)
            return False
        else:
            limpa()
            p("Você deve digitar apenas S ou N.")
            sleep(2)
            limpa()



jogo()
