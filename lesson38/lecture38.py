from fastapi import FastAPI

app = FastAPI(
    title="FastAPI",
    version="1.0.0",
    description="FastAPI project"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

