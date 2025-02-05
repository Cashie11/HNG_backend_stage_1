from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="Number Classification API",
             description="API that returns mathematical properties and fun facts about numbers")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is perfect."""
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_properties(n: int) -> list:
    """Get the properties of a number according to specified combinations."""
    is_arm = is_armstrong(n)
    is_even = n % 2 == 0
    
    if is_arm:
        return ["armstrong", "even"] if is_even else ["armstrong", "odd"]
    return ["even"] if is_even else ["odd"]

def get_fun_fact(n: int) -> str:
    """Get a fun fact about the number."""
    if is_armstrong(n):
        digits = [int(d) for d in str(n)]
        fun_fact = f"{n} is an Armstrong number because " + " + ".join(f"{d}^{len(digits)}" for d in digits) + f" = {n} //gotten from the numbers API"
        return fun_fact
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        if response.status_code == 200:
            return response.text + " //gotten from the numbers API"
    except requests.exceptions.RequestException:
        pass
    return "Fun fact unavailable."

@app.get("/api/classify-number", response_model_exclude_unset=True)
async def classify_number(number: str = Query(..., description="Number to classify")):
    """
    Classify a number and return its mathematical properties.
    
    Parameters:
    - number: The number to analyze
    
    Returns:
    - JSON object containing number properties
    """
    try:
        num = int(number)
        return {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": get_properties(num),
            "digit_sum": sum(int(d) for d in str(num)),
            "fun_fact": get_fun_fact(num)
        }
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"number": "alphabet", "error": True}
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify API status."""
    return {"status": "healthy"}

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Number to classify")):
    try:
        num = int(number)
      
        if abs(num) > 1e9:  
            return JSONResponse(
                status_code=400,
                content={"number": "too large", "error": True}
            )
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"number": "invalid", "error": True}
        )
    
def get_fun_fact(n: int) -> str:
    if is_armstrong(n):
        digits = [int(d) for d in str(n)]
        fun_fact = f"{n} is an Armstrong number because " + " + ".join(f"{d}^{len(digits)}" for d in digits) + f" = {n} //gotten from the numbers API"
        return fun_fact
    try:
        response = requests.get(f"http://numbersapi.com/{n}", timeout=3)  # reduced timeout
        if response.status_code == 200:
            return response.text + " //gotten from the numbers API"
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        return "Fun fact unavailable due to external API timeout."
        