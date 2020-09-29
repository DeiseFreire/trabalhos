# -----------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Shell Script profissional Mod.2 #33 - Exercício 11: Função de busca de produtos em shell script
# https://www.youtube.com/watch?v=Jdq6TukFBt4&list=PLLCFxfe9wkl-jXrzZsL7rGLVxwyr8KyLF&index=33
# https://github.com/Geofisicando/Curso-Shell-Script-Profissional-mod-2/tree/master/aula_33
# -----------------------------------------------------------------------------------------------

'''
cat lista_compras.txt
sabonete: 2.5
creme dental: 2
escova de dente: 4
café: 3.5
carne: 10 

gedit biblioteca.sh &'''

a biblioteca ponto sh para o nosso exemplo de busca de produtos na nossa lista compras 
# !/bin/bash
#
# Função de buscas de produto em uma lista de compras
buscaproduto(){
PRODUTO="$1"
ARQUIVO="$2"
cat "$ARQUIVO" | cut -d":" -f1 | grep -q "$PRODUTO"
["$?" -ne "0" ] && {
echo "Produto $PRODUTO não encontrado em $ARQUIVO"
return 1
}
sed -n "/$PRODUTO/p" "$ARQUIVO" | sed "s/:/ /;s/$/R\$/" 
}
'''
cat lista_compras.txt | cut -d":" -f1
sabonete
creme dental 
escova de dente
café
carne'''
'''
# !/bin/bash
#
# Exercício sobre funções em Shell Script
# Carrega a biblioteca de funções
source biblioteca.sh
ARQUIVO="lista_compras.txt"
buscaproduto "carne" "$ARQUIVO"
buscaproduto "peixe" "$ARQUIVO"
buscaproduto "creme dental "$ARQUIVO"
'''
cat lista_compras.txt
sabonete:2.5
creme dental:2
escova de dente:4
café:3.5
carne:10'''

