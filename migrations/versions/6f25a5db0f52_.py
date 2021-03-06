"""empty message

Revision ID: 6f25a5db0f52
Revises: ded253652462
Create Date: 2020-06-02 09:35:13.287152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f25a5db0f52'
down_revision = 'ded253652462'
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
    op.drop_index('ix_items_spm_id', table_name='items')
    op.drop_table('items')
    op.add_column('courier', sa.Column('location', sa.String(length=100), nullable=True))
    op.drop_column('courier', 'loc')
    op.drop_index('ix_review_item_id', table_name='review')
    op.drop_constraint('review_item_id_fkey', 'review', type_='foreignkey')
    op.drop_column('review', 'item_id')
    op.add_column('shopping_cart', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('shopping_list', sa.Column('acc_num', sa.Integer(), nullable=True))
    op.add_column('shopping_list', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_shopping_list_acc_num'), 'shopping_list', ['acc_num'], unique=False)
    op.drop_index('ix_shopping_list_item_id', table_name='shopping_list')
    op.drop_constraint('shopping_list_item_id_fkey', 'shopping_list', type_='foreignkey')
    op.create_foreign_key(None, 'shopping_list', 'usr', ['acc_num'], ['acc_num'])
    op.drop_column('shopping_list', 'quantity')
    op.drop_column('shopping_list', 'item_id')
    op.add_column('usi', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('usi', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('usi', sa.Column('quantity', sa.Integer(), nullable=True))
    op.drop_index('ix_usi_item_id', table_name='usi')
    op.drop_constraint('usi_acc_num_fkey', 'usi', type_='foreignkey')
    op.drop_constraint('usi_item_id_fkey', 'usi', type_='foreignkey')
    op.drop_column('usi', 'acc_num')
    op.drop_column('usi', 'item_id')
    # ### end Alembic commands ###


def downgrade_cpstnpro():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usi', sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('usi', sa.Column('acc_num', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('usi_item_id_fkey', 'usi', 'items', ['item_id'], ['item_id'])
    op.create_foreign_key('usi_acc_num_fkey', 'usi', 'usr', ['acc_num'], ['acc_num'])
    op.create_index('ix_usi_item_id', 'usi', ['item_id'], unique=False)
    op.drop_column('usi', 'quantity')
    op.drop_column('usi', 'id')
    op.drop_column('usi', 'created_date')
    op.add_column('shopping_list', sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('shopping_list', sa.Column('quantity', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'shopping_list', type_='foreignkey')
    op.create_foreign_key('shopping_list_item_id_fkey', 'shopping_list', 'items', ['item_id'], ['item_id'])
    op.create_index('ix_shopping_list_item_id', 'shopping_list', ['item_id'], unique=False)
    op.drop_index(op.f('ix_shopping_list_acc_num'), table_name='shopping_list')
    op.drop_column('shopping_list', 'date_created')
    op.drop_column('shopping_list', 'acc_num')
    op.drop_column('shopping_cart', 'date_created')
    op.add_column('review', sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('review_item_id_fkey', 'review', 'items', ['item_id'], ['item_id'])
    op.create_index('ix_review_item_id', 'review', ['item_id'], unique=False)
    op.add_column('courier', sa.Column('loc', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('courier', 'location')
    op.create_table('items',
    sa.Column('item_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('item_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('price', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('brand', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('desc_item', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('i_type', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('dislikes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('exp_date', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('spm_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['spm_id'], ['supermarket.spm_id'], name='items_spm_id_fkey'),
    sa.PrimaryKeyConstraint('item_id', name='items_pkey')
    )
    op.create_index('ix_items_spm_id', 'items', ['spm_id'], unique=False)
    # ### end Alembic commands ###

