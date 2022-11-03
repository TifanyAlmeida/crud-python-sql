CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_add_lista_compras`(id_prod int, qtd int)
BEGIN
	INSERT INTO lista_compras VALUES(null, now(), id_prod, qtd, False);
END