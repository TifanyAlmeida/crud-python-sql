import mysql.connector
import bcrypt

conexao = mysql.connector.connect(user='root', password = '1234', host='127.0.0.1', database='ecommerce')
cursor = conexao.cursor()

def mostrar_menu():

    print("\n\n########### MENU ##########")
    print("1 - Cadastro")
    print("2 - Login")
    op = int(input("- Opção: "))

    if op == 1 or op == 2:
        verificar(op)
    else:
        print("\n*Esse item não foi encontrado em nosso Menu!\n")
        mostrar_menu()

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

    else:
       chamar_menu_produto()

####
def exibir_produto():
    cursor.execute('SELECT * FROM Produto')
    for (id_produto,nome,preco,qtd_estoque) in cursor:
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
    colunas = ['nome', 'qtd_estoque','preco']
    
    print("\n1 - Nome")
    print("2 - Estoque")
    print("3 - Preço")
    coluna = int(input("\n- Coluna Desejada(ex: 1): "))
    coluna = colunas[coluna-1]

    novo_valor = input("Novo Valor: ")

    if coluna == 1:
        novo_valor = int(novo_valor)
    elif coluna == 2:
        novo_valor = float(novo_valor)

    query = 'UPDATE Produto SET %s = %s WHERE id_produto = %s'
    dados = (coluna, novo_valor, id)
    cursor.execute(query, dados)
    conexao.commit()

def deletar_produto():
    id = int(input("\n+ N° Produto: "))
    query = 'DELETE * FROM Produto WHERE id_produto = %s'
    dados = (id, )
    cursor.execute(query, dados)
    conexao.commit()

####
def chamar_menu_produto():
    
    print("\n\n----------- Ecommerce -----------")
    print("1 - Exibir Produtos cadastrados")
    print("2 - Cadastrar Produto")
    print("3 - Editar Produto")
    print("4 - Excluir Produto")
    print('5 - Sair')
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
        print("\n# Até Logo! #\n")
        mostrar_menu()

    else:
        print("\n* Esta opção não corresponde ao nosso menu!\n")
    
    chamar_menu_produto()

mostrar_menu()

    # # verificar desincriptado
    # query_cad = 'SELECT COUNT(*) FROM Usuario WHERE email = %s or senha = %s'
    # dados = (email, hashed, email)
    # cursor.execute(query_cad,dados)
    # max_row = cursor.fetchall()