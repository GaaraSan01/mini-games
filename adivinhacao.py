import random

def Adivinhacao():
    game = '***** Bem vindo ao jogo de adivinhação! *****'
    print(len(game) * '*')
    print(game)
    print(len(game) * '*')
    #Regras do jogo
    secret_number_float = random.randrange(1,101)
    secret_number = round(secret_number_float)
    total_rodait = 3
    rodait = 1
    point = 1000

    # Nivel de dificuldade
    print('Escolha o nivel de dificuldade')
    print('(1) Facil, (2) Medio, (3) Dificil')
    nivel = int(input('Dificuldade: '))

    if(nivel == 1):
        total_rodait = 20
    elif(nivel == 2):
        total_rodait = 10
    else:
        total_rodait = 5
    for rodait in range(1, total_rodait + 1):
        rodadas = f'Total de tentativas: {rodait}:{total_rodait}'
        print(len(rodadas) * '-')
        print(rodadas)
        print(len(rodadas) * '-')

        pontuacao = f'Pontuação total: {point}'
        print(len(pontuacao) * '-')
        print(pontuacao)
        print(len(pontuacao) * '-')

        kick = input('Digite um numero entre 1 e 100: ')
        convertion_kick = int(kick)

        #Validações do jogo
        validation = convertion_kick == secret_number
        error_up = convertion_kick > secret_number

        if(convertion_kick < 1 or convertion_kick > 100):
            print('Você deve digitar um numero entre 1 e 100')
            continue

        if(validation):
            print('Você acertou!')
            break
        else:
            if(error_up):
                print('Você errou! Digitou um numero acima')
            else:
                print('Você errou! Digitou um numero abaixo.')
            point_decreament = abs(convertion_kick - secret_number)
            point = point - point_decreament

    print('Fim do jogo')

if(__name__ == '__main__'):
    Adivinhacao()