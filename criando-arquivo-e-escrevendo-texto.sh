# -------------------------------------------------------------------------------------------
# Fonte: 
# Shell Script - Atividade 2 - Criando arquivo e escrevendo texto
# https://www.youtube.com/watch?v=mP_I1uR0A70&list=PLh7NspZkGKR-8vj6n1iKi1wtlSMORVgo2&index=2
# -------------------------------------------------------------------------------------------

'''
2) Dentro do diretório mydir, criado na etapa anterior, o shell # script deve imprimir o seu nome e matrícula no arquivo SeuNome.txt 
(substitua o SeuNome.txt pelo seu próprio nome. Exemplo: se o seu # nome é José, coloque Jose.txt). (2 pontos)
'''
$ code atividade2.sh
$ sudo chmod +x atividade2.sh
$ ./atividade2.sh
Nome: Deise Freire
echo 'Nome: Deise Freire' > ~/mydir/Deise.txt
$ code /home/deise/mydir/Deise.txt
$ rm ~/mydir/Deise.txt
echo 'Matrícula: 123456789' 
$ ./atividade2.sh
$ code ./home/deise/mydir/Deise.txt
echo 'Matrícula: 123456789' >> ~/mydir/Deise.txt 
$ ./atividade2.sh
$ code /home/deise/mydir/Deise.txt
