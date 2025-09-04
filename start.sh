#!/bin/bash

echo "🚀 Iniciando FullStack Application..."

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado. Por favor instala Docker primero."
    exit 1
fi

# Verificar si Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose no está instalado. Por favor instala Docker Compose primero."
    exit 1
fi

echo "✅ Docker y Docker Compose están instalados"

# Crear archivo .env si no existe
if [ ! -f .env ]; then
    echo "📝 Creando archivo .env desde env.example..."
    cp env.example .env
fi

# Construir y ejecutar los servicios
echo "🐳 Construyendo y ejecutando servicios con Docker Compose..."
docker-compose up --build -d

echo "⏳ Esperando a que los servicios estén listos..."
sleep 10

# Verificar el estado de los servicios
echo "🔍 Verificando estado de los servicios..."
docker-compose ps

echo ""
echo "🎉 ¡Aplicación iniciada exitosamente!"
echo ""
echo "🌐 Acceso a la aplicación:"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:5000"
echo "   Base de datos: localhost:5432"
echo ""
echo "📋 Comandos útiles:"
echo "   Ver logs: docker-compose logs -f"
echo "   Detener: docker-compose down"
echo "   Reiniciar: docker-compose restart"
echo ""
echo "🔧 Para desarrollo local:"
echo "   Backend: cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && flask run"
echo "   Frontend: cd frontend && npm install && npm run dev"
