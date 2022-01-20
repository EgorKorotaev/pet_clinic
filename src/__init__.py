import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/owner/{owner_id}")
def foo():
    return {"message": "Hello World"}


@app.get('/favicon.ico')
def favicon():
    return FileResponse('favicon.ico')


if __name__ == "__main__":
    uvicorn.run("src.__init__:app", host="127.0.0.1", port=5000, log_level="info", workers=4, reload=True)
