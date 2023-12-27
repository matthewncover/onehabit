import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, INTEGER, TEXT, TIMESTAMP

from onehabit.data.schemas import SA_BASE

class Dialogue(SA_BASE):
    __tablename__ = "dialogues"
    __table_args__ = {"schema": "coach"}

    id_seq = sa.Sequence("seq_dialogues_id", schema="coach", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    user_id = sa.Column(BIGINT, sa.ForeignKey("users.users.id"))
    dialogue_name = sa.Column(VARCHAR(255))
    dialogue_version = sa.Column(INTEGER)
    dialogue_text = sa.Column(TEXT, nullable=False)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    user = relationship("User", back_populates="dialogues")
    prompts = relationship("Prompt", back_populates="dialogue")

    def __repr__(self):
        return f"<Dialogue(id={self.id}, name={self.dialogue_name}, version={self.dialogue_version})>"
