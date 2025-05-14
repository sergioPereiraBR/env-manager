# .env_manager/src/env_manager/infrastructure/database/models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base # Importar Base de connection.py

class DBProject(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    project_type = Column(String(100))
    description = Column(String(500))
    environments = relationship("DBEnvironment", back_populates="project")
    config_values = relationship("DBConfigValue", back_populates="project")


class DBEnvironment(Base):
    __tablename__ = "environments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    description = Column(String(500))
    project = relationship("DBProject", back_populates="environments")
    config_values = relationship("DBConfigValue", back_populates="environment")
    # __table_args__ = (UniqueConstraint('name', 'project_id', name='_project_environment_uc'),) # Nome do ambiente único por projeto


class DBConfigVariable(Base):
    __tablename__ = "config_variables"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, index=True, nullable=False) # Nome da variável deve ser único globalmente? Ou por projeto?
    description = Column(String(500))
    is_secret = Column(Boolean, default=False)
    data_type = Column(String(50), default="string")
    # Se o nome for por projeto, adicione project_id aqui
    config_values = relationship("DBConfigValue", back_populates="variable")


class DBConfigValue(Base):
    __tablename__ = "project_config_values"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    environment_id = Column(Integer, ForeignKey("environments.id"), nullable=False)
    variable_id = Column(Integer, ForeignKey("config_variables.id"), nullable=False)
    value = Column(String(2048), nullable=False) # Aumentar tamanho para valores longos/criptografados

    project = relationship("DBProject", back_populates="config_values")
    environment = relationship("DBEnvironment", back_populates="config_values")
    variable = relationship("DBConfigVariable", back_populates="config_values")
    # __table_args__ = (UniqueConstraint('project_id', 'environment_id', 'variable_id', name='_proj_env_var_uc'),)