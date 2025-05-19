-- Excluir um banco de dados
DROP DATABASE hospital;

-- Criar um Banco de Dados
-- CREATE DATABASE hospital;
CREATE DATABASE IF NOT EXISTS hospital;

-- Selecionar um banco de dados para ser utilizado
USE hospital;

-- Criando uma tabela
CREATE TABLE equipamentos_medicos (
pk_equipamento_medico INT PRIMARY KEY AUTO_INCREMENT,
nome_equipamento_medico VARCHAR(100) NOT NULL
);

CREATE TABLE salas_atendimentos(
pk_sala_atendimento INT PRIMARY KEY AUTO_INCREMENT,
numero_sala_atendimento VARCHAR(50) NOT NULL,
tipo_sala_atendimento VARCHAR(50) NOT NULL,
fk_equipamento_medico INT,
FOREIGN KEY (fk_equipamento_medico) REFERENCES equipamentos_medicos (pk_equipamento_medico)
);

CREATE TABLE especialidades(
pk_especialidade INT PRIMARY KEY AUTO_INCREMENT,
nome_especialidade VARCHAR(10) NOT NULL
);

-- Renomear uma tabela
ALTER TABLE expecialidade RENAME TO especialidade;

-- Excluir uma tabela
DROP TABLE especialidade;

-- Adicionar um atributo a uma tabela
ALTER TABLE especialidade ADD nome_especialidade VARCHAR(100) NOT NULL;
ALTER TABLE especialidade ADD pk_especialidade INT PRIMARY KEY AUTO_INCREMENT;

-- Excluir um atributo de uma tabela
ALTER TABLE especialidade DROP COLUMN nome_especialidade;
ALTER TABLE especialidade DROP COLUMN pk_expecialidade;

CREATE TABLE medicos(
pk_medico INT PRIMARY KEY AUTO_INCREMENT,
nome_medico VARCHAR(150) NOT NULL,
crm VARCHAR(30) NOT NULL,
email_medico VARCHAR(30) NOT NULL,
fk_especialidade INT,
FOREIGN KEY (fk_especialidade) REFERENCES especialidades (pk_especialidade)
);

-- Adicionando uma chave estrangeira em uma tabela existente
ALTER TABLE salas_atendimentos ADD COLUMN fk_medico INT;
ALTER TABLE salas_atendimentos ADD CONSTRAINT fk_medico FOREIGN KEY (fk_medico) REFERENCES medicos(pk_medico);