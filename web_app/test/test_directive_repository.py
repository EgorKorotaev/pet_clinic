from pet_clinic.app.domain.directive import Directive
from pet_clinic.app.storage.directive_repository import DirectiveRepository
from test_table import create_test_table


def test_save_directive():  # integration test
    # given
    directive_id = "_42"
    directive = Directive(id=directive_id, title="title", cost="1000")
    db = create_test_table()
    directive_repository = DirectiveRepository(db)

    # when
    directive_repository.save_directive(directive)

    # then
    sql = "SELECT id, title, cost FROM directives WHERE id = ?"
    result = db.execute(sql, [directive_id]).fetchall()[0]
    assert result == (directive_id, directive.title, directive.cost)
