# Création de l'entité Actor
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP

from sdv.infrastructure.sql.entities import Base


class ActorSQL(Base):
    __tablename__ = "actor"
    id = Column("actor_id", Integer, primary_key=True)
    first_name = Column("first_name", VARCHAR(45))
    last_name = Column("last_name", VARCHAR(45))
    last_update = Column("last_update", TIMESTAMP)
