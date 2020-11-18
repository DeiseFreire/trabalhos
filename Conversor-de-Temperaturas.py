# --------------------------------------------------------------------------------------------
# Fonte da ideia:
# Exercício Python #014 - Conversor de Temperaturas
# https://www.youtube.com/watch?v=9l_Gay8BuAw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=15
# --------------------------------------------------------------------------------------------

'''
Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
'''

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
print('A temperatura de {} °C corresponde a {} °F!'.format(c, f)) 
