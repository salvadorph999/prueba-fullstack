from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

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

class ConceptoCatalogo(BaseModel):
    """Elemento de un catálogo regulatorio: clave + descripción."""
    clave: str
    descripcion: str


# Reporte R13 A-1311 (CNBV):

#526 531 529 554 (Capital contribuido)
#533 562 566 563 570 549 539 561 564 (Capital ganado)
#560 (Total Capital contable)

# "Estado de cambios en el capital contable de la sociedad controladora".
CATALOGO_CAPITAL_CONTABLE_A1311: List[ConceptoCatalogo] = [
    
    ConceptoCatalogo(clave="526", descripcion="Capital social"),
    ConceptoCatalogo(clave="529", descripcion="Prima en venta de acciones"),
    ConceptoCatalogo(clave="531", descripcion="Aportaciones para futuros aumentos de capital formalizadas por su órgano de gobierno"),
    ConceptoCatalogo(clave="533", descripcion="Reservas de capital"),
    ConceptoCatalogo(clave="539", descripcion="Efecto acumulado por conversión"),
    ConceptoCatalogo(clave="549", descripcion="Remedición de beneficios definidos a los empleados"),
    ConceptoCatalogo(clave="554", descripcion="Instrumentos financieros que califican como capital"),
    ConceptoCatalogo(clave="560", descripcion="Total Capital contable"),
    ConceptoCatalogo(clave="561", descripcion="Resultado por tenencia de activos no monetarios"),
    ConceptoCatalogo(clave="562", descripcion="Resultados acumulados"),
    ConceptoCatalogo(clave="563", descripcion="Valuación de instrumentos financieros para cobrar o vender"),
    ConceptoCatalogo(clave="564", descripcion="Participación en ORI de otras entidades"),
    ConceptoCatalogo(clave="566", descripcion="Valuación de instrumentos financieros negociables"),
    ConceptoCatalogo(clave="570", descripcion="Ingresos y gastos relacionados con activos mantenidos para su disposición"),
    
    # Total
]


@app.get("/estadoCambiosCapitalContable", response_model=List[ConceptoCatalogo])
def get_estado_cambios_capital_contable():
    """Retorna el catálogo del reporte R13 A-1311: Estado de cambios en el
    capital contable de la sociedad controladora (clave y descripción)."""
    return CATALOGO_CAPITAL_CONTABLE_A1311