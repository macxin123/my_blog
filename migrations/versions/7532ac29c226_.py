"""empty message

Revision ID: 7532ac29c226
Revises: 146260141319
Create Date: 2020-08-20 20:05:00.590836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7532ac29c226'
down_revision = '146260141319'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.Column('level', sa.SmallInteger(), nullable=True),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('reg_time', sa.DateTime(), nullable=True),
    sa.Column('signature', sa.Text(), nullable=True),
    sa.Column('balace', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('user_flower', sa.Integer(), nullable=True),
    sa.Column('avatar', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('articles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('a_content', sa.Text(), nullable=True),
    sa.Column('good', sa.Integer(), nullable=True),
    sa.Column('bad', sa.Integer(), nullable=True),
    sa.Column('a_flower', sa.Integer(), nullable=True),
    sa.Column('a_time', sa.DateTime(), nullable=True),
    sa.Column('collection', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('articles')
    op.drop_table('users')
    # ### end Alembic commands ###
