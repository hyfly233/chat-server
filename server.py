import uvicorn
from langserve.server import FastAPI, add_routes

from models.ollama_llama import llamaChain, do_message, get_session_history
from utils.audio_tool import transcribe_audio, text_to_speech, audio_to_stream
from fastapi import UploadFile, File
import os


def app() -> FastAPI:
    fastApi = FastAPI(
        title="LangChain",
        description="A language model chain",
        version="0.1.0"
    )

    add_routes(fastApi, llamaChain(), path="/llama3/test")

    @fastApi.post("/chat/{session_id}")
    async def chat(session_id: str, text: str):
        return {"response": do_message(session_id, text)}

    @fastApi.get("/history/{session_id}")
    async def history(session_id: str):
        return {"history": get_session_history(session_id)}

    @fastApi.post("/transcribe")
    async def transcribe(file: UploadFile = File(...)):
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        text = transcribe_audio(file_location)
        os.remove(file_location)
        return {"text": text}

    @fastApi.post("/synthesize")
    async def synthesize(text: str):
        output_file = "output.mp3"
        text_to_speech(text, output_file)
        return {"message": "Text has been converted to speech", "file": output_file}

    @fastApi.post("/audio_stream")
    async def audio_stream(file: UploadFile = File(...)):
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        audio_stream = audio_to_stream(file_location)
        os.remove(file_location)
        return {"audio_stream": audio_stream.getvalue()}

    return fastApi


if __name__ == '__main__':
    uvicorn.run(app(), host="0.0.0.0", port=18000)
