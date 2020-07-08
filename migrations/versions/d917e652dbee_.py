"""empty message

Revision ID: d917e652dbee
Revises: d2a9a693f233
Create Date: 2020-07-02 16:52:32.214157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd917e652dbee'
down_revision = 'd2a9a693f233'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_cpstnpro():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('rating_desc', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade_cpstnpro():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'rating_desc')
    # ### end Alembic commands ###
