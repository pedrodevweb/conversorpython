# -*- coding: utf-8 -*-
"""python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A4UAKh54Kk5qPnKyHFl8M3eol0y36VYU
"""

import time
print("Eu sou uma IA e irei de guiar :)")
time.sleep(0.5)
print("Consigo converter todas unidades do SI")
time.sleep(0.5)
print("Com o objetivo de deixar a experiência mais interativa digite seu nome:")
nome = input()
time.sleep(0.5)
print("Olá {}, qual unidade deseja converter?".format(nome))
time.sleep(0.2)

print("Tempo - 1")
time.sleep(0.2)

print("Massa - 2")
time.sleep(0.2)

print("Quantidade de matéria - 3")
time.sleep(0.2)

print("Corrente elétrica - 4")
time.sleep(0.2)

print("Comprimento - 5")
time.sleep(0.2)

print("Intensidade luminosa - 6")
time.sleep(0.2)

print("Temperatura - 7")
time.sleep(0.2)

print("{}, digite o código correspondente :)".format(nome))
codigo = int(input())

time.sleep(0.2)

if codigo == 1:
    print("Ebaaaa, o tempo é minha unidade favorita")
    time.sleep(0.2)
    print("Digite o valor do tempo")
    time.sleep(0.2)
    tempo = float(input())
    time.sleep(0.2)
    print("Agora meu amigo {}, escolha qual transformação quer fazer:".format(nome))
    time.sleep(0.2)

    print("Segundos para Minutos - 1")
    time.sleep(0.2)

    print("Minutos para Horas - 2")
    time.sleep(0.2)

    print("Segundos para Horas - 3")
    time.sleep(0.2)

    print("Horas para Segundos - 4")
    time.sleep(0.2)

    inf = input()
    if inf == 1:
        min = tempo/60
        print("{}, {} segundos são equivalentes a {} minutos".format(nome, tempo, min))
        print("Deseja fazer outra operação ou quer finalizar?")
        print("1 - Finalizar")
        print("2 - Outra operação")
        de = input()
        if de == 1:
            print("Okay, até a próxima {}".format(nome))

        if de == 2:
            print("Okay, voltando ao menu anterior")

    if inf == 2:
        min = tempo/60
        print("{}, {} minutos são equivalentes a {} horas".format(nome, tempo, min))
        print("Deseja fazer outra operação ou quer finalizar?")
        print("1 - Finalizar")
        print("2 - Outra operação")
        de = input()
        if de == 1:
            print("Okay, até a próxima {}".format(nome))

        if de == 2:
            print("Okay, voltando ao menu anterior")

    if inf == 3:
        min = tempo/3600
        print("{}, {} segundos são equivalentes a {} horas".format(nome, tempo, min))
        print("Deseja fazer outra operação ou quer finalizar?")
        print("1 - Finalizar")
        print("2 - Outra operação")
        de = input()
        if de == 1:
            print("Okay, até a próxima {}".format(nome))

        if de == 2:
            print("Okay, voltando ao menu anterior")

    if inf == 4:
        min = tempo*3600
        print("{}, {} horas são equivalentes a {} segundos".format(nome, tempo, min))
        print("Deseja fazer outra operação ou quer finalizar?")
        print("1 - Finalizar")
        print("2 - Outra operação")
        de = input()
        if de == 1:
            print("Okay, até a próxima {}".format(nome))

        if de == 2:
            print("Okay, voltando ao menu anterior")

if codigo == 2:
    time.sleep(0.2)
    print("Uhummm, escolheu massa né rsrsrs")
    time.sleep(0.2)
    print("Acho que tem alguém preocupado com o peso ein")
    time.sleep(0.2)
    print("rsrsrs")
    time.sleep(0.2)
