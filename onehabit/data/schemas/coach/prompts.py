import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, TEXT, TIMESTAMP, VARCHAR

from onehabit.data.schemas import SA_BASE

class Prompt(SA_BASE):
    __tablename__ = "prompts"
    __table_args__ = {"schema": "coach"}

    id_seq = sa.Sequence("seq_prompts_id", schema="coach", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    dialogue_name = sa.Column(VARCHAR(255), unique=True, nullable=False)
    prompt_text = sa.Column(TEXT, nullable=False)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    def __repr__(self):
        return f"<Prompt(id={self.id}, name={self.dialogue_name})>"