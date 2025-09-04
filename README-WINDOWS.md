# 🪟 Guía de Instalación para Windows

Esta guía te ayudará a configurar y ejecutar el proyecto fullstack en Windows.

## 📋 Prerrequisitos

### 1. **Node.js** (v18 o superior)
- Descarga desde: https://nodejs.org/
- Instala la versión LTS (Long Term Support)
- Verifica la instalación: `node --version`

### 2. **Python** (v3.9 o superior)
- Descarga desde: https://python.org/
- **IMPORTANTE**: Marca "Add Python to PATH" durante la instalación
- Verifica la instalación: `python --version`

### 3. **Git** (opcional pero recomendado)
- Descarga desde: https://git-scm.com/
- Verifica la instalación: `git --version`

## 🚀 Instalación Rápida

### Opción 1: Script Automático (Recomendado)
1. Haz doble clic en `start-windows.bat`
2. El script verificará las dependencias automáticamente
3. Iniciará los servicios en modo desarrollo local

### Opción 2: Instalación Manual

#### Paso 1: Instalar Dependencias del Frontend
```cmd
cd frontend
npm install
```

#### Paso 2: Instalar Dependencias del Backend
```cmd
cd backend
pip install -r requirements-windows.txt
```

## 🔧 Configuración

### Variables de Entorno
1. Copia `env.example` a `.env`
2. Modifica las siguientes variables:
```env
FLASK_ENV=development
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=sqlite:///backend/dev.db
VITE_API_URL=http://localhost:5000
```

## 🏃‍♂️ Ejecutar el Proyecto

### Modo Desarrollo Local (Recomendado para Windows)

#### Backend (Flask)
```cmd
cd backend
python run.py
```
- El backend estará disponible en: http://localhost:5000
- Usa SQLite para desarrollo local (más fácil en Windows)

#### Frontend (React)
```cmd
cd frontend
npm run dev
```
- El frontend estará disponible en: http://localhost:3000
- Se recarga automáticamente al hacer cambios

### Modo Docker (Opcional)
Si tienes Docker instalado:
```cmd
docker-compose up --build
```

## 🧪 Testing

### Backend Tests
```cmd
cd backend
pytest
```

### Frontend Tests
```cmd
cd frontend
npm test
```

## 🛠️ Herramientas de Desarrollo

### Formateo de Código
```cmd
# Backend
cd backend
black .
isort .

# Frontend
cd frontend
npm run lint
```

### Linting
```cmd
# Backend
cd backend
flake8 .

# Frontend
cd frontend
npm run lint
```

## 📁 Estructura del Proyecto
```
Prueba_githubaction/
├── frontend/           # React + TypeScript
│   ├── src/
│   ├── package.json
│   └── ...
├── backend/            # Flask + SQLAlchemy
│   ├── app/
│   ├── requirements-windows.txt
│   └── ...
├── start-windows.bat   # Script de inicio para Windows
├── README-WINDOWS.md   # Esta guía
└── ...
```

## 🔍 Solución de Problemas

### Error: "psycopg2-binary no se puede instalar"
- **Solución**: Usa `requirements-windows.txt` en lugar de `requirements.txt`
- **Alternativa**: El proyecto funciona con SQLite en desarrollo local

### Error: "Node.js no encontrado"
- **Solución**: Instala Node.js desde https://nodejs.org/
- **Verificación**: `node --version`

### Error: "Python no encontrado"
- **Solución**: Instala Python desde https://python.org/
- **IMPORTANTE**: Marca "Add Python to PATH"
- **Verificación**: `python --version`

### Error: "npm no encontrado"
- **Solución**: Reinstala Node.js (incluye npm)
- **Verificación**: `npm --version`

### Error: "pip no encontrado"
- **Solución**: Reinstala Python (incluye pip)
- **Verificación**: `pip --version`

## 🌐 Acceso a la Aplicación

Una vez iniciados los servicios:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Health Check**: http://localhost:5000/api/health

## 📚 Recursos Adicionales

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de React](https://reactjs.org/)
- [Documentación de Vite](https://vitejs.dev/)
- [Documentación de Tailwind CSS](https://tailwindcss.com/)

## 🆘 Soporte

Si encuentras problemas:
1. Verifica que todas las dependencias estén instaladas
2. Revisa la consola para mensajes de error
3. Asegúrate de que los puertos 3000 y 5000 estén libres
4. Reinicia los servicios si es necesario

¡Disfruta desarrollando! 🚀
