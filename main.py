# main.py
from fastapi import FastAPI

app = FastAPI()

# In-memory storage for simplicity
users = {}
events = [{"id": 1, "name": "Music Concert"}, {"id": 2, "name": "Tech Meetup"}]

@app.post("/users")
def add_user(user_id: str, preference: str):
    users[user_id] = {"preference": preference}
    return {"message": "User added"}

@app.get("/events")
def get_events():
    return events

@app.get("/recommendations/{user_id}")
def recommend_events(user_id: str):
    user_pref = users.get(user_id, {}).get("preference")
    recommended_events = [event for event in events if event["name"].lower() == user_pref.lower()]
    return recommended_events if recommended_events else {"message": "No matching events found"}
