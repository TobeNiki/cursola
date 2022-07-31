from fastapi import FastAPI
from fastapi import FastAPI, Header, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from app.routers import cursola, user
from app.auth import authentication
from typing import Optional, List
from db import models
from db.database import engine

app = FastAPI()
app.include_router(router=cursola.router)
app.include_router(router=user.router)
app.include_router(router=authentication.router)

@app.get("/header")
def custom_header(
    response: Response,
    custom_header: Optional[List[str]] = Header(None)
    ):
    response.headers['custom_response_header'] = ". ".join(custom_header)
    return f"{custom_header}"

models.Base.metadata.create_all(engine)


origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
