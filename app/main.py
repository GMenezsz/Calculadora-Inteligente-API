from fastapi import FastAPI
from app.rotas import router as rotas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Calculadora Inteligente")

app.include_router(rotas)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)