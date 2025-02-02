import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from llama_index.core.node_parser import TokenTextSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

import faiss
from llama_index.core import (
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
    Document,
)
from llama_index.vector_stores.faiss import FaissVectorStore

from app.config import Configs


cfg = Configs()


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

QUERY_ENGINE = None

@app.on_event('startup')
def init_module():
    global QUERY_ENGINE
    # setup embedding model
    embedding_model_name = 'BAAI/bge-m3'
    embedding_model_name = cfg.EMBEDDING_MDOEL
    embed_model = HuggingFaceEmbedding(model_name=embedding_model_name,max_length=1024)
    # setup env
    Settings.llm = None
    Settings.embed_model = embed_model

    dim = 1024
    faiss_index = faiss.IndexFlatIP(dim)

    persist_dir = './index'
    vector_store = FaissVectorStore.from_persist_dir(persist_dir)
    storage_context = StorageContext.from_defaults(vector_store=vector_store, persist_dir=persist_dir)
    index = load_index_from_storage(storage_context=storage_context)
    QUERY_ENGINE = index.as_query_engine(similarity_top_k=3)
    print('== service started ==')


@app.on_event('shutdown')
def terminate_module():
    pass


@app.get('/')
def home():
    res = 'welcome to RAG service'
    return PlainTextResponse(res)


@app.get('/index')
def index():
    """ it is your homework to finish it
    """
    pass


@app.get('/search')
def search(query:str):
    res = QUERY_ENGINE.query(query)

    return PlainTextResponse(res.response)
