from fastapi import APIRouter
from pydantic import BaseModel
import requests

class Demo(BaseModel):
    query:str


router = APIRouter(prefix="/api")


@router.post('/search')
def search_query(request:Demo):
    request_query = request.model_dump()
    url = "http://localhost:8002/api/search"
    payload = {
        "query":request_query['query'],
    }
    k = requests.post(url,json=payload)
    return k.json()