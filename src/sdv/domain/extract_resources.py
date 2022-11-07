from typing import Optional, List

from sdv.domain.documents.actor_es_document import ActorEsDocument
from sdv.domain.documents.document_type import DocumentType
from sdv.domain.ports.resources_repository import ResourcesRepository


class ExtractResources:
    def __init__(self, actor_repository: ResourcesRepository):
        self._resources_repository = {DocumentType.ACTOR: actor_repository}

    def execute(
        self, document_type: Optional[DocumentType] = None, ids: Optional[list[int]] = None
    ) -> List[ActorEsDocument]:
        entities = []
        if document_type and document_type in self._resources_repository:
            entities = (
                self._resources_repository[document_type].find_all()
                if not ids
                else self._resources_repository[document_type].find_by_ids(ids)
            )
        elif not document_type:
            entities = [
                entity for repository in self._resources_repository.values() for entity in repository.find_all()
            ]
        return [entity.to_document() for entity in entities]
