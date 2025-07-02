# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("AIzaSyDlRkxmCsIJ562nLZYAMU0WL7aQ1hRE8Qg"))  # Store key properly in .env or secrets
# model= genai.GenerativeModel("gemini-2.0-flash")
# chat = model.start_chat(history=[])

# def get_gemini_response(question):
#     response = chat.send_message(question,stream=True)
#     return response

# #initialize chat history

# st.set_page_config(page_title="Gemini Chatbot", page_icon=":robot:")
# st.header("Gemini Chatbot")

# #initialize chat session state

# if "chat_history" not in st.session_state:
#     st.session_state['chat_history'] = []

# # User input
# input = st.text_input("Input:", key="input")
# submit = st.button("Ask me")

# if submit and input:
#     response = get_gemini_response(input)
#     st.session_state['chat_history'].append({"user": input, "bot": response})      #...
#     st.subheader("response is")

#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append({"bot", chunk.text})

# st.subheader("Chat History is :")

# for role,text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")









# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st
# import os
# import google.generativeai as genai
# from streamlit_lottie import st_lottie
# import requests

# # Configure API key securely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# if not GOOGLE_API_KEY:
#     st.error("❌ GOOGLE_API_KEY not found in environment variables.")
#     st.stop()

# # Configure the Gemini API
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-2.0-flash")
# chat = model.start_chat(history=[])

# # Function to send message

# def get_gemini_response(question):
#     response = chat.send_message(question, stream=True)
#     return response

# # Load Lottie animation (for visual enhancement)
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # Set page config and styles
# st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")
# theme=st.selectbox("Select Theme", ["Light", "Dark"])

# dark_mode = st.toggle("🌙 Dark Mode")
# theme = "Dark Mode" if dark_mode else "Light Mode"

# # Dynamic theming based on user choice
# if theme == "Dark Mode":
#     st.markdown("""
#         <style>
#         .stApp {
#             background-color: #121212;
#             color: #e0e0e0;
#         }
#         .chat-bubble {
#             background-color: #4acc47;
#             color: #fff;
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#         }
#         .user-bubble {
#             background-color: #4ea7cf;
#             color: #fff;
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#         }
#         input, textarea {
#             background-color: #222 !important;
#             color: white !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
# else:
#     st.markdown("""
#         <style>
#         .stApp {
#             background-color: #f2f5f9;
#             color: #333;
#         }
#         .chat-bubble {
#             background-color: #4ea7cf;
#             color: #fff;
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#         }
#         .user-bubble {
#             background-color:  #4acc47;
#             color: #fff;
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#         }
#         </style>
#     """, unsafe_allow_html=True)


# st.title("Gemini Chatbot 🤖")
# st.markdown("Chat with Google's Gemini AI in a beautiful interface")

# # Display Lottie animation (optional)
# lottie_anim = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_touohxv0.json")
# if lottie_anim:
#     st_lottie(lottie_anim, height=200)

# # Initialize chat history in session
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Input box and button
# user_input = st.text_input("Ask something:", key="input")
# submit = st.button("🔍 Ask")

# # Handle user input
# if submit and user_input:
#     st.session_state.chat_history.append({"role": "user", "text": user_input})
#     with st.spinner("Thinking..."):
#         response = get_gemini_response(user_input)
#         full_response = ""
#         for chunk in response:
#             full_response += chunk.text
#         st.session_state.chat_history.append({"role": "bot", "text": full_response})

# # Display chat history
# st.subheader("💬 Chat History")
# for entry in st.session_state.chat_history:
#     if entry['role'] == "user":
#         st.markdown(f"<div class='user-bubble'><strong>👤 You:</strong> {entry['text']}</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(f"<div class='chat-bubble'><strong>🤖 Gemini:</strong> {entry['text']}</div>", unsafe_allow_html=True)
















import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure API key for google generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

APP_TITLE = "SimpleAi Co Services"
LOGO_TEXT = "SimpleAi"
THEME_LIGHT = "light"
THEME_DARK = "dark"


# Initialize session state variables
if "theme" not in st.session_state:
    st.session_state.theme = THEME_LIGHT

if "text_size" not in st.session_state:
    st.session_state.text_size = 18

if "page" not in st.session_state:
    st.session_state.page = "Ask AI"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

model = genai.GenerativeModel("gemini-2.0-flash")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def inject_css():
    css = f"""
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined');

    :root {{
      --font-family: 'Inter', sans-serif;

      --color-bg-light: #ffffff;
      --color-text-light: #374151;
      --color-text-muted-light: #6b7280;
      --color-primary-light: #4f46e5;
      --color-primary-hover-light: #4338ca;
      --color-card-bg-light: #f9fafb;
      --color-border-light: #e5e7eb;

      --color-bg-dark: #12121d;
      --color-text-dark: #e0e0e0;
      --color-text-muted-dark: #9ca3af;
      --color-primary-dark: #818cf8;
      --color-primary-hover-dark: #6366f1;
      --color-card-bg-dark: #1e1e2f;
      --color-border-dark: #3f3f56;

      --border-radius: 12px;
      --transition-speed: 0.3s;
      --box-shadow-light: 0 4px 10px rgba(0,0,0,0.05);
      --box-shadow-dark: 0 4px 10px rgba(0,0,0,0.8);
    }}

    html[data-theme="{THEME_LIGHT}"] {{
      background-color: var(--color-bg-light);
      color: var(--color-text-light);
      font-family: var(--font-family);
    }}

    html[data-theme="{THEME_DARK}"] {{
      background-color: var(--color-bg-dark);
      color: var(--color-text-dark);
      font-family: var(--font-family);
    }}

    .stApp {{
      background-color: transparent !important;
      color: inherit !important;
      font-family: var(--font-family) !important;
    }}

    div.stTextInput > div > div > input[type="text"] {{
      background-color: var(--color-bg-light);
      color: var(--color-text-light);
      border: 1.5px solid var(--color-border-light);
      border-radius: var(--border-radius);
      padding: 0.6rem 0.9rem;
      font-size: 1rem;
      transition: background-color var(--transition-speed), color var(--transition-speed);
      box-sizing: border-box;
    }}

    html[data-theme="{THEME_DARK}"] div.stTextInput > div > div > input[type="text"] {{
      background-color: var(--color-bg-dark);
      color: var(--color-text-dark);
      border: 1.5px solid var(--color-border-dark);
    }}

    .response-card {{
      background-color: var(--color-card-bg-light);
      color: var(--color-text-light);
      border-radius: var(--border-radius);
      padding: 1rem 1.5rem;
      box-shadow: var(--box-shadow-light);
      white-space: pre-wrap;
      word-wrap: break-word;
      margin-top: 1rem;
      font-size: {st.session_state.text_size}px;
      transition: background-color var(--transition-speed), color var(--transition-speed);
      border: 1px solid var(--color-border-light);
      user-select: text;
      animation: fadeIn 0.4s ease forwards;
    }}

    html[data-theme="{THEME_DARK}"] .response-card {{
      background-color: var(--color-card-bg-dark);
      color: var(--color-text-dark);
      box-shadow: var(--box-shadow-dark);
      border: 1px solid var(--color-border-dark);
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    header {{
      position: sticky;
      top: 0;
      z-index: 9999;
      background-color: var(--color-bg-light);
      color: var(--color-text-light);
      border-bottom: 1px solid var(--color-border-light);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1rem 2rem;
      font-weight: 800;
      font-size: 1.75rem;
      box-shadow: var(--box-shadow-light);
      transition: background-color var(--transition-speed), color var(--transition-speed);
    }}

    html[data-theme="{THEME_DARK}"] header {{
      background-color: var(--color-bg-dark);
      color: var(--color-text-dark);
      border-bottom: 1px solid var(--color-border-dark);
      box-shadow: var(--box-shadow-dark);
    }}

    .logo {{
      letter-spacing: 0.06em;
      user-select: none;
      cursor: default;
    }}

    nav.desktop-nav {{
      display: flex;
      gap: 1.5rem;
      align-items: center;
    }}

    nav.desktop-nav button {{
      background: none;
      border: none;
      color: inherit;
      font-weight: 600;
      cursor: pointer;
      font-size: 1.05rem;
      padding: 0.5rem 0.8rem;
      border-radius: var(--border-radius);
      transition: background-color var(--transition-speed), color var(--transition-speed);
    }}

    nav.desktop-nav button:hover,
    nav.desktop-nav button:focus {{
      background-color: var(--color-primary-light);
      color: white;
      outline: none;
    }}

    html[data-theme="{THEME_DARK}"] nav.desktop-nav button:hover,
    html[data-theme="{THEME_DARK}"] nav.desktop-nav button:focus {{
      background-color: var(--color-primary-dark);
      color: white;
    }}

    nav.desktop-nav button.active {{
      background-color: var(--color-primary-light);
      color: white;
      cursor: default;
    }}

    html[data-theme="{THEME_DARK}"] nav.desktop-nav button.active {{
      background-color: var(--color-primary-dark);
      color: white;
    }}

    .btn-primary {{
      background-color: var(--color-primary-light);
      border: none;
      color: white;
      padding: 0.75rem 1.8rem;
      border-radius: var(--border-radius);
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      transition: background-color var(--transition-speed), box-shadow var(--transition-speed);
      user-select: none;
      margin-top: 1rem;
    }}

    .btn-primary:hover,
    .btn-primary:focus {{
      background-color: var(--color-primary-hover-light);
      box-shadow: 0 8px 20px rgba(79, 70, 229, 0.55);
      outline: none;
    }}

    html[data-theme="{THEME_DARK}"] .btn-primary {{
      background-color: var(--color-primary-dark);
    }}

    html[data-theme="{THEME_DARK}"] .btn-primary:hover,
    html[data-theme="{THEME_DARK}"] .btn-primary:focus {{
      background-color: var(--color-primary-hover-dark);
      box-shadow: 0 8px 20px rgba(129, 140, 248, 0.5);
    }}

    main.content-area {{
      flex-grow: 1;
      padding: 2rem 2rem;
      display: grid;
      grid-template-columns: 1fr;
      gap: 2rem;
      max-width: 100%;
      min-height: calc(100vh - 88px - 60px);
    }}

    @media (min-width: 768px) {{
      main.content-area {{
        grid-template-columns: 280px 1fr;
        padding: 2rem 3rem;
      }}
    }}

    aside.sidebar {{
      background-color: var(--color-card-bg-light);
      border: 1px solid var(--color-border-light);
      border-radius: var(--border-radius);
      padding: 1rem;
      min-width: 280px;
      height: calc(100vh - 88px);
      position: sticky;
      top: 88px;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: var(--box-shadow-light);
    }}

    html[data-theme="{THEME_DARK}"] aside.sidebar {{
      background-color: var(--color-card-bg-dark);
      border: 1px solid var(--color-border-dark);
      box-shadow: var(--box-shadow-dark);
    }}

    aside.sidebar button {{
      background-color: transparent;
      border: none;
      color: inherit;
      padding: 0.6rem 1rem;
      border-radius: var(--border-radius);
      text-align: left;
      font-weight: 600;
      cursor: pointer;
      transition: background-color var(--transition-speed);
      font-size: 1rem;
    }}

    aside.sidebar button:hover,
    aside.sidebar button:focus {{
      background-color: var(--color-primary-light);
      color: white;
      outline: none;
    }}

    html[data-theme="{THEME_DARK}"] aside.sidebar button:hover,
    html[data-theme="{THEME_DARK}"] aside.sidebar button:focus {{
      background-color: var(--color-primary-dark);
      color: white;
    }}

    aside.sidebar button.active {{
      background-color: var(--color-primary-light);
      color: white;
      cursor: default;
    }}

    html[data-theme="{THEME_DARK}"] aside.sidebar button.active {{
      background-color: var(--color-primary-dark);
      color: white;
    }}

    footer {{
      text-align: center;
      padding: 1rem 0;
      font-size: 0.875rem;
      color: var(--color-text-muted-light);
      border-top: 1px solid var(--color-border-light);
      margin-top: auto;
      transition: border-color var(--transition-speed), color var(--transition-speed);
    }}

    html[data-theme="{THEME_DARK}"] footer {{
      color: var(--color-text-muted-dark);
      border-color: var(--color-border-dark);
    }}

    /* News feed grid and cards */

    .news-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }}

    @media (min-width: 641px) {{
      .news-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    @media (min-width: 1024px) {{
      .news-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
    }}

    .news-card {{
      background-color: var(--color-card-bg-light);
      border-radius: var(--border-radius);
      box-shadow: var(--box-shadow-light);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform var(--transition-speed), box-shadow var(--transition-speed);
      cursor: pointer;
      user-select: none;
    }}

    html[data-theme="{THEME_DARK}"] .news-card {{
      background-color: var(--color-card-bg-dark);
      box-shadow: var(--box-shadow-dark);
    }}

    .news-card:hover,
    .news-card:focus {{
      transform: translateY(-6px);
      box-shadow: 0 10px 30px var(--color-primary-light);
      outline: none;
    }}

    html[data-theme="{THEME_DARK}"] .news-card:hover,
    html[data-theme="{THEME_DARK}"] .news-card:focus {{
      box-shadow: 0 10px 30px var(--color-primary-dark);
    }}

    .news-card img {{
      width: 100%;
      height: auto;
      aspect-ratio: 4 / 3;
      object-fit: cover;
      border-bottom: 1px solid var(--color-border-light);
    }}

    html[data-theme="{THEME_DARK}"] .news-card img {{
      border-bottom: 1px solid var(--color-border-dark);
    }}

    .news-card .content {{
      padding: 1rem 1.25rem;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }}

    .news-card h3 {{
      margin-top: 0;
      margin-bottom: 0.5rem;
      font-size: 1.125rem;
      font-weight: 700;
      color: var(--color-text-light);
      transition: color var(--transition-speed);
    }}

    html[data-theme="{THEME_DARK}"] .news-card h3 {{
      color: var(--color-text-dark);
    }}

    .news-card p {{
      color: var(--color-text-muted-light);
      font-size: 0.95rem;
      flex-grow: 1;
      margin-bottom: 0.5rem;
      transition: color var(--transition-speed);
    }}

    html[data-theme="{THEME_DARK}"] .news-card p {{
      color: var(--color-text-muted-dark);
    }}

    /* Read more link styling */
    .read-more-link {{
      color: var(--color-primary-light);
      font-weight: 600;
      text-decoration: none;
      transition: color 0.3s ease, text-decoration 0.3s ease;
      cursor: pointer;
      align-self: flex-start;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      user-select: none;
    }}

    .read-more-link:hover,
    .read-more-link:focus {{
      text-decoration: underline;
      color: var(--color-primary-hover-light);
      outline: none;
    }}

    html[data-theme="{THEME_DARK}"] .read-more-link {{
      color: var(--color-primary-dark);
    }}

    html[data-theme="{THEME_DARK}"] .read-more-link:hover,
    html[data-theme="{THEME_DARK}"] .read-more-link:focus {{
      color: var(--color-primary-hover-dark);
    }}

    .material-icons-outlined.read-more-icon {{
      font-size: 16px;
      margin-left: 2px;
      user-select: none;
    }}
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def toggle_theme():
    st.session_state.theme = THEME_DARK if st.session_state.theme == THEME_LIGHT else THEME_LIGHT
    st.experimental_rerun()

def increase_text_size():
    if st.session_state.text_size < 24:
        st.session_state.text_size += 2

def decrease_text_size():
    if st.session_state.text_size > 14:
        st.session_state.text_size -= 2

def render_header():
    st.markdown(
        f"""
        <header>
          <div class="logo">{LOGO_TEXT}</div>
        </header>
        """,
        unsafe_allow_html=True,
    )

def render_ask_ai():
    st.subheader("Ask AI - Gemini powered Q&A")
    prompt = st.text_input("Your Query", key="input", placeholder="Type your question here...")
    submit = st.button("Ask SimpleAi")
    if submit and prompt.strip():
        with st.spinner("Generating response..."):
            resp_text = get_gemini_response(prompt.strip())
            st.markdown(f'<div class="response-card fade-in">{resp_text}</div>', unsafe_allow_html=True)

def render_news_feed():
    st.subheader("News Feed - Aggregated Articles")
    st.markdown(
        f'<p style="font-size: {st.session_state.text_size}px; color: var(--color-text-muted-light); margin-bottom: 1rem;">Showing a curated set of news articles for you. (Example static demo)</p>',
        unsafe_allow_html=True
    )
    articles = [
        {
            "title": "AI Revolutionizes Healthcare Industry",
            "summary": "Cutting-edge AI solutions are improving diagnostics, treatments, and patient care worldwide.",
            "image": "https://placehold.co/600x400/png?text=AI+Healthcare+Innovation",
            "url": "#"
        },
        {
            "title": "New Breakthroughs in Renewable Energy",
            "summary": "Scientists announce advancements in solar and wind technology with higher efficiency.",
            "image": "https://placehold.co/600x400/png?text=Renewable+Energy",
            "url": "#"
        },
        {
            "title": "Tech Giants Invest in Quantum Computing",
            "summary": "Major companies are accelerating research to build practical quantum computers.",
            "image": "https://placehold.co/600x400/png?text=Quantum+Computing",
            "url": "#"
        }
    ]
    st.markdown('<div class="news-grid">', unsafe_allow_html=True)
    for article in articles:
        st.markdown(
            f"""
            <article tabindex="0" class="news-card" role="article" aria-label="{article['title']}">
                <img src="{article['image']}" alt="{article['title']} image" loading="lazy" />
                <div class="content" style="font-size: {st.session_state.text_size}px;">
                    <h3>{article['title']}</h3>
                    <p>{article['summary']}</p>
                    <a href="{article['url']}" class="read-more-link" aria-label="Read more about {article['title']}" target="_blank" rel="noopener noreferrer">
                        Read more
                        <span class="material-icons-outlined read-more-icon" aria-hidden="true">arrow_forward</span>
                    </a>
                </div>
            </article>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

def render_settings():
    st.subheader("Settings")
    st.markdown("### Theme")
    current_theme = st.session_state.theme
    new_theme = st.radio(
        "Select Theme",
        options=[THEME_LIGHT.capitalize(), THEME_DARK.capitalize()],
        index=0 if current_theme == THEME_LIGHT else 1,
        horizontal=True,
        key="theme_radio"
    )
    if new_theme.lower() != current_theme:
        toggle_theme()
    st.markdown("### Text Size")
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("A-", key="decrease-text"):
            decrease_text_size()
    with col2:
        st.markdown(f'<p style="text-align:center; font-size: {st.session_state.text_size}px; margin:0;">{st.session_state.text_size}px</p>', unsafe_allow_html=True)
    with col3:
        if st.button("A+", key="increase-text"):
            increase_text_size()

def main():
    inject_css()

    page = st.sidebar.radio(
        "Navigation",
        options=["Ask AI", "News Feed", "Settings"],
        index=["Ask AI", "News Feed", "Settings"].index(st.session_state.page)
    )
    st.session_state.page = page

    st.markdown(
        f"""
        <script>
        (function() {{
          const theme = "{st.session_state.theme}";
          document.documentElement.setAttribute('data-theme', theme);
        }})();
        </script>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    render_header()

    if page == "Ask AI":
        render_ask_ai()
    elif page == "News Feed":
        render_news_feed()
    else:
        render_settings()

    st.markdown(
        """
        <footer>
          &copy; 2025 SimpleAi Co - All Rights Reserved
        </footer>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()    
