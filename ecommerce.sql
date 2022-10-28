CREATE DATABASE ecommerce;
USE ecommerce;

CREATE TABLE Usuario(
	id_usuario int auto_increment primary key,
    nome varchar(50) not null,
    email varchar(50) not null,
    senha varchar(8) not null
);

INSERT INTO Usuario VALUES(null, 'Tifany', 'ti@email.com', '1234Ti');

SELECT * FROM Usuario, Produto, Pedido, PedidoItem;

CREATE DATABASE ecommerce;
USE ecommerce;


CREATE TABLE Produto(
	id_produto int auto_increment primary key,
    nome varchar(50) not null,
    qtd_estoque int not null,
    preco decimal not null
);

INSERT INTO Produto VALUES(id_produto, 'Lays', 153, 7.69);
INSERT INTO Produto VALUES(id_produto, 'Coca-Cola', 40, 5.50);
INSERT INTO Produto VALUES(id_produto, 'Pão de Queijo', 12, 2.00);
INSERT INTO Produto VALUES(id_produto, 'Bioleve de Maçã Verde', 100, 4.59);
INSERT INTO Produto VALUES(id_produto, 'Cheetos', 500, 15.99);

CREATE TABLE Pedido(
	id_pedido int auto_increment primary key,
    nome_cliente varchar(50) not null,
    valor_total decimal not null,
    hora_pedido datetime
);

CREATE TABLE PedidoItem(
	id_pedido_item int auto_increment primary key,
    qtd int not null,
    preco_unitario decimal not null,
    fk_produto int not null,
    fk_pedido int not null,
    FOREIGN KEY(fk_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY(fk_pedido) REFERENCES Pedido(id_pedido)
);