import uvicorn
from langserve.server import FastAPI, add_routes

from models.ollama_llama import llamaChain


def app() -> FastAPI:
    fastApi = FastAPI(
        title="LangChain",
        description="A language model chain",
        version="0.1.0"
    )

    add_routes(fastApi, llamaChain(), path="/llama3/test")
    return fastApi


if __name__ == '__main__':
    uvicorn.run(app(), host="0.0.0.0", port=18000)
