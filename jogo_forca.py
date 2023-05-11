#iniciando um novo projjeto de jogo

def forca():
    print("=" * 20)
    print("Jorgo da forca")
    print("=" * 20)

    palavra_secreta = "pneumoultramicroscopicossilicovulcanoconiótico"
    enforcou = False
    acertou = False
    jogada = ""
    palavra = []
    for i in range(0, len(palavra_secreta)):
        palavra.append("")
    print(palavra)

    
    #palavra = ["", "", "", "", "", "", "", ""]

    while ( not enforcou and not acertou):
        jogada = str(input("Qual letra? ")).strip(" ").lower()[0]
        print("jogando....")

        if (jogada in palavra_secreta):
            print("Você acertou!!")
            index = 0

            for letra in palavra_secreta:
                if jogada == letra:
                    print(f"Encontrei a letra {jogada} na posição {index + 1}")
                    palavra[index] = jogada
                index += 1
                
            
            


        elif (jogada != palavra_secreta):
            print("Você errou!")

        print(palavra)
                

if (__name__ == "__main__"):
    forca()