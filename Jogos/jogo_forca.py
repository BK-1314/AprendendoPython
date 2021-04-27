import random

def jogar():

    mensagem_abertura()
    palavra_secreta = gerar_palavra()
    letras_acertadas = inivcializa_letras_secretas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6




    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            define_acerto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            print(f"Que Pena, você errou! Faltam {(tentativas-erros)} tentativas")

        falta = str(letras_acertadas.count("_"))
        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print("")
        print(f"Ainda faltam acertar {falta} letras")
        print(letras_acertadas)

    if(acertou):
        mensagem_ganhador()
    else:
        mensage_perdedor(palavra_secreta)


def mensagem_abertura():
    print("********************************\n**Bem vindo ao jogo da Forca!**\n********************************")
def gerar_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def inivcializa_letras_secretas(palavra):
    return["_" for letra  in palavra]
def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute
def define_acerto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_ganhador():
    print("Você Ganhou")
def mensage_perdedor(palavra_secreta):
    print(f"Você Perdeu, você exedeu o limite de tentativas! A palavra secreta era{palavra_secreta}")
if(__name__=="__main__"):
    jogar()