import sqlite3
from sqlite3 import Connection

from pet_clinic.app.domain.directive import Directive
from pet_clinic.app.storage import get_db_path
from pet_clinic.app.usecase.create_directive import DirectivePersister


class DirectiveRepository(DirectivePersister):
    def __init__(self, db: Connection):
        self.db = db

    def save_directive(self, directive: Directive) -> None:
        sql = "INSERT INTO directives (id, title, cost) values(?, ?, ?)"
        data = (directive.id, directive.title, directive.cost)
        self.db.execute(sql, data)


def get_directive_repository() -> DirectiveRepository:
    return DirectiveRepository(sqlite3.connect(get_db_path()))
