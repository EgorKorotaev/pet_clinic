from dataclasses import dataclass

import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse


@dataclass
class Item:
    name: str
    password: str


app = FastAPI()


@app.get("/")
def root():
    return Item('foo', 'bar')


@app.get("/owner/{owner_id}")
def foo():
    return {"message": "Hello World"}


@app.get('/favicon.ico')
def favicon():
    return FileResponse('../../media/favicon.ico')


if __name__ == "__main__":
    uvicorn.run("server.src.__init__:app", host="127.0.0.1", port=5000, log_level="info", workers=4, reload=True)
