from fastapi import FastAPI
import httpx

app = FastAPI()
service3_url = "http://container3:8003"


@app.post("/calculate")
async def calculate_square(value: int):
    try:
        if value < 0:
            return {"error": "Negative values are not allowed."}

        square = value ** 2

        # Send a POST request to Service 3 with the result
        async with httpx.AsyncClient() as client:
            response_from_service3 = await client.post(f"{service3_url}/print?result={square}")

        # Ensure Service 3's response is successful
        if response_from_service3.status_code == 200:
            result_from_service3 = response_from_service3.json().get("result")
        else:
            return {"error": "An error occurred in Service 3"}

        # Return the combined response with result from Service 2 and message from Service 3
        print(result_from_service3)
        return {"result": result_from_service3}
    except Exception as e:
        return {"error": "An error occurred while calculating the square"}
