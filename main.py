import os.path
import pandas as pd

# Verifica se o arquivo existe. Se não existir, cria um novo arquivo com as colunas necessárias.
if not os.path.exists('estoque.csv'):
    novo_arquivo = pd.DataFrame(columns=['Nome do Produto', 'Quantidade em Estoque', 'Preço', 'Data de Entrada no Estoque'])
    novo_arquivo.to_csv('estoque.csv', index=False, sep=';')

# Função para adicionar um novo item ao estoque
def adicionar_item():
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    
    # Verifica o preço inserido e corrige se necessário
    preco_invalido = True
    while preco_invalido:
        preco = input("Digite o preço unitário: ")
        preco = preco.replace(",", ".")
        try:
            preco = float(preco)
            preco_invalido = False
        except ValueError:
            print("Preço inválido. Tente novamente.")
    
    data_entrada = input("Digite a data de entrada no estoque (yyyy-mm-dd): ")
    novo_item = {'Nome do Produto': nome_produto, 'Quantidade em Estoque': quantidade, 'Preço': preco, 'Data de Entrada no Estoque': data_entrada}
    df_novo_item = pd.DataFrame([novo_item])
    df = pd.read_csv('estoque.csv', sep=';')
    df = pd.concat([df, df_novo_item], ignore_index=True)
    df.to_csv('estoque.csv', index=False, sep=';')
    print("Item adicionado com sucesso!")

# Função para atualizar um item existente no estoque
def atualizar_item():
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    df = pd.read_csv('estoque.csv')
    item = df.loc[df['Nome do Produto'] == nome_produto]
    if len(item) == 0:
        print("O produto não foi encontrado.")
    else:
        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        novo_preco = float(input("Digite o novo preço unitário: "))
        df.loc[df['Nome do Produto'] == nome_produto,
               'Quantidade em Estoque'] = nova_quantidade
        df.loc[df['Nome do Produto'] == nome_produto, 'Preço'] = novo_preco
        df.to_csv('estoque.csv', index=False)
        print("Item atualizado com sucesso!")

# Função para remover um item do estoque


def remover_item():
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    df = pd.read_csv('estoque.csv')
    item = df.loc[df['Nome do Produto'] == nome_produto]
    if len(item) == 0:
        print("O produto não foi encontrado.")
    else:
        df = df.drop(df[df['Nome do Produto'] == nome_produto].index)
        df.to_csv('estoque.csv', index=False)
        print("Item removido com sucesso!")

# Função para pesquisar o estoque por nome do produto


def pesquisar_item():
    nome_produto = input("Digite o nome do produto que deseja pesquisar: ")
    df = pd.read_csv('estoque.csv')
    resultados = df.loc[df['Nome do Produto'] == nome_produto]
    if len(resultados) == 0:
        print("Nenhum resultado encontrado.")
    else:
        print(resultados)

# Função para imprimir todo o estoque


def imprimir_estoque():
    df = pd.read_csv('estoque.csv')
    print(df)


# Loop principal do programa
while True:
    print("\nControle de Estoque")
    print("-------------------")
    print("1 - Adicionar Item")
    print("2 - Atualizar Item")
    print("3 - Remover Item")
    print("4 - Pesquisar Item")
    print("5 - Imprimir Estoque")
    print("0 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == '1':
        adicionar_item()
    elif opcao == '2':
        atualizar_item()
    elif opcao == '3':
        remover_item()
    elif opcao == '4':
        pesquisar_item()
    elif opcao == '5':
        imprimir_estoque()
    elif opcao == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")
