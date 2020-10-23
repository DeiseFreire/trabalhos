~$ apt-show-versions # pertence ao sistema de gerenciamento de pacotes 
apt  # é um comando que pode ser utilizado para verificar se existem atualizações de pacotes para o sistema 
sudo apt-get install apt-show-versions 
ctrl + l # chama o manual do comando 
~$ man apt-show-versions # lista as versões de pacotes disponíveis na distribuição 
# ele faz uma verificação no arquivo de status do dpkg e também nas listas do apt e descobre os pacotes que estão instalados 
# e as versões de pacotes disponíveis e também as distribuições e mostra as opções de atualização dentro da distribuição especificada 
apt-show-versions # opções [-h] [[-p] package name] [-a] [-b] 
-p # para olhar as informações a respeito daquele pacote 
-r ou --regex # manda exibir apenas as informações dos pacote que são atualizáveis 
-u # todas as versões dos pacotes selecinados 
-a # imprimi apenas o nome do pacote e distribuição dos pacotes atualizáveis em vez de todas as informações sobre eles 
-i # informações mais verbosas 
-stf # permitem especificar um arquivo para ser utilizado no lugar do status do dpkg 
-ld # para utilizar um diretório 
~$napt-show-versions # sem nenhuma opção. Traz uma lista enorme dos pacotes que estão instalados no sistema e que estão atualizados 
grep # filtra os pacotes 
-1 # vai mostrar apenas os pacotes que são atualizáveis 
~$ apt-show-versions -u 
~$ apt-show-versions -r ^x11 # pacotes que tem alguma coisa a ver com gráficos
