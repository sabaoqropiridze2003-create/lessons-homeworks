from pydantic import BaseModel

class TravelRequest(BaseModel):
    request: str

class TravelResponse(BaseModel):
    thread_id: str
    status: str
    destination_info: str | None = None
    food_info: str | None = None
    budget_info: str | None = None
    final_plan: str | None = None