from fastapi import FastAPI
from langchain_zero.chains import translate_text_chain
from langserve import add_routes


# create Fast API app
app = FastAPI(
  title="LangChain Server Translate",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces for translate texts",
)

# 5. Adding chain route
add_routes(
    app,
    translate_text_chain(),
    path="/translate",
)

