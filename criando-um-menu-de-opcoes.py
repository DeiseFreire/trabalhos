# --------------------------------------------------------------------------------------------
# Fonte da ideia:
# Exercício Python #059 - Criando um Menu de Opções
# https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=60
# --------------------------------------------------------------------------------------------

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
print('''  [1] somar
[2] multiplicar
[3] maior
[4] novo números 
[5] sair do programa''')
opção = int(input('Qual é a sua opção? '))
if opção ==1:
elif opção == 2:
elif opção == 3:
elif opção == 4:
elif opção == 5:
else:
print('Opção inválida. Tente novamente')
print('=-='*10)
print('Fim do programa! Volte sempre!')  
