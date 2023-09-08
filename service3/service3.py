from fastapi import FastAPI

app = FastAPI()

@app.post("/print")
async def print_result(result: int):
    print(f"Result from Service 2: {result}")
    return {"result": result}
