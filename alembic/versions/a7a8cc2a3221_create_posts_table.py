"""create posts table

Revision ID: a7a8cc2a3221
Revises: 
Create Date: 2022-11-07 15:10:02.696344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7a8cc2a3221'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
