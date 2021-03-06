"""two new tables

Revision ID: c80025cbaabd
Revises: 6094c61fb04c
Create Date: 2020-09-05 09:26:30.564506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c80025cbaabd'
down_revision = '6094c61fb04c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.create_index(op.f('ix_author_author'), 'author', ['author'], unique=False)
    op.create_table('title',
    sa.Column('title_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('title_id')
    )
    op.create_index(op.f('ix_title_title'), 'title', ['title'], unique=True)
    op.create_table('Book',
    sa.Column('title_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.author_id'], ),
    sa.ForeignKeyConstraint(['title_id'], ['title.title_id'], )
    )
    op.drop_index('ix_borrowed_borrowed_date', table_name='borrowed')
    op.drop_table('borrowed')
    op.drop_index('ix_book_author', table_name='book')
    op.drop_index('ix_book_title', table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=True),
    sa.Column('author', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_book_title', 'book', ['title'], unique=1)
    op.create_index('ix_book_author', 'book', ['author'], unique=False)
    op.create_table('borrowed',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('borrowed_date', sa.DATETIME(), nullable=True),
    sa.Column('book_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_borrowed_borrowed_date', 'borrowed', ['borrowed_date'], unique=False)
    op.drop_table('Book')
    op.drop_index(op.f('ix_title_title'), table_name='title')
    op.drop_table('title')
    op.drop_index(op.f('ix_author_author'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
