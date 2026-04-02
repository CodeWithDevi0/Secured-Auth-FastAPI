from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth 

app = FastAPI(title="Secured Authentication API")

# Your standard CORS setup for the Vue.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def home():
    return {"message": "Welcome to the Secured Authentication API!"}

# Tell the main app to use the routes from auth.py
app.include_router(auth.router)