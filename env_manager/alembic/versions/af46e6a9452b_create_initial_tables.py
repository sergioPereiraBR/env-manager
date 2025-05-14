"""create_initial_tables

Revision ID: af46e6a9452b
Revises: 
Create Date: 2025-05-13 19:24:49.627080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af46e6a9452b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), unique=True, index=True, nullable=False),
        sa.Column('project_type', sa.String(length=100)),
        sa.Column('description', sa.String(length=500)),
    )
    op.create_table(
        'environments',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), index=True, nullable=False),
        sa.Column('project_id', sa.Integer(), sa.ForeignKey('projects.id'), nullable=False),
        sa.Column('description', sa.String(length=500)),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='fk_environment_project'),
        sa.UniqueConstraint('name', 'project_id', name='_project_environment_uc')
    )
    op.create_table(
        'config_variables',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), unique=True, index=True, nullable=False),
        sa.Column('description', sa.String(length=500)),
        sa.Column('is_secret', sa.Boolean(), default=False),
        sa.Column('data_type', sa.String(length=50), default='string'),
    )
    op.create_table(
        'project_config_values',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column('project_id', sa.Integer(), sa.ForeignKey('projects.id'), nullable=False),
        sa.Column('environment_id', sa.Integer(), sa.ForeignKey('environments.id'), nullable=False),
        sa.Column('variable_id', sa.Integer(), sa.ForeignKey('config_variables.id'), nullable=False),
        sa.Column('value', sa.String(length=2048), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='fk_config_value_project'),
        sa.ForeignKeyConstraint(['environment_id'], ['environments.id'], name='fk_config_value_environment'),
        sa.ForeignKeyConstraint(['variable_id'], ['config_variables.id'], name='fk_config_value_variable'),
        sa.UniqueConstraint('project_id', 'environment_id', 'variable_id', name='_proj_env_var_uc')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('project_config_values')
    op.drop_table('config_variables')
    op.drop_table('environments')
    op.drop_table('projects')
