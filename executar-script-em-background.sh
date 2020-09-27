# ---------------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Shell Script profissional Mod.2 #35 - Gerenciamento de processos: Executar script em background
# https://www.youtube.com/watch?v=aU0sPnLp6eY&list=PLLCFxfe9wkl-jXrzZsL7rGLVxwyr8KyLF&index=36
# https://github.com/Geofisicando/Curso-Shell-Script-Profissional-mod-2/blob/master/aula_35/exemplo.sh
# ----------------------------------------------------------------------------------------------------

#!/bin/bash
# 
# Exemplo de programa para rodar em foreground 
i="0"
while:
do 
let i=i+1
echo"($i) Olá, pessoal!"
sleep 5
done

'''
./exemplo.sh 
ls
./exemplo.sh &
tail -f log.txt
exemplo.sh log.txt
./exemplo.sh > log.txt & 
'''
