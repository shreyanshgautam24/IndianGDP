"""empty message

Revision ID: a001069573a8
Revises: 
Create Date: 2023-03-09 16:04:14.406808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a001069573a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('indian_gdp',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gdp_usd', sa.Integer(), nullable=False),
    sa.Column('gdp_year', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('indian_gdp')
    # ### end Alembic commands ###
