import fastapi

app = fastapi.FastAPI()

@app.post("/return_name")
def read_root(data: dict):
    name = data.get("name")
    return {"name": name}
