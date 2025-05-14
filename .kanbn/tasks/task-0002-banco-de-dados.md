---
created: 2025-05-13T05:13:52.302Z
updated: 2025-05-13T14:19:18.657Z
assigned: 'Sergio Pereira'
progress: 0
tags:
  - TASK-0002
started: 2025-05-13T00:00:00.000Z
---

# TASK-0002 - Banco de Dados

TASK-0002 - Definir Esquema e Conectar ao MySQL Remoto:

## Sub-tasks

- [x] TASK-0002-ST-001 - Definir modelos SQLAlchemy para DBProject, DBEnvironment, DBConfigVariable, DBConfigValue em infrastructure/database/models.py. (Focar nos campos essenciais primeiro).
- [x] TASK-0002-ST-002 - Implementar infrastructure/database/connection.py para conectar ao MySQL remoto (ler credenciais do .env local).
- [ ] TASK-0002-ST-003 - Configurar Alembic (alembic init, editar env.py).
- [ ] TASK-0002-ST-004 - Criar a primeira migration (alembic revision -m "create_initial_tables") com op.create_table para as 4 tabelas.
- [ ] TASK-0002-ST-005 - Aplicar a migration no banco remoto (alembic upgrade head).
- [ ] TASK-0002-ST-006 - Critério de Aceite: Tabelas criadas com sucesso no banco de dados MySQL remoto. Conexão estabelecida a partir do script Python local.

## Comments

- date: 2025-05-13T14:19:07.330Z
  PS D:\02_trabalho\01_dev_software\pereira_dev\tools\env_manager> poetry add sqlalchemy mysqlclient alembic python-dotenv cryptography
