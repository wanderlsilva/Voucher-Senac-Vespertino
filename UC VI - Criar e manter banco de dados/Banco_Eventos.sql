-- Criação do Banco de Dados
CREATE DATABASE SistemaEventos;
USE SistemaEventos;

-- Criação das Tabelas
CREATE TABLE Local (
    id_local INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(200),
    capacidade INT
);

CREATE TABLE CategoriaEvento (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE Evento (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    data DATE,
    carga_horaria INT,
    id_local INT,
    id_categoria INT,
    FOREIGN KEY (id_local) REFERENCES Local(id_local),
    FOREIGN KEY (id_categoria) REFERENCES CategoriaEvento(id_categoria)
);

CREATE TABLE Instrutor (
    id_instrutor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    especialidade VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE Participante (
    id_participante INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(14),
    email VARCHAR(100)
);

CREATE TABLE Tema (
    id_tema INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    descricao TEXT
);

CREATE TABLE Evento_Tema (
    id_evento INT,
    id_tema INT,
    PRIMARY KEY (id_evento, id_tema),
    FOREIGN KEY (id_evento) REFERENCES Evento(id_evento),
    FOREIGN KEY (id_tema) REFERENCES Tema(id_tema)
);

CREATE TABLE Inscricao (
    id_inscricao INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT,
    id_participante INT,
    data_inscricao DATE,
    FOREIGN KEY (id_evento) REFERENCES Evento(id_evento),
    FOREIGN KEY (id_participante) REFERENCES Participante(id_participante)
);

CREATE TABLE Certificado (
    id_certificado INT AUTO_INCREMENT PRIMARY KEY,
    id_participante INT,
    id_evento INT,
    status VARCHAR(20),
    data_emissao DATE,
    FOREIGN KEY (id_participante) REFERENCES Participante(id_participante),
    FOREIGN KEY (id_evento) REFERENCES Evento(id_evento)
);

-- Inserção de Dados
INSERT INTO Local (nome, endereco, capacidade) VALUES
('Auditório Central', 'Rua das Flores, 123', 300),
('Sala de Reunião', 'Av. Paulista, 456', 50),
('Centro de Convenções', 'Rua A, 789', 500);

INSERT INTO CategoriaEvento (nome) VALUES
('Workshop'),
('Palestra'),
('Treinamento');

INSERT INTO Evento (nome, data, carga_horaria, id_local, id_categoria) VALUES
('Workshop de Python', '2025-06-10', 8, 1, 1),
('Palestra sobre IA', '2025-07-15', 2, 2, 2),
('Treinamento em SQL', '2025-08-20', 6, 3, 3);

INSERT INTO Instrutor (nome, especialidade, email) VALUES
('Ana Souza', 'Python', 'ana@eventos.com'),
('Carlos Lima', 'Inteligência Artificial', 'carlos@eventos.com'),
('Fernanda Costa', 'SQL e Bancos de Dados', 'fernanda@eventos.com');

INSERT INTO Participante (nome, cpf, email) VALUES
('João Silva', '123.456.789-00', 'joao@exemplo.com'),
('Maria Santos', '987.654.321-00', 'maria@exemplo.com'),
('Pedro Oliveira', '111.222.333-44', 'pedro@exemplo.com');

INSERT INTO Tema (titulo, descricao) VALUES
('Introdução ao Python', 'Conceitos básicos da linguagem Python.'),
('Redes Neurais', 'Aplicações de IA com redes neurais.'),
('Consultas SQL', 'Criação e otimização de consultas.');

INSERT INTO Evento_Tema (id_evento, id_tema) VALUES
(1,1), (2,2), (3,3);

INSERT INTO Inscricao (id_evento, id_participante, data_inscricao) VALUES
(1,1,'2025-06-01'),
(2,2,'2025-07-01'),
(3,3,'2025-08-01');

INSERT INTO Certificado (id_participante, id_evento, status, data_emissao) VALUES
(1,1,'Emitido','2025-06-15'),
(2,2,'Emitido','2025-07-20'),
(3,3,'Não Emitido',NULL);

-- Consultas (DQL)
-- 1. Listar todos os eventos e seus instrutores (vamos assumir um relacionamento por tema)
SELECT E.nome AS Evento, T.titulo AS Tema, I.nome AS Instrutor
FROM Evento E
JOIN Evento_Tema ET ON E.id_evento = ET.id_evento
JOIN Tema T ON ET.id_tema = T.id_tema
JOIN Instrutor I ON T.id_tema = I.id_instrutor; -- Opcional, se associarmos tema a instrutor

-- 2. Listar os participantes de um evento específico (ex: id_evento=1)
SELECT P.nome AS Participante
FROM Participante P
JOIN Inscricao I ON P.id_participante = I.id_participante
WHERE I.id_evento = 1;

-- 3. Listar inscrições de um participante e o status do certificado
SELECT E.nome AS Evento, C.status, C.data_emissao
FROM Certificado C
JOIN Evento E ON C.id_evento = E.id_evento
WHERE C.id_participante = 1;

-- 4. Listar temas abordados por evento
SELECT E.nome AS Evento, T.titulo AS Tema
FROM Evento E
JOIN Evento_Tema ET ON E.id_evento = ET.id_evento
JOIN Tema T ON ET.id_tema = T.id_tema;

-- INNER JOINs
-- a) Nome do participante, nome do evento e nome do instrutor (relacionamento indireto)
SELECT P.nome AS Participante, E.nome AS Evento, I.nome AS Instrutor
FROM Inscricao INSC
JOIN Participante P ON INSC.id_participante = P.id_participante
JOIN Evento E ON INSC.id_evento = E.id_evento
JOIN Evento_Tema ET ON E.id_evento = ET.id_evento
JOIN Tema T ON ET.id_tema = T.id_tema
JOIN Instrutor I ON T.id_tema = I.id_instrutor; -- Opcional se associar tema a instrutor

-- b) Lista de eventos, local e data
SELECT E.nome AS Evento, L.nome AS Local, E.data
FROM Evento E
JOIN Local L ON E.id_local = L.id_local;

