from uuid import uuid4

from schemas import CodeReviewResponse, CodeReviewRequest, ResumeRequest

from fastapi import FastAPI, HTTPException
from langgraph.types import Command


app = FastAPI(
    title="AI Code Review Service",
    description="A service that reviews code using AI",
    version="0.1.0"
)

def make_config(thread_id: str):
    return {
        "configurable": {
            "thread_id": thread_id
        }
    }

def build_response(thread_id: str, snapshot):
    values = snapshot.values

    if snapshot.next == ("human_approval", ):
        status = "waiting_human_approval"
    elif not snapshot.next:
        status = values.get("status", "completed")
    else:
        status = values.get("status", "in_progress")

    return CodeReviewResponse(
        thread_id=thread_id,
        status=status,
        code=values.get("generated_code"),
        review_status=values.get("review_status"),
        review_feedback=values.get("review_feedback"),
        attempts=values.get("attempts", 0),
        human_decision=values.get("human_decision")
    )