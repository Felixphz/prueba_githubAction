# Full-Stack Application with Docker & CI/CD

Esta es una aplicación completa full-stack que incluye:

## 🏗️ Arquitectura

- **Backend**: API REST con Flask (Python)
- **Frontend**: React con TypeScript
- **Base de datos**: PostgreSQL
- **Docker**: Contenedores para cada servicio
- **GitHub Actions**: Pipeline de CI/CD

## 🚀 Tecnologías

- **Backend**: Python 3.9+, Flask, SQLAlchemy, Flask-CORS
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS
- **Base de datos**: PostgreSQL 14
- **Docker**: Docker Compose para orquestación
- **CI/CD**: GitHub Actions

## 📁 Estructura del Proyecto

```
├── backend/                 # API Flask
│   ├── app/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/               # React App
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── database/               # Scripts de BD
│   └── init.sql
├── docker-compose.yml      # Orquestación de servicios
├── .github/               # GitHub Actions
│   └── workflows/
└── README.md
```

## 🐳 Ejecutar con Docker

```bash
# Construir y ejecutar todos los servicios
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down
```

## 🌐 Acceso a la Aplicación

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Base de datos**: localhost:5432

## 🔧 Desarrollo Local

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📊 API Endpoints

- `GET /api/users` - Listar usuarios
- `POST /api/users` - Crear usuario
- `GET /api/users/<id>` - Obtener usuario por ID
- `PUT /api/users/<id>` - Actualizar usuario
- `DELETE /api/users/<id>` - Eliminar usuario

## 🧪 Testing

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

## 🚀 Deployment

El proyecto incluye GitHub Actions para:
- Tests automáticos en cada push
- Build y deploy automático en main branch
- Docker image building
- Security scanning
