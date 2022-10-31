CREATE PROCEDURE `sp_aumentar_preco_produto` (id_prod int, aumento float)
BEGIN
	UPDATE Produto SET preco = preco+((preco*aumento)/100) WHERE id_produto = id_prod;
END
