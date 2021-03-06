"""empty message

Revision ID: 4c3dda216aa6
Revises: 1e95e076d815
Create Date: 2020-11-11 17:38:21.626529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c3dda216aa6'
down_revision = '1e95e076d815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('projection', sa.Float(), nullable=True))
    op.add_column('player', sa.Column('team', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('player', 'team')
    op.drop_column('player', 'projection')
    # ### end Alembic commands ###
