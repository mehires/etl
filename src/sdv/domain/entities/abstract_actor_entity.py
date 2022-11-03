import abc
from sdv.domain.documents.actor_document import ActorDocument
class AbstractActorEntity(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_document(self) -> ActorDocument:
        raise NotImplementedError

