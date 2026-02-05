from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

def success_response():
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "method": "GET",
            "message": "Hello from Flask"
        },
        headers={
            "Content-Type": "application/json"
        }
    )

def error_405_response():
    return JSONResponse(
        status_code=405,
        content={
            "status": "error",
            "message": "Method not allowed"
        },
        headers={
            "Content-Type": "application/json"
        }
    )

def error_404_response():
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "Not found"
        },
        headers={
            "Content-Type": "application/json"
        }
    )

@app.middleware("http")
async def global_guard(request: Request, call_next):
    if request.url.path != "/":
        return error_404_response()

    if request.method != "GET":
        return error_405_response()

    return await call_next(request)

@app.get("/", include_in_schema=False)
async def home():
    return success_response()

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return error_404_response()

@app.exception_handler(405)
async def method_not_allowed_handler(request: Request, exc):
    return error_405_response()
