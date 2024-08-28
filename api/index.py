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

app = FastAPI(docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
