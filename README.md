<div align="center">
      <h1>ProjetoAPI</h1>
      <h3>Projeto de Banco de Dados Distribuídos, com Back-end e Front-end e Job <br>para ETL e Analytics em DWcom Deploy para Produção</h3>
</div>
<div align="center">
      <h2>Menu</h2>
      <p>
            <a href="#introducao"><span>:small_blue_diamond:</span>Introdução </a>
            <a href="#comousar"><span>:small_blue_diamond:</span>Como usar</a>
            <a href="#backlog"><span>:small_blue_diamond:</span>Backlog</a>
            <a href="#bd"><span>:small_blue_diamond:</span>Banco de Dados</a>
            <a href="#dashboard"><span>:small_blue_diamond:</span>Protótipo Dashboard</a>
            <a href="#equipe"><span>:small_blue_diamond:</span>Equipe</a>
      </p>
</div>

<a name="introducao"></a>
## :scroll: Introdução

### Visão do Projeto

Desenvolver  uma  solução  de  dados  voltada  ao ensino  à  distância  para  a  gestão  e  oferta  de conhecimento,  dando  suporte  às  mais  diversas  arquiteturas  de  aprendizagem,  alinhado  com  os objetivos estratégicos a serem alcançados por cada organização que atendemos como clientes. Fazer a gestão de logs para alimentar um Data Warehouse afim de possibilitar a melhor gestão estratégica do negócio.


### Apresentação da Evolução do Projeto
:white_check_mark: Sprint 1  | :white_large_square: Sprint 2 | :white_large_square: Sprint 3 | :white_large_square:  Sprint 4  
--------- |--------- |--------- |--------- |
[Aguarde]() |[Aguarde]() |[Aguarde]() |[Aguarde]() |

### Planejamento

Para fazer o planejamento foi utilizado a metodologia de "Design Thinking". Segundo o wikipedia, Design Thinking é o conjunto de ideias e insights para abordar problemas, relacionados a futuras aquisições de informações, análise de conhecimento e propostas de soluções.

:arrows_counterclockwise:O design thinking consiste em 5 partes ciclicas: empatia, definição, ideação, prototipo, teste.

- A primeira etapa (empatia) do primeiro ciclo foi realizada junto ao cliente.
- A etapa de definição é realizada durante as plannings do projeto.
- A etapa de ideação e prototipo são realizadas durante a sprint e 
- A etapa de teste é realizada sempre que um prototipo vira funcionalidade através do fluxo de CI (continuous integration) e CD (continuous deploy/delivery) do projeto.

### Cronograma

- [x] 16/08/2021 até 22/08/2021 - Kick Off do Projeto
- [x] 30/08/2021 até 19/09/2021 - Sprint 1
- [ ] 20/09/2021 até 10/10/2021 - Sprint 2
- [ ] 18/10/2021 até 07/10/2021 - Sprint 3
- [ ] 08/11/2021 até 28/11/2021 - Sprint 4
- [ ] 29/11/2021 até xx/12/2021 - Sprint Apresentação Final
- [ ] xx/xx/2021 até xx/xx/2021 - Sprint Feira de Soluções

### Gitflow

Aqui é discutido o Gitflow Workflow. Gitflow é um dos muitos estilos de [fluxos de trabalho Git](https://www.atlassian.com/br/git/tutorials/comparing-workflows) que você e sua equipe podem utilizar.

Alguns dos principais aprendizados para saber sobre o Gitflow são:

- O fluxo de trabalho é ótimo para um fluxo de trabalho de software baseado em lançamento.
- O Gitflow oferece um canal dedicado de hotfixes para produção.

O fluxo geral do Gitflow é:

1. Uma ramificação `development` é criada a partir da `main`
2. Uma ramificação de `release` é criada a partir da ramificação de `development`
3. As ramificações de `feature` são criadas a partir da ramificação de `development`
4. Quando um `feature` é concluído, deve ser aberto um Pull Request para `development`
5. Para completar o PR é necessário ser homologado pelo PO
6. Quando a ramificação `release` é feita, é feito o merge dela na ramificação `development` e na `main`
7. Se for detectado um item na `main`, uma ramificação de `hotfix` vai ser criada a partir da `main`
8. Depois que o `hotfix` for concluído, existe o mesmo processo de homologação, ele passa por merge para a ramificação `development` e à `main`

<a name="comousar"></a>
## :capital_abcd: Como usar

### Dockerfiles para os serviços utilizados

#### Instalando o docker: 
- Windows: https://docs.docker.com/desktop/windows/install/
**obs.: Caso possua 2 hds e/ou queira uma melhor customização dos recursos utilizados, recomendo utilizar o Hyper-v no lugar do WSL (https://docs.microsoft.com/pt-br/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)**
- Linux: https://docs.docker.com/engine/install/ubuntu/  || https://docs.docker.com/compose/install/

#### Subindo os containers
`docker-compose -f <arquivo.yml> up -d`

#### Down containers 
``docker-compose <arquivo.yml> down``

#### Executando o sqlSever a partir do docker
- Pull da imagem:
`docker pull mcr.microsoft.com/mssql/server`
- Executando o serviço do sqlSever
`docker run --name sqlserver -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<SUA_SENHA>" -p 1433:1433 -d mcr.microsoft.com/mssql/server`

### Endereços importantes:

- Servidor do chat: http://157.245.243.16:3000/ (Importante que seja http por enquanto)
- Servidor sqlSever: 157.245.243.16:1433
- Servidor Primary Mongo: 157.245.243.16:3002
- Portas Mongo Secundary: 3003, 3004

<a name="arquitetura"></a>
## :bookmark_tabs: Arquitetura do Projeto

<a name="backlog"></a>
## :memo: Backlog

### USER STORIES
Na descrição dos story cards, temos 4 personas: Aluno, Tutor, Gestor e Administrado.

- Como aluno, eu sou capaz de acessar o chat em tempo real para interagir/discutir com outros alunos e tutores;;
- Como tutor, eu sou capaz de acessar o chat do aluno para interagir/discutir com outros alunos;
- Como aluno, eu sou capaz de acessar o chatbot da plataforma para buscar orientações rápidas;
- Como aluno/tutor, eu sou capaz de acessar o sistema de LMS;
- Como gestor, eu sou capaz de adicionar/editar/excluir cursos;
- Como tutor, eu sou capaz de acessar um dashboard com painéis informativos específicos para tutoria;
- Como gestor, eu sou capaz de acessar um dashboard com painéis informativos específicos para gestão;
- Como administrador, eu sou capaz de acessar um dashboard com painéis informativos específicos para administração;

### Requisitos Funcionais

#### :white_medium_square: Sprint 1
<strong>1</strong> - Definir as tabelas FATO do Data Warehouse;

<strong>2</strong> - Definir as dimensões e granularidade do Data Warehouse;

<strong>3</strong> - Desenvolver um chat em tempo real com capacidade de até 1000 usuários simultâneos, capaz de gerar log das mensagens;

<strong>4</strong> - Definir ferramentas para o pipeline ETL;

#### :white_medium_square: Sprint 2


<strong>5</strong> - Refatorar a plataforma de  LMS desenvolvida pela turma do 3º semestre de banco de dados (no primeiro semestre de 2021), para armazenar os dados do chatbot em um banco de dados não-relacional;

<strong>6</strong> - Criar rotinas para extrair os dados da plataforma e transformar os dados para posteriormente serem inseridos no Data Warehouse (a parte de carregamento dos dados será trabalhada na última sprint);

####  :white_medium_square: Sprint 3

<strong>7</strong> - Definir os gráficos para visualização dos Dashboards;

<strong>8</strong> - Criar um sistema OLAP com visualizações (com dados de testes) diferentes para os 3 tipos de usuário (Tutor, Gestor e ADM);

<strong>9</strong> - Integrar o sistema OLAP com o Data Warehouse.

<strong>10</strong> - Refatorar a plataforma de  LMS desenvolvida pela turma do 3º semestre de banco de dados (no primeiro semestre de 2021), para armazenar os dados dos logs em um banco de dados não-relacional;

#### :white_medium_square: Sprint 4

<strong>11</strong> - Reestruturar os logs da aplicação de acordo com as métricas esperadas no Data Warehouse ( Ativação, Engajamento, Desempenho, Participação, Avaliação de reação, Registro do tempo de participação no curso)

<strong>12</strong> - Criar rotinas para carregar os dados no Data Warehouse.

### :white_square_button: Requisitos não Funcionais

- Documentação completa e clara
- Facilidade de uso
- Segurança
- Escalabilidade

<a name="bd"></a>
## :floppy_disk: 5. Diagrama do Banco de Dados

 ![Diagrama do Banco de Dados](https://github.com/api-fatec-bd/api/blob/main/dw/untitled.png)

<a name="dashboard"></a>
## :capital_abcd:Protótipo Dashboard (OLAP)

<img src="https://user-images.githubusercontent.com/45483678/133944681-61d8d788-c48c-49a6-8eed-8ad03ec6f983.png" >
<img src="https://user-images.githubusercontent.com/45483678/133944684-42b16949-7979-4198-b5cd-7acba2689571.png">
<img src="https://user-images.githubusercontent.com/45483678/133944696-f7b08271-7bed-462e-b184-0eaca8420d7e.png">
<img src="https://user-images.githubusercontent.com/45483678/133944704-a0f85b76-b9d5-4123-9b76-e417f5be107b.png">

<a name="equipe"></a>
## :muscle: Equipe

| Gabriel Angelo | Fernanda Ramos | Nathan Nascimento | Paulo Filipini | Vitor Daniel  |
|---|---|---|---|---|
| [linkedIn](https://www.linkedin.com/in/gabriel-angelo-a4b251116/) | [linkedIn](https://www.linkedin.com/in/fernanda-ramos-de-padua-salles-44329b157/) | [linkedIn](https://www.linkedin.com/in/n4htan/) | [linkedIn](https://www.linkedin.com/in/paulo-henrique-filipini/) | [linkedIn](#) |
| <img src="https://avatars.githubusercontent.com/u/73532594?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/55774508?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/19509794?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/45483678?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/55815066?v=4" width="100px"> |


| André Lars | Daniel Delgado | Felipe Braga | Giovanni Guidace | Jéssica Isri  |
|---|---|---|---|---|
| [linkedIn](https://www.linkedin.com/in/andre-lars-da-cunha/) | [linkedIn](https://www.linkedin.com/in/daniel-delgado-274096194/) | [linkedIn](https://www.linkedin.com/in/felipegbraga/) |  [linkedIn](https://www.linkedin.com/in/giovanni-guidace-61982812a/) | [linkedIn](https://www.linkedin.com/in/jessica-dias1/) |
| <img src="https://avatars.githubusercontent.com/u/26588283?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/50891053?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/13703888?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/62898187?v=4" width="100px"> | <img src="https://avatars.githubusercontent.com/u/65822756?v=4" width="100px"> |

