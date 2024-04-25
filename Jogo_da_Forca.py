import random
from os import system, name

#Função para limpar a tela em cada rodada
def limpa_tela ():
   
    #windows
    if name == 'nt':
       _= system('cls')
    # Mac ou LINUX
    else:
        _= system('clear')  

#Função do jogo
def game():
    limpa_tela()
    print("\n Bem-vindo(a) ao Jogo da forca!")
    print("\n Adivinhe a palavra:")
    print("\n Tema do jogo frutas")

    #Lista de palavras para o jogo
    palavra= ["maçã", "banana", "laranja", "uva", "manga", "abacaxi", "morango",
          "melancia", "limão", "pera", "kiwi", "cereja", "pêssego", "abacate",
          "ameixa", "goiaba", "caqui", "figo", "melão", "pitaya", "tangerina",
          "jabuticaba", "carambola", "framboesa", "papaya", "mirtilo",
          "nectarina", "romã", "grapefruit", "maracujá"]
    #Escolhendo as palavra aleatórias
    palavra = random.choice(palavra)
    # List comprehensin
    letras_descobertas = ['_' for letra in palavra]
    #Tentativas
    chances = 6
    # Lista para letras erradas
    letras_erradas =[]
    # loop enquanto número de chances do usuario, for maior que 0
    while chances > 0:
        
        #print
        print("".join(letras_descobertas))
        print('\n Chances Restantes!', chances)
        print(' Letras Erradas:', ' '.join(letras_erradas))


        # Tentativas
        tentativas = input('\n Digite uma Letra ').lower()

        # Condicional
        if tentativas in palavra:
            index = 0
            for letra in palavra:
                if tentativas == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativas)

        # Condicional

        if "_" not in letras_descobertas:
            print("\n Você venceu, a palavra era:", palavra)
            
            break
    if "_" in letras_descobertas:
        print('\n Você perdeu, a palavra era:', palavra)
        
 

# Bloco main
if __name__ == "__main__":
    game()
    print('\n Parabéns, Você está aprendendo python!')
    input("\n Pressione Enter para jogar novamente..")
else:
    __name__ == "__main__",
game()


   