"""added link filename

Revision ID: 6cbb783a2883
Revises: cef03da1b332
Create Date: 2023-08-08 01:54:39.986295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cbb783a2883'
down_revision: Union[str, None] = 'cef03da1b332'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('link', sa.String(), nullable=False))
    op.add_column('songs', sa.Column('filename', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songs', 'filename')
    op.drop_column('songs', 'link')
    # ### end Alembic commands ###