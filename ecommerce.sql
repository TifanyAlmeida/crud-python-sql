CREATE DATABASE ecommerce;
USE ecommerce;

-- USUÁRIO
CREATE TABLE Usuario(
	id_usuario int auto_increment primary key,
    nome varchar(50) not null,
    email varchar(50) not null,
    senha varchar(255) not null
);
SELECT * FROM Usuario;

-- PRODUTO
CREATE TABLE Produto(
	id_produto int auto_increment primary key,
    nome varchar(50) not null,
    qtd_estoque int not null,
    preco decimal(5, 2) not null
);


SELECT * FROM Produto;

-- PEDIDO
CREATE TABLE Pedido(
	id_pedido int auto_increment primary key,
    nome_cliente varchar(50) not null,
    valor_total decimal(5, 2),
    hora_pedido datetime
);
SELECT * FROM Pedido;

-- PEDIDO ITEM
CREATE TABLE PedidoItem(
	id_pedido_item int auto_increment primary key,
    qtd int,
    preco_unitario decimal(5, 2),
    fk_produto int,
    fk_pedido int,
    FOREIGN KEY(fk_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY(fk_pedido) REFERENCES Pedido(id_pedido)
);

SELECT * FROM PedidoItem;

-- LISTA DE COMPRAS
CREATE TABLE lista_compras (
	id_lista_compras int auto_increment primary key,
	data_registro datetime,
    fk_produto int,
    FOREIGN KEY(fk_produto) REFERENCES Produto(id_produto),
    quantidade int,
    comprado boolean
);

SELECT * FROM lista_compras;

-- TRIGGERS
CREATE TABLE Logs_Acao_Prod(
	id_log_acao_prod int auto_increment primary key,
    hora datetime,
    acao varchar(50)
);

SELECT * FROM  Logs_Acao_Prod;

CREATE TABLE Logs_Acao_Ped(
	id_log_acao_ped int auto_increment primary key,
    hora datetime,
    acao varchar(50)
);
SELECT * FROM  Logs_Acao_Ped;
