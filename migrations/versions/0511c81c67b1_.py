"""empty message

Revision ID: 0511c81c67b1
Revises: 98c938f80837
Create Date: 2020-04-20 22:08:27.684596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0511c81c67b1'
down_revision = '98c938f80837'
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
    op.drop_column('usr', 'fav_colour')
    # ### end Alembic commands ###


def downgrade_cpstnpro():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usr', sa.Column('fav_colour', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

