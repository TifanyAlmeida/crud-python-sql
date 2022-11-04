CREATE DEFINER=`root`@`localhost` TRIGGER `pedido_BEFORE_DELETE` BEFORE DELETE ON `pedido` FOR EACH ROW BEGIN
	 INSERT INTO Logs_Acao_Ped VALUES(null, now(), 'Deletar');
END