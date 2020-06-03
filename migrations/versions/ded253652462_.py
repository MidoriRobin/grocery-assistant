"""empty message

Revision ID: ded253652462
Revises: 3614a1aeb688
Create Date: 2020-06-02 09:33:45.104507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ded253652462'
down_revision = '3614a1aeb688'
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
    op.drop_index('ix_courier_spm_name', table_name='courier')
    op.drop_table('courier')
    op.add_column('items', sa.Column('cour_id', sa.Integer(), nullable=False))
    op.add_column('items', sa.Column('cour_name', sa.String(length=100), nullable=True))
    op.add_column('items', sa.Column('location', sa.String(length=100), nullable=True))
    op.add_column('items', sa.Column('spm_name', sa.String(length=60), nullable=True))
    op.alter_column('items', 'price',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.DECIMAL(precision=10, scale=2),
               existing_nullable=True)
    op.create_index(op.f('ix_items_spm_name'), 'items', ['spm_name'], unique=True)
    op.create_foreign_key(None, 'items', 'supermarket', ['spm_name'], ['spm_name'], ondelete='CASCADE')
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
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_index(op.f('ix_items_spm_name'), table_name='items')
    op.alter_column('items', 'price',
               existing_type=sa.DECIMAL(precision=10, scale=2),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
    op.drop_column('items', 'spm_name')
    op.drop_column('items', 'location')
    op.drop_column('items', 'cour_name')
    op.drop_column('items', 'cour_id')
    op.create_table('courier',
    sa.Column('cour_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('cour_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('spm_name', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('loc', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['spm_name'], ['supermarket.spm_name'], name='courier_spm_name_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('cour_id', name='courier_pkey')
    )
    op.create_index('ix_courier_spm_name', 'courier', ['spm_name'], unique=True)
    # ### end Alembic commands ###

