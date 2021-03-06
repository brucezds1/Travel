"""empty message

Revision ID: e7f6ed6afcc2
Revises: 
Create Date: 2021-10-09 18:24:03.029416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7f6ed6afcc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'adminlog', 'admin', ['admin_id'], ['id'])
    op.create_foreign_key(None, 'collect', 'scenic', ['scenic_id'], ['id'])
    op.create_foreign_key(None, 'collect', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'oplog', 'admin', ['admin_id'], ['id'])
    op.create_foreign_key(None, 'scenic', 'area', ['area_id'], ['id'])
    op.create_foreign_key(None, 'travels', 'scenic', ['scenic_id'], ['id'])
    op.create_foreign_key(None, 'userlog', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'userlog', type_='foreignkey')
    op.drop_constraint(None, 'travels', type_='foreignkey')
    op.drop_constraint(None, 'scenic', type_='foreignkey')
    op.drop_constraint(None, 'oplog', type_='foreignkey')
    op.drop_constraint(None, 'collect', type_='foreignkey')
    op.drop_constraint(None, 'collect', type_='foreignkey')
    op.drop_constraint(None, 'adminlog', type_='foreignkey')
    # ### end Alembic commands ###
