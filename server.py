# server.py

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from interpreter import interpreter
import json


# interpreter --model "azure/Ananke4-1106-US-WEST" --api_base "https://anankeus.openai.azure.com/" --api_key "61bc1aab37364618ae0df70bf5f340dd" --api_version "2024-02-15-preview" --max_output 10000
interpreter.llm.model = "azure/Ananke3-1106-US-WEST"
interpreter.llm.context_window = 32000
interpreter.llm.max_tokens = 4096
interpreter.llm.max_output = 10000
interpreter.llm.api_base = "https://anankeus.openai.azure.com/"
interpreter.llm.api_key = "61bc1aab37364618ae0df70bf5f340dd"
interpreter.llm.api_version = "2024-02-15-preview"
interpreter.auto_run = True

app = FastAPI()

@app.get("/chat")
def chat_endpoint(message: str):
    def event_stream():
        for result in interpreter.chat(message, stream=True):
            result = json.dumps(result)
            yield f"data: {result}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/history")
def history_endpoint():
    return interpreter.messages
