#roleta russa 
########################
import time
from time import sleep
import os
import random
from pygame import mixer
########################
#audios do jogo 
mixer.init()
def audio0():
    mixer.music.load("Py-Roulette/suspense.mp3")
    mixer.music.play(-1)
def audio1():
    mixer.music.load("Py-Roulette/roleta.mp3")
    mixer.music.play(2)
def audio2():
    mixer.music.load("Py-Roulette/shot.mp3")
    mixer.music.play()
def audio3():
    mixer.music.load("Py-Roulette/cock.mp3")
    mixer.music.play()
def audio4():
    mixer.init()
    mixer.music.load("Py-Roulette/happy.mp3")
    mixer.music.play(-4)
def audio5():
    mixer.music.load("Py-Roulette/soviet.mp3")
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
    while True:
        try:
            num = int(input("Escolha um numero ( de 1 a 6 ) : "))
            if 1 <= num <= 6:
                break
            else:
                limpa()
                print("❌ Por favor, escolha um número entre 1 e 6.")
                sleep(2)
                limpa()
        except ValueError:
            limpa()
            print("Digite apenas números!")
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
        sleep(0.7)
        audio5()
        sleep(5)
        limpa()
        
    else:
        p(f"😅 Você se safou! O tambor parou no {disparo}")
        audio4()
        sleep(6)
        limpa()
        
def repetir():
    while True:
        jogo()
        while True: 
            resposta = input("Deseja jogar novamente? (S/N): ").lower()

            if resposta == "s":
                limpa()
                break
            elif resposta == "n":
                limpa()
                p("Obrigado por jogar, vejo você em breve.")
                sleep(2)
                limpa()
                return
            else:
                limpa()
                p("Você deve digitar apenas S ou N.")
                sleep(2)
                limpa()
            

repetir()
