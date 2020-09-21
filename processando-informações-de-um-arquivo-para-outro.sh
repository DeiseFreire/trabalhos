# -------------------------------------------------------------------------------------------
# Fonte da ideia:
# Shell Script - Atividade 4 - Parte 1 - Processando informações de um arquivo para outro
# https://www.youtube.com/watch?v=198kEfUinG8&list=PLh7NspZkGKR-8vj6n1iKi1wtlSMORVgo2&index=4
# --------------------------------------------------------------------------------------------

'''
4) Verifique dinamicamente novamente o arquivo /etc/passwd e imprima no arquivo SeuNome.txt somente os usuários que utilizam o shell bash, 
numerando-os e utilizando o seguinte texto: "# - O usuário xxxx usa bash", onde # é o número do usuário, de acordo com a ordem em que aparece 
no arquivo e xxxx é o nome do login do usuário. (3 pontos)
'''

cut -d':' -f1,7 /etc/passwd | grep '/bin/bash' > ~/mydir/Igor.txt

cérebro-binário[09-scripts] $ sudo chmod +x atividade.sh
cérebro-binário[09-scripts] $ ./atividade4.sh
cérebro-binário[09-scripts] $ code /home/deise/mydir/Deise.txt
cérebro-binário[09-scripts] $ ./atividade4.sh
^Ccérebro-binário[09-scripts] $ ./atividade4.sh
^Ccérebro-binário[09-scripts] $ ./atividade4.sh
cérebro-binário[09-scripts] $ code /home/deise/mydir/Deise.txt
cérebro-binário[09-scripts] $ ./atividade4.sh
cérebro-binário[09-scripts] $ code /home/deise/mydir/Deise.txt
