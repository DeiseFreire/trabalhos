# Exercício Python #008 - Conversor de Medidas
# https://www.youtube.com/watch?v=KjcdG05EAZc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=9

medida = float (input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A média de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
