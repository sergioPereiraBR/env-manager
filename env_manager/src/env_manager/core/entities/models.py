# env_manager/src/env_manager/core/entities/models.py
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Project:
    id: Optional[int] = None
    name: str = field(default="")
    tag: Optional[str] = None 
    project_type: Optional[str] = None
    description: Optional[str] = None

# Marco/Ministone - Agrupamento de tarefas/Fase de Projeto/Sprint/../Entre outros - Tabela para agrupar tarefas

# Tabela de tarefas

# Tabela de Subtarefas

@dataclass
class Environment:
    id: Optional[int] = None
    name: str = field(default="") # Ex: "local_dev_sergio", "staging_devsolar", "prod_cliente_x"
    project_id: Optional[int] = None # FK
    description: Optional[str] = None

@dataclass
class ConfigVariable:
    id: Optional[int] = None
    name: str = field(default="") # Ex: NEXT_PUBLIC_API_URL
    description: Optional[str] = None
    is_secret: bool = False
    data_type: str = "string" # string, number, boolean, json_string

@dataclass
class ConfigValue:
    id: Optional[int] = None
    project_id: int
    environment_id: int
    variable_id: int
    value: str # Armazenar tudo como string, converter no uso. Segredos serão criptografados aqui.
    # last_updated: Optional[datetime] = None # Opcional