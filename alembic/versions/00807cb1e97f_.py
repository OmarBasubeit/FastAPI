"""empty message

Revision ID: 00807cb1e97f
Revises: 7421e6d288de, 8865e5cb7053
Create Date: 2022-11-09 15:39:29.697700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00807cb1e97f'
down_revision = ('7421e6d288de', '8865e5cb7053')
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
