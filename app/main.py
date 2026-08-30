from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Calculadora Inteligente")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    if request.method == "OPTIONS":
        response = Response(status_code=200)
    else:
        response = await call_next(request)
    
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

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
from app.routers.caixa import router as router_caixa

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
app.include_router(router_caixa)

@app.api_route("/health", methods=["GET", "HEAD"])
def health_check():
    return {"status": "ok"}
