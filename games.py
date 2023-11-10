from adivinhacao import Adivinhacao
from forca import Forca

print('Escolha um jogo')
print('(1) Adivinhação (2) Forca')


game = int(input('Qual game tu quer jogar? '))

if(game == 1):
    Adivinhacao()
else:
    Forca()