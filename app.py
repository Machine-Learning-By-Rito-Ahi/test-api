from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/home")
def home():
    return {"message": "This is home..."}

@app.post("/api/generate_interview")
def generate_interview():
    return {"message": "Interview generated successfully."}

@app.post("/api/generate_itinerary")
def generate_itinerary():
    return {"message": "Itinerary generated successfully."}

# Entry point to run with: python app.py
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8888, reload=True)
