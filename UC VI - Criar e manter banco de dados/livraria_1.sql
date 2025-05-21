-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 21/05/2025 às 21:40
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `livraria`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `autores`
--

CREATE TABLE `autores` (
  `pk_autor` int(11) NOT NULL,
  `nome_autor` varchar(100) NOT NULL,
  `data_nascimento_autor` date NOT NULL,
  `fk_nacionalidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `autores`
--

INSERT INTO `autores` (`pk_autor`, `nome_autor`, `data_nascimento_autor`, `fk_nacionalidade`) VALUES
(1, 'José', '1978-04-08', 1),
(2, 'Maria', '1962-07-08', 2),
(3, 'Thon', '1974-07-01', 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `categorias`
--

CREATE TABLE `categorias` (
  `pk_categoria` int(11) NOT NULL,
  `nome_categoria` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `categorias`
--

INSERT INTO `categorias` (`pk_categoria`, `nome_categoria`) VALUES
(1, 'Romance'),
(2, 'Fantasia'),
(3, 'Ficção Científica'),
(4, 'Terror'),
(5, 'Drama'),
(6, 'Suspense');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cidades`
--

CREATE TABLE `cidades` (
  `pk_cidade` int(11) NOT NULL,
  `nome_cidade` varchar(100) NOT NULL,
  `fk_estado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cidades`
--

INSERT INTO `cidades` (`pk_cidade`, `nome_cidade`, `fk_estado`) VALUES
(1, 'Corumbá', 1),
(2, 'Cuiabá', 4),
(3, 'Bauru', 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `clientes`
--

CREATE TABLE `clientes` (
  `pk_cliente` int(11) NOT NULL,
  `nome_cliente` varchar(100) NOT NULL,
  `cpf` int(11) NOT NULL,
  `data_nascimento_cliente` date NOT NULL,
  `cep` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `fk_cidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `clientes`
--

INSERT INTO `clientes` (`pk_cliente`, `nome_cliente`, `cpf`, `data_nascimento_cliente`, `cep`, `email`, `endereco`, `fk_cidade`) VALUES
(1, 'Antonio', 1122334455, '1987-02-24', '79000-080', 'antonio@gmail.com', 'Frei Mariano', 1),
(2, 'Maria', 99887766, '2000-07-04', '79000-070', 'maria@gmail.com', 'América', 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `estados`
--

CREATE TABLE `estados` (
  `pk_estado` int(11) NOT NULL,
  `nome_estado` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `estados`
--

INSERT INTO `estados` (`pk_estado`, `nome_estado`) VALUES
(1, 'Mato Grosso do Sul'),
(2, 'Rio de Janeiro'),
(3, 'São Paulo'),
(4, 'Mato Grosso'),
(5, 'Fortaleza'),
(6, 'Rio Grande do Sul'),
(7, 'Rio Grande do Norte');

-- --------------------------------------------------------

--
-- Estrutura para tabela `estoques`
--

CREATE TABLE `estoques` (
  `pk_estoque` int(11) NOT NULL,
  `quantidade_estoque` int(11) NOT NULL,
  `fk_livro` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `estoques`
--

INSERT INTO `estoques` (`pk_estoque`, `quantidade_estoque`, `fk_livro`) VALUES
(1, 50, 1),
(2, 280, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `itens_pedidos`
--

CREATE TABLE `itens_pedidos` (
  `fk_livro` int(11) DEFAULT NULL,
  `fk_pedido` int(11) DEFAULT NULL,
  `quantidade_item` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `itens_pedidos`
--

INSERT INTO `itens_pedidos` (`fk_livro`, `fk_pedido`, `quantidade_item`) VALUES
(1, 2, 5),
(1, 1, 3),
(2, 1, 4);

-- --------------------------------------------------------

--
-- Estrutura para tabela `livros`
--

CREATE TABLE `livros` (
  `pk_livro` int(11) NOT NULL,
  `isbn` int(15) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `ano` date NOT NULL,
  `editora` varchar(100) NOT NULL,
  `preco` decimal(10,2) NOT NULL,
  `fk_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `livros`
--

INSERT INTO `livros` (`pk_livro`, `isbn`, `titulo`, `ano`, `editora`, `preco`, `fk_categoria`) VALUES
(1, 648725, 'Três Corações', '1998-04-30', 'Dilma', 350.00, 1),
(2, 264254, 'Senhor dos anéis', '2010-05-10', 'Abreu', 580.00, 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `livros_autores`
--

CREATE TABLE `livros_autores` (
  `pk_livro_autor` int(11) NOT NULL,
  `fk_livro` int(11) DEFAULT NULL,
  `fk_autor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `livros_autores`
--

INSERT INTO `livros_autores` (`pk_livro_autor`, `fk_livro`, `fk_autor`) VALUES
(1, 2, 1),
(2, 2, 3),
(3, 1, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `nacionalidades`
--

CREATE TABLE `nacionalidades` (
  `pk_nacionalidade` int(11) NOT NULL,
  `nome_nacionalidade` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `nacionalidades`
--

INSERT INTO `nacionalidades` (`pk_nacionalidade`, `nome_nacionalidade`) VALUES
(1, 'Brasil'),
(2, 'Portugal'),
(3, 'Estados Unidos'),
(4, 'Bolivia');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedidos`
--

CREATE TABLE `pedidos` (
  `pk_pedido` int(11) NOT NULL,
  `data_pedido` date NOT NULL,
  `status_pedido` enum('Finalizado','Cancelado') NOT NULL,
  `valor_pedido` decimal(10,2) NOT NULL,
  `fk_cliente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pedidos`
--

INSERT INTO `pedidos` (`pk_pedido`, `data_pedido`, `status_pedido`, `valor_pedido`, `fk_cliente`) VALUES
(1, '2025-05-18', 'Finalizado', 289.00, 2),
(2, '2025-04-10', 'Cancelado', 999.00, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`pk_autor`),
  ADD KEY `fk_autores_nacionalidade` (`fk_nacionalidade`);

--
-- Índices de tabela `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`pk_categoria`);

--
-- Índices de tabela `cidades`
--
ALTER TABLE `cidades`
  ADD PRIMARY KEY (`pk_cidade`),
  ADD KEY `fk_cidades_estado` (`fk_estado`);

--
-- Índices de tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`pk_cliente`),
  ADD KEY `fk_clientes_cidade` (`fk_cidade`);

--
-- Índices de tabela `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`pk_estado`);

--
-- Índices de tabela `estoques`
--
ALTER TABLE `estoques`
  ADD PRIMARY KEY (`pk_estoque`),
  ADD KEY `fk_estoques_livro` (`fk_livro`);

--
-- Índices de tabela `itens_pedidos`
--
ALTER TABLE `itens_pedidos`
  ADD KEY `fk_itens_livro` (`fk_livro`),
  ADD KEY `fk_itens_pedido` (`fk_pedido`);

--
-- Índices de tabela `livros`
--
ALTER TABLE `livros`
  ADD PRIMARY KEY (`pk_livro`),
  ADD KEY `fk_livros_categoria` (`fk_categoria`);

--
-- Índices de tabela `livros_autores`
--
ALTER TABLE `livros_autores`
  ADD PRIMARY KEY (`pk_livro_autor`),
  ADD KEY `fk_livros_autores_livro` (`fk_livro`),
  ADD KEY `fk_livros_autores_autor` (`fk_autor`);

--
-- Índices de tabela `nacionalidades`
--
ALTER TABLE `nacionalidades`
  ADD PRIMARY KEY (`pk_nacionalidade`);

--
-- Índices de tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`pk_pedido`),
  ADD KEY `fk_pedidos_cliente` (`fk_cliente`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `autores`
--
ALTER TABLE `autores`
  MODIFY `pk_autor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `categorias`
--
ALTER TABLE `categorias`
  MODIFY `pk_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `cidades`
--
ALTER TABLE `cidades`
  MODIFY `pk_cidade` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `pk_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `estados`
--
ALTER TABLE `estados`
  MODIFY `pk_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `estoques`
--
ALTER TABLE `estoques`
  MODIFY `pk_estoque` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `pk_livro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `livros_autores`
--
ALTER TABLE `livros_autores`
  MODIFY `pk_livro_autor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `nacionalidades`
--
ALTER TABLE `nacionalidades`
  MODIFY `pk_nacionalidade` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `pk_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `autores`
--
ALTER TABLE `autores`
  ADD CONSTRAINT `fk_autores_nacionalidade` FOREIGN KEY (`fk_nacionalidade`) REFERENCES `nacionalidades` (`pk_nacionalidade`);

--
-- Restrições para tabelas `cidades`
--
ALTER TABLE `cidades`
  ADD CONSTRAINT `fk_cidades_estado` FOREIGN KEY (`fk_estado`) REFERENCES `estados` (`pk_estado`);

--
-- Restrições para tabelas `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `fk_clientes_cidade` FOREIGN KEY (`fk_cidade`) REFERENCES `cidades` (`pk_cidade`);

--
-- Restrições para tabelas `estoques`
--
ALTER TABLE `estoques`
  ADD CONSTRAINT `fk_estoques_livro` FOREIGN KEY (`fk_livro`) REFERENCES `livros` (`pk_livro`);

--
-- Restrições para tabelas `itens_pedidos`
--
ALTER TABLE `itens_pedidos`
  ADD CONSTRAINT `fk_itens_livro` FOREIGN KEY (`fk_livro`) REFERENCES `livros` (`pk_livro`),
  ADD CONSTRAINT `fk_itens_pedido` FOREIGN KEY (`fk_pedido`) REFERENCES `pedidos` (`pk_pedido`);

--
-- Restrições para tabelas `livros`
--
ALTER TABLE `livros`
  ADD CONSTRAINT `fk_livros_categoria` FOREIGN KEY (`fk_categoria`) REFERENCES `categorias` (`pk_categoria`);

--
-- Restrições para tabelas `livros_autores`
--
ALTER TABLE `livros_autores`
  ADD CONSTRAINT `fk_livros_autores_autor` FOREIGN KEY (`fk_autor`) REFERENCES `autores` (`pk_autor`),
  ADD CONSTRAINT `fk_livros_autores_livro` FOREIGN KEY (`fk_livro`) REFERENCES `livros` (`pk_livro`);

--
-- Restrições para tabelas `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `fk_pedidos_cliente` FOREIGN KEY (`fk_cliente`) REFERENCES `clientes` (`pk_cliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
