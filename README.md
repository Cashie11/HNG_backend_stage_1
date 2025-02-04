# Number Classification API

A FastAPI-based REST API that analyzes numbers and provides various mathematical properties including primality, perfectness, and Armstrong numbers. The API also includes fun facts about numbers using the Numbers API.

## Features

- Number classification (prime, perfect, Armstrong)
- Even/odd determination
- Digit sum calculation
- Fun facts about numbers
- Error handling for invalid inputs

## Prerequisites

Before running this application, make sure you have the following installed:
- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository (if using version control):
   ```bash
   git clone https://github.com/Cashie11/HNG_backend_stage_1.git
   cd number-classification-api
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install fastapi uvicorn requests
   ```

## Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The `--reload` flag enables auto-reload on code changes (recommended for development)

2. The API will be available at:
   - Main URL: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`
   - Alternative API Documentation: `http://localhost:8000/redoc`

## API Endpoints

### GET /api/classify-number

Analyzes a number and returns its mathematical properties.

#### Query Parameters

- `number` (required): The number to analyze

#### Success Response

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371 //gotten from the numbers API"
}
```

#### Error Response

```json
{
    "number": "alphabet",
    "error": true
}
```

## Testing the API

You can test the API using any of the following methods:

### Using cURL

```bash
# Test with a valid number
curl "http://localhost:8000/api/classify-number?number=371"

# Test with invalid input
curl "http://localhost:8000/api/classify-number?number=abc"
```

### Using Web Browser

Visit the following URLs in your web browser:
- `http://localhost:8000/api/classify-number?number=371`
- `http://localhost:8000/api/classify-number?number=abc`

### Using Postman

1. Create a new GET request
2. Enter URL: `http://localhost:8000/api/classify-number`
3. Add query parameter:
   - Key: `number`
   - Value: `371` (or any other number)
4. Send the request

## Code Structure

The main components of the API include:

- `is_prime()`: Checks if a number is prime
- `is_perfect()`: Checks if a number is perfect
- `is_armstrong()`: Checks if a number is an Armstrong number
- `get_fun_fact()`: Retrieves fun facts about numbers
- Main API route handler with error handling

## Error Handling

The API includes error handling for:
- Invalid inputs (non-numeric values)
- Connection issues with the Numbers API
- General error cases

## Dependencies

- FastAPI: Web framework for building APIs
- Uvicorn: ASGI server implementation
- Requests: HTTP library for Python

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

### **Contributing**  
We welcome contributions! To contribute:  
1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:  
   ```bash
   git commit -m "Added new feature"
   ```
4. Push changes:  
   ```bash
   git push origin feature-branch
   ```
5. Open a **Pull Request** on GitHub.  

---
## **Contact**  
For any questions or support, feel free to reach out via email:  
📧 frankizuchukwu094@gmail.com
