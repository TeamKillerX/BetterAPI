import requests

from fastapi import FastAPI, UploadFile, File, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security import APIKeyHeader
from fastapi import Depends, HTTPException, status
from fastapi.openapi.utils import get_openapi
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
from fastapi.responses import *
from fastapi import Request, Header
from fastapi import Body, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException
from fastapi import Request, Depends

app = FastAPI(docs_url="/", redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chatgpt")
async def chatgpt(query: str):
    url = "https://randydev-ryuzaki-api.hf.space/chatgpt-old"
    payload = {"query": query}
    response = requests.post(url, payload)
    if response.status_code == 200:
        response_json = response.json()
        return {"message": response_json["randydev"]["message"]}
    raise HTTPException(status_code=404, detail="Error 404")


