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
        response = httpx.request(method, url, timeout=REQUEST_TIMEOUT, **kwargs)
    except httpx.RequestError as exc:
        raise APIError(f"Could not connect to API at {api_base_url()}. Check if FastAPI is running.") from exc

    if not response.is_success:
        try:
            detail = response.json().get("detail", response.text)
        except ValueError:
            detail = response.text
        raise APIError(f"API returned HTTP {response.status_code}: {detail}")

    return response.json()

def load_workflow(thread_id: str) -> dict[str, Any]:
    return request_json("GET", f"/api/travel-plan/{thread_id}")

def main() -> None:
    st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")
    
    if "active_thread_id" not in st.session_state:
        st.session_state.active_thread_id = ""
    if "workflow" not in st.session_state:
        st.session_state.workflow = None

    # --- Sidebar (როგორც სურათზეა) ---
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
                    with st.spinner("Loading travel plan..."):
                        workflow = load_workflow(thread_id)
                    st.session_state.active_thread_id = thread_id
                    st.session_state.workflow = workflow
                    st.success("Travel plan loaded.")
                except APIError as exc:
                    st.error(str(exc))

    # --- Main Page ---
    st.title("✈️ Multi-Agent Travel Planner")
    st.write("Enter your travel preferences, and our team of AI experts (Destination, Culinary, and Budget) will build a complete trip plan for you.")

    with st.form("travel_form"):
        user_request = st.text_area(
            "Describe your dream trip",
            height=120,
            placeholder="For example: I want to go to Paris for 4 days. I am interested in museums, good local food, and I have a medium budget.",
        )
        submitted = st.form_submit_button("Generate Travel Plan", type="primary")

    if submitted:
        if not user_request.strip():
            st.warning("Please describe your trip first.")
        else:
            try:
                with st.spinner("Agents are collaborating (Analyzing destination, food, and budget)..."):
                    workflow = request_json("POST", "/api/travel-plan", json={"request": user_request.strip()})
                
                thread_id = workflow.get("thread_id")
                st.session_state.active_thread_id = thread_id
                st.session_state.workflow = workflow
                st.success(f"Travel plan generated successfully! Thread ID: {thread_id}")
            except APIError as exc:
                st.error(str(exc))

    workflow = st.session_state.workflow
    thread_id = st.session_state.active_thread_id
    
    if workflow:
        st.divider()
        st.header("Your Travel Itinerary")
        if thread_id:
            st.caption(f"Thread ID: `{thread_id}`")

        tab1, tab2, tab3, tab4 = st.tabs(["🌟 Final Plan", "🏛️ Destination Sights", "🍴 Culinary Guide", "💰 Budget Breakdown"])

        with tab1:
            st.markdown(workflow.get("final_plan", "No plan available."))

        with tab2:
            st.markdown(workflow.get("destination_info", "No info available."))

        with tab3:
            st.markdown(workflow.get("food_info", "No info available."))

        with tab4:
            st.markdown(workflow.get("budget_info", "No info available."))

if __name__ == "__main__":
    main()