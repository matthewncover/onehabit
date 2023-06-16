import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, TEXT, TIMESTAMP

from onehabit.data.schemas import SA_BASE

class Prompt(SA_BASE):
    __tablename__ = "prompts"
    __table_args__ = {"schema": "coach"}

    id = sa.Column(BIGINT, primary_key=True)
    dialogue_id = sa.Column(BIGINT, sa.ForeignKey("coach.dialogues.id"))
    prompt_text = sa.Column(TEXT, nullable=False)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    dialogue = relationship("Dialogue", back_populates="prompts")

    def __repr__(self):
        return f"<Prompt(id={self.id}, dialogue_id={self.dialogue_id})>"