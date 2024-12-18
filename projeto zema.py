# Função para incluir pedido no vetor
def novo_pedido(lista_pedidos, id_pedido):
    if len(lista_pedidos) == 10: # se a lista tiver 10 itens dentro dela, não add mais pedidos
        print("Fila Cheia – Não Pode Mais Incluir Pedidos")
    else:
        lista_pedidos.append(id_pedido) # append = adicionar no final da lista
        print(f"Pedido {id_pedido} adicionado!")
    return id_pedido + 1 # soma + 1 para que não haja id's repetidos


# Função para excluir um pedido do vetor
def atender_pedido(lista_pedidos):
    if len(lista_pedidos) == 0: # se a lista estiver vazia, nao dá p atender pedidos
        print("Lista Vazia – Não Existem Pedidos para Atender")
    else:
        atendido = lista_pedidos.pop(0)
        print(f"Pedido {atendido} atendido!")
        print("Lista de pedidos atual:", lista_pedidos)


# Função para listar os pedidos do vetor
def listar_pedidos(lista_pedidos):
    if len(lista_pedidos) == 0:
        print("Lista Vazia – Não Existem Pedidos")
    else:
        print("Lista de pedidos:", lista_pedidos)


# Função para pesquisar os pedidos do vetor
def pesquisar_pedido(lista_pedidos):
    if len(lista_pedidos) == 0:
        print("Lista Vazia – Não Existem Pedidos")
    else:
        try: # o try tenta executar o codigo abaixo e o except verifica exceção
            id_pesquisa = int(input("Informe o ID do pedido que deseja encontrar: "))
            indice = lista_pedidos.index(id_pesquisa) # pesquisa pelo id
            print(f'O pedido {id_pesquisa} está na posição {indice + 1}')
        except ValueError:
            print("O pedido informado não está na lista.")


# Função para encerrar o programa
def encerrar(lista_pedidos):
    if len(lista_pedidos) == 0:
        print("Encerrando o programa...")
    else:
        print("Não é possível encerrar o programa pois ainda existem pedidos a serem atendidos!")


# Função principal
def main():
    lista_pedidos = []  # Vetor vazio que deve ter no máximo 10
    id_pedido = 1

    while True:
        opcao = input('''
        ##### LANCHONETE #######
        # 1 - Incluir Pedido   #
        # 2 - Atender Pedido   #
        # 3 - Listar Pedidos   #
        # 4 - Pesquisar Pedido #
        # 5 - Encerrar         #
        ########################  

        Opção: ''')

        if opcao == '1':
            id_pedido = novo_pedido(lista_pedidos, id_pedido)
        elif opcao == '2':
            atender_pedido(lista_pedidos)
        elif opcao == '3':
            listar_pedidos(lista_pedidos)
        elif opcao == '4':
            pesquisar_pedido(lista_pedidos)
        elif opcao == '5':
            encerrar(lista_pedidos)
            if len(lista_pedidos) == 0:
                break
        else:
            print("Opção inválida. Por favor, digite um número entre 1 e 5.")


if __name__ == "__main__":
    main()
