import streamlit as st
from PIL import Image

st.set_page_config(page_title="Aniket Kundal | Portfolio", page_icon="", layout="wide")

# Hero Section
st.markdown("""
    <div style='text-align: center; padding: 4rem 1rem; background: linear-gradient(to bottom right, #6366f1, #3b82f6); color: white; border-radius: 20px;'>
        <img src='https://pbs.twimg.com/profile_images/1911448532260626432/vy2fcfzH_400x400.jpg' style='width: 160px; height: 160px; border-radius: 50%; border: 4px solid white; box-shadow: 0 0 20px rgba(0,0,0,0.2); animation: fadeIn 2s;'>
        <h1 style='font-size: 3rem; margin-top: 1rem;'>Hi, I'm <span style='color: #ffe600;'>Aniket Kundal</span></h1>
        <p style='font-size: 1.3rem;'>B.Tech CSE Student | Aspiring Software Developer</p>
    </div>

    <style>
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .project-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        padding: 20px;
        margin: 10px 0;
        background-color: #f9fafb;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        animation: fadeIn 1.5s;
        text-align: center;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    }
    .social-tile {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        padding: 20px;
        background-color: #f9fafb;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        animation: fadeIn 1.5s;
    }
    .social-tile:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# About Section
st.header("About Me")
st.write("""
I'm a Second-year Computer Science Engineering student passionate about building impactful software solutions.  
I enjoy web development, solving DSA problems, and exploring the world of AI/ML.
""")

# Skills Section
st.header("Skills")
skills = ["Python", "C", "C++", "Java", "DSA", "MySQL", "HTML", "CSS", "JavaScript"]
cols = st.columns(len(skills))
for i, skill in enumerate(skills):
    with cols[i]:
        st.markdown(f"<div style='padding: 8px 16px; background-color: #e0e7ff; color: #3730a3; border-radius: 20px; text-align: center; font-weight: 500; animation: fadeIn 1s;'>{skill}</div>", unsafe_allow_html=True)

# Projects Section
st.header("Projects")
project_data = {
    "Spotify Analysis": {
        
        "desc": "Analyzed user streaming patterns with Python and Matplotlib.",
        "link": "https://github.com/Aniketkundal9172/Analyzing-Spotify-Streaming-Patterns-User-Behavior"
        
    },
    "Secure Auth Module": {
        "desc": "C++ & DSA-based inventory system with live stock tracking.",
        "link": "https://github.com/Aniketkundal9172/Secure-Secure-Authentication-Module"
    },
    "AI Marketing Assistant": {
        "desc": "Coming Soon...",
        "link": "#"
    }
}

for title, content in project_data.items():
    with st.container():
        st.markdown(f"""
            <a href="{content['link']}" target="_blank" style="text-decoration: none;">
                <div class="project-card" style='background-color: #f9fafb; padding: 20px; margin: 10px 0; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); animation: fadeIn 1.5s;'>
                    <h3 style='color: #1e3a8a;'>{title}</h3>
                    <p style='color: #111827;'>{content['desc']}</p>
                </div>
            </a>
        """, unsafe_allow_html=True)

# Connect with Me Section (Moved to last)
st.header("Connect with Me")

# Create 3 columns for the social media links
cols = st.columns(3)

# LinkedIn
with cols[0]:
    st.markdown("""
        <a href="https://www.linkedin.com/in/aniket-kundal/" target="_blank">
            <div class="social-tile">
                <img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" style="width: 50px; height: 50px;">
                <h3 style="color: #1e3a8a; margin-top: 10px;">LinkedIn</h3>
            </div>
        </a>
    """, unsafe_allow_html=True)

# GitHub
with cols[1]:
    st.markdown("""
        <a href="https://github.com/Aniketkundal9172" target="_blank">
            <div class="social-tile">
                <img src="https://img.icons8.com/ios_filled/512/github.png" style="width: 50px; height: 50px;">
                <h3 style="color: #1e3a8a; margin-top: 10px;">GitHub</h3>
            </div>
        </a>
    """, unsafe_allow_html=True)

# Twitter
with cols[2]:
    st.markdown("""
        <a href="https://x.com/aniket_kun80983" target="_blank">
            <div class="social-tile">
                <img src="https://static.vecteezy.com/system/resources/previews/042/148/611/non_2x/new-twitter-x-logo-twitter-icon-x-social-media-icon-free-png.png" style="width: 50px; height: 50px;">
                <h3 style="color: #1e3a8a; margin-top: 10px;">Twitter</h3>
            </div>
        </a>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr />
    <p style='text-align: center; color: gray;'>© 2025 Aniket Kundal | Built with ❤️ using Python & Streamlit</p>
""", unsafe_allow_html=True)
