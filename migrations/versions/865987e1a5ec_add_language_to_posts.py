"""add language to posts

Revision ID: 865987e1a5ec
Revises: 47831413639e
Create Date: 2018-11-09 15:08:17.360835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '865987e1a5ec'
down_revision = '47831413639e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
