CREATE DEFINER=`root`@`localhost` TRIGGER `produto_AFTER_INSERT` AFTER INSERT ON `produto` FOR EACH ROW BEGIN
	INSERT INTO Logs_Acao_Prod VALUES(null, now());
END