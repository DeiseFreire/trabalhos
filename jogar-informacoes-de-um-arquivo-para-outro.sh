# -------------------------------------------------------------------------------------------
# Fonte: 
# Shell Script - Atividade 3 - Jogar informações de um arquivo para outro
# https://www.youtube.com/watch?v=iXQ-_tQgkkw&list=PLh7NspZkGKR-8vj6n1iKi1wtlSMORVgo2&index=3
# --------------------------------------------------------------------------------------------

'''
3) Verifique dinamicamente o arquivo /etc/passwd e imprima os 5 últimos registros de usuários no 
arquivo SeuNome.txt, selecionando apenas as colunas referentes ao nome do usuário, diretório home e 
shell padrão do usuário. (3 pontos)
'''
# tail -n 5 /etc/passwd
# field (campo)
# cut -d':' -f1,6,7 
tail -n 5 /etc/passwd | cut -d':' -f1,6,7 >> ~/mydir/Deise.txt
$ code /home/deise/mydir/Deise.txt
$ sudo chmod +x atividade3.sh
[sudo] senha  para deise: 
$ ./atividade3.sh
Nome: Deise Freire
Matrícula: 123456789
ice:/var/lib/ice:/usr/sbin/nologin
mumble-server:/var/lib/mumble-server:/usr/sbin/nologin
pulse:/var/run/pulse:/usr/sbin/nologin
smmta:/var/lib/sendmail:/usr/sbin/nologin 
smmsp:/var/lib/sendmail:/usr/sbin/nologin  
