from fastapi import FastAPI
import httpx

app = FastAPI()
service2_url = "http://container2:8002"


@app.post("/input")
async def get_input(value: int):
    # Send a POST request to Service 2 with value as a query parameter
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{service2_url}/calculate?value={value}")

    # Extract the result from the response
    result = response.json().get("result")

    return {"value": value, "result": result}
