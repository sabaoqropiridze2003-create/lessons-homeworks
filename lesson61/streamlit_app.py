import os
from typing import Any

import httpx
import streamlit as st


DEFAULT_API_BASE_URL = "http://localhost:8000"
REQUEST_TIMEOUT = httpx.Timeout(120.0, connect=10.0)


class APIError(Exception):
    pass


def api_base_url() -> str:
    return os.getenv("API_BASE_URL", DEFAULT_API_BASE_URL).rstrip("/")


def request_json(method: str, path: str, **kwargs: Any) -> dict[str, Any]:
    url = f"{api_base_url()}{path}"
    try:
        response = httpx.request(
            method,
            url,
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )
    except httpx.TimeoutException as exc:
        raise APIError(
            "The API request timed out. The workflow may still be running; "
            "refresh its status before submitting another request."
        ) from exc
    except httpx.RequestError as exc:
        raise APIError(
            f"Could not connect to the API at {api_base_url()}. "
            "Check that FastAPI is running and API_BASE_URL is correct."
        ) from exc

    if not response.is_success:
        try:
            detail = response.json().get("detail", response.text)
        except ValueError:
            detail = response.text
        raise APIError(f"API returned HTTP {response.status_code}: {detail}")

    try:
        data = response.json()
    except ValueError as exc:
        raise APIError("The API returned an invalid JSON response.") from exc

    if not isinstance(data, dict):
        raise APIError("The API returned a response in an unexpected format.")
    return data


def load_workflow(thread_id: str) -> dict[str, Any]:
    return request_json("GET", f"/api/code-review/{thread_id}")


def submit_decision(thread_id: str, decision: str) -> dict[str, Any]:
    return request_json(
        "POST",
        f"/api/code-review/{thread_id}/resume",
        json={"decision": decision},
    )


def status_label(workflow: dict[str, Any]) -> str:
    status = workflow.get("status")
    decision = workflow.get("human_decision")
    if decision == "approved":
        return "Completed — approved by human"
    if decision == "rejected" or status == "rejected":
        return "Rejected by human"
    if status in {"waiting_human_approval", "waiting_for_approval"}:
        return "Waiting for human approval"
    if status:
        return str(status).replace("_", " ").capitalize()
    return "Status unavailable"


def render_workflow(workflow: dict[str, Any]) -> None:
    st.subheader("Workflow status")
    st.info(status_label(workflow))

    attempts = workflow.get("attempts", 0)
    review_status = workflow.get("review_status")
    feedback = workflow.get("review_feedback")
    code = workflow.get("code")

    st.caption(f"Generation attempts: {attempts}")
    st.caption(
        "The API exposes the latest attempt only; it does not provide "
        "intermediate events or prior-attempt history."
    )

    if code:
        st.subheader("Latest generated code")
        st.code(code, language="python")
    else:
        st.info("No generated code is available in the API response yet.")

    if review_status:
        st.subheader("Reviewer verdict")
        st.write(str(review_status).capitalize())
    if feedback:
        st.subheader("Reviewer feedback")
        st.caption("Model-generated feedback; this is not a verified test result.")
        st.write(feedback)

    st.caption(
        "Generated code is displayed for review only. The frontend does not execute it."
    )


def main() -> None:
    st.set_page_config(page_title="AI Code Review", page_icon="🧪", layout="wide")
    st.title("AI Code Review")
    st.write(
        "Submit a Python coding request, inspect the generated code and model "
        "review, then approve or reject the workflow."
    )

    if "active_thread_id" not in st.session_state:
        st.session_state.active_thread_id = ""
    if "workflow" not in st.session_state:
        st.session_state.workflow = None

    with st.sidebar:
        st.subheader("API configuration")
        st.code(api_base_url())
        st.caption("Set API_BASE_URL in the environment to use another API server.")
        st.subheader("Recover a workflow")
        recovery_id = st.text_input(
            "Thread ID",
            value=st.session_state.active_thread_id,
            key="recovery_thread_id",
        )
        if st.button("Load workflow", use_container_width=True):
            thread_id = recovery_id.strip()
            if not thread_id:
                st.warning("Enter a thread ID.")
            else:
                try:
                    with st.spinner("Loading workflow status..."):
                        workflow = load_workflow(thread_id)
                    st.session_state.active_thread_id = thread_id
                    st.session_state.workflow = workflow
                    st.success("Workflow loaded.")
                except APIError as exc:
                    st.error(str(exc))
                    if "404" in str(exc):
                        st.info(
                            "This workflow may not exist or may have been lost "
                            "when the API restarted; its state is held in memory."
                        )

    st.subheader("Submit a code request")
    with st.form("code_request_form"):
        user_request = st.text_area(
            "Describe the Python program you want",
            height=160,
            placeholder="For example: Write a function that validates an email address...",
        )
        submitted = st.form_submit_button("Generate and review", type="primary")

    if submitted:
        if not user_request.strip():
            st.warning("Describe the program before submitting.")
        else:
            try:
                with st.spinner(
                    "Generating and reviewing code. The current API runs this "
                    "workflow synchronously..."
                ):
                    workflow = request_json(
                        "POST",
                        "/api/code-review",
                        json={"request": user_request.strip()},
                    )
                thread_id = workflow.get("thread_id")
                if not isinstance(thread_id, str) or not thread_id:
                    raise APIError(
                        "The API response did not include a valid thread ID."
                    )
                st.session_state.active_thread_id = thread_id
                st.session_state.workflow = workflow
                st.success(f"Workflow started. Thread ID: {thread_id}")
            except APIError as exc:
                st.error(str(exc))

    workflow = st.session_state.workflow
    thread_id = st.session_state.active_thread_id
    if workflow and thread_id:
        st.divider()
        st.header("Current workflow")
        st.caption(f"Thread ID: `{thread_id}`")

        col_refresh, _ = st.columns([1, 4])
        if col_refresh.button("Refresh status"):
            try:
                with st.spinner("Refreshing workflow status..."):
                    workflow = load_workflow(thread_id)
                st.session_state.workflow = workflow
            except APIError as exc:
                st.error(str(exc))
                if "404" in str(exc):
                    st.info(
                        "The workflow could not be recovered. The backend stores "
                        "workflow state in memory, so a service restart loses it."
                    )

        render_workflow(st.session_state.workflow)

        current = st.session_state.workflow
        pending_approval = current.get("status") in {
            "waiting_human_approval",
            "waiting_for_approval",
        }
        if pending_approval and current.get("human_decision") in (None, ""):
            st.subheader("Human approval")
            st.warning("Review the latest code and model-generated feedback first.")
            approve_col, reject_col = st.columns(2)
            if approve_col.button(
                "Approve",
                type="primary",
                use_container_width=True,
                key="approve_workflow",
            ):
                try:
                    with st.spinner("Submitting approval..."):
                        updated = submit_decision(thread_id, "approved")
                    st.session_state.workflow = updated
                    st.success("Human approval submitted.")
                    st.rerun()
                except APIError as exc:
                    st.error(f"Approval was not confirmed: {exc}")
            if reject_col.button(
                "Reject",
                use_container_width=True,
                key="reject_workflow",
            ):
                try:
                    with st.spinner("Submitting rejection..."):
                        updated = submit_decision(thread_id, "rejected")
                    st.session_state.workflow = updated
                    st.warning(
                        "Human rejection submitted. Rejection ends this workflow; "
                        "it does not request another generation attempt."
                    )
                    st.rerun()
                except APIError as exc:
                    st.error(f"Rejection was not confirmed: {exc}")

    st.divider()
    st.caption(
        "Progress limitation: the existing API does not expose live agent events "
        "or attempt history. The create request blocks until the workflow reaches "
        "its approval pause, so this page cannot show intermediate generation or "
        "review progress."
    )


if __name__ == "__main__":
    main()