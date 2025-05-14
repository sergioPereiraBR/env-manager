---
created: 2025-05-13T05:14:42.436Z
updated: 2025-05-13T05:14:43.523Z
assigned: 'Sergio Pereira'
progress: 0
tags:
  - TASK-0006
---

# TASK-0006 - CLI

TASK-0006 - Criar Comandos CLI Básicos para Adicionar Dados e Gerar Arquivo:

## Sub-tasks

- [ ] TASK-0006-ST-001 - Adicionar biblioteca typer ou click (poetry add typer).
- [ ] TASK-0006-ST-002 - Criar main_cli.py.
- [ ] TASK-0006-ST-003 - Implementar comandos CLI (usando Typer/Click):
- [ ] add-project --name <nome_projeto>
- [ ] TASK-0006-ST-004 - add-env --project <nome_projeto> --name <nome_ambiente>
- [ ] TASK-0006-ST-005 - add-var --name <nome_variavel> [--secret]
- [ ] TASK-0006-ST-006 - set-value --project <nome_projeto> --env <nome_ambiente> --var <nome_variavel> --value <valor_>
- [ ] TASK-0006-ST-007 - generate-env --project <nome_projeto> --env <nome_ambiente> [--output-file .env.local]
- [ ] TASK-0006-ST-008 - Os controladores CLI em infrastructure/adapters/cli_controller.py chamariam os casos de uso, que por sua vez usariam o repositório.
- [ ] TASK-0006-ST-009 - Critério de Aceite: Capaz de executar os comandos via console para adicionar um projeto, ambiente, variável, definir um valor, e gerar um arquivo .env com esses dados.
