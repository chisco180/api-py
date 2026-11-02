"""Create content colum to posts table

Revision ID: b4fd7537cb71
Revises: 8e9d58155ceb
Create Date: 2026-10-31 11:30:20.623663

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b4fd7537cb71"
down_revision: Union[str, Sequence[str], None] = "8e9d58155ceb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
