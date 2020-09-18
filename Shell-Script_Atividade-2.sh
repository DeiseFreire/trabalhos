# -------------------------------------------------------------------------------------------------------------------
# Fonte: 
# Shell Script - Atividade 2 - Criando arquivo e escrevendo texto
# https://www.youtube.com/watch?v=mP_I1uR0A70&list=PLh7NspZkGKR-8vj6n1iKi1wtlSMORVgo2&index=2
# -------------------------------------------------------------------------------------------------------------------

'''
Atividade: Shell Script Básico
Escreva um shell script que execute as seguintes tarefas:
1) Verifique se existe o diretório mydir dentro do seu diretório home. Se não existir, crie o diretório. (2 pontos)
'''

if [ ! -d ~/mydir ]; then
echo 'Criando diretório'
mkdir ~/mydir
if [ "$?" -eq "0" ]; then
echo 'Diretório criado com sucesso'
else
echo 'erro ao criar diretório'
fi
else
echo 'diretório já existe'
fi
