from fastapi import FastAPI
from app.rotas import router as rotas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Calculadora Inteligente")

# 1. Primeiro o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Depois as rotas e o root
app.include_router(rotas)

@app.get("/")
def read_root():
    return {"message": "API rodando!"}
