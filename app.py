import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="IPL Win Predictor",
    page_icon="🏏",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return pickle.load(open('pipe.pkl', 'rb'))

model = load_model()

# ---------------- TEAMS ----------------
teams = sorted([
    'Chennai Super Kings',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Delhi Capitals',
    'Sunrisers Hyderabad',
    'Rajasthan Royals',
    'Punjab Kings',
    'Lucknow Super Giants',
    'Gujarat Titans'
])

# ---------------- CITIES ----------------
cities = sorted([
    'Mumbai',
    'Chennai',
    'Kolkata',
    'Delhi',
    'Bangalore',
    'Hyderabad',
    'Ahmedabad',
    'Jaipur',
    'Chandigarh',
    'Pune',
    'Visakhapatnam',
    'Navi Mumbai',
    'Dharamsala',
    'Ranchi',
    'Nagpur',
    'Cuttack',
    'Raipur'
])

# ---------------- TITLE ----------------
st.title("🏏 IPL Win Predictor")

# ---------------- TEAM SELECTION ----------------
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        "Select the batting team",
        teams
    )

with col2:
    bowling_options = [
        team for team in teams
        if team != batting_team
    ]

    bowling_team = st.selectbox(
        "Select the bowling team",
        bowling_options
    )

# ---------------- CITY ----------------
city = st.selectbox(
    "Select host city",
    cities
)

# ---------------- TARGET ----------------
target = st.number_input(
    "Target",
    min_value=1,
    max_value=300,
    value=180
)

# ---------------- MATCH DETAILS ----------------
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input(
        "Score",
        min_value=0,
        max_value=300,
        value=80
    )

with col4:
    overs = st.number_input(
        "Overs completed",
        min_value=0.1,
        max_value=20.0,
        value=10.0,
        step=0.1
    )

with col5:
    wickets_out = st.number_input(
        "Wickets out",
        min_value=0,
        max_value=10,
        value=2
    )

# ---------------- PREDICT BUTTON ----------------
if st.button("Predict Probability"):

    # Validation
    if batting_team == bowling_team:
        st.error(
            "Batting and Bowling team can't be same!"
        )

    elif score > target:
        st.error(
            "Score cannot be greater than target!"
        )

    else:

        # Calculate values automatically
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets_left = 10 - wickets_out

        # Avoid division by zero
        if overs == 0:
            crr = 0
        else:
            crr = score / overs

        if balls_left == 0:
            rrr = 0
        else:
            rrr = (runs_left * 6) / balls_left

        # Create dataframe
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'target_runs': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Prediction probability
        result = model.predict_proba(input_df)

        batting_team_prob = round(
            result[0][1] * 100,
            2
        )

        bowling_team_prob = round(
            result[0][0] * 100,
            2
        )

        # ---------------- RESULT ----------------
        st.subheader("Prediction Result")

        st.success(
            f"{batting_team} Winning Probability: "
            f"{batting_team_prob}%"
        )

        st.error(
            f"{bowling_team} Winning Probability: "
            f"{bowling_team_prob}%"
        )

        # Winner
        if batting_team_prob > bowling_team_prob:
            st.balloons()
            st.success(
                f"🏆 {batting_team} is more likely to WIN!"
            )
        else:
            st.success(
                f"🏆 {bowling_team} is more likely to WIN!"
            )

        # Match stats
        st.write("### Match Situation")

        st.write(f"Runs Left: {runs_left}")
        st.write(f"Balls Left: {balls_left}")
        st.write(f"Wickets Left: {wickets_left}")
        st.write(f"Current Run Rate: {round(crr,2)}")
        st.write(f"Required Run Rate: {round(rrr,2)}")