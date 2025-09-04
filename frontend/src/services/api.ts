import axios, { AxiosError, AxiosResponse } from 'axios';
import { User, CreateUserData, UpdateUserData, ApiResponse } from '../types/user';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

// Configuración de axios con interceptores
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 segundos de timeout
});

// Interceptor para respuestas
api.interceptors.response.use(
  (response: AxiosResponse) => response,
  (error: AxiosError) => {
    if (error.response?.status === 404) {
      console.error('Recurso no encontrado:', error.config?.url);
    } else if (error.response?.status >= 500) {
      console.error('Error del servidor:', error.response.data);
    } else if (error.code === 'ECONNABORTED') {
      console.error('Timeout de la petición');
    }
    return Promise.reject(error);
  }
);

// Función helper para manejar errores
const handleApiError = (error: any): ApiResponse<any> => {
  if (axios.isAxiosError(error)) {
    if (error.response?.data?.error) {
      return {
        success: false,
        error: error.response.data.error,
      };
    }
    if (error.response?.status === 404) {
      return {
        success: false,
        error: 'Recurso no encontrado',
      };
    }
    if (error.response?.status >= 500) {
      return {
        success: false,
        error: 'Error interno del servidor',
      };
    }
  }
  return {
    success: false,
    error: 'Error de conexión',
  };
};

export const userService = {
  // Obtener todos los usuarios con paginación
  async getUsers(page: number = 1, perPage: number = 50): Promise<ApiResponse<User[]>> {
    try {
      const response = await api.get('/api/users', {
        params: { page, per_page: perPage }
      });
      return response.data;
    } catch (error) {
      return handleApiError(error);
    }
  },

  // Obtener usuario por ID
  async getUser(id: number): Promise<ApiResponse<User>> {
    try {
      const response = await api.get(`/api/users/${id}`);
      return response.data;
    } catch (error) {
      return handleApiError(error);
    }
  },

  // Crear nuevo usuario
  async createUser(userData: CreateUserData): Promise<ApiResponse<User>> {
    try {
      const response = await api.post('/api/users', userData);
      return response.data;
    } catch (error) {
      return handleApiError(error);
    }
  },

  // Actualizar usuario
  async updateUser(id: number, userData: UpdateUserData): Promise<ApiResponse<User>> {
    try {
      const response = await api.put(`/api/users/${id}`, userData);
      return response.data;
    } catch (error) {
      return handleApiError(error);
    }
  },

  // Eliminar usuario
  async deleteUser(id: number): Promise<ApiResponse<null>> {
    try {
      const response = await api.delete(`/api/users/${id}`);
      return response.data;
    } catch (error) {
      return handleApiError(error);
    }
  },

  // Health check
  async healthCheck(): Promise<ApiResponse<any>> {
    try {
      const response = await api.get('/api/health');
      return response.data;
    } catch (error) {
      return handleApiError(error);
    }
  },
};

export default api;
