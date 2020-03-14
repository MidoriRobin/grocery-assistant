"""empty message

Revision ID: c1aa9f185949
Revises: 2531d4c535d3
Create Date: 2020-03-11 10:51:15.480779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1aa9f185949'
down_revision = '2531d4c535d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catalog', sa.Column('desc', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('catalog', 'desc')
    # ### end Alembic commands ###