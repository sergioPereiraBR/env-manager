---
created: 2025-05-13T05:14:26.950Z
updated: 2025-05-13T12:34:35.111Z
assigned: 'Sergio Pereira'
progress: 0
tags:
  - TASK-0004
---

# TASK-0004 - Repositório

TASK-0004 - Implementar Operações CRUD Básicas para Projetos e Variáveis:

## Sub-tasks

- [ ] TASK-0004-ST-001 - Definir interfaces básicas em interfaces/repository_interface.py para:
- [ ] TASK-0004-ST-002 - add_project(project: Project) -> Project
- [ ] TASK-0004-ST-003 - get_project_by_name(name: str) -> Optional[Project]
- [ ] TASK-0004-ST-004 - add_config_variable(variable: ConfigVariable) -> ConfigVariable
- [ ] TASK-0004-ST-005 - get_variable_by_name(name: str) -> Optional[ConfigVariable]
- [ ] TASK-0004-ST-006 - add_config_value(value: ConfigValue) -> ConfigValue
- [ ] TASK-0004-ST-007 - get_config_values_for_project_env(project_id: int, env_id: int) -> List[ConfigValue] (Pode precisar de join com ConfigVariable para pegar o nome da variável).
- [ ] TASK-0004-ST-008 - Implementar essas interfaces em infrastructure/database/repository.py usando SQLAlchemy para interagir com DBProject, DBEnvironment, DBConfigVariable, DBConfigValue. (Focar em adicionar e buscar por nome/ID por enquanto).
- [ ] TASK-0004-ST-009 - Critério de Aceite: Capaz de adicionar um projeto, uma variável e um valor de configuração, e depois buscá-los programaticamente.
