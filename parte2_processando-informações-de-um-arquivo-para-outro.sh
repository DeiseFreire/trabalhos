# -------------------------------------------------------------------------------------------
# Fonte da ideia:
# Shell Script - Atividade 4 - Parte 2 - Processando informações de um arquivo para outro
# https://www.youtube.com/watch?v=MNf99Vk22lM&list=PLh7NspZkGKR-8vj6n1iKi1wtlSMORVgo2&index=5
# -------------------------------------------------------------------------------------------

'''
4) Verifique dinamicamente novamente o arquivo /etc/passwd e imprima no arquivo SeuNome.txt somente os usuários que utilizam o shell bash, 
numerando-os e utilizando o seguinte texto: "# - O usuário xxxx usa bash", onde # é o número do usuário, de acordo com a ordem em que aparece 
no arquivo e xxxx é o nome do login do usuário. (3 pontos)
'''

i=1
grep '/bin/bash'/etc/passwd |cut -d':' -f1| \
while read line; do 
echo "$i - O usuário $line usa bash" >> ~/mydir/Deise.txt
i=$((i+1))
done 


