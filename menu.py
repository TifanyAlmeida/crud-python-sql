import mysql.connector
import bcrypt
# login não está funcionando
# produto ok: falta os triggers e a cricao da tabela de compras com estoque zerado

conexao = mysql.connector.connect(user='root', password = '1234', host='127.0.0.1', database='ecommerce')
cursor = conexao.cursor()

def mostrar_menu():

    print("\n\n########### MENU ##########")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")
    op = int(input("- Opção: "))

    if op == 1 or op == 2:
        verificar(op)
    if op == 3:
        exit()
    else:
        print("\n*Esse item não foi encontrado em nosso Menu!\n")
        mostrar_menu()
#

def chamar_menu_ecommerce():
    print("\n######### Ecommerce ##########")
    print("1 - Produtos")
    print("2 - Pedidos")
    print("3 - Voltar")

    ops = int(input("\n- Opção: "))

    if ops == 1:
        chamar_menu_produto()
    elif ops == 2:
        chamar_menu_pedido()
    elif ops == 3:
        mostrar_menu()
    else:
        print("\n*Esse item não foi encontrado em nosso Menu !\n")
    
    chamar_menu_ecommerce()


def exibirPedido():
    cursor.execute('SELECT * FROM Pedido')
    for (id_pedido, nome_cliente, valor_total, hora_pedido) in cursor:
        print(f'\n{id_pedido} - {nome_cliente} - Total R$ {valor_total} - ({hora_pedido})\n')

def exibirPedidoItem():
    cursor.execute('SELECT * FROM PedidoItem')
    for (id_pedido_item, qtd, preco_unitario, fk_produto, fk_pedido) in cursor:
        print(f'\n{id_pedido_item} - {qtd} Unidade R$ {preco_unitario} (fk_produto {fk_produto}, fk_pedido {fk_pedido})\n')

def  verificar_estoque(valor):

    query = 'SELECT qtd_estoque FROM Produto WHERE id_produto = %s'
    dados = (valor, )
    cursor.execute(query, dados)
    if int(cursor.fetchall()[0][0]) <= 0:
        return False
    else:
        return True

def chamar_menu_pedido():
    print("\n ######### Pedidos ########\n")
    print("1 - Exibir os pedidos existentes")
    print("2 - Criar um pedido novo")
    print("3 - Adicionar produto a um pedido")
    print("4 - Remover produto de um pedido")
    print("5 - Calcular Total do Pedido")
    print("6 - Voltar")
    opcao = int(input("\n- Opção: "))

    if opcao == 1:
        exibirPedido()

    elif opcao == 2:
        cliente = input("\nNome do Cliente: ")
        query = 'INSERT INTO Pedido VALUES(null, %s, 0, now())'
        dados = (cliente, )
        cursor.execute(query, dados)
        conexao.commit()
        exibirPedido()

    elif opcao == 3:
        exibir_produto()
        fk_produto = int(input("\nN° do Produto: "))

        if verificar_estoque(fk_produto):

            qtd = int(input("\nQuantidade Desejada: "))
            exibirPedido()
            fk_pedido = int(input("\nAdicionar em qual Pedido: "))

            query = 'INSERT INTO PedidoItem VALUES(null, %s, (SELECT preco FROM Produto WHERE id_produto = %s), %s, %s)'
            dados = (qtd, fk_produto, fk_produto, fk_pedido)

            cursor.execute(query, dados)
            conexao.commit()

            cursor.execute('UPDATE Produto SET qtd_estoque = qtd_estoque - (SELECT qtd FROM PedidoItem WHERE id_pedido_item = (select last_insert_id()))\
            WHERE id_produto = (SELECT fk_produto FROM PedidoItem WHERE id_pedido_item = (select last_insert_id()))')

            conexao.commit()
            exibirPedidoItem()

        else:
            print("\n* Produto fora de estoque, será adicionado na lista de compras * \n")
            # criar a inserção com procedure na tabela de lista de compras


    elif opcao == 4:
        exibirPedidoItem()
        id_pedido = int(input("\n N° de Item do Pedido: "))
        query = 'DELETE FROM PedidoItem WHERE id_pedido_item = %s'
        dados = (id_pedido, )
        cursor.execute(query, dados)
        conexao.commit()

    elif opcao == 5:
        exibirPedido()
        pedido = int(input("\nN° do Pedido Desejado: "))
        calcular_total_pedido(pedido)
        exibirPedido()

    elif opcao == 6:
        chamar_menu_ecommerce()

    else:
        print("\n*Esse item não foi encontrado em nosso Menu !\n")
    
    chamar_menu_pedido()

def calcular_total_pedido(pedido):

    query = 'call sp_calcultar_valor_total(%s)'
    dados = (pedido, )
    cursor.execute(query, dados)
    conexao.commit()

def verificar(op):

    nome = input("\nNome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    # hashed_password = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
    
    if op == 1:

        # if max_row == 0:
        query = 'INSERT INTO Usuario VALUES(null, %s, %s, %s)'
        dados = (nome, email, senha)
        cursor.execute(query, dados)
        conexao.commit()
        mostrar_menu()

    if op == 2:
        # validação
        chamar_menu_ecommerce()

    else:
       chamar_menu_produto()

####
def exibir_produto():
    cursor.execute('SELECT * FROM Produto')
    for (id_produto,nome,qtd_estoque, preco) in cursor:
        print(f'\n{id_produto} - {nome} R$ {preco} (estoque): {qtd_estoque}\n')

def cadastrar_produto():
    produto = input("\nProduto: ")
    preco = float(input("R$ "))
    qtd_estoque = int(input("Estoque: "))

    query = 'INSERT INTO Produto VALUES(null, %s, %s, %s)'
    dados = (produto, preco, qtd_estoque)
    cursor.execute(query, dados)
    conexao.commit()

def alterar_produto():

    id = int(input("\n+ N° Produto: "))
    
    print("\n1 - Nome")
    print("2 - Estoque")
    print("3 - Preço")
    coluna = int(input("\n- Coluna Desejada(ex: 1): "))
    novo_valor = input("Novo Valor: ")

    if coluna == 1:
        query = "UPDATE Produto SET nome = %s WHERE id_produto = %s"
        dados = (novo_valor, id)

    elif coluna == 2:
        novo_valor = int(novo_valor)
        query = "UPDATE Produto SET qtd_estoque = %s WHERE id_produto = %s"
        dados = (novo_valor, id)

    elif coluna == 3:
        novo_valor = float(novo_valor)
        query = "UPDATE Produto SET preco = %s WHERE id_produto = %s"
        dados = (novo_valor, id)

    else:
        print("\n* Digite Apenas Itens do Menu\n")
        alterar_produto()
    
    cursor.execute(query, dados)
    conexao.commit()

def deletar_produto():
    id = int(input("\n+ N° Produto: "))
    query = 'DELETE FROM Produto WHERE id_produto = %s'
    dados = (id, )
    cursor.execute(query, dados)
    conexao.commit()

def chamar_menu_produto():
    
    print("\n\n----------- Produtos -----------")
    print("1 - Exibir Produtos cadastrados")
    print("2 - Cadastrar Produto")
    print("3 - Editar Produto")
    print("4 - Excluir Produto")
    print("5 - Aumentar o preço dos produtos em X %")
    print("6 - Diminuir o preço dos produtos em Y %")
    print('7 - Voltar')
    op = int(input("\n- Opção: "))
    print("-------------------------------------")
    print("\n")

    if op == 1:
        exibir_produto()

    elif op == 2:
       cadastrar_produto()
       exibir_produto()
        
    elif op == 3:
        exibir_produto()
        alterar_produto()
        exibir_produto()

    elif op == 4:
        exibir_produto()
        deletar_produto()
        exibir_produto()

    elif op == 5:
        exibir_produto()
        id_prod = int(input("N° do Produto: "))
        porcentagem = float(input("Porcentagem de Aumento: "))

        query = 'call sp_aumentar_preco_produto(%s, %s)'
        dados = (id_prod, porcentagem)
        cursor.execute(query, dados)
        conexao.commit()

        exibir_produto()

    elif op == 6:
        exibir_produto()
        id_prod = int(input("N° do Produto: "))
        porcentagem = float(input("Porcentagem de Diminuição: "))

        query = 'call sp_diminuir_preco_produto(%s, %s)'
        dados = (id_prod, porcentagem)
        cursor.execute(query, dados)
        conexao.commit()

        exibir_produto()

    elif op == 7:
        print("\n# Até Logo! #\n")
        chamar_menu_ecommerce()

    else:
        print("\n* Esta opção não corresponde ao nosso menu!\n")
    
    chamar_menu_produto()

mostrar_menu()

    # # verificar desincriptado
    # query_cad = 'SELECT COUNT(*) FROM Usuario WHERE email = %s or senha = %s'
    # dados = (email, hashed, email)
    # cursor.execute(query_cad,dados)
    # max_row = cursor.fetchall()
