from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_fun_fact(n: int) -> str:
    if is_armstrong(n):
        digits = [int(d) for d in str(n)]
        fun_fact = f"{n} is an Armstrong number because " + " + ".join(f"{d}^{len(digits)}" for d in digits) + f" = {n} //gotten from the numbers API"
        return fun_fact
    try:
        response = requests.get(f"http://numbersapi.com/{n}", timeout=5)
        if response.status_code == 200:
            return response.text + " //gotten from the numbers API"
    except requests.exceptions.RequestException:
        pass
    return "Fun fact unavailable."

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Number to classify")):
    try:
        num = int(number)  # Try to convert string to integer
        properties = []
        if is_prime(num):
            properties.append("prime")
        if is_perfect(num):
            properties.append("perfect")
        if is_armstrong(num):
            properties.append("armstrong")
        if num % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        
        return {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(num)),
            "fun_fact": get_fun_fact(num)
        }
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"number": "alphabet", "error": True}
        )