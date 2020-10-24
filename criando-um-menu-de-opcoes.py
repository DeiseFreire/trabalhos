# --------------------------------------------------------------------------------------------
# Fonte da ideia:
# Exercício Python #059 - Criando um Menu de Opções
# https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=60
# --------------------------------------------------------------------------------------------

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
print('''[1] somar
[2] multiplicar
[3] maior
[4] novo números 
[5] sair do programa''')
opção = str(input('Qual é a sua opção? '))
print('Fim do programa! Volte sempre!')  
