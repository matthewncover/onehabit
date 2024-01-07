import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, JSONB, VARCHAR, INTEGER, TEXT, TIMESTAMP

from onehabit.data.schemas import SA_BASE

class Dialogue(SA_BASE):
    __tablename__ = "dialogues"
    __table_args__ = {"schema": "coach"}

    id_seq = sa.Sequence("seq_dialogues_id", schema="coach", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    user_id = sa.Column(BIGINT, sa.ForeignKey("users.users.id"))
    name = sa.Column(VARCHAR(255))
    version = sa.Column(INTEGER)
    full_text = sa.Column(JSONB)
    summarized_text = sa.Column(JSONB)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    user = relationship("User", back_populates="dialogues")

    def __repr__(self):
        return f"<Dialogue(id={self.id}, name={self.name}, version={self.version})>"
