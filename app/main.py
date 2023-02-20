from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload


class DataInput(BaseModel):
    msg: str


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.post("/", response_model=DataInput)
async def write_main(data: DataInput):
    # return jsonable_encoder(data)
    return data.dict()


@app.patch("/", response_model=DataInput)
async def update_main(data: DataInput):
    new_data = data
    new_data.msg += " Update"
    return new_data.dict()


@app.delete("/{id}")
async def delete_main(id: int):
    data = DataInput(msg=str(id))
    return data.dict()
