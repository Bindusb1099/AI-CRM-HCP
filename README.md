AI-powered CRM system for Healthcare Field Representatives to manage HCP (Doctor) interactions using FastAPI, LangGraph, Groq LLM, PostgreSQL, and React.

The system uses a LangGraph-based AI agent workflow combined with an LLM (Groq - Gemma2) to intelligently route user requests, generate insights, and assist in decision-making.

⚙️ Tech Stack
Backend
FastAPI
LangGraph (State-based AI workflow)
LangChain
Groq LLM (Gemma2-9B)
PostgreSQL
Frontend
React.js
Axios
React Router
🧠 LangGraph + LLM Architecture

The AI system is built using a LangGraph StateGraph workflow:

User Input
   ↓
Intent Detection Node
   ↓
Tool Router Node
   ↓
┌────────────────────────────┐
│  Either:                  │
│  • CRM Tools              │
│  • OR LLM (Groq AI)      │
└────────────────────────────┘
   ↓
Final Response
🔹 LangGraph Nodes:
detect_intent → Classifies user request
run_tool → Executes CRM tools or LLM fallback
🔹 LLM Usage:
Groq Chat Model (Gemma2-9B)
Used for natural language responses when no tool matches
Provides AI-based CRM insights
🗄️ Database Schema
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

Frontend:

http://localhost:3000

🔗 System Flow
Frontend → FastAPI → LangGraph Agent → LLM / Tools → PostgreSQL → Response → UI
💬 Features

✔ Log HCP interactions
✔ Edit follow-ups
✔ Fetch doctor profiles
✔ AI-generated summaries
✔ Next best action suggestions
✔ Chat-based CRM interface
