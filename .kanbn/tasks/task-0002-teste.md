---
created: 2025-05-12T23:04:16.429Z
updated: 2025-05-12T23:09:49.930Z
assigned: 'Sergio Pereira'
progress: 0
tags:
  - TASK-0002
  - TASK-0003
  - TASK-0004
  - TASK-0004-ST-012
  - TASK-0005
---

# TASK-0002 TESTE

Product Backlog para Sprint 1 (Timebox: 1 Semana - Foco MVP)

Tema da Sprint: Estabelecer a fundação da ferramenta: conexão com banco, estrutura de dados básica, e a capacidade de gerar um arquivo .env simples via CLI.

## Comments

- author: Sergio Pereira
  date: 2025-05-11T14:33:06.631Z
  Itens do Backlog (Priorizados - Do Mais para o Menos Crítico para o MVP):
  
  1. [Configuração] Configurar Ambiente de Desenvolvimento Python:
  Tarefas:
  -- Instalar Pyenv e configurar a versão Python desejada (ex: 3.10+).
  -- Instalar Poetry.
  -- Inicializar o projeto Poetry (poetry init).
  -- Configurar o ambiente virtual do Poetry para usar o Python do Pyenv.
  -- Criar estrutura básica de pastas (config_manager, tests).
  -- Configurar .gitignore básico.
  -- Critério de Aceite: Projeto Poetry inicializado, ambiente virtual ativo com a versão Python correta.
  
  2. [Banco de Dados] Definir Esquema e Conectar ao MySQL Remoto:
  Tarefas:
  -- Definir modelos SQLAlchemy para DBProject, DBEnvironment, DBConfigVariable, DBConfigValue em infrastructure/database/models.py. (Focar nos campos essenciais primeiro).
  -- Implementar infrastructure/database/connection.py para conectar ao MySQL remoto (ler credenciais do .env local).
  -- Configurar Alembic (alembic init, editar env.py).
  -- Criar a primeira migration (alembic revision -m "create_initial_tables") com op.create_table para as 4 tabelas.
  -- Aplicar a migration no banco remoto (alembic upgrade head).
  -- Critério de Aceite: Tabelas criadas com sucesso no banco de dados MySQL remoto. Conexão estabelecida a partir do script Python local.
  
  3. [Core] Definir Entidades de Domínio:
  -- Tarefas:
  -- Criar dataclasses Python simples em core/entities/models.py para Project, Environment, ConfigVariable, ConfigValue (sem lógica de banco aqui, apenas estrutura de dados).
  -- Critério de Aceite: Dataclasses definidas e utilizáveis.
  
  4. [Repositório] Implementar Operações CRUD Básicas para Projetos e Variáveis:
  Tarefas:
  -- Definir interfaces básicas em interfaces/repository_interface.py para:
  -- add_project(project: Project) -> Project
  -- get_project_by_name(name: str) -> Optional[Project]
  -- add_config_variable(variable: ConfigVariable) -> ConfigVariable
  -- get_variable_by_name(name: str) -> Optional[ConfigVariable]
  -- add_config_value(value: ConfigValue) -> ConfigValue
  -- get_config_values_for_project_env(project_id: int, env_id: int) -> List[ConfigValue] (Pode precisar de join com ConfigVariable para pegar o nome da variável).
  -- Implementar essas interfaces em infrastructure/database/repository.py usando SQLAlchemy para interagir com DBProject, DBEnvironment, DBConfigVariable, DBConfigValue. (Focar em adicionar e buscar por nome/ID por enquanto).
  -- Critério de Aceite: Capaz de adicionar um projeto, uma variável e um valor de configuração, e depois buscá-los programaticamente.
  
  5. [Caso de Uso] Implementar Lógica para Gerar Conteúdo de Arquivo .env:
  Tarefas:
  -- Criar um caso de uso simples em core/use_cases/config_generation.py (ou similar).
  -- Função generate_env_file_content(project_name: str, env_name: str) -> str:
  -- Usa o repositório para buscar todas as ConfigValue (e os nomes das ConfigVariable associadas) para um dado projeto e ambiente.
  -- Formata os pares nome=valor em uma string, com cada par em uma nova linha.
  -- (Stretch Goal para esta sprint): Lidar com a descriptografia de segredos se a criptografia for implementada. Para o MVP, podemos assumir que os valores são texto puro.
  -- Critério de Aceite: Função retorna uma string formatada corretamente como um arquivo .env.
  
  6. [CLI] Criar Comandos CLI Básicos para Adicionar Dados e Gerar Arquivo:
  Tarefas:
  -- Adicionar biblioteca typer ou click (poetry add typer).
  -- Criar main_cli.py.
  -- Implementar comandos CLI (usando Typer/Click):
  -- add-project --name <nome_projeto>
  -- add-env --project <nome_projeto> --name <nome_ambiente>
  -- add-var --name <nome_variavel> [--secret]
  -- set-value --project <nome_projeto> --env <nome_ambiente> --var <nome_variavel> --value <valor>
  -- generate-env --project <nome_projeto> --env <nome_ambiente> [--output-file .env.local]
  -- Os controladores CLI em infrastructure/adapters/cli_controller.py chamariam os casos de uso, que por sua vez usariam o repositório.
  -- Critério de Aceite: Capaz de executar os comandos via console para adicionar um projeto, ambiente, variável, definir um valor, e gerar um arquivo .env com esses dados.
  
  7. [Testes] Escrever Testes Unitários Mínimos (Pytest):
  Tarefas:
  -- Configurar Pytest (poetry add --group dev pytest pytest-cov).
  -- Escrever testes unitários para:
  -- A função generate_env_file_content (mockando o repositório).
  -- Pelo menos uma operação de adição do repositório (mockando a sessão do DB ou usando SQLite in-memory).
  -- Critério de Aceite: Testes básicos passam e pytest-cov mostra alguma cobertura.
  
  8. [Documentação] README.md Inicial:
  Tarefas:
  -- Criar README.md com:
  -- Breve descrição do projeto.
  -- Instruções de setup do ambiente de desenvolvimento (Pyenv, Poetry).
  -- Como rodar as migrations.
  -- Exemplos dos comandos CLI básicos.
  -- Critério de Aceite: README básico criado.
  
  Itens Fora do Escopo desta Sprint MVP (Podem ser para Sprints Futuras):
  
  -- Interface Gráfica (UI Web ou Desktop).
  -- Criptografia robusta de segredos (fazer o básico se der tempo, mas a implementação completa pode ser complexa).
  -- Geração de arquivos de configuração complexos (JSON, YAML com templates).
  -- Autenticação/Autorização para a ferramenta.
  -- Funcionalidades CLI avançadas (listar, deletar, atualizar em massa, etc.).
  -- Cobertura de testes exaustiva.
  -- Integração com CI/CD para a própria ferramenta.
  
  Foco da Semana:
  
  O objetivo é, ao final da semana, ter uma ferramenta CLI funcional que possa se conectar ao banco, permitir o cadastro de dados básicos e gerar um arquivo .env simples. Se a criptografia for muito complexa, ela pode ser um "stretch goal" ou ser adiada, focando primeiro em ter o fluxo de dados funcionando com texto puro.
  Este backlog é ambicioso para uma semana, então a priorização interna das tarefas de cada item será crucial. Foque em ter o caminho feliz ("happy path") funcionando.
