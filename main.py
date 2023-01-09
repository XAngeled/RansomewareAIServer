from fastapi import FastAPI
from pydantic import BaseModel
from framework import is_ransom

app = FastAPI()


class FileContent(BaseModel):
    name: str
    content: str


@app.post("/test_file/")
def read_item(file: FileContent):
    return {"is_ransom": True if is_ransom(file.content) == 1 else False}
