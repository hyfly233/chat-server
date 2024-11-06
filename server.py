import uvicorn
from langserve.server import FastAPI, add_routes

from models.ollama_llama import llamaChain, do_message, get_session_history


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

    return fastApi


if __name__ == '__main__':
    uvicorn.run(app(), host="0.0.0.0", port=18000)
