from uuid import uuid4

from schemas import CodeReviewResponse, CodeReviewRequest, ResumeRequest

from fastapi import FastAPI, HTTPException, Request
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

@app.get("/")
def read_root():
    return {
        "service": "AI Code Review Service",
        "version": "0.1.0",
        "status": "running"
    }

@app.post("/api/code-review", response_model=CodeReviewResponse)
def create_code_review(request: CodeReviewRequest, http_request: Request):

    graph = http_request.app.state.graph

    thread_id = str(uuid4())

    config = make_config(thread_id)

    initial_state = {
        "user_request": request.request,
        "generated_code": "",
        "review_status": "",
        "review_feedback": "",
        "attempts": 0,
        "human_decision": "",
        "status": "started"
    }

    graph.invoke(
        initial_state,
        config=config
    )

    snapshot = graph.get_state(config)

    return build_response(thread_id, snapshot)


@app.get("/api/code-review/{thread_id}", response_model=CodeReviewResponse)
def get_code_review(thread_id: str, http_request: Request):

    graph = http_request.app.state.graph

    config = make_config(thread_id)

    try:
        snapshot = graph.get_state(config)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Code review workflow not found"
        )

    if not snapshot.values:
        raise HTTPException(
            status_code=404,
            detail="Code review workflow not found"
        )

    return build_response(thread_id, snapshot)


@app.post("/api/code-review/{thread_id}/resume", response_model=CodeReviewResponse)
def resume_code_review(thread_id: str, request: ResumeRequest, http_request: Request):

    graph = http_request.app.state.graph

    config = make_config(thread_id)

    snapshot = graph.get_state(config)

    if not snapshot.values:
        raise HTTPException(
            status_code=404,
            detail="Code review workflow not found"
        )

    if snapshot.next != ("human_approval", ):
        raise HTTPException(
            status_code=400,
            detail="This workflow is not waiting for human approval."
        )

    graph.invoke(
        Command(
            resume=request.decision
        ),
        config=config
    )

    snapshot = graph.get_state(config)

    return build_response(thread_id, snapshot)