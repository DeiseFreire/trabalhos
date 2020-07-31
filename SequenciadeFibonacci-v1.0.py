#Exercício Python #063 - Sequência de Fibonacci v1.0
#https://www.youtube.com/watch?v=w7yn1_Mfu0E

print('-'*30)
pritn('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
pritn('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
t3 = t1 + t2 
print(' -> {}'.format(t3), end='')
t1 = t2
t2 = t3 
cont += 1
pritn(' -> FIM')
print('~'*30)
