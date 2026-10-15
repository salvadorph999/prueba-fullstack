# App Catálogos - Angular

Aplicación web desarrollada con **Angular 17** que consume una API REST y muestra los catálogos de **Estado de Cambios** y **Periodos** tras un proceso de login.

---

## Requisitos

| Herramienta   | Versión mínima |
|---------------|---------------|
| Node.js       | 18+           |
| npm           | 9+            |
| Angular CLI   | 17+           |

### Verificar instalación
```bash
node --version
npm --version
```

### Instalar Angular CLI (si no lo tienes)
```bash
npm install -g @angular/cli
```

---

## Instalación y ejecución

### 1. Entrar al directorio del proyecto
```bash
cd proyecto-angular
```

### 2. Instalar dependencias
```bash
npm install
```

### 3. Configurar la URL del API

Abre el archivo `src/app/catalogos/catalogos.service.ts` y ajusta la constante `API_URL` según el backend que estés usando:

```typescript
// Spring Boot (Java)  → puerto 8080
const API_URL = 'http://localhost:8080';

// FastAPI (Python)    → puerto 8000
const API_URL = 'http://localhost:8000';
```

> **Importante:** El backend debe estar corriendo antes de iniciar la aplicación Angular.

### 4. Ejecutar la aplicación
```bash
ng serve
```

La aplicación quedará disponible en: **http://localhost:4200**

---

## Pantallas

### 1. Login (`/login`)
- Captura de usuario y contraseña.
- Redirige a la pantalla de catálogos si son correctas.
- Muestra mensaje de error si son incorrectas.

### 2. Catálogos (`/catalogos`)
- Muestra los datos de `/estadoCambios` y `/periodos` en tarjetas separadas.
- Botón de "Cerrar Sesión" que regresa al login.
- Ruta protegida: si el usuario no ha iniciado sesión, redirige al login automáticamente.

---

## Estructura del proyecto

```
proyecto-angular/
├── angular.json
├── package.json
├── tsconfig.json
├── README.md
└── src/
    ├── index.html
    ├── main.ts
    ├── styles.css
    └── app/
        ├── app.component.ts        ← Componente raíz
        ├── app.config.ts           ← Configuración de la app
        ├── app.routes.ts           ← Definición de rutas
        ├── auth.guard.ts           ← Protección de rutas privadas
        ├── login/
        │   ├── login.component.ts  ← Lógica del login
        │   ├── login.component.html
        │   └── login.component.css
        └── catalogos/
            ├── catalogos.component.ts   ← Lógica de catálogos
            ├── catalogos.component.html
            ├── catalogos.component.css
            └── catalogos.service.ts     ← Llamadas HTTP al API
```

---

## Notas
- La sesión se guarda en `sessionStorage` y se pierde al cerrar el navegador.
- El puerto de desarrollo es configurable: `ng serve --port 4201`
