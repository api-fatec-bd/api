-- -----------------------------------------------------
-- Table dim_usuario
-- -----------------------------------------------------
CREATE TABLE dim_usuario (
  id_usuario BIGINT IDENTITY NOT NULL PRIMARY KEY NONCLUSTERED,
  nome_usuario VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  codigo_permissao INT NOT NULL,
  descricao_permissao VARCHAR(50) NOT NULL,
  tel_1 VARCHAR(45) NULL,
  tel_2 VARCHAR(45) NULL
 );

-- -----------------------------------------------------
-- Table dim_turma
-- -----------------------------------------------------
CREATE TABLE dim_turma (
  id_turma BIGINT IDENTITY NOT NULL PRIMARY KEY NONCLUSTERED,
  descricao VARCHAR(50) NOT NULL,
  id_professor BIGINT NOT NULL,
  INDEX fk_id_professor_idx (id_professor ASC),
  CONSTRAINT fk_id_professor
    FOREIGN KEY (id_professor)
    REFERENCES dim_usuario (id_usuario)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
	GO

-- -----------------------------------------------------
-- Table dim_curso
-- -----------------------------------------------------
CREATE TABLE dim_curso (
  id_curso INT IDENTITY NOT NULL PRIMARY KEY NONCLUSTERED,
  descricao VARCHAR(50) NOT NULL,
  graduação VARCHAR(50) NOT NULL,
  duracao INT NOT NULL,
  )
GO

-- -----------------------------------------------------
-- Table dim_disciplina
-- -----------------------------------------------------
CREATE TABLE dim_disciplina (
  id_disciplina BIGINT IDENTITY NOT NULL PRIMARY KEY NONCLUSTERED,
  id_curso INT NOT NULL,
  descricao VARCHAR(50) NOT NULL,
  id_turma BIGINT NOT NULL,
  INDEX fk_id_curso_idx (id_curso ASC),
  CONSTRAINT fk_id_curso
    FOREIGN KEY (id_curso)
    REFERENCES dim_curso (id_curso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
GO


-- -----------------------------------------------------
-- Table fact_matricula
-- -----------------------------------------------------
CREATE TABLE fact_matricula (
  id_matricula BIGINT PRIMARY KEY NOT NULL,
  data_inicio DATETIME NOT NULL,
  data_fim DATETIME NOT NULL,
  id_aluno BIGINT NOT NULL REFERENCES dim_usuario (id_usuario),
  id_turma BIGINT NOT NULL REFERENCES dim_turma (id_turma),
  id_disciplina BIGINT NOT NULL REFERENCES dim_disciplina (id_disciplina),
  id_certificado BIGINT NULL,
  numero_certificado VARCHAR(45) NULL,
  status_matricula BIT NOT NULL,
  quantidade_matricula INT NOT NULL,
  INDEX fk_data_inicio_idx (data_inicio ASC),
  INDEX fk_data_fim_idx (data_fim ASC)
  )
  GO

-- -----------------------------------------------------
-- Table fact_nota
-- -----------------------------------------------------
CREATE TABLE fact_nota (
  id_nota BIGINT PRIMARY KEY NOT NULL,
  id_aluno BIGINT NOT NULL REFERENCES dim_usuario (id_usuario),
  nota FLOAT NOT NULL,
  nota_avaliacao FLOAT NOT NULL,
  percentual_nota FLOAT NOT NULL,
  id_disciplina BIGINT NOT NULL REFERENCES dim_disciplina (id_disciplina),
  data DATETIME NOT NULL,
  INDEX fk_id_aluno_idx (id_aluno ASC),
  INDEX fk_id_disciplina_idx (id_disciplina ASC)
  )
  GO


-- -----------------------------------------------------
-- Table dim_aula
-- -----------------------------------------------------
CREATE TABLE dim_aula (
  id_aula BIGINT PRIMARY KEY NOT NULL,
  data DATETIME NOT NULL,
  id_disciplina BIGINT NOT NULL REFERENCES dim_disciplina (id_disciplina),
  titulo VARCHAR(45) NULL,
  duracao FLOAT NOT NULL,
  assunto VARCHAR(100) NULL,
  INDEX fk_id_disciplina_idx (id_disciplina ASC),
  INDEX fk_data_idx (data ASC) 
  )
GO


-- -----------------------------------------------------
-- Table fact_aluno_aula
-- -----------------------------------------------------
CREATE TABLE fact_aluno_aula (
  id_aluno_aula BIGINT PRIMARY KEY NOT NULL,
  id_aluno BIGINT NOT NULL REFERENCES dim_usuario (id_usuario),
  reacao_valor FLOAT NULL,
  data_reacao DATETIME NOT NULL, 
  id_aula BIGINT NOT NULL REFERENCES dim_aula (id_aula),
  quantidade_msg INT NULL,
  tempo_participacao FLOAT NULL,
  media_reacao FLOAT NULL,

  INDEX fk_data_idx (data_reacao ASC),
  INDEX fk_id_aula_idx (id_aula ASC),
  INDEX fk_id_aluno_idx (id_aluno ASC)
  )
  GO


-- -----------------------------------------------------
-- Table fact_login_plataforma
-- -----------------------------------------------------
CREATE TABLE fact_login_plataforma (
  id_usuario BIGINT NOT NULL PRIMARY KEY REFERENCES dim_usuario (id_usuario),
  data_login DATETIME NOT NULL,
  data_logoff  DATETIME NOT NULL,
  quantidade_acesso INT NOT NULL,
  INDEX fk_data_login_idx (data_login ASC),
  INDEX fk_data_logoff_idx (data_logoff ASC)
	)
GO