"""empty message

Revision ID: fbaa1c23b4d7
Revises: 
Create Date: 2017-04-02 21:04:58.777527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbaa1c23b4d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config_notify',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ram', sa.Integer(), nullable=True),
    sa.Column('rom', sa.Integer(), nullable=True),
    sa.Column('cpu', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('programme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('version', sa.String(length=60), nullable=True),
    sa.Column('link', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('virtualmachines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('ipAddress', sa.String(length=15), nullable=True),
    sa.Column('userName', sa.String(length=60), nullable=True),
    sa.Column('password_hs', sa.String(length=128), nullable=True),
    sa.Column('rootName', sa.String(length=200), nullable=True),
    sa.Column('passwordRoot_hs', sa.String(length=128), nullable=True),
    sa.Column('os', sa.String(length=60), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('ram', sa.Integer(), nullable=True),
    sa.Column('rom', sa.Integer(), nullable=True),
    sa.Column('cpu', sa.Integer(), nullable=True),
    sa.Column('config_notify_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['config_notify_id'], ['config_notify.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_virtualmachines_ipAddress'), 'virtualmachines', ['ipAddress'], unique=True)
    op.create_index(op.f('ix_virtualmachines_name'), 'virtualmachines', ['name'], unique=True)
    op.create_table('vm_programmes',
    sa.Column('VirtualMachines_id', sa.Integer(), nullable=False),
    sa.Column('Programme_id', sa.Integer(), nullable=False),
    sa.Column('date_install', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['Programme_id'], ['programme.id'], ),
    sa.ForeignKeyConstraint(['VirtualMachines_id'], ['virtualmachines.id'], ),
    sa.PrimaryKeyConstraint('VirtualMachines_id', 'Programme_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vm_programmes')
    op.drop_index(op.f('ix_virtualmachines_name'), table_name='virtualmachines')
    op.drop_index(op.f('ix_virtualmachines_ipAddress'), table_name='virtualmachines')
    op.drop_table('virtualmachines')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('programme')
    op.drop_table('config_notify')
    # ### end Alembic commands ###
