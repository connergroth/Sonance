"""Add all models

Revision ID: 8c2e68080243
Revises: 
Create Date: 2025-01-26 19:38:51.390234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8c2e68080243'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('artist', sa.String(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('aoty_score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.Column('aoty_score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artists_id'), 'artists', ['id'], unique=False)
    op.create_table('tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('artist', sa.String(), nullable=False),
    sa.Column('album', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.Column('aoty_score', sa.Integer(), nullable=True),
    sa.Column('audio_features', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tracks_id'), 'tracks', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_has', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('album', sa.Integer(), nullable=False),
    sa.Column('recommendation_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recommendations_id'), 'recommendations', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_recommendations_id'), table_name='recommendations')
    op.drop_table('recommendations')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tracks_id'), table_name='tracks')
    op.drop_table('tracks')
    op.drop_index(op.f('ix_artists_id'), table_name='artists')
    op.drop_table('artists')
    op.drop_table('albums')
    # ### end Alembic commands ###