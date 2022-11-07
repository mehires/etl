import abc
from dataclasses import dataclass
from datetime import datetime

from sdv.domain.documents.actor_es_document import ActorEsDocument
from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity


@dataclass
class Actor(AbstractActorEntity):
    id: int
    first_name: str
    last_name: str
    last_update: datetime

    def to_document(self) -> ActorEsDocument:
        # on peut faire des traitements
        return ActorEsDocument(
            id=self.id, first_name=self.first_name, last_name=self.last_name, last_update=self.last_update
        )
