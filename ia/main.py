from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
import nltk
import re
import torch

nltk.download("punkt")
nltk.download("punkt_tab")


MODEL_NAME = "facebook/mbart-large-50"  
DEVICE = 0 if torch.cuda.is_available() else -1

summarizer = pipeline(
    "summarization",
    model=MODEL_NAME,
    device=DEVICE
)


app = FastAPI(title="API de Resúmenes IA - Mejorada")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    texto: str
    max_length: int = 150
    min_length: int = 50


def limpiar_texto(texto: str) -> str:
    texto = re.sub(r'\s+', ' ', texto)      
    texto = re.sub(r'\n+', ' ', texto)      
    texto = re.sub(r'\[.*?\]', '', texto)   
    texto = re.sub(r'\(.*?\)', '', texto)   
    return texto.strip()


def dividir_en_chunks(texto, max_palabras=400):
    oraciones = nltk.sent_tokenize(texto, language="spanish")
    chunks, chunk = [], ""

    for oracion in oraciones:
        if len((chunk + oracion).split()) <= max_palabras:
            chunk += " " + oracion
        else:
            chunks.append(chunk.strip())
            chunk = oracion

    if chunk:
        chunks.append(chunk.strip())

    return chunks


def resumir_texto_largo(texto: str, max_length=150, min_length=50):
    chunks = dividir_en_chunks(texto)
    resumenes = []

    for idx, chunk in enumerate(chunks):
        try:
            resumen = summarizer(
                chunk,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )[0]["summary_text"]

            resumenes.append(resumen)

        except Exception as e:
            print(f"❌ Error en chunk {idx}: {e}")
            continue

    resumen_final = " ".join(resumenes)

    # Segundo pase (refinarlo si quedo muyy largo)
    if len(resumen_final.split()) > max_length:
        resumen_final = summarizer(
            resumen_final,
            max_length=max_length,
            min_length=min_length // 2,
            do_sample=False
        )[0]["summary_text"]

    return resumen_final


@app.get("/")
def home():
    return {"mensaje": "La API está funcionando correctamente 🚀"}


@app.post("/resumir")
def generar_resumen(req: TextRequest):

    if not req.texto.strip():
        return {"error": "No se recibió texto válido."}

    if len(req.texto) > 15000:
        return {"error": "Texto demasiado largo (máx 15,000 caracteres)"}

    texto_limpio = limpiar_texto(req.texto)

    resumen_final = resumir_texto_largo(
        texto_limpio,
        max_length=req.max_length,
        min_length=req.min_length
    )

    return {
        "resumen": resumen_final
    }
