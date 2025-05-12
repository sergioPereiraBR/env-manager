---
created: 2025-05-11T20:26:48.834Z
updated: 2025-05-12T00:31:27.383Z
assigned: 'Sergio Pereira'
progress: 1
tags:
  - start
  - 'teste, projeto'
due: 2025-05-09T00:00:00.000Z
started: 2025-05-09T00:00:00.000Z
completed: 2025-05-09T00:00:00.000Z
---

# Criar ambiente para desenvolvimento

Preparar as condições mínimas para iniciar o projeto

## Sub-tasks

- [ ] Criar uma ambiente vitual e com as dependências isoladas do resto do sistema
- [ ] Instalar as ferramentas para início do projeto
- [ ] iniciar o projeto
- [ ] iniciar o respositório local
- [ ] criar e iniciar o repositório remoto

## Relations

- [Id-task ](.md)

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
