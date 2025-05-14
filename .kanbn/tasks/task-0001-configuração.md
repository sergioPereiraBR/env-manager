---
created: 2025-05-13T05:14:18.978Z
updated: 2025-05-13T15:37:50.806Z
assigned: 'Sergio Pereira'
progress: 1
tags:
  - TASK-0001
due: 2025-05-12T00:00:00.000Z
started: 2025-05-11T00:00:00.000Z
completed: 2025-05-12T00:00:00.000Z
---

# TASK-0001 -  Configuração

TASK-0001 -  Configurar Ambiente de Desenvolvimento Python:

  Product Backlog para Sprint 1 (Timebox: 1 Semana - Foco MVP)

  Tema da Sprint: Estabelecer a fundação da ferramenta: conexão com banco, estrutura de dados básica, e a capacidade de gerar um arquivo .env simples via CLI.

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

## Sub-tasks

- [x] TASK-0001-ST-001 - Configurar com Pyenv a versão 3.11.4 do Python.
- [x] TASK-0001-ST-002 - Inicializar o projeto pelo Poetry
- [x] TASK-0001-ST-003 - Configurar o ambiente virtual do Poetry para usar o Python do Pyenv.
- [x] TASK-0001-ST-004 - Criar estrutura básica de pastas (config_manager, tests).
- [x] TASK-0001-ST-005 - Cria o projeto inicial e executa sem erro ao apresentar uma mensagem
- [x] TASK-0001-ST-006 - Configurar .gitignore básico.
- [x] TASK-0001-ST-007 - Configura o gh CLI para criar o repositório remoto
- [x] TASK-0001-ST-008 - Renomeia a branch padrão para "main"
- [x] TASK-0001-ST-009 - Commit inicial na branch dev - git commit -m "Commit inicial: estrutura básica do projeto"
- [x] TASK-0001-ST-010 - Configura conexão remote  git remote add origin https://github.com/sergioPereiraBR/env-manager.git
- [x] TASK-0001-ST-011 - Aponta para a branch e envia para o repositório remoto:  git push -u origin main
- [x] TASK-0001-ST-012 - Crie a branch de desenvolvimento: git checkout -b dev
- [x] TASK-0001-ST-013 - Aponta pra branch dev e envia para o repositório remoto:  git push -u origin dev
- [x] TASK-0001-ST-014 - Atribui tarefas e subtarefas no Kanban para inívio do desenvolvimento
- [x] TASK-0001-ST-015 - Critério de Aceite: Projeto Poetry inicializado, ambiente virtual ativo com a versão Python correta.
- [ ] "python.paythonPath" = "D:\\02_trabalho\\01_dev_software\\pereira_dev\\tools\\env_manager\\env_manager\\.venv\\Scripts\\python.exe"
- [ ] poetry add sqlalchemy mysqlclient alembic python-dotenv cryptography

## Comments

- author: Sergio Pereira
  date: 2025-05-11T20:30:59.057Z
  Start
- author: Sergio Pereira
  date: 2025-05-11T21:47:21.642Z
  %USERPROFILE%\.pyenv\pyenv-win\bin
  %USERPROFILE%\.pyenv\pyenv-win\shims
  
  C:\Users\sergi\.pyenv\pyenv-win\bin
  C:\Users\sergi\.pyenv\pyenv-win\shims
  
  [System.Environment]::SetEnvironmentVariable("PATH", "%USERPROFILE%\.pyenv\pyenv-win\bin;%USERPROFILE%\.pyenv\pyenv-win\shims;" + $env:Path, "Machine")
- author: Sergio Pereira
  date: 2025-05-11T23:29:09.224Z
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager> python --version
  Python 3.11.4
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager> poetry new env_manager
  Created package env_manager in env_manager
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager> dir
  
      Directory: D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager
  
  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  d----          11/05/2025    11:29                .kanbn
  d----          11/05/2025    20:21                env_manager
  -a---          11/05/2025    19:28              8 .python-version
  
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager> tree
  Listagem de caminhos de pasta para o volume Acervo
  O número de série do volume é 0C58-80A8
  D:.
  ├───.kanbn
  │   └───tasks
  └───env_manager
      ├───src
      │   └───env_manager
      └───tests
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager> cd env_manager
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager> dir
  
      Directory: D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager
  
  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  d----          11/05/2025    20:21                src
  d----          11/05/2025    20:21                tests
  -a---          11/05/2025    20:21            403 pyproject.toml
  -a---          11/05/2025    20:21              0 README.md
  
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager> tree
  Listagem de caminhos de pasta para o volume Acervo
  O número de série do volume é 0C58-80A8
  D:.
  ├───src
  │   └───env_manager
  └───tests
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager> python --version
  Python 3.11.4
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager> poetry install
  Creating virtualenv env-manager in D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager\.venv
  Updating dependencies
  Resolving dependencies... (0.2s)
  
  Writing lock file
  
  Installing the current project: env-manager (0.1.0)
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager> poetry env info
  
  Virtualenv
  Python:         3.11.4
  Implementation: CPython
  Path:           D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager\.venv
  Executable:     D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager\env_manager\.venv\Scripts\python.exe
  Valid:          True
  
  Base
  Platform:   win32
  OS:         nt
  Python:     3.11.4
  Path:       C:\Users\sergi\.pyenv\pyenv-win\versions\3.11.4
  Executable: C:\Users\sergi\.pyenv\pyenv-win\versions\3.11.4\python.exe
