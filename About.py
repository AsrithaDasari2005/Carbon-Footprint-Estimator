import streamlit as st

st.set_page_config(page_title="About Us", layout="wide")

st.title("About Us")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        color: #ffffff;
    }
    .block-container {
        background-color: rgba(0, 100, 0, 0.4);
        padding: 2rem;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #e6ffe6;
    }
    .about-section {
        background-color: rgba(0, 100, 0, 0.4);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: justify;
    }
    .mission-section {
        background-color: rgba(0, 100, 0, 0.4);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: justify;
    }
    .team-section {
        background-color: rgba(0, 100, 0, 0.4);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .team-member {
        margin-bottom: 1rem;
        text-align: center;
    }
    .team-member img {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="about-section">
        <h2>Our Mission</h2>
        <p>
            Our mission is to empower individuals to understand and reduce their carbon footprint. We believe that by providing clear,
            actionable information, we can help people make more sustainable choices in their daily lives and contribute to a healthier planet.
            We aim to make carbon footprint calculation accessible and easy to understand for everyone.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="mission-section">
        <h2>Our Goal</h2>
        <p>
            We aim to provide a user-friendly tool that calculates your daily carbon emissions, giving you a starting point for reducing your impact.
            We want to encourage eco-friendly practices and help users visualize how their choices affect the environment.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="team-section">
        <h2>Meet the Developer</h2>
        <div class="row">
            <div class="col-md-4 team-member">
                <h4>Asritha</h4>
                <p>Lead Developer</p>
                <a href="https://www.linkedin.com/in/asrithadasari">LinkedIn</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Style for the sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-image: linear-gradient(#2e7d32, #388e3c);
        color: white;
    }
    [data-testid="stSidebar"] div {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
