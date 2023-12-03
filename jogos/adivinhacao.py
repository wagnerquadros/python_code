import random

def jogar():
    print("=================================")
    print("Bem vindo ao jogo de Adivinhação!")
    print("=================================")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qualo nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou: ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100, boca aberta!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print("Você acertou!")
            print("Pontuação:", pontos)
            break
        else:
            if maior:
                print("Errooooou!!!! O seu chute foi maior que o número secreto")
            elif menor:
                print("Errooooou!!!! O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("O número secreto era {}".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()