"""empty message

Revision ID: 06912f03f52d
Revises: 55c491fd7d2a
Create Date: 2022-11-10 09:20:17.671023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06912f03f52d'
down_revision = '55c491fd7d2a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass