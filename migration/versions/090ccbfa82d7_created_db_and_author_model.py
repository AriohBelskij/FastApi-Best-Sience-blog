"""created db and author model

Revision ID: 090ccbfa82d7
Revises: 
Create Date: 2023-07-18 14:22:58.789608

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '090ccbfa82d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('uuid', sa.UUID(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('middle_name', sa.String(), nullable=True),
                    sa.Column('surname', sa.String(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('field', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('author')
    # ### end Alembic commands ###