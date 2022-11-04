CREATE DEFINER=`root`@`localhost` TRIGGER `produto_BEFORE_INSERT` BEFORE INSERT ON `produto` FOR EACH ROW BEGIN
	 INSERT INTO Logs_Acao_Prod VALUES(null, now(), 'Inserir');
END