import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse


app = FastAPI( title='RAG SERVICE',
               description = '',
             )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event('startup')
def init_module():
    pass


@app.on_event('shutdown')
def terminate_module():
    pass


@app.get('/')
def home():
    res = 'welcome to RAG service'
    return PlainTextResponse(res)


@app.get('/search')
def search(query:str):
    res = f'your query is {query}'
    return PlainTextResponse(res)
