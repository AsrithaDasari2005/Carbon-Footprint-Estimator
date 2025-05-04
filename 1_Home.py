import streamlit as st  # type: ignore

st.set_page_config(layout="wide", page_title="Carbon Footprint Estimator")
st.title("Carbon Footprint Estimator 🌱")

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
    .stButton > button {
        background-color: #66bb6a;
        color: white;
        border: none;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #81c784;
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

# Emission factors database
EMISSION_FACTORS = {
    "India": {
        "energy_consumption": {
            # Carbon footprint generation types
            # Type 1: Electricity
            "electricity": {
                "solar": 0.041,  # kg CO2/kWh (solar energy)
                "coal": 1.050,   # kg CO2/kWh (coal energy)
                "hydro": 0.024,  # kg CO2/kWh (hydropower energy)
            },
            # Type 2: Transportation
            "transportation": {
                "bus": 0.068,    # kg CO2/passenger-km (bus)
                "bike": 0.103,   # kg CO2/km (bike)
                "car": 0.192,    # kg CO2/km (car)
                "walk_cycle": 0, # kg CO2/km (walking or cycling)
            },
            # Type 3: Diet
            "diet": {
                "red_meat": 27.0,    # kg CO2e/kg food (red meat)
                "white_meat": 6.9,   # kg CO2e/kg food (white meat: chicken, fish, etc.)
                "Vegetarian": 2.5,   # kg CO2e/kg food (vegetarian diet)
            }
        },
        # Waste Production Types
        "waste_production": {
            "wet_waste": 0.614,  # kg CO2e/kg waste (food/organic waste)
            "plastic_waste": 2.50,  # kg CO2e/kg waste (plastic waste)
            "paper_waste": 1.10,  # kg CO2e/kg waste (paper waste)
        }
    }
}

col1, col2 = st.columns(2)

with col1:
    st.header("Energy Consumption")
    
    # Electricity
    electricity_options = ["solar", "coal", "hydro"]
    selected_electricity = st.selectbox("Your electricity consumption mode", electricity_options)
    st.subheader("Monthly electricity consumption (in kWh)")
    monthly_kwh = st.slider("", 0, 1000, key="electricity_input")
    co2_electricity = round((monthly_kwh / 30) * EMISSION_FACTORS["India"]["energy_consumption"]["electricity"][selected_electricity], 2)

    # Transportation
    transportation_options = ["bike", "car", "bus", "walk_cycle"]
    selected_transport = st.selectbox("Your transport mode", transportation_options)
    st.subheader("Today distance travelled (in km)")
    distance = st.slider("", 0, 100, key="distance_input")
    co2_transportion = round(distance * EMISSION_FACTORS["India"]["energy_consumption"]["transportation"][selected_transport], 2)

    # Diet
    diet_options = {"Vegetarian": "Vegetarian", "white_meat": "White meat", "red_meat": "Red meat"}
    selected_diet = st.selectbox("Your Dietary Preference", diet_options)
    st.subheader("No of meals you ate")
    meals = st.slider("", 0, 6, key="meals_input")
    co2_diet = round(meals * EMISSION_FACTORS["India"]["energy_consumption"]["diet"][selected_diet], 2)

with col2:
    st.header("Waste Production")

    # Wet waste
    st.subheader("Wet waste generated (in kgs)")
    wet = st.slider("", 0.0, 20.0, key="wet_input")
    co2_wet = round(wet * EMISSION_FACTORS["India"]["waste_production"]["wet_waste"], 2)

    # Plastic waste
    st.subheader("Plastic waste generated (in kgs)")
    plastic = st.slider("", 0.0, 20.0, key="plastic_input")
    co2_plastic = round(plastic * EMISSION_FACTORS["India"]["waste_production"]["plastic_waste"], 2)

    # Paper waste
    st.subheader("Paper waste generated (in kgs)")
    paper = st.slider("", 0.0, 20.0, key="paper_input")
    co2_paper = round(paper * EMISSION_FACTORS["India"]["waste_production"]["paper_waste"], 2)

if st.button("Calculate Carbon Footprint"):
    st.header("Results")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("By Energy Consumption")
        st.info(f"Electricity: {co2_electricity} kg/day")
        st.info(f"Transportation: {co2_transportion} kg/day")
        st.info(f"Diet: {co2_diet} kg/day")

    with col4:
        st.subheader("By Waste Production")
        st.info(f"Wet waste: {co2_wet} kg/day")
        st.info(f"Plastic waste: {co2_plastic} kg/day")
        st.info(f"Paper waste: {co2_paper} kg/day")

    total_footprint = round(
        co2_electricity + co2_transportion + co2_diet + co2_wet + co2_plastic + co2_paper, 2)
    
    st.markdown("---")
    st.subheader("🌍 Total Carbon Footprint")
    st.success(f"{total_footprint} kg/day")

    if total_footprint < 3:
        st.write("🟢 Excellent", "Amazing! You're living a very eco-friendly life.")
    elif total_footprint < 6:
        st.write(" Very Good", "Great job! You’re doing better than most people.")
    elif total_footprint < 9:
        st.write("🟡 It's OK, You're on the right track. A few small changes can help even more.")
    elif total_footprint < 15:
        st.write("🟡 The current situation is not good need to make lifestyle changes")
    else:
        st.write("🔴 You need to include lot of major lifestyle change since lot of damage is already done")
