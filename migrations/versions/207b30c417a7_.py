"""empty message

Revision ID: 207b30c417a7
Revises: 
Create Date: 2023-12-14 18:49:06.183919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207b30c417a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_binary', sa.LargeBinary(), nullable=True))
        batch_op.add_column(sa.Column('image_color', sa.String(length=32), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.drop_column('image_color')
        batch_op.drop_column('image_binary')

    # ### end Alembic commands ###