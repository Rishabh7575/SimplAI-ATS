# 📄 ATS Resume Checker

Welcome to the **ATS Resume Checker**! This web application leverages the power of **Gemini AI** to help job seekers analyze, improve, and evaluate their resumes against job descriptions. 

## 🚀 Features
- **Resume Evaluation**: Get professional insights on how well your resume aligns with specific job roles.
- **Skill Improvement Suggestions**: Receive tailored advice on enhancing your skills based on your resume and job descriptions.
- **ATS Match Percentage**: Understand how well your resume matches the requirements of the job description, including missing keywords.

## 🛠️ Technologies Used
- **[Streamlit](https://streamlit.io/)**: A powerful framework for building interactive web applications in Python.
- **[Google Generative AI](https://cloud.google.com/generative-ai)**: Utilized for generating intelligent content and feedback on resumes.
- **[Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)**: For image processing, specifically converting PDF pages into images.
- **[pdf2image](https://pdf2image.readthedocs.io/en/latest/)**: Converts PDF files into images for easy content extraction.
- **[dotenv](https://pypi.org/project/python-dotenv/)**: Manages environment variables securely, keeping sensitive information safe.
- **[Requests](https://docs.python-requests.org/en/latest/)**: Handles HTTP requests to fetch external resources.
- **[Streamlit Lottie](https://github.com/streamlit/streamlit-lottie)**: Integrates Lottie animations for a more engaging user experience.

## 📥 Installation
To get started with the ATS Resume Checker, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rishabh7575/SimplAI-ATS.git
   cd ats-resume-checker

   pip install -r requirements.txt

   GOOGLE_API_KEY=your_api_key_here(not mine dude)

   streamlit run app.py
   
