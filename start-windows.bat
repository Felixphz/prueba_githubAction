@echo off
echo ========================================
echo    INICIANDO PROYECTO FULLSTACK
echo ========================================
echo.

echo Verificando dependencias...
echo.

echo [1/3] Verificando Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js no esta instalado
    echo Por favor instala Node.js desde: https://nodejs.org/
    pause
    exit /b 1
)
echo ✓ Node.js encontrado

echo.
echo [2/3] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado
    echo Por favor instala Python desde: https://python.org/
    pause
    exit /b 1
)
echo ✓ Python encontrado

echo.
echo [3/3] Verificando Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ADVERTENCIA: Docker no esta instalado
    echo El proyecto funcionara en modo desarrollo local
    echo.
    echo Iniciando en modo desarrollo local...
    goto :dev_mode
)

echo ✓ Docker encontrado
echo.
echo Iniciando con Docker...
docker-compose up --build
goto :end

:dev_mode
echo.
echo ========================================
echo    MODO DESARROLLO LOCAL
echo ========================================
echo.
echo Iniciando backend (Flask)...
start "Backend" cmd /k "cd backend && python run.py"
timeout /t 3 /nobreak >nul

echo.
echo Iniciando frontend (React)...
start "Frontend" cmd /k "cd frontend && npm run dev"
timeout /t 3 /nobreak >nul

echo.
echo ✓ Servicios iniciados
echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Presiona cualquier tecla para cerrar...
pause >nul

:end
echo.
echo Proyecto detenido
pause
