from abc import abstractmethod, ABC
from dataclasses import dataclass
from uuid import uuid4

from pet_clinic.app.domain.directive import Directive


@dataclass
class CreateDirectiveRequest:
    title: str
    cost: str


class DirectivePersister(ABC):
    @abstractmethod
    def save_directive(self, directive: Directive) -> None:
        pass


def create_directive(
    create_directive_request: CreateDirectiveRequest,
    directive_persister: DirectivePersister,
) -> str:
    directive_id = str(uuid4())
    directive = Directive(
        id=directive_id,
        title=create_directive_request.title,
        cost=create_directive_request.cost,
    )
    directive_persister.save_directive(directive)
    return directive_id
