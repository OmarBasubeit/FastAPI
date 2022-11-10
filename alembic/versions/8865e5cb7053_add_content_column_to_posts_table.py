"""add content column to posts table

Revision ID: 8865e5cb7053
Revises: a7a8cc2a3221
Create Date: 2022-11-09 14:51:05.906302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8865e5cb7053'
down_revision = 'a7a8cc2a3221'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
