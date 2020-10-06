# --------------------------SCRIPT -------------------------------
for num in 1 2 3 4 5 6 7 8 9 10 
do 
echo "Número: $num"
done

# -------------------- ENTRADA DE TELA --------------------------
'''
~/Documentos$ nano break.sh
~/Documentos$ chmod 777 break.sh 
~/Documentos$ ./break.sh 
# ------------------------ SAÍDA --------------------------------
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
Número: 6
Número: 7
Número: 8
Número: 9
Número: 10 '''
# --------------------------SCRIPT -------------------------------
for num in 1 2 3 4 5 6 7 8 9 10 
do 
if [ $num -eq 6 ]
then
break
echo "Número: $num"
done
  
# --------------------------SCRIPT -------------------------------
#!/bin/bash
# Testando comando break em Shell Scripting
for num in 1 2 3 4 5 6 7 8 9 10 
do 
if [ $num -eq 6 ]
then
break
echo "Número: $num"
done
echo "Laço for finalizado"

# ------------------------ SAÍDA --------------------------------
'''
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
Número: 6
Número: 7
Número: 8
Número: 9
Número: 10

# -------------------- ENTRADA DE TELA --------------------------

~/Documentos$
teste-break.sh     
~/Documentos$ ls -l
total 8
-rwxrwxrwx 1 deise deise 190 Set 28 17:53 break.sh
lrwxrwxrwx 1 deise deise 10 Ago 9 20:44 group -> /etc/group
-rwxrwxrwx 1 deise deise 407 Set 28 17:48 teste-break.sh
~/Documentos$ '''

# -------------------------- SCRIPT -------------------------------
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
      

