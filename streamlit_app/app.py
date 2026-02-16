import streamlit as st
import requests
import time

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="RNN QA System",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 30px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Header Section
# -----------------------------
st.markdown('<div class="main-title">🤖 RNN Question Answering System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask any question and let the model answer it intelligently.</div>', unsafe_allow_html=True)

# -----------------------------
# API URL (Configurable)
# -----------------------------
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/predict")


# -----------------------------
# Input Section
# -----------------------------
with st.container():
    question = st.text_area("Enter your question below:", height=100)

# -----------------------------
# Button + Response Section
# -----------------------------
if st.button("🔍 Get Answer", use_container_width=True):

    if not question.strip():
        st.warning("⚠️ Please enter a valid question.")
    else:
        with st.spinner("Thinking... 🤔"):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=10
                )

                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer found.")
                    
                    st.success("✅ Answer")
                    st.markdown(f"### 📝 {answer}")

                else:
                    st.error(f"API Error: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("🚫 Cannot connect to API. Make sure FastAPI is running.")
            except requests.exceptions.Timeout:
                st.error("⏳ Request timed out.")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    '<div class="footer">Built by Zeeshan Bhutto ❤️ </div>',
    unsafe_allow_html=True
)
