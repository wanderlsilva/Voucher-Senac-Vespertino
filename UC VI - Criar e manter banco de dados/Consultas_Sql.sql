-- CONSULTAS SIMPLES ----
SELECT * FROM livros;
SELECT titulo FROM livros;
SELECT isbn AS 'Registro do Livro', preco AS 'Preço R$: ' FROM livros;

-- CONSULTAS COM FILTRAGEM ----
SELECT * FROM livros WHERE preco > 400;
SELECT * FROM livros WHERE preco > 300 AND fk_categoria > 1;
SELECT * FROM livros WHERE titulo LIKE 's%';

-- CONSULTAS COM ORDENAÇÃO
SELECT * FROM livros ORDER BY isbn ASC;
SELECT * FROM livros ORDER BY isbn DESC;
SELECT * FROM livros ORDER BY isbn ASC LIMIT 3;

-- CONSULTA OM AGREGAÇÃO
SELECT cidades.nome_cidade, estados.nome_estado, cidades.fk_estado, estados.pk_estado
FROM cidades
INNER JOIN estados ON cidades.fk_estado = estados.pk_estado;

SELECT clientes.nome_cliente, cidades.nome_cidade, estados.nome_estado
FROM clientes
INNER JOIN cidades ON clientes.fk_cidade = cidades.pk_cidade
INNER JOIN estados ON cidades.fk_estado = estados.pk_estado
GROUP BY cidades.fk_estado;

SELECT COUNT(titulo) FROM livros;

SELECT livros.titulo, categorias.nome_categoria, estoques.quantidade_estoque, autores.nome_autor, nacionalidades.nome_nacionalidade
FROM livros_autores
INNER JOIN livros ON livros.pk_livro = livros_autores.fk_livro
INNER JOIN autores ON autores.pk_autor = livros_autores.fk_autor
INNER JOIN nacionalidades ON nacionalidades.pk_nacionalidade = autores.fk_nacionalidade
INNER JOIN categorias ON categorias.pk_categoria = livros.fk_categoria
INNER JOIN estoques ON livros.pk_livro = estoques.fk_livro;

/*INSERT INTO livros (isbn, titulo, ano, editora, preco, fk_categoria)
VALUES
(236456523, 'Livro A', '1985-09-05', 'Zeus', '120,00', 2),
(85261841, 'Livro B', '1986-07-15', 'Ave', '680,00', 5),
(79856231, 'Livro C', '1987-01-25', 'Monza', '890,00', 6),
(11531556, 'Livro D', '1988-03-09', 'Bela', '430,00', 4),
(69897461, 'Livro E', '1989-08-12', 'Reus', '740,00', 3);*/
