# ipl-win-predictor
A simple and interactive Machine Learning project that predicts the winning probability of IPL teams during a live match.
This project is built using historical IPL match data and provides real-time win probability predictions based on the current match situation like score, wickets, overs, target, run rate, etc.
📌 About The Project
Cricket fans often wonder:
“Which team is winning right now?”
This project tries to answer that question using Machine Learning.
The model analyzes previous IPL match data and predicts the chances of both teams winning during the second innings of a match.
🚀 Features
Predicts live winning probability
User-friendly Streamlit interface
Real-time match analysis
Uses historical IPL data
Simple and clean UI
Machine Learning based prediction system
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
📂 Dataset
The project uses two IPL datasets:
matches.csv
Contains:
Teams
Winners
Match venue
Toss details
Match results
deliveries.csv
Contains:
Ball-by-ball information
Runs scored
Wickets
Overs data
⚙️ How It Works
The model takes inputs such as:
Batting Team
Bowling Team
City
Target Score
Current Score
Overs Completed
Wickets Lost
Then it calculates:
Runs Left
Balls Left
Required Run Rate
Current Run Rate
Finally, the ML model predicts:
Winning probability of batting team
Winning probability of bowling teamIPL Match Winner Prediction using Machine Learning and Ensemble Learning
https://ipl-win-predictor-ksohpwxgxghshankkt94gw.streamlit.app/
