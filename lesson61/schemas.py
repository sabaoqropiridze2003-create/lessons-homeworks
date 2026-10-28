from pydantic import BaseModel, Field
from typing import Literal

class ReviewResult(BaseModel):
    status: Literal["approved", "rejected"]
    feedback: str

class CodeReviewRequest(BaseModel):
    request: str

class ResumeRequest(BaseModel):
    decision: Literal["approved", "rejected"]

class CodeReviewResponse(BaseModel):
    thread_id: str
    status: str
    code: str | None = None
    review_status: str | None = None
    review_feedback: str | None = None
    attempts: int = 0
    human_decision: str | None = None