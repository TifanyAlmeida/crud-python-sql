USE ecommerce;

CREATE TABLE Logs_Acao_Prod(
	id_log_acao_prod int auto_increment primary key,
    hora datetime
);
CREATE TABLE Logs_Acao_Ped(
	id_log_acao_ped int auto_increment primary key,
    hora datetime
);
drop table Logs_Acao_Prod;
drop table Logs_Acao_Ped;

CREATE TABLE Usuario(
	id_usuario int auto_increment primary key,
    nome varchar(50) not null,
    email varchar(50) not null,
    senha varchar(8) not null
);

INSERT INTO Usuario VALUES(null, 'Tifany', 'ti@email.com', '1234Ti');
SELECT * FROM Usuario, Produto, Pedido, PedidoItem;

CREATE TABLE Produto(
	id_produto int auto_increment primary key,
    nome varchar(50) not null,
    qtd_estoque int not null,
    preco decimal(5, 2) not null
);

INSERT INTO Produto VALUES(id_produto, 'Lays', 153, 7.69);
INSERT INTO Produto VALUES(id_produto, 'Coca-Cola', 40, 5.50);
INSERT INTO Produto VALUES(id_produto, 'Pão de Queijo', 12, 2.00);
INSERT INTO Produto VALUES(id_produto, 'Bioleve de Maçã Verde', 100, 4.59);
INSERT INTO Produto VALUES(id_produto, 'Cheetos', 500, 15.99);

CREATE TABLE Pedido(
	id_pedido int auto_increment primary key,
    nome_cliente varchar(50) not null,
    valor_total decimal(5, 2),
    hora_pedido datetime
);

INSERT INTO Pedido VALUES(id_pedido, 'Tatiane', 0, now());
INSERT INTO Pedido VALUES(id_pedido, 'Tifany', 0, now());
INSERT INTO Pedido VALUES(id_pedido, 'Bella', 0, now());


CREATE TABLE PedidoItem(
	id_pedido_item int auto_increment primary key,
    qtd int,
    preco_unitario decimal(5, 2),
    fk_produto int,
    fk_pedido int,
    FOREIGN KEY(fk_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY(fk_pedido) REFERENCES Pedido(id_pedido)
);
call sp_add_lista_compras(1, 2);
CREATE TABLE lista_compras (
	id_lista_compras int auto_increment primary key,
	data_registro datetime,
    fk_produto int,
    FOREIGN KEY(fk_produto) REFERENCES Produto(id_produto),
    quantidade int,
    comprado boolean
);

drop table pedido;
drop table pedidoItem;
drop table produto;
drop table lista_compras;
Select * from Pedido;
SELECT * FROM Produto;
SELECT * FROM PedidoItem;
SELECT * FROM lista_compras;