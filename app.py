import streamlit as st
from PIL import Image
from streamlit.components.v1 import html

# Page config
st.set_page_config(page_title="Hyma Reddy", page_icon="💼", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            font-size: 1.5em;
            color: #16a085;
        }
        .section-title {
            font-size: 1.3em;
            margin-top: 30px;
            margin-bottom: 10px;
            color: #2980b9;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            margin-top: 50px;
            color: #95a5a6;
        }
        .card {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Info
st.sidebar.image("my_photo.jpg", width=150)
st.sidebar.title("Hyma Reddy")
st.sidebar.markdown("**Role:** Student")
st.sidebar.markdown("📍 Visakhapatnam, India")
st.sidebar.markdown("📫 [Email](mailto:hymareddy8332@gmail.com)")
st.sidebar.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/hyma-reddy-b696ba294/)")
st.sidebar.markdown("🐙 [GitHub](https://github.com/hyma8332)")

# Main content
st.markdown("<div class='main-title'>Hello, I'm Hyma Reddy</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Student | Data Science | AI/ML Enthusiast</div>", unsafe_allow_html=True)

st.markdown("""<div class='section-title'>🧑‍💼 About Me</div>
Highly motivated and curious Computer Science (AI & ML) graduate passionate about applying machine
learning to real-world challenges. Seeking a Data Scientist Internship at a reputed organization to
contribute to impactful ML projects while gaining experience in model development, evaluation, and
experimentation. Eager to explore Generative AI applications in a collaborative environment

<div class='section-title'>🧠 Skills</div>""", unsafe_allow_html=True)
st.markdown("""
- **Languages:** Python, SQL, C
- **ML Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Transformers
- **Concepts:** Regression, Classification, Clustering, NLP, Generative AI (basic), Feature Engineering
- **Tools:** GitHub, Jupyter Notebook, VS Code
- **Databases:** MySQL
- **Cloud & DevOps:** AWS (EC2, S3)
- **Soft Skills:** Analytical Thinking, Team Collaboration, Rapid Learning
""")

st.markdown("<div class='section-title'>💼 Experience</div>", unsafe_allow_html=True)
st.markdown("""
**Intern** – RINL Visakhapatnam (May 2024 - June 2024)  
- Built a Random Forest Regressor model to analyze blast furnace parameters.
- Identified critical values affecting furnace performance using real-time manufacturing data. 
- Applied optimization techniques and evaluated performance using MSE.
**Intern** - Growth Ninja (July 2023 - September 2023)
- Developed an Article Recommendation System using NLP techniques.
- Processed and modeled text data to deliver relevant article suggestions.
- Gained experience in multi-tier application design and system integration.
""")


st.markdown("<div class='section-title'>📂 Projects</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
    <b>Image Captioning with Advanced Techniques</b><br>
    ● Designed a deep learning-based image captioning system using the BLIP (Bootstrapped Language-Image Pretraining) model.
    ● Integrated computer vision and NLP to generate accurate textual descriptions of uploaded or captured images.
    ● Enhanced accessibility with Text-to-Speech (TTS) features and keyword extraction for retrieving related Wikipedia and Google results.

    
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <b>Article Recommendation System</b><br>
    ● Developed a content-based article recommendation engine using TF-IDF and cosine similarity.
    ● Processed user preferences and article metadata to deliver personalized suggestions.

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <b>Predicting Critical Parameters of Blast Furnace</b><br>
    ● Modeled a regression problem using Random Forest on industrial blast furnace data.
    ● Identified and analyzed critical process parameters using Mean Squared Error as the performance metric.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <b>Portfolio</b><br>
    Built a website to show my portfolio
    </div>
    """, unsafe_allow_html=True)

st.markdown("### 📄 Resume")
resume_url = "https://drive.google.com/uc?export=download&id=1X21TzmCbiu_tOLYz0Qz6zKXhXB_atcBZ"
st.markdown(f"[👉 Download My Resume (PDF)]({resume_url})", unsafe_allow_html=True)

st.markdown("<div class='section-title'>📞 Contact</div>", unsafe_allow_html=True)
st.markdown("""
- Email: hymareddy8332@gmail.com
- LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/hyma-reddy-b696ba294/)
- GitHub: [github.com/yourprofile](https://github.com/hyma8332)
""")

st.markdown("<div class='footer'>© 2025 Hyma Reddy | Powered by Streamlit</div>", unsafe_allow_html=True)