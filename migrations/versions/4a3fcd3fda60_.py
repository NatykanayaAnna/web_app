"""empty message

Revision ID: 4a3fcd3fda60
Revises: 29a52f5e26e7
Create Date: 2022-06-18 18:54:00.830003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a3fcd3fda60'
down_revision = '29a52f5e26e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('banners', sa.Column('url', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('banners', 'url')
    # ### end Alembic commands ###
