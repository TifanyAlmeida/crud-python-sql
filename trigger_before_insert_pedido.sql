CREATE DEFINER=`root`@`localhost` TRIGGER `pedido_BEFORE_INSERT` BEFORE INSERT ON `pedido` FOR EACH ROW BEGIN
	 INSERT INTO Logs_Acao_Ped VALUES(null, now(), 'Inserir');
END