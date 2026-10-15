from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI(title="API Catálogos", version="1.0.0")

# Habilitar CORS para permitir peticiones desde Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/estadoCambios", response_model=List[str])
def get_estado_cambios():
    """Retorna el catálogo de estados de cambios."""
    return [
        "Pendiente",
        "En Revisión",
        "Aprobado",
        "Rechazado",
        "En Implementación",
        "Completado",
        "Cancelado",
    ]


@app.get("/periodos", response_model=List[str])
def get_periodos():
    """Retorna el catálogo de periodos disponibles."""
    return [
        "Enero 2024",
        "Febrero 2024",
        "Marzo 2024",
        "Abril 2024",
        "Mayo 2024",
        "Junio 2024",
        "Julio 2024",
        "Agosto 2024",
        "Septiembre 2024",
        "Octubre 2024",
        "Noviembre 2024",
        "Diciembre 2024",
    ]
