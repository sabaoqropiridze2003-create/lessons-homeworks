from uuid import uuid4
from schemas import TravelRequest, TravelResponse
from fastapi import FastAPI, HTTPException, Request
from database import lifespan

app = FastAPI(
    title="Multi-Agent Travel Planner API",
    description="API for planning trips using specialized destination, food, and budget agents",
    version="1.0.0",
    lifespan=lifespan
)

def make_config(thread_id: str):
    return {"configurable": {"thread_id": thread_id}}

def build_response(thread_id: str, snapshot):
    values = snapshot.values
    return TravelResponse(
        thread_id=thread_id,
        status=values.get("status", "in_progress"),
        destination_info=values.get("destination_info"),
        food_info=values.get("food_info"),
        budget_info=values.get("budget_info"),
        final_plan=values.get("final_plan")
    )

@app.post("/api/travel-plan", response_model=TravelResponse)
def create_travel_plan(request: TravelRequest, http_request: Request):

    graph = http_request.app.state.graph

    thread_id = str(uuid4())

    config = make_config(thread_id)

    initial_state = {
        "user_request": request.request,
        "destination_info": "",
        "food_info": "",
        "budget_info": "",
        "final_plan": "",
        "status": "started"
    }

    graph.invoke(initial_state, config=config)

    snapshot = graph.get_state(config)

    return build_response(thread_id, snapshot)

@app.get("/api/travel-plan/{thread_id}", response_model=TravelResponse)
def get_travel_plan(thread_id: str, http_request: Request):

    graph = http_request.app.state.graph
    
    config = make_config(thread_id)

    try:
        snapshot = graph.get_state(config)
    except Exception:
        raise HTTPException(status_code=404, detail="Travel plan workflow not found")

    if not snapshot.values:
        raise HTTPException(status_code=404, detail="Travel plan workflow not found")

    return build_response(thread_id, snapshot)