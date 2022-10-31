CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_diminuir_preco_produto`(id_prod int, diminuicao float)
BEGIN
	UPDATE Produto SET preco = preco-((preco*diminuicao)/100) WHERE id_produto = id_prod;
END