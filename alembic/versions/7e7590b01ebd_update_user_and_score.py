"""update user and score

Revision ID: 7e7590b01ebd
Revises: bf59d3b6c7f2
Create Date: 2022-09-15 20:36:17.151862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7e7590b01ebd'
down_revision = 'bf59d3b6c7f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('score', 'user_name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=False,
               existing_comment='用户名')
    op.alter_column('score', 'answer_title',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=False,
               existing_comment='答案文件名')
    op.alter_column('score', 'answer_detail',
               existing_type=mysql.TEXT(collation='utf8mb4_general_ci'),
               nullable=False,
               existing_comment='答案详情')
    op.alter_column('score', 'answer_result',
               existing_type=mysql.TEXT(collation='utf8mb4_general_ci'),
               nullable=False,
               existing_comment='答案结果')
    op.alter_column('score', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=False,
               existing_comment='回答时间',
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=20),
               nullable=False,
               existing_comment='用户名')
    op.alter_column('user', 'hashed_password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=300),
               nullable=False,
               existing_comment='密码')
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=False,
               existing_comment='邮箱')
    op.alter_column('user', 'full_name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=False,
               existing_comment='全名')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'full_name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=True,
               existing_comment='全名')
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=True,
               existing_comment='邮箱')
    op.alter_column('user', 'hashed_password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=300),
               nullable=True,
               existing_comment='密码')
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=20),
               nullable=True,
               existing_comment='用户名')
    op.alter_column('score', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=True,
               existing_comment='回答时间',
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('score', 'answer_result',
               existing_type=mysql.TEXT(collation='utf8mb4_general_ci'),
               nullable=True,
               existing_comment='答案结果')
    op.alter_column('score', 'answer_detail',
               existing_type=mysql.TEXT(collation='utf8mb4_general_ci'),
               nullable=True,
               existing_comment='答案详情')
    op.alter_column('score', 'answer_title',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=True,
               existing_comment='答案文件名')
    op.alter_column('score', 'user_name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=True,
               existing_comment='用户名')
    # ### end Alembic commands ###
