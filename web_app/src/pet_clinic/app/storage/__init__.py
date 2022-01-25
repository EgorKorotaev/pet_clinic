import os

DB_PATH = os.path.join(__file__, "..", "pet_clinic.db")


def get_db_path() -> str:
    return DB_PATH


def set_db_path(path: str):
    global DB_PATH
    DB_PATH = path
