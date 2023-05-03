import jogo_forca
import jogo_adivinha

print("="*45)
print("Escolha 1 para forca | 2 para adivinhação.")
print("="*45)

jogo = int(input("Qual jogo quer jogar?"))

if (jogo == 1):
    print("Você escolheu o jogo forca!")
    jogo_forca.forca()

elif (jogo == 2):
    print("Você escolheu o jogo adivinhação!")
    jogo_adivinha.adivinhacao()