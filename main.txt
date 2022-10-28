import mysql.connector

cnx = mysql.connector.connect(user='root',password='user123',host='127.0.0.1',database='ecommercev2')

cursor = cnx.cursor()
cursor.execute('SELECT * FROM produto')
# produto = cursor.fetchall()
# print(produto)

for (id,nome,qtd,preco) in cursor:
    print(f'{nome} - {preco}')
    
nomeProduto = input('Digite o nome do produto: ')
query = 'Insert into produto values(null,%s,%s,%s)'
dados = (nomeProduto,"100","100")
cursor.execute(query,dados)
cnx.commit()