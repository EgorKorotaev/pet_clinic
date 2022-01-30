import sqlite3


def create_test_table():
    db = sqlite3.connect("test_db.db")

    db.execute(
        """
        DROP TABLE IF EXISTS pets;
        """
    )
    db.execute(
        """
        CREATE TABLE pets (
            id TEXT NOT NULL PRIMARY KEY,
            name TEXT,
            data_created TEXT
        ); 
        """
    )

    db.execute(
        """
        DROP TABLE IF EXISTS directives;
        """
    )
    db.execute(
        """
        CREATE TABLE directives (
            id TEXT NOT NULL PRIMARY KEY,
            title TEXT,
            cost TEXT
        );
        """
    )

    # db.execute(
    #     """
    #     DROP TABLE IF EXISTS pet_directives;
    #     """
    # )
    # db.execute(
    #     """
    #     CREATE TABLE pet_directives (
    #         id TEXT NOT NULL PRIMARY KEY,
    #         pet_id TEXT,
    #         directives_id TEXT,
    #         data_created TEXT
    #     );
    #     """
    # )

    return db
