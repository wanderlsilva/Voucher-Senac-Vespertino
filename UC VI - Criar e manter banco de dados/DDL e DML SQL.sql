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
ALTER TABLE prescricoes DROP FOREIGN KEY fk_medico;
ALTER TABLE `prescricoes`
	DROP COLUMN `fk_medico`,
	DROP INDEX `fk_medico`,
	DROP FOREIGN KEY `prescricoes_ibfk_1`;


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

-- Tabela Fornecedores
CREATE TABLE fornecedores(
pk_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
nome_fornecedor VARCHAR(100) NOT NULL,
cnpj VARCHAR(15) NOT NULL
);

-- Tabela Medicamentos
CREATE TABLE medicamentos(
pk_medicamento INT PRIMARY KEY AUTO_INCREMENT,
nome_medicamento VARCHAR(100) NOT NULL,
dosagem VARCHAR(50) NOT NULL,
fk_fornecedor INT,
FOREIGN KEY (fk_fornecedor) REFERENCES fornecedores (pk_fornecedor)
);

-- Tabela Prescrição
CREATE TABLE prescricoes(
pk_prescricao INT PRIMARY KEY AUTO_INCREMENT,
descricao_prescricao VARCHAR(250) NOT NULL,
fk_medico INT,
FOREIGN KEY (fk_medico) REFERENCES medicos (pk_medico)
);

-- Adicionando uma chave estrangeira em uma tabela existente
ALTER TABLE prescricoes ADD COLUMN fk_medicamento INT;
ALTER TABLE prescricoes ADD CONSTRAINT fk_medicamento FOREIGN KEY (fk_medicamento) REFERENCES medicamentos(pk_medicamento);

-- Tabela Paciente
CREATE TABLE pacientes(
pk_paciente INT PRIMARY KEY AUTO_INCREMENT,
nome_paciente VARCHAR(150) NOT NULL,
data_nascimento DATE NOT NULL,
cpf VARCHAR(11) NOT NULL
);

-- Tabela Consulta
CREATE TABLE consultas(
pk_consulta INT PRIMARY KEY AUTO_INCREMENT,
data_consulta DATE,
fk_medico INT,
fk_paciente INT,
FOREIGN KEY (fk_medico) REFERENCES medicos (pk_medico),
FOREIGN KEY (fk_paciente) REFERENCES pacientes (pk_paciente)
);

-- Adicionando uma chave estrangeira em uma tabela existente
ALTER TABLE prescricoes ADD COLUMN fk_consulta INT;
ALTER TABLE prescricoes ADD CONSTRAINT fk_consulta FOREIGN KEY (fk_consulta) REFERENCES consultas(pk_consulta);

CREATE TABLE convenios(
pk_convenio INT PRIMARY KEY AUTO_INCREMENT,
nome_convenio VARCHAR(100) NOT NULL,
tipo_convenio VARCHAR(50) NOT NULL
);


-- Adicionando uma chave estrangeira em uma tabela existente
ALTER TABLE pacientes ADD COLUMN fk_convenio INT;
ALTER TABLE pacientes ADD CONSTRAINT fk_convenio FOREIGN KEY (fk_convenio) REFERENCES convenios(pk_convenio);

CREATE TABLE prontuarios(
pk_prontuario INT PRIMARY KEY AUTO_INCREMENT,
historio_prontuario VARCHAR(255) NOT NULL,
fk_paciente INT,
FOREIGN KEY (fk_paciente) REFERENCES pacientes(pk_paciente)
);

CREATE TABLE exames(
pk_exame INT PRIMARY KEY AUTO_INCREMENT,
nome_exame VARCHAR(100) NOT NULL,
tipo_exame VARCHAR(50) NOT NULL,
data_exame DATE
);

CREATE TABLE resultados_exames(
pk_resultado_exame INT PRIMARY KEY AUTO_INCREMENT,
descricao_resultado TEXT,
fk_paciente INT,
fk_exame INT,
FOREIGN KEY (fk_paciente) REFERENCES pacientes(pk_paciente),
FOREIGN KEY (fk_exame) REFERENCES exames(pk_exame)
);

CREATE TABLE enfermeiros(
pk_enfermeiro INT PRIMARY KEY AUTO_INCREMENT,
nome_enfermeiro VARCHAR(100) NOT NULL,
coren VARCHAR(50) NOT NULL
);

CREATE TABLE internacoes(
pk_internacao INT PRIMARY KEY AUTO_INCREMENT,
data_internacao DATE,
data_alta DATE,
fk_paciente INT,
fk_enfermeiro INT,
FOREIGN KEY (fk_paciente) REFERENCES pacientes(pk_paciente),
FOREIGN KEY (fk_enfermeiro) REFERENCES enfermeiros(pk_enfermeiro)
);