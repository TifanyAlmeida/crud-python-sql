CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_calcultar_valor_total`(pedido int)
BEGIN
	UPDATE Pedido SET valor_total = (SELECT preco FROM Produto WHERE id_produto
    = 
    (SELECT fk_produto FROM PedidoItem WHERE fk_pedido = pedido))
    * 
    (SELECT qtd FROM PedidoItem WHERE fk_pedido = pedido) WHERE id_pedido = (SELECT fk_pedido FROM PedidoItem WHERE fk_pedido = pedido);
END