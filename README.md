# IPL-Win-Predictor

IPL Win Predictor is a Machine Learning based web application that predicts the winning probability of IPL teams during a live match.  
The project uses historical IPL match data and calculates real-time winning chances based on match conditions such as target, score, wickets, overs, and current run rate.

---

## About The Project

This project was built to understand how Machine Learning can be applied in sports analytics.  
The model predicts the probability of the batting team winning the match during the second innings.

The application takes live match inputs and returns:

- Winning probability of the batting team
- Winning probability of the bowling team
- Match situation analysis based on current score and overs

The project is developed using Python, Pandas, Scikit-learn, and Streamlit.

---

## Features

- Real-time IPL win probability prediction
- Interactive and simple user interface
- Trained using historical IPL match data
- Machine Learning pipeline for prediction
- Supports multiple IPL teams and cities
- Fast prediction results

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## Machine Learning Workflow

1. Data Collection  
2. Data Cleaning and Preprocessing  
3. Feature Engineering  
4. Model Training  
5. Model Evaluation  
6. Model Deployment using Streamlit

---

## Input Parameters

The prediction depends on the following inputs:

- Batting Team
- Bowling Team
- Host City
- Target Score
- Current Score
- Overs Completed
- Wickets Out

---

## Project Structure

```bash
ipl-win-predictor/
│
├── app.py
├── pipe.pkl
├── final_processed_ipl_data.xls
├── requirements.txt
├── README.md
└── Pictures

## Live Demo

Website Link:  
https://ipl-win-predictor-ksohpwxgxghshankkt94gw.streamlit.app
