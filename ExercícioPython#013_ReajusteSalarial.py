# --------------------------------------------------------------------------------------------
# Fonte da ideia:
# Exercício Python #013 - Reajuste Salarial
# https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=14
# --------------------------------------------------------------------------------------------

salário = float( input( 'Qual é o salário do funcionário? R$' ) )
novo = salário + (salário * 15 / 100)
print( 'Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format( salário, novo ) )
