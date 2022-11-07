import abc
from sdv.domain.documents.actor_es_document import ActorEsDocument


class AbstractActorEntity(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_document(self) -> ActorEsDocument:
        raise NotImplementedError
