"""init_db

Revision ID: 7d485af1f44e
Revises: 
Create Date: 2024-07-22 22:19:47.514183

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7d485af1f44e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('channel_book_id', sa.String(length=20), nullable=True),
    sa.Column('book_name', sa.String(length=100), nullable=True),
    sa.Column('cate_id', sa.Integer(), nullable=True),
    sa.Column('cate_name', sa.String(length=50), nullable=True),
    sa.Column('channel_type', sa.SmallInteger(), nullable=True),
    sa.Column('author_name', sa.String(length=50), nullable=True),
    sa.Column('chapter_num', sa.Integer(), nullable=True),
    sa.Column('is_publish', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('cover', sa.String(length=300), nullable=True),
    sa.Column('intro', mysql.TEXT(), nullable=True),
    sa.Column('word_count', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('showed', sa.Boolean(), server_default=sa.text('0'), nullable=True),
    sa.Column('source', sa.String(length=50), nullable=True),
    sa.Column('ranking', sa.Integer(), server_default='0', nullable=True),
    sa.Column('short_des', sa.String(length=50), server_default='', nullable=True),
    sa.Column('collect_count', sa.Integer(), server_default='0', nullable=True),
    sa.Column('heat', sa.Integer(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('book_id'),
    sa.UniqueConstraint('channel_book_id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_cate_id'), ['cate_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_channel_type'), ['channel_type'], unique=False)

    op.create_table('book_big_category',
    sa.Column('cate_id', sa.Integer(), nullable=False),
    sa.Column('cate_name', sa.String(length=50), nullable=True),
    sa.Column('channel', sa.Integer(), nullable=True),
    sa.Column('showed', sa.Boolean(), server_default='1', nullable=True),
    sa.Column('icon', sa.String(length=100), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('cate_id')
    )
    op.create_table('book_category',
    sa.Column('cate_id', sa.Integer(), nullable=False),
    sa.Column('cate_name', sa.String(length=50), nullable=True),
    sa.Column('showed', sa.Boolean(), server_default='1', nullable=True),
    sa.Column('icon', sa.String(length=100), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('cate_id')
    )
    op.create_table('book_chapter_content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('volume_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.Column('content', mysql.MEDIUMTEXT(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book_chapter_content', schema=None) as batch_op:
        batch_op.create_index('ix_book_id_chapter_id', ['book_id', 'chapter_id'], unique=False)

    op.create_table('book_chapters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('volume_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.Column('chapter_name', sa.String(length=100), nullable=True),
    sa.Column('word_count', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('book_chapters', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_chapters_book_id'), ['book_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_chapters_chapter_id'), ['chapter_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_chapters_volume_id'), ['volume_id'], unique=False)

    op.create_table('book_shelf',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('book_name', sa.String(length=100), nullable=True),
    sa.Column('cover', sa.String(length=300), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book_shelf', schema=None) as batch_op:
        batch_op.create_index('ix_book_id_user_id', ['book_id', 'user_id'], unique=True)
        batch_op.create_index(batch_op.f('ix_book_shelf_book_id'), ['book_id'], unique=False)

    op.create_table('book_volume',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('volume_id', sa.Integer(), nullable=True),
    sa.Column('volume_name', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('chapter_count', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book_volume', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_volume_book_id'), ['book_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_volume_volume_id'), ['volume_id'], unique=False)

    op.create_table('read_rate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.Column('chapter_name', sa.String(length=100), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('search_key_word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keyword', sa.String(length=100), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('is_hot', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('openId', sa.String(length=128), nullable=True),
    sa.Column('nickName', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.Integer(), server_default='0', nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('province', sa.String(length=120), nullable=True),
    sa.Column('country', sa.String(length=120), nullable=True),
    sa.Column('avatarUrl', sa.String(length=200), nullable=True),
    sa.Column('preference', sa.Integer(), server_default='0', nullable=True),
    sa.Column('brightness', sa.Integer(), server_default='30', nullable=True),
    sa.Column('fontSize', sa.Integer(), server_default='14', nullable=True),
    sa.Column('background', sa.String(length=10), nullable=True),
    sa.Column('turn', sa.String(length=10), nullable=True),
    sa.Column('last_read', sa.Integer(), nullable=True),
    sa.Column('last_read_chapter_id', sa.Integer(), nullable=True),
    sa.Column('modified', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('openId')
    )
    op.create_table('book_category_relation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('big_cate_id', sa.Integer(), nullable=True),
    sa.Column('cate_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['big_cate_id'], ['book_big_category.cate_id'], ),
    sa.ForeignKeyConstraint(['cate_id'], ['book_category.cate_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('browse_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('browse_history')
    op.drop_table('book_category_relation')
    op.drop_table('user')
    op.drop_table('search_key_word')
    op.drop_table('read_rate')
    with op.batch_alter_table('book_volume', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_volume_volume_id'))
        batch_op.drop_index(batch_op.f('ix_book_volume_book_id'))

    op.drop_table('book_volume')
    with op.batch_alter_table('book_shelf', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_shelf_book_id'))
        batch_op.drop_index('ix_book_id_user_id')

    op.drop_table('book_shelf')
    with op.batch_alter_table('book_chapters', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_chapters_volume_id'))
        batch_op.drop_index(batch_op.f('ix_book_chapters_chapter_id'))
        batch_op.drop_index(batch_op.f('ix_book_chapters_book_id'))

    op.drop_table('book_chapters')
    with op.batch_alter_table('book_chapter_content', schema=None) as batch_op:
        batch_op.drop_index('ix_book_id_chapter_id')

    op.drop_table('book_chapter_content')
    op.drop_table('book_category')
    op.drop_table('book_big_category')
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_channel_type'))
        batch_op.drop_index(batch_op.f('ix_book_cate_id'))

    op.drop_table('book')
    # ### end Alembic commands ###
