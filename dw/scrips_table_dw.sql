CREATE TABLE IF NOT EXISTS public.dim_aula
(
    id_aula bigserial NOT NULL,
    data_inicio timestamp without time zone NOT NULL,
    data_fim timestamp without time zone NOT NULL,
    id_disciplina bigint NOT NULL,
    titulo character varying(45),
    duracao double precision NOT NULL,
    assunto character varying(100),
    PRIMARY KEY (id_aula)
);

CREATE TABLE IF NOT EXISTS public.dim_curso
(
    id_curso serial NOT NULL,
    descricao character varying(50) NOT NULL,
    graduacao character varying(50) NOT NULL,
    duracao integer NOT NULL,
    PRIMARY KEY (id_curso)
);

CREATE TABLE IF NOT EXISTS public.dim_disciplina
(
    id_disciplina bigserial NOT NULL,
    id_curso integer NOT NULL,
    descricao character varying(50) NOT NULL,
    id_turma bigint NOT NULL,
    PRIMARY KEY (id_disciplina)
);

CREATE TABLE IF NOT EXISTS public.dim_turma
(
    id_turma bigserial NOT NULL,
    descricao character varying(50) NOT NULL,
    id_professor bigint NOT NULL,
    PRIMARY KEY (id_turma)
);

CREATE TABLE IF NOT EXISTS public.dim_usuario
(
    id_usuario bigserial NOT NULL,
    nome_usuario character varying(100),
    username character varying(50),
    codigo_perfil integer NOT NULL,
    descricao_perfil character varying(50) NOT NULL,
    UNIQUE (username),
    PRIMARY KEY (id_usuario)
);

CREATE TABLE IF NOT EXISTS public.fact_aluno_aula
(
    id_aluno_aula bigserial NOT NULL,
    id_aluno bigint NOT NULL,
    id_aula bigint NOT NULL,
    tempo_participacao double precision,
    reacao double precision,
    PRIMARY KEY (id_aluno_aula)
);

CREATE TABLE IF NOT EXISTS public.fact_acesso
(
    id_usuario bigserial NOT NULL,
    data_login timestamp without time zone NOT NULL,
    data_logoff timestamp without time zone NOT NULL,
    origem character (1),
    PRIMARY KEY(id_usuario,data_login,origem)
);

CREATE TABLE IF NOT EXISTS public.fact_matricula
(
    id_matricula bigserial NOT NULL,
    data_inicio timestamp without time zone NOT NULL,
    data_fim timestamp without time zone NOT NULL,
    id_aluno bigint NOT NULL,
    id_turma bigint NOT NULL,
    id_disciplina bigint NOT NULL,
    id_certificado bigint,
    numero_certificado character varying(45),
    status_matricula bit(1) NOT NULL,
    quantidade_matricula integer NOT NULL,
    PRIMARY KEY (id_matricula)
);

CREATE TABLE IF NOT EXISTS public.fact_nota
(
    id_nota bigserial NOT NULL,
    id_aluno bigint NOT NULL,
    id_disciplina bigint NOT NULL,
    nota double precision NOT NULL,
    nota_avaliacao double precision NOT NULL,
    percentual_nota double precision NOT NULL,
    data timestamp without time zone NOT NULL,
    PRIMARY KEY (id_nota)
);

CREATE TABLE IF NOT EXISTS public.dim_chat
(
    id_chat character varying(50) NOT NULL,
    data_inicio timestamp without time zone NOT NULL,
    data_fim timestamp without time zone NOT NULL,
    quantidade_usuario int NOT NULL,
    descricao character varying(80) NOT NULL,
    duracao double precision NOT NULL,
    PRIMARY KEY (id_chat)
);

CREATE TABLE IF NOT EXISTS public.fact_usuario_chat
(
   id_usuario_chat bigserial NOT NULL,
   id_usuario bigint NOT NULL,
   id_chat character varying(50) NOT NULL,
   data_login timestamp without time zone NOT NULL,
   data_logoff timestamp without time zone NOT NULL,
   quantidade_mensagens integer NOT NULL,
   data_ultima_msg timestamp without time zone NOT NULL,
   tempo_participacao double precision NOT NULL,
   PRIMARY KEY (id_usuario_chat)
);

CREATE TABLE IF NOT EXISTS public.fact_usuario_conteudo
(
	id_usuario_conteudo bigserial NOT NULL,
    id_usuario bigint NOT NULL,
	data_upload timestamp without time zone NOT NULL,
	data_download timestamp without time zone NOT NULL,
    id_conteudo bigint NOT NULL,
    id_disciplina bigint NOT NULL,
    id_aula bigint NOT NULL,
	PRIMARY KEY (id_usuario_conteudo)	
);



ALTER TABLE public.dim_disciplina
    ADD FOREIGN KEY (id_curso)
    REFERENCES public.dim_curso (id_curso)
    NOT VALID;

ALTER TABLE public.dim_aula
    ADD FOREIGN KEY (id_disciplina)
    REFERENCES public.dim_disciplina (id_disciplina)
    NOT VALID;

ALTER TABLE public.fact_aluno_aula
    ADD FOREIGN KEY (id_aluno)
    REFERENCES public.dim_usuario (id_usuario)
    NOT VALID;

ALTER TABLE public.fact_aluno_aula
    ADD FOREIGN KEY (id_aula)
    REFERENCES public.dim_aula (id_aula)
    NOT VALID;

ALTER TABLE public.fact_acesso
    ADD FOREIGN KEY (id_usuario)
    REFERENCES public.dim_usuario (id_usuario)
    NOT VALID;

ALTER TABLE public.fact_matricula
    ADD FOREIGN KEY (id_aluno)
    REFERENCES public.dim_usuario (id_usuario)
    NOT VALID;

ALTER TABLE public.fact_matricula
    ADD FOREIGN KEY (id_disciplina)
    REFERENCES public.dim_disciplina (id_disciplina)
    NOT VALID;

ALTER TABLE public.fact_matricula
    ADD FOREIGN KEY (id_turma)
    REFERENCES public.dim_turma (id_turma)
    NOT VALID;

ALTER TABLE public.fact_nota
    ADD FOREIGN KEY (id_aluno)
    REFERENCES public.dim_usuario (id_usuario)
    NOT VALID;

ALTER TABLE public.fact_nota
    ADD FOREIGN KEY (id_disciplina)
    REFERENCES public.dim_disciplina (id_disciplina)
    NOT VALID;

ALTER TABLE public.fact_usuario_conteudo
    ADD FOREIGN KEY (id_usuario)
    REFERENCES public.dim_usuario (id_usuario)
    NOT VALID;

ALTER TABLE public.fact_usuario_conteudo
    ADD FOREIGN KEY (id_disciplina)
    REFERENCES public.dim_disciplina (id_disciplina)
    NOT VALID;

ALTER TABLE public.fact_usuario_conteudo
    ADD FOREIGN KEY (id_aula)
    REFERENCES public.dim_aula (id_aula)
    NOT VALID;

ALTER TABLE public.fact_usuario_chat
    ADD FOREIGN KEY (id_usuario)
    REFERENCES public.dim_usuario (id_usuario)
    NOT VALID;

END;