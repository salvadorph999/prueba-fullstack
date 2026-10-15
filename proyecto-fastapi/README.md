# API Catálogos - FastAPI (Python)

API REST desarrollada con **Python + FastAPI** que expone dos endpoints de catálogos.

---

## Requisitos

| Herramienta | Versión mínima |
|-------------|---------------|
| Python      | 3.9+          |
| pip         | 21+           |

### Verificar instalación
```bash
python --version
pip --version
```

---

## Instalación y ejecución

### 1. Entrar al directorio del proyecto
```bash
cd proyecto-fastapi
```

### 2. (Recomendado) Crear un entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Mac / Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
uvicorn main:app --reload
```

La API quedará disponible en: **http://localhost:8000**

> El flag `--reload` hace que el servidor se reinicie automáticamente al guardar cambios en el código.

---

## Endpoints disponibles

### GET /estadoCambios
Devuelve la lista de estados de cambios.

```bash
curl http://localhost:8000/estadoCambios
```

Respuesta esperada:
```json
["Pendiente","En Revisión","Aprobado","Rechazado","En Implementación","Completado","Cancelado"]
```

---

### GET /periodos
Devuelve la lista de periodos disponibles.

```bash
curl http://localhost:8000/periodos
```

Respuesta esperada:
```json
["Enero 2024","Febrero 2024","Marzo 2024", ...]
```

---

## Documentación interactiva (extra)

FastAPI genera documentación automática. Con la aplicación corriendo, puedes visitarla en:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Estructura del proyecto

```
proyecto-fastapi/
├── main.py           ← Aplicación principal con los endpoints
├── requirements.txt  ← Dependencias del proyecto
└── README.md
```

---

## Notas
- CORS habilitado para todos los orígenes (`*`) para facilitar pruebas locales.
- Puerto configurable al iniciar uvicorn: `uvicorn main:app --reload --port 8000`
