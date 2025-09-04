-- Crear base de datos
CREATE DATABASE fullstack_app;

-- Conectar a la base de datos
\c fullstack_app;

-- Crear tabla de usuarios
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear índices para mejorar el rendimiento
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);

-- Insertar algunos usuarios de ejemplo
INSERT INTO users (username, email, first_name, last_name) VALUES
('admin', 'admin@example.com', 'Administrador', 'Sistema'),
('juan', 'juan@example.com', 'Juan', 'Pérez'),
('maria', 'maria@example.com', 'María', 'García'),
('carlos', 'carlos@example.com', 'Carlos', 'López');

-- Crear función para actualizar automáticamente updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Crear trigger para actualizar updated_at automáticamente
CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();

-- Crear usuario para la aplicación
CREATE USER app_user WITH PASSWORD 'app_password';

-- Otorgar permisos
GRANT ALL PRIVILEGES ON DATABASE fullstack_app TO app_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO app_user;
