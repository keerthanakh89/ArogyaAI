from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "ArogyaAI Backend Running"}

@app.post("/triage")
def triage(symptoms: list[str]):
    return {"urgency": "moderate", "suggestion": "Consult doctor within 24 hours"}
