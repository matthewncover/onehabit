import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, TEXT, BOOLEAN, TIMESTAMP, JSONB
from pydantic import BaseModel

from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import JSONBPydantic

class ObservationDataModel(BaseModel):
    pass

class Observation(SA_BASE):
    __tablename__ = "observations"
    __table_args__ = {"schema": "observations"}

    id_seq = sa.Sequence("seq_observations_id", schema="observations", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    user_id = sa.Column(BIGINT, sa.ForeignKey("users.users.id"))
    observation_name = sa.Column(TEXT, nullable=False)
    observation_description = sa.Column(TEXT)
    data = sa.Column(JSONBPydantic(ObservationDataModel), nullable=False)

    archived = sa.Column(BOOLEAN, default=False, nullable=False)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    user = relationship("User", back_populates="observations")

    def __repr__(self):
        return f"<Observation(id={self.id}, name={self.observation_name})>"