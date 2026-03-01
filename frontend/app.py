import streamlit as st
import requests

# Configure Page
st.set_page_config(
    page_title="TraceAI - Code Analysis",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Backend URL (FastAPI)
BACKEND_URL = "http://localhost:8001"

# Custom CSS for Premium AWS/Enterprise Look
st.markdown("""
<style>
    /* Enterprise Dark Theme */
    .stApp {
        background-color: #0f1b2a;
        font-family: 'Inter', 'Amazon Ember', 'Helvetica Neue', sans-serif;
        color: #e0e6ed;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #16202c;
        border-right: 1px solid #233040;
    }
    
    .css-1d391kg {
        background-color: #16202c;
    }
    
    /* Headers */
    h1 {
        color: #ff9900 !important;
        font-weight: 700 !important;
        font-size: 2.25rem !important;
        letter-spacing: -0.02em;
        margin-bottom: 0rem !important;
        padding-bottom: 0rem !important;
    }
    
    h2 {
        color: #f2f3f3 !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
        border-bottom: 1px solid #233040;
        padding-bottom: 0.5rem;
    }

    h3 {
        color: #d1d5db !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
    }
    
    /* Subtitle */
    .subtitle-text {
        color: #8795a1;
        font-size: 1.05rem;
        margin-bottom: 2rem;
        border-bottom: 1px solid #233040;
        padding-bottom: 1rem;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #ff9900;
        color: #0f1b2a;
        font-weight: 700;
        border: 1px solid #ff9900;
        border-radius: 2px;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
        width: 100%;
    }
    
    .stButton > button:hover {
        background-color: #ec7211;
        border-color: #ec7211;
        color: #ffffff;
    }
    
    /* File Uploader Container */
    [data-testid="stFileUploader"] {
        background-color: #1c2735;
        border: 1px dashed #3a4553;
        border-radius: 4px;
        padding: 1rem;
    }
    
    /* Input Areas */
    .stTextArea > div > div > textarea {
        background-color: #1c2735;
        color: #e0e6ed;
        border: 1px solid #3a4553;
        border-radius: 2px;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #ff9900;
        box-shadow: 0 0 0 1px #ff9900;
    }
    
    /* Result Section */
    .result-section {
        background-color: #1c2735;
        border: 1px solid #233040;
        border-left: 4px solid #00a4fb;
        padding: 1.75rem;
        border-radius: 4px;
        margin-top: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    
    /* Code Blocks within Markdown */
    pre {
        background-color: #0f1b2a !important;
        border: 1px solid #233040 !important;
        border-radius: 4px !important;
    }
    
    code {
        color: #ff9900 !important;
    }
</style>
""", unsafe_allow_html=True)

# App UI Header
st.markdown('<h1>TraceAI Console</h1>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text"><strong>Amazon Bedrock Powered</strong> • Automated Codebase Root-Cause Analysis</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1024px-Amazon_Web_Services_Logo.svg.png", width=150)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Control Panel")
    st.markdown("Use this workspace to index serverless functions, EC2 instances code, or raw ZIP repositories.")
    st.info("Ensure Bedrock access is configured in your AWS environment for Titan & Nova Lite.")
    
    st.markdown("---")
    st.markdown("**Region:** us-east-1")
    st.markdown("**Status:** Online")

# Main Content Columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("<h2>1. Vectorize Repository</h2>", unsafe_allow_html=True)
    st.markdown("<span style='color: #8795a1; font-size: 0.9rem;'>Upload a .zip containing your source files. TraceAI will chunk and embed the logic using Titan Multimodal Embeddings.</span>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload Source Code (.zip)", type=["zip"], label_visibility="collapsed")
    
    if st.button("Start Indexing Process", key="index_btn"):
        if uploaded_file:
            with st.spinner("Extracting and vectorizing via Bedrock..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/zip")}
                    response = requests.post(f"{BACKEND_URL}/upload", files=files)
                    if response.status_code == 200:
                        st.success(f"Index Built Successfully. Validated {response.json()['file_count']} files.")
                    else:
                        st.error(f"Service Error: {response.json().get('detail', 'Unknown error')}")
                except Exception as e:
                    st.error(f"Endpoint Unreachable: {e}")
        else:
            st.warning("Please upload a .zip file first.")

with col2:
    st.markdown("<h2>2. Analyze Trace</h2>", unsafe_allow_html=True)
    st.markdown("<span style='color: #8795a1; font-size: 0.9rem;'>Provide the application stack trace. TraceAI will cross-reference the vector database and generate a root-cause fix via Amazon Nova.</span>", unsafe_allow_html=True)
    
    error_trace = st.text_area("Stack Trace / Log Output", placeholder="e.g., File 'lambda_function.py', line 42, in handler\nKeyError: 'user_id'", height=185, label_visibility="collapsed")
    
    if st.button("Synthesize Solution", key="analyze_btn"):
        if error_trace:
            with st.spinner("Querying vector database and synthesizing fix..."):
                try:
                    response = requests.post(f"{BACKEND_URL}/analyze", json={"error_trace": error_trace})
                    if response.status_code == 200:
                        st.session_state["analysis_result"] = response.json()["analysis"]
                    else:
                        st.error(f"Service Error: {response.json().get('detail', 'Unknown error')}")
                except Exception as e:
                    st.error(f"Endpoint Unreachable: {e}")
        else:
            st.warning("Please provide a stack trace to analyze.")

# Display Results
if "analysis_result" in st.session_state:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2>Remediation Blueprint</h2>", unsafe_allow_html=True)
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    st.markdown(st.session_state["analysis_result"])
    st.markdown('</div>', unsafe_allow_html=True)
