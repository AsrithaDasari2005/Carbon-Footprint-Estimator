import streamlit as st
from streamlit_player import st_player

st.title("Tips")
st.write("REDUCE AND UNDERSTAND CARBON FOOTPRINTS")
st.write("Click the below links to learn about sustainable living")
st.markdown("https://www.youtube.com/@Shwetakataria_/featured")
st.markdown('https://www.youtube.com/@GoingZeroWaste')
st_player('https://youtu.be/2CS_ndHkEnw?feature=shared')
st_player('https://youtu.be/du7LWt2ZiK0?feature=shared')
st_player('https://youtu.be/tCsJ7mD_fQ0?feature=shared')
st_player('https://youtu.be/JAyuHIthHco?feature=shared')
st_player('https://youtu.be/QysiRwibglg?feature=shared')

# Style for main block
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
    </style>
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
