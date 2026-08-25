from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Calculadora Inteligente")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers.gastos import router as router_gastos
from app.routers.media import router as router_media
from app.routers.financiamento import router as router_financiamento
from app.routers.juros_compostos import router as router_juros_compostos
from app.routers.combustivel import router as router_combustivel
from app.routers.motorista import router as router_motorista
from app.routers.eletrodomesticos import router as router_eletrodomesticos
from app.routers.autonomos import router as router_autonomos
from app.routers.regra_tres import router as router_regra_tres
from app.routers.alcool_gasolina import router as router_alcool_gasolina

app.include_router(router_gastos)
app.include_router(router_media)
app.include_router(router_financiamento)
app.include_router(router_juros_compostos)
app.include_router(router_combustivel)
app.include_router(router_motorista)
app.include_router(router_eletrodomesticos)
app.include_router(router_autonomos)
app.include_router(router_regra_tres)
app.include_router(router_alcool_gasolina)

@app.get("/")
def read_root():
    return {"message": "API rodando!"}
