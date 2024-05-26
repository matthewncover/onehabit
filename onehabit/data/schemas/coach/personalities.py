import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, TEXT, JSONB, TIMESTAMP

from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import DataUtils

class Personality(SA_BASE):

    PROMPT_PLACEHOLDER = '<coach_personality_prompt>'

    __tablename__ = "personalities"
    __table_args__ = {"schema": "coach"}

    id_seq = sa.Sequence("seq_personalities_id", schema="coach", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    name = sa.Column(VARCHAR(255), nullable=False)
    description = sa.Column(TEXT, nullable=False)
    data = sa.Column(JSONB, default='{}', nullable=False)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    def to_dict(self):
        return DataUtils.serialize(self)

    def __repr__(self):
        return f"<Personality(id={self.id}, name={self.name})>"