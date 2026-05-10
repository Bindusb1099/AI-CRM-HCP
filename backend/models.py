from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class EditRequest(BaseModel):
    
    interaction_id: int
    new_followup_date: str