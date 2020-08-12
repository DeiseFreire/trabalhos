# Exercício Python #012 - Calculando Descontos
# https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=13

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
