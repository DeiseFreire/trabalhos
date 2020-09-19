# -------------------------------------------------------------------------------------------------------------------
# Fonte: 
# Shell Script - Atividade 1 - Criando diretório caso não exista
# https://www.youtube.com/watch?v=sMnfPeOZQPc&list=PLh7NspZkGKR-8vj6n1iKi1wtlSMORVgo2&index=1
# -------------------------------------------------------------------------------------------------------------------

'''

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
