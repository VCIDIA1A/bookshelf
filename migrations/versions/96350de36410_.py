"""empty message

Revision ID: 96350de36410
Revises: f362e3305185
Create Date: 2023-03-19 09:00:55.495577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96350de36410'
down_revision = 'f362e3305185'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('thema', sa.String(length=40), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_column('thema')

    # ### end Alembic commands ###