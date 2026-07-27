from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent
from handlers import set_restaurant
from menu import MENU

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Keep conversation history in memory (fine for a demo, resets on restart)
conversation = []

class ChatRequest(BaseModel):
    message: str

class SelectRestaurantRequest(BaseModel):
    restaurant_id: str

@app.get("/restaurants")
def list_restaurants(city: str = ""):
    """Return restaurants, optionally filtered by a location the customer typed in."""
    all_restaurants = [
        {"id": rid, "name": r["name"], "city": r["city"], "cuisine": r["cuisine"]}
        for rid, r in MENU.items()
    ]

    if not city.strip():
        return {"restaurants": all_restaurants, "matched_location": False}

    matches = [r for r in all_restaurants if city.strip().lower() in r["city"].lower()]

    if matches:
        return {"restaurants": matches, "matched_location": True}
    else:
        # No restaurants in that exact location yet — fall back to showing
        # everything rather than a dead-end empty screen in the demo.
        return {"restaurants": all_restaurants, "matched_location": False}

@app.post("/select-restaurant")
def select_restaurant(req: SelectRestaurantRequest):
    """Called when the customer picks a restaurant on the website, before chat starts."""
    result = set_restaurant(req.restaurant_id)
    conversation.clear()  # fresh conversation for the new restaurant
    return result

@app.post("/chat")
def chat(req: ChatRequest):
    conversation.append({"role": "user", "content": req.message})
    reply = run_agent(conversation)
    conversation.append({"role": "assistant", "content": reply})
    return {"reply": reply}