# 🚀 Guía Completa: GitHub Actions para tu Proyecto Fullstack

## 📋 **PASO 1: Crear Repositorio en GitHub**

### **1.1. Crear nuevo repositorio:**
1. Ve a [GitHub.com](https://github.com)
2. Haz clic en **"New repository"** (botón verde)
3. Configuración:
   - **Repository name**: `fullstack-project` (o el nombre que prefieras)
   - **Description**: `Fullstack application with Flask backend, React frontend, and CI/CD`
   - **Visibility**: Public (o Private si prefieres)
   - **NO marques**: "Add a README file" (ya tienes uno)
   - **NO marques**: "Add .gitignore" (ya tienes uno)
   - **NO marques**: "Choose a license"

### **1.2. Copiar la URL del repositorio:**
Después de crear el repositorio, GitHub te mostrará una URL como:
```
https://github.com/tu-usuario/fullstack-project.git
```

---

## 📋 **PASO 2: Conectar tu Proyecto Local con GitHub**

### **2.1. Agregar el remote origin:**
```bash
# Reemplaza 'tu-usuario' y 'fullstack-project' con tus datos
git remote add origin https://github.com/tu-usuario/fullstack-project.git
```

### **2.2. Cambiar la rama principal a 'main':**
```bash
# Crear y cambiar a la rama main
git branch -M main

# Subir el código a GitHub
git push -u origin main
```

---

## 📋 **PASO 3: Configurar GitHub Actions**

### **3.1. Verificar que el workflow esté activo:**
1. Ve a tu repositorio en GitHub
2. Haz clic en la pestaña **"Actions"**
3. Deberías ver el workflow **"CI/CD Pipeline"**

### **3.2. Configurar Secrets (si es necesario):**
1. Ve a **Settings** > **Secrets and variables** > **Actions**
2. Agregar secrets si necesitas:
   ```
   DOCKER_USERNAME: tu-usuario-docker
   DOCKER_PASSWORD: tu-password-docker
   ```

### **3.3. Configurar Environments (opcional):**
1. Ve a **Settings** > **Environments**
2. Crear environments:
   - `staging`
   - `production`

---

## 📋 **PASO 4: Probar GitHub Actions**

### **4.1. Hacer un cambio y push:**
```bash
# Hacer un pequeño cambio
echo "# Test GitHub Actions" >> README.md

# Agregar, commit y push
git add README.md
git commit -m "Test: Trigger GitHub Actions"
git push origin main
```

### **4.2. Verificar en GitHub:**
1. Ve a la pestaña **"Actions"**
2. Deberías ver un nuevo workflow ejecutándose
3. Haz clic en el workflow para ver los detalles

---

## 📋 **PASO 5: Comandos Completos de Git**

### **5.1. Comandos básicos:**
```bash
# Ver estado
git status

# Agregar archivos
git add .
git add archivo-especifico.txt

# Hacer commit
git commit -m "Descripción del cambio"

# Subir cambios
git push origin main

# Bajar cambios
git pull origin main
```

### **5.2. Comandos para ramas:**
```bash
# Crear nueva rama
git checkout -b nueva-funcionalidad

# Cambiar de rama
git checkout main
git checkout nueva-funcionalidad

# Subir nueva rama
git push origin nueva-funcionalidad

# Crear Pull Request desde GitHub
```

### **5.3. Comandos de configuración:**
```bash
# Configurar usuario (si no está configurado)
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# Ver configuración
git config --list
```

---

## 📋 **PASO 6: Estructura del Workflow**

### **6.1. ¿Qué hace cada job?**

#### **Backend Tests:**
- ✅ Instala Python 3.9
- ✅ Configura PostgreSQL
- ✅ Instala dependencias
- ✅ Ejecuta tests con pytest

#### **Frontend Tests:**
- ✅ Instala Node.js 18
- ✅ Instala dependencias npm
- ✅ Ejecuta linting
- ✅ Ejecuta tests con cobertura

#### **Build and Push:**
- ✅ Construye imágenes Docker
- ✅ Sube a GitHub Container Registry
- ✅ Solo se ejecuta en rama `main`

#### **Security Scan:**
- ✅ Escanea vulnerabilidades con Trivy
- ✅ Sube reportes a Security tab

#### **Deploy:**
- ✅ Despliega a staging (rama `develop`)
- ✅ Despliega a production (rama `main`)

---

## 📋 **PASO 7: Monitoreo y Debugging**

### **7.1. Ver logs de GitHub Actions:**
1. Ve a **Actions** > **CI/CD Pipeline**
2. Haz clic en el workflow que falló
3. Haz clic en el job que falló
4. Revisa los logs para encontrar el error

### **7.2. Errores comunes y soluciones:**

#### **Error: "Tests failed"**
```bash
# Ejecutar tests localmente
cd backend
python -m pytest -v

cd frontend
npm test
```

#### **Error: "Docker build failed"**
```bash
# Probar build localmente
docker build -t test-backend ./backend
docker build -t test-frontend ./frontend
```

#### **Error: "Permission denied"**
- Verificar que el repositorio tenga permisos de Packages
- Verificar que GITHUB_TOKEN tenga permisos correctos

---

## 📋 **PASO 8: Personalización Avanzada**

### **8.1. Agregar más tests:**
```yaml
- name: Run integration tests
  run: |
    cd backend
    python -m pytest tests/integration/ -v
```

### **8.2. Agregar deployment real:**
```yaml
- name: Deploy to production
  run: |
    # Ejemplo con Kubernetes
    kubectl apply -f k8s/
    
    # O con Docker Compose
    docker-compose -f docker-compose.prod.yml up -d
```

### **8.3. Agregar notificaciones:**
```yaml
- name: Notify on failure
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: failure
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

---

## 📋 **PASO 9: Comandos de Ejemplo Completos**

### **9.1. Secuencia completa para subir proyecto:**
```bash
# 1. Inicializar (si no está inicializado)
git init

# 2. Agregar archivos
git add .

# 3. Primer commit
git commit -m "Initial commit: Fullstack project"

# 4. Agregar remote (reemplaza con tu URL)
git remote add origin https://github.com/tu-usuario/fullstack-project.git

# 5. Cambiar a main
git branch -M main

# 6. Subir a GitHub
git push -u origin main
```

### **9.2. Secuencia para cambios futuros:**
```bash
# 1. Ver cambios
git status

# 2. Agregar cambios
git add .

# 3. Commit
git commit -m "Descripción del cambio"

# 4. Push
git push origin main
```

---

## 🎯 **Resultado Final**

Después de seguir estos pasos tendrás:

✅ **Repositorio en GitHub** con tu código
✅ **GitHub Actions** ejecutándose automáticamente
✅ **Tests automáticos** en cada push/PR
✅ **Imágenes Docker** construidas automáticamente
✅ **Escaneo de seguridad** automático
✅ **Deployment** automático según la rama

---

## 🆘 **Soporte**

Si tienes problemas:

1. **Revisa los logs** en GitHub Actions
2. **Ejecuta tests localmente** para verificar
3. **Verifica permisos** del repositorio
4. **Consulta la documentación** de GitHub Actions

¡Tu proyecto estará completamente automatizado! 🚀
