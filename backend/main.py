from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import re

app = FastAPI()

# Libera CORS para permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique o domínio do frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

class Texto(BaseModel):
    conteudo: str
    idioma_origem: str = "EN"    # Fixado para inglês para evitar erros
    idioma_destino: str = "PT"   # Fixado para português

def simplificar_texto(texto):
    # Substitui termos técnicos por explicações simples
    return re.sub(
        r'\b(function|method|parameter|instance|object|class)\b',
        lambda m: {
            'function': 'função',
            'method': 'método',
            'parameter': 'parâmetro',
            'instance': 'exemplo de objeto',
            'object': 'objeto',
            'class': 'modelo de objeto'
        }[m.group()],
        texto
    )

@app.post("/traduzir")
async def traduzir_texto(dados: Texto):
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "auth_key": "69a823d9-bf52-40ac-9f81-3936d26db5c2:fx",  # Substitua pela sua chave real (COM :fx no final)
        "text": dados.conteudo,
        "source_lang": dados.idioma_origem,
        "target_lang": dados.idioma_destino
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        traduzido = response.json()["translations"][0]["text"]
        simplificado = simplificar_texto(traduzido)
        return {
            "traduzido": traduzido,
            "simplificado": simplificado
        }
    except Exception as e:
        return {"erro": f"Falha na tradução com DeepL: {str(e)}"}
