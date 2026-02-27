import streamlit as st
import requests
import os

# Configure Page
st.set_page_config(
    page_title="TraceAI - AI Mentor for Debugging",
    page_icon="🔍",
    layout="wide"
)

# Backend URL (FastAPI)
BACKEND_URL = "http://localhost:8001"

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #0f1116;
        color: #e6edf3;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4f46e5, #0ea5e9);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
    }
    .header-text {
        color: #0ea5e9;
        font-weight: 800;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .subtitle-text {
        color: #8b949e;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .result-section {
        background-color: #161b22;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-top: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# App UI
st.markdown('<h1 class="header-text">TraceAI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">AI Mentor for Debugging Real-World Code</p>', unsafe_allow_html=True)

with st.sidebar:
    st.title("Settings")
    st.info("Upload your project ZIP and paste an error trace to get a root-cause explanation.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Step 1: Index your Project")
    uploaded_file = st.file_uploader("Upload Project ZIP", type=["zip"])
    
    if st.button("Index Repository") and uploaded_file:
        with st.spinner("Analyzing and indexing repository..."):
            try:
                files = {"file": uploaded_file.getvalue()}
                # Re-wrapping as a file-like object for requests
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/zip")}
                response = requests.post(f"{BACKEND_URL}/upload", files=files)
                if response.status_code == 200:
                    st.success(f"Successfully indexed! Found {response.json()['file_count']} files.")
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Connection failed: {e}")

with col2:
    st.subheader("Step 2: Describe the Error")
    error_trace = st.text_area("Paste Stack Trace or Error Message", placeholder="e.g. ValueError: Cannot convert string to float...", height=200)
    
    if st.button("Fix this Bug") and error_trace:
        with st.spinner("Retrieving relevant code and analyzing..."):
            try:
                response = requests.post(f"{BACKEND_URL}/analyze", json={"error_trace": error_trace})
                if response.status_code == 200:
                    st.session_state["analysis_result"] = response.json()["analysis"]
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Connection failed: {e}")

# Display Results
if "analysis_result" in st.session_state:
    st.markdown("---")
    st.subheader("AI Analysis & Fix")
    st.markdown(f'<div class="result-section">', unsafe_allow_html=True)
    st.markdown(st.session_state["analysis_result"])
    st.markdown('</div>', unsafe_allow_html=True)
