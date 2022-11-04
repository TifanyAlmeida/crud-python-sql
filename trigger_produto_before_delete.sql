CREATE DEFINER=`root`@`localhost` TRIGGER `produto_BEFORE_DELETE` BEFORE DELETE ON `produto` FOR EACH ROW BEGIN
	    INSERT INTO Logs_Acao_Prod VALUES(null, now(), 'Deletar');
END