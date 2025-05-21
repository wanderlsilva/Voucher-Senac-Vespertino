-- DROP DATABASE livraria;
CREATE DATABASE IF NOT EXISTS livraria;

USE livraria;

CREATE TABLE estoques(
pk_estoque INT PRIMARY KEY AUTO_INCREMENT,
quantidade_estoque INT NOT NULL,
fk_livro INT
);

CREATE TABLE categorias(
pk_categoria INT PRIMARY KEY AUTO_INCREMENT,
nome_categoria VARCHAR(100) NOT NULL
);

CREATE TABLE livros(
pk_livro INT PRIMARY KEY AUTO_INCREMENT,
isbn INT(15) NOT NULL,
titulo VARCHAR(100) NOT NULL,
ano DATE NOT NULL,
editora VARCHAR(100) NOT NULL,
preco DECIMAL(10,2) NOT NULL,
fk_categoria INT
);

CREATE TABLE livros_autores(
pk_livro_autor INT PRIMARY KEY AUTO_INCREMENT,
fk_livro INT,
fk_autor INT
);

CREATE TABLE autores(
pk_autor INT PRIMARY KEY AUTO_INCREMENT,
nome_autor VARCHAR(100) NOT NULL,
data_nascimento_autor DATE NOT NULL,
fk_nacionalidade INT
);

CREATE TABLE nacionalidades(
pk_nacionalidade INT PRIMARY KEY AUTO_INCREMENT,
nome_nacionalidade VARCHAR(100) NOT NULL
);

CREATE TABLE estados(
pk_estado INT PRIMARY KEY AUTO_INCREMENT,
nome_estado VARCHAR(100) NOT NULL
);

CREATE TABLE cidades(
pk_cidade INT PRIMARY KEY AUTO_INCREMENT,
nome_cidade VARCHAR(100) NOT NULL,
fk_estado INT
);

CREATE TABLE clientes(
pk_cliente INT PRIMARY KEY AUTO_INCREMENT,
nome_cliente VARCHAR(100) NOT NULL,
cpf INT(11) NOT NULL,
data_nascimento_cliente DATE NOT NULL,
cep VARCHAR(10) NOT NULL,
email VARCHAR(50) NOT NULL,
endereco VARCHAR(100) NOT NULL
);

CREATE TABLE pedidos(
pk_pedido INT PRIMARY KEY AUTO_INCREMENT,
data_pedido DATE NOT NULL,
status_pedido ENUM ('Finalizado','Cancelado') NOT NULL,
valor_pedido DECIMAL(10,2) NOT NULL,
fk_cliente INT
);

CREATE TABLE itens_pedidos(
fk_livro INT,
fk_pedido INT,
quantidade_item INT NOT NULL
);

ALTER TABLE estoques ADD CONSTRAINT fk_estoques_livro FOREIGN KEY (fk_livro) REFERENCES livros(pk_livro);
ALTER TABLE livros ADD CONSTRAINT fk_livros_categoria FOREIGN KEY (fk_categoria) REFERENCES categorias(pk_categoria);
ALTER TABLE autores ADD CONSTRAINT fk_autores_nacionalidade FOREIGN KEY (fk_nacionalidade) REFERENCES nacionalidades(pk_nacionalidade);
ALTER TABLE livros_autores ADD CONSTRAINT fk_livros_autores_livro FOREIGN KEY (fk_livro) REFERENCES livros(pk_livro);
ALTER TABLE livros_autores ADD CONSTRAINT fk_livros_autores_autor FOREIGN KEY (fk_autor) REFERENCES autores(pk_autor);
ALTER TABLE cidades ADD CONSTRAINT fk_cidades_estado FOREIGN KEY (fk_estado) REFERENCES estados(pk_estado);
ALTER TABLE clientes ADD COLUMN fk_cidade INT;
ALTER TABLE clientes ADD CONSTRAINT fk_clientes_cidade FOREIGN KEY (fk_cidade) REFERENCES cidades(pk_cidade);
ALTER TABLE pedidos ADD CONSTRAINT fk_pedidos_cliente FOREIGN KEY (fk_cliente) REFERENCES clientes(pk_cliente);
ALTER TABLE itens_pedidos ADD CONSTRAINT fk_itens_livro FOREIGN KEY (fk_livro) REFERENCES livros(pk_livro);
ALTER TABLE itens_pedidos ADD CONSTRAINT fk_itens_pedido FOREIGN KEY (fk_pedido) REFERENCES pedidos(pk_pedido);
