from abc import ABC

from sdv.domain.ports.resources_repository import ResourcesRepository


class ActorSQLRepository(ResourcesRepository, ABC):
    def __int__(self, engine):
        self._engine = engine
