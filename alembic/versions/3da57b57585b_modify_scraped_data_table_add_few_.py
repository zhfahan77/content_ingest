"""Modify scraped_data table, add few columns

Revision ID: 3da57b57585b
Revises: c2e73dfbb689
Create Date: 2023-10-19 23:15:05.771878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3da57b57585b'
down_revision: Union[str, None] = 'c2e73dfbb689'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scraped_data', sa.Column('domain', sa.String(length=128), nullable=False))
    op.add_column('scraped_data', sa.Column('path', sa.String(length=256), nullable=False))
    op.create_index(op.f('ix_scraped_data_domain'), 'scraped_data', ['domain'], unique=False)
    op.drop_column('scraped_data', 'url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scraped_data', sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_scraped_data_domain'), table_name='scraped_data')
    op.drop_column('scraped_data', 'path')
    op.drop_column('scraped_data', 'domain')
    # ### end Alembic commands ###
