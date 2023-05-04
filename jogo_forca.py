#iniciando um novo projjeto de jogo

def forca():
    print("=" * 20)
    print("Jorgo da forca")
    print("=" * 20)

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    jogada = ""
    palavra = []

    while ( not enforcou and not acertou):
        jogada = str(input("Qual letra? ")).lower()
        print("jogando....")

        if (jogada in palavra_secreta):
            print("Você acertou!!")
            index = 0

            for letra in palavra_secreta:
                if jogada == letra:
                    print(f"Encontrei a letra {jogada} na posição {index + 1}")
                index += 1
            
            


        elif (jogada != palavra_secreta):
            print("Você errou!")

        
                

if (__name__ == "__main__"):
    forca()