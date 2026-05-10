from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ChatRequest
from agent import agent

# 1️⃣ FIRST create app
app = FastAPI()

# 2️⃣ THEN add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ routes
@app.get("/")
def home():
    return {"message": "AI CRM Backend Running"}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        result = agent.invoke({"user_input": req.message})
        return {"response": result["response"]}
    except Exception as e:
        return {"error": str(e)}