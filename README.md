AI-powered CRM system for Healthcare Field Representatives to manage HCP (Doctor) interactions, built using FastAPI, LangGraph, PostgreSQL, and React.

The system allows logging interactions, editing follow-ups, fetching doctor profiles, and generating AI-based insights.

⚙️ Tech Stack

Backend:

FastAPI
LangGraph
LangChain
Groq LLM
PostgreSQL

Frontend:

React.js
Axios
🧠 Features
Log doctor/HCP interactions
Edit follow-up dates
Fetch HCP profiles
Generate interaction summaries
AI-based next best action suggestions
Chat-based CRM interface
🗄️ Database Tables
HCP Table
id
name
specialty
hospital
city
Interactions Table
id
hcp_id
date
interaction_type
products_discussed
summary
follow_up_date
created_at
⚙️ Backend Setup
pip install fastapi uvicorn langgraph langchain groq psycopg2-binary python-dotenv

Run server:

uvicorn main:app --reload

API Docs:

http://127.0.0.1:8000/docs
🌐 Frontend Setup
npm install
npm install axios react-router-dom
npm start

Frontend runs at:

http://localhost:3000
🔗 API Flow

Frontend → FastAPI Backend → LangGraph AI Agent → PostgreSQL → Response → UI

💬 Sample Input
log interaction with doctor
Output:
Interaction logged successfully
🔐 Environment Variables

Create .env file:

GROQ_API_KEY=your_api_key
DB_URL=postgresql://postgres:postgres@localhost:5432/crm_db
📌 Project Status

✔ Completed for Naukri Round 1 Assignment
✔ Backend + AI Agent integrated
✔ Frontend connected with API

👨‍💻 Author

Developed as part of AI CRM Assignment Project
