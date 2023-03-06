from fastapi import FastAPI

app = FastAPI()
app.title = "Mi primera aplicación con FastAPI"
app.version == "0.0.1"

@app.get("/", tags=["home"])

def message():
    return "This is a test message xD"