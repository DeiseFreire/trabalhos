#13.4 - Quantas tentativas faltam? 

#Sempre é importante dar feedback ao usuário quando ele realiza alguma ação no sistema. No caso da forca, quando o jogador errar uma letra, 
#queremos indicar isso, juntamente com quantas tentativas faltam. Em outras palavras queremos mostrar para o jogador quantas rodadas ele 
#ainda pode jogar antes de ser enforcado. Que código poderíamos escrever para dar esse feedback ao jogador?
*********************************
***Bem vindo ao jogo da Forca!***
*********************************
['_', '_', '_', '_', '_', '_']
Qual letra? b
['b', '_', '_', '_', '_', '_']
Qual letra? a
['b', 'a', '_', 'a', '_', 'a']
Qual letra? n
['b', 'a', 'n', 'a', 'n', 'a']
Qual letra?

# Encerrando o jogo quando o usuário errar seis vezes
enforcou = False
acertou = False
erros = 0

while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    if (chute in palavra_secreta): # Verifica se o usuário errou alguma palavra para incrementar a variável 
        index = 0
        for letra in palavra_secreta: # Verifica se o chute está na palavra
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra # O código é executado
            index = index + 1 # A variável é incrementada se o chute for errado
    else:
        erros = erros + 1 # Verifica se a variável incrementada é igual a 6
    enforcou = erros == 6 # Serve para encerrar o jogo depois de executar 6 vezes
    print(letras_acertadas)
