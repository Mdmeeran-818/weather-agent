from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Frontend coding connect aaga permission (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    city: str
    health_conditions: str
    commute_mode: str

@app.post("/advise")
async def process_weather(data: UserInput):
    health = data.health_conditions.lower()
    commute = data.commute_mode.lower()
    
    # Real weather connectivity ready aagura varai beginner-friendly automated logic
    if "asthma" in health:
        status = "HEALTH ALERT / CAUTION"
        advice = f"Weather in {data.city} looks okay, but pollen levels might be high. Carry your inhaler."
    elif "bicycle" in commute:
        status = "CONVENIENCE ROUTINE"
        advice = f"Cloudy skies expected in {data.city}. Good for cycling, but carry a raincoat just in case!"
    else:
        status = "NORMAL / ROUTINE"
        advice = f"Weather conditions are standard in {data.city}. Have a great day ahead!"
        
    return {"status": status, "advice": advice}