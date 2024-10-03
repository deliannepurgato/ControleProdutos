# Controle de Estoque com Python 

Este é um simples controle de estoque feito em Python com o uso da biblioteca Pandas.

## :gear: Funcionamento
O controle de estoque é feito através de um arquivo CSV onde são armazenados os dados dos produtos como nome, quantidade em estoque, preço unitário e data de entrada no estoque. A partir deste arquivo é possível adicionar, remover e atualizar informações dos produtos.

## :computer: Tecnologias utilizadas
- Python 3
- Pandas 1.3.4

## :rocket: Como usar
Para usar este controle de estoque, você precisa ter o Python 3 instalado em sua máquina, assim como a biblioteca Pandas. 

1. Faça o download do arquivo `controle_de_estoque.py` para o seu computador
2. Abra o terminal e navegue até o diretório onde o arquivo está salvo
3. Digite o comando `python3 controle_de_estoque.py` para executar o programa

## :memo: Funcionalidades
- Adicionar um novo item ao estoque
- Remover um item do estoque
- Atualizar as informações de um item existente no estoque
- Listar todos os itens no estoque
- Visualizar a quantidade total de itens e o valor total em estoque

## :warning: Observações
- Se o arquivo CSV não existir no diretório, o programa irá criar um novo arquivo com as colunas necessárias
- Ao adicionar um novo item, o programa verifica se o preço inserido é válido e corrige se necessário
- O separador utilizado no arquivo CSV é o ponto e vírgula (;), o que permite que os dados se ajustem corretamente na tabela caso o arquivo seja aberto no Excel


