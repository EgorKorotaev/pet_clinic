import uvicorn
import sqlite3 as sl

bd = sl.connect('pet_clinic.db')


def create_table():
    try:
        with bd:
            bd.execute("""
                CREATE TABLE PETS (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    species TEXT,
                    name TEXT,
                    owner TEXT,
                    status TEXT,
                    diagnosis TEXT,
                    doctor TEXT
                ); 
            """)
    except Exception:
        pass


def uvicorn_start():
    create_table()
    uvicorn.run("pet_clinic.app.app:app", host="127.0.0.1", port=8000, log_level="info", workers=4, reload=True)


if __name__ == "__main__":
    uvicorn_start()
