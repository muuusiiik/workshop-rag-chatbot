from pydantic_settings import BaseSettings

class Configs(BaseSettings):
    EMBEDDING_MDOEL:str='BAAI/bge-m3'

    class Config:
        env_file='.env'

