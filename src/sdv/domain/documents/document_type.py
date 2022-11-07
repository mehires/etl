import enum
from dataclasses import dataclass


@dataclass
class DocumentTypeData:
    label: str


class DocumentType(enum.Enum):
    ACTOR = DocumentTypeData("actor")

    @property
    def label(self):
        return self.value.label

    @classmethod
    def from_text(cls, text: str):
        for document_type in cls:
            if document_type.value.label == text:
                return document_type
        raise ValueError("Invalid document type")
