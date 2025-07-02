# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os
# import google.generativeai as genai
# from PIL import Image
# import pdf2image
# import io
# import base64

# # Configure API key securely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# if not GOOGLE_API_KEY:
#     st.error("GOOGLE_API_KEY not found in environment variables.")
#     st.stop()

# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-2.0-flash")

# def get_gemini_response(prompt, pdf_content, user_query):
#     response = model.generate_content([prompt, pdf_content[0], user_query])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read(),dpi=500,poppler_path=r'D:\poppler-24.08.0\Library\bin')
#         first_page = images[0]

#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='PNG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/png",
#                 "data": base64.b64encode(img_byte_arr).decode('utf-8'),
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No PDF file uploaded.")

# # Streamlit App Setup
# st.set_page_config(page_title="ATS Resume Checker", page_icon=":robot_face:", layout="wide")
# st.header("ATS Resume Parser")
# input_text = st.text_area("Your Query (Optional):", key="input")

# uploaded_file = st.file_uploader("Upload a Resume PDF", type=["pdf"], key="pdf")
# if uploaded_file is not None:
#     st.success("✅ PDF submitted successfully!")

# submit1 = st.button("Tell me about my Resume")
# submit2 = st.button("How can I Improve my Skills")
# submit3 = st.button("Percentage Match")

# input_prompt1 = """You are experienced in the field of Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis. Your task is to review the provided resume against the job description. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the application in relation to the job specializations."""

# input_prompt2 = """You are a Technical Human Resource Manager with expertise in Data Science. Your role is to scrutinize the resume in light of the provided job description. Share insights on the candidate's suitability for the role and offer advice on enhancing the candidate's skills."""

# input_prompt3 = """Act like an ATS (Applicant Tracking System). Analyze how well this resume matches the job description provided. Give a percentage match and explain which keywords or skills are missing."""

# if submit1:
#     if uploaded_file:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("🧾 Evaluation Result")
#         st.write(response)
#     else:
#         st.warning("⚠️ Please upload the resume.")

# elif submit2:
#     if uploaded_file:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt2, pdf_content, input_text)
#         st.subheader("📈 Skill Improvement Suggestions")
#         st.write(response)
#     else:
#         st.warning("⚠️ Please upload the resume.")

# elif submit3:
#     if uploaded_file:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("📊 ATS Match Report")
#         st.write(response)
#     else:
#         st.warning("⚠️ Please upload the resume.")







from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import pdf2image
import io
import base64
import requests
from streamlit_lottie import st_lottie

# Configure API key securely
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in environment variables.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def get_gemini_response(prompt, pdf_content, user_query):
    response = model.generate_content([prompt, pdf_content[0], user_query])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(), dpi=500, poppler_path=r'D:\poppler-24.08.0\Library\bin')
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/png",
                "data": base64.b64encode(img_byte_arr).decode('utf-8'),
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No PDF file uploaded.")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page Configuration
st.set_page_config(page_title="ATS Resume Checker", page_icon=":robot_face:", layout="wide")

dark_mode = st.toggle("🌙 Dark Mode")

theme = "Dark Mode" if dark_mode else "Light Mode"

# Custom CSS
if theme == "Dark Mode":
    
    st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #e0e0e0;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
    }
    .stFileUploader label {
        font-weight: bold;
        color: white;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 12px;
        transition-duration: 0.4s;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #45a049;
        color: white;
        transform: scale(1.05);
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)
    
else:
    st.markdown("""
    <style>
    .stApp {
        background-color:  #ADD8E6;
        color: #333;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
    }
    .stFileUploader label {
        font-weight: bold;
        color: #000000;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 12px;
        transition-duration: 0.4s;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #45a049;
        color: white;
        transform: scale(1.05);
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header with animation
lottie_resume = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_j1adxtyb.json")
if lottie_resume:
    st_lottie(lottie_resume, height=200, key="resume")

st.title("\U0001F4BC ATS Resume Parser")
st.markdown("#### Analyze, Improve & Evaluate your Resume with the power of Gemini AI")

# Input Section
input_text = st.text_area("\U0001F50D Optional Query (e.g., job description)", key="input")

uploaded_file = st.file_uploader("Upload your Resume in PDF format", type=["pdf"], key="pdf")
if uploaded_file is not None:
    st.success("\u2705 PDF submitted successfully!")

# Buttons with Columns
col1, col2, col3 = st.columns(3)

with col1:
    submit1 = st.button("\U0001F4CB Evaluate Resume")
with col2:
    submit2 = st.button("\U0001F4AA Improve My Skills")
with col3:
    submit3 = st.button("\U0001F4CA ATS Match %")

# Prompts
input_prompt1 = """You are experienced in the field of Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis. Your task is to review the provided resume against the job description. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the application in relation to the job specializations."""

input_prompt2 = """You are a Technical Human Resource Manager with expertise in Data Science. Your role is to scrutinize the resume in light of the provided job description. Share insights on the candidate's suitability for the role and offer advice on enhancing the candidate's skills."""

input_prompt3 = """Act like an ATS (Applicant Tracking System). Analyze how well this resume matches the job description provided. Give a percentage match and explain which keywords or skills are missing."""

# Response Logic
if submit1:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("\U0001F4DD Evaluation Result")
        st.success(response)
    else:
        st.warning("\u26A0\uFE0F Please upload the resume.")

elif submit2:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("\U0001F4AA Skill Suggestions")
        st.info(response)
    else:
        st.warning("\u26A0\uFE0F Please upload the resume.")

elif submit3:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("\U0001F4CA ATS Match Report")
        st.info(response)
    else:
        st.warning("\u26A0\uFE0F Please upload the resume.")











# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as genai
# from PIL import Image
# import pdf2image
# import io
# import base64
# import requests
# from streamlit_lottie import st_lottie

# # Load environment variables
# load_dotenv()

# # Configure API key securely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# if not GOOGLE_API_KEY:
#     st.error("GOOGLE_API_KEY not found in environment variables.")
#     st.stop()

# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-2.0-flash")

# def get_gemini_response(prompt, pdf_content, user_query):
#     response = model.generate_content([prompt, pdf_content[0], user_query])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read(), dpi=500)
#         first_page = images[0]

#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='PNG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/png",
#                 "data": base64.b64encode(img_byte_arr).decode('utf-8'),
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No PDF file uploaded.")

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # Page Configuration
# st.set_page_config(page_title="ATS Resume Checker", page_icon=":robot_face:", layout="wide")

# # Theme Toggle
# dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=False)

# # Custom CSS
# if dark_mode:
#     st.markdown("""
#     <style>
#     .stApp {
#         background-color: #121212;
#         color: #e0e0e0;
#     }
#     .stTextArea textarea {
#         background-color: #1e1e2f;
#         border-radius: 10px;
#         padding: 10px;
#         color: #e0e0e0;
#     }
#     .stFileUploader label {
#         font-weight: bold;
#         color: #ffffff;
#     }
#     .stButton button {
#         background-color: #4CAF50;
#         color: white;
#         padding: 10px 24px;
#         border: none;
#         border-radius: 12px;
#         transition-duration: 0.4s;
#         font-weight: bold;
#     }
#     .stButton button:hover {
#         background-color: #45a049;
#         color: white;
#         transform: scale(1.05);
#     }
#     .reportview-container .main .block-container {
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#     }
#     </style>
# """, unsafe_allow_html=True)
# else:
#     st.markdown("""
#     <style>
#     .stApp {
#         background-color: #f2f5f9;
#         color: #333;
#     }
#     .stTextArea textarea {
#         background-color: #ffffff;
#         border-radius: 10px;
#         padding: 10px;
#         color: #333;
#     }
#     .stFileUploader label {
#         font-weight: bold;
#         color: #000000;
#     }
#     .stButton button {
#         background-color: #4CAF50;
#         color: white;
#         padding: 10px 24px;
#         border: none;
#         border-radius: 12px;
#         transition-duration: 0.4s;
#         font-weight: bold;
#     }
#     .stButton button:hover {
#         background-color: #45a049;
#         color: white;
#         transform: scale(1.05);
#     }
#     .reportview-container .main .block-container {
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Header with animation
# lottie_resume = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_j1adxtyb.json")
# if lottie_resume:
#     st_lottie(lottie_resume, height=200, key="resume")

# st.title("\U0001F4BC ATS Resume Parser")
# st.markdown("#### Analyze, Improve & Evaluate your Resume with the power of Gemini AI")

# # Input Section
# input_text = st.text_area("\U0001F50D Optional Query (e.g., job description)", key="input")

# uploaded_file = st.file_uploader("Upload your Resume in PDF format", type=["pdf"], key="pdf")
# if uploaded_file is not None:
#     st.success("\u2705 PDF submitted successfully!")

# # Buttons with Columns
# col1, col2, col3 = st.columns(3)

# with col1:
#     submit1 = st.button("\U0001F4CB Evaluate Resume")
# with col2:
#     submit2 = st.button("\U0001F4AA Improve My Skills")
# with col3:
#     submit3 = st.button("\U0001F4CA ATS Match %")

# # Prompts
# input_prompt1 = """You are experienced in the field of Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis. Your task is to review the provided resume against the job description. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the application in relation to the job specializations."""

# input_prompt2 = """You are a Technical Human Resource Manager with expertise in Data Science. Your role is to scrutinize the resume in light of the provided job description. Share insights on the candidate's suitability for the role and offer advice on enhancing the candidate's skills."""

# input_prompt3 = """Act like an ATS (Applicant Tracking System). Analyze how well this resume matches the job description provided. Give a percentage match and explain which keywords or skills are missing."""

# # Response Logic
# if submit1:
#     if uploaded_file:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("\U0001F4DD Evaluation Result")
#         st.write(response)
#     else:
#         st.warning("\u26A0\uFE0F Please upload the resume.")

# elif submit2:
#     if uploaded_file:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt2, pdf_content, input_text)
#         st.subheader("\U0001F4AA Skill Suggestions")
#         st.write(response)
#     else:
#         st.warning("\u26A0\uFE0F Please upload the resume.")

# elif submit3:
#     if uploaded_file:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("\U0001F4CA ATS Match Report")
#         st.write(response)
#     else:
#         st.warning("\u26A0\uFE0F Please upload the resume.")
