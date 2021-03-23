import jogo_forca as forca
import jogo_adivinhacao as adiv

def escolha_jogos():
    print("===========================")
    print("===== Escolha um Jogo =====")
    print("===========================")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual Jogo Deseja Jogar? "))

    if (jogo == 1):
        print("Jogando Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Jogo da Forca")
        adiv.jogar()
    else:
        print("Jogo não encontrado")

if (__name__ == "__main__"):
    escolha_jogos()