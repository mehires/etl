from typing import List

from sqlalchemy.orm import Session

from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity
from sdv.domain.entities.actor import Actor
from sdv.domain.ports.resources_repository import ResourcesRepository
from sdv.infrastructure.sql.entities.actor_sql import ActorSQL


class ActorSQLRepository(ResourcesRepository):
    def __init__(self, engine):
        self.engine = engine

    def find_all(self) -> List[AbstractActorEntity]:
        with Session(self.engine) as session:
            return [self._create_entity(actor) for actor in session.query(ActorSQL)]

    def find_by_ids(self, ids: List[int]) -> List[AbstractActorEntity]:
        pass

    @staticmethod
    def _create_entity(actor: ActorSQL) -> Actor:
        return Actor(id=actor.id, first_name=actor.first_name, last_name=actor.last_name, last_update=actor.last_update)
