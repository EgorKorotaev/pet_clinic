from dataclasses import dataclass

from pet_clinic.app.domain.directive import Directive
from pet_clinic.app.usecase.create_directive import (
    create_directive,
    CreateDirectiveRequest,
    DirectivePersister,
)


@dataclass
class TestStorage(DirectivePersister):
    directive: Directive | None = None

    def save_directive(self, directive: Directive) -> None:
        self.directive = directive

    def get_result(self) -> Directive:
        return self.directive


def test_pet_is_registered():  # unit test
    # given
    directive_title = "title"
    directive_cost = "cost"
    create_directive_request = CreateDirectiveRequest(directive_title, directive_cost)
    test_storage = TestStorage()

    # when
    directive_id = create_directive(create_directive_request, test_storage)

    # then
    directive_expected = Directive(
        id=directive_id, title=directive_title, cost=directive_cost
    )
    directive_actual = test_storage.get_result()
    assert directive_expected == directive_actual
