# -------------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Shell Scripting - Declaração break - encerrando loops prematuramente
# https://www.youtube.com/watch?v=sfO3ePx8dWY&list=PLucm8g_ezqNrYgjXC8_CgbvHbvI7dDfhs&index=31&t=0s
# -------------------------------------------------------------------------------------------------

#!/bin/bash
# Testando comando em um laço while
read -p "Digite um número entre 1 e 10" num
while [ $num -ne 0 ]
do 
if [ $num -gt 10 ]
then
break
fi
echo " Número digitado: $num"
read -p "Digite um número entre 1 e 10: " num
done
if [ $num -eq 0 ]
then
echo "Você encerrou o programa digitando zero"
else
echo "Você digitou um valor maior do que 10. Programa finalizado"
fi
# ------------------------ SAÍDA --------------------------------
'''
Digite um número entre 1 e 10 3 
Número digitado: 3
Digite um número entre 1 e 10: 6   
Número digitado: 6 
Digite um número entre 1 e 10: 9
Número digitado: 9   
Digite um número entre 1 e 10: 10
Número digitado: 10
Digite um número entre 1 e 10: 1
Número digitado: 1
Digite um número entre 1 e 10: 0
Número digitado: 0 
Digite um número entre 1 e 10: 2
Número digitado: 2
Digite um número entre 1 e 10: 7
Número digitado: 7
Digite um número entre 1 e 10: 12
Número digitado: 12  
Você digitou um valor maior do que 10. Programa finalizado ''' 
      
# -------------------- ENTRADA DO TECLADO ------------------------
'''
~/Documentos$ nano break.sh
~/Documentos$ chmod 777 break.sh 
~/Documentos$ ./break.sh 
~/Documentos$ ls -l
teste-break.sh     
# ------------------------ SAÍDA -----------------------------------
total 8
-rwxrwxrwx 1 deise deise 190 Set 28 17:53 break.sh
lrwxrwxrwx 1 deise deise 10 Ago 9 20:44 group -> /etc/group
-rwxrwxrwx 1 deise deise 407 Set 28 17:48 teste-break.sh
~/Documentos$ '''

