Sentiment Mode Analyzer API 

A sentiment analysis application built with FastAPI and Streamlit that analyzes text sentiment and returns the overall mode sentiment.

Project Overview

This project provides:
•	RESTful API using FastAPI
•	Text sentiment analysis using TextBlob
•	Input validation with Pydantic
•	Unit testing with Pytest
•	Interactive frontend dashboard using Streamlit
•	Deployment-ready configuration

Architecture

User → Streamlit Dashboard → FastAPI Backend → Sentiment Model → JSON Response

Technologies Used

•	FastAPI
•	Uvicorn
•	TextBlob
•	Streamlit
•	Pytest
•	Requests

Installation

git clone <your-repo-url>
cd sentiment-mode-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Run Backend

uvicorn app.main:app --reload

API Docs:

http://127.0.0.1:8000/docs


Run Streamlit Dashboard

streamlit run streamlit_app.py


 Run Unit Tests
 
 pytest -v

 API Endpoint
 
POST /analyze
Request:
{
  "texts": ["I love coding", "This is bad"]
}
Response:
{
  "results": [...],
  "mode": "Positive"
}

 Deployment
 
Backend deployed on Render
Frontend deployed on Streamlit Cloud


Learning Outcomes

•	API design
•	Data validation
•	Error handling
•	Unit testing
•	Frontend-backend integration
•	Deployment

