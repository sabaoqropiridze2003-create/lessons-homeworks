from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/info")
def read_info():
    return {"name": "my first app",
            "version": "1.0",
            "description": "my first app"
            }

@app.get("/users")
def read_users():
    return [{"id":1, "name": "girogi", "grade":100},
            {"id":2, "name": "saba", "grade":78},
            {"id":3, "name": "anano", "grade":86}
            ]