from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: Request):

    if not req.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is empty")

    try:
        response = requests.post(
            "http://host.docker.internal:11434/api/chat",  # ✅ FIXED
            json={
                "model": "qwen2.5:0.5b",
                "messages": [
                    {"role": "user", "content": req.prompt}
                ],
                "stream": False
            }
        )

        data = response.json()
        answer = data["message"]["content"].strip()

        return {"response": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    return {"status": "ok", "model": "qwen2.5:0.5b"}