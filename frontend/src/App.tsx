import React, { useState, useEffect } from 'react';
import { User, CreateUserData, UpdateUserData } from './types/user';
import { userService } from './services/api';
import UserList from './components/UserList';
import UserForm from './components/UserForm';
import { Plus, X, CheckCircle, AlertCircle } from 'lucide-react';

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingUser, setEditingUser] = useState<User | null>(null);
  const [formLoading, setFormLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [pagination, setPagination] = useState<any>(null);
  const [notification, setNotification] = useState<{
    type: 'success' | 'error';
    message: string;
  } | null>(null);

  useEffect(() => {
    fetchUsers(currentPage);
  }, [currentPage]);

  const fetchUsers = async (page: number = 1) => {
    try {
      setLoading(true);
      const response = await userService.getUsers(page);
      if (response.success && response.data) {
        setUsers(response.data);
        if (response.pagination) {
          setPagination(response.pagination);
        }
      } else {
        showNotification('error', response.error || 'Error al cargar usuarios');
      }
    } catch (error) {
      showNotification('error', 'Error al cargar usuarios');
    } finally {
      setLoading(false);
    }
  };

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
  };

  const handleCreateUser = async (userData: CreateUserData) => {
    try {
      setFormLoading(true);
      const response = await userService.createUser(userData);
      
      if (response.success && response.data) {
        // Refrescar la lista y volver a la primera página
        setCurrentPage(1);
        await fetchUsers(1);
        setShowForm(false);
        showNotification('success', 'Usuario creado exitosamente');
      } else {
        showNotification('error', response.error || 'Error al crear usuario');
      }
    } catch (error) {
      showNotification('error', 'Error al crear usuario');
    } finally {
      setFormLoading(false);
    }
  };

  const handleUpdateUser = async (userData: UpdateUserData) => {
    if (!editingUser) return;
    
    try {
      setFormLoading(true);
      const response = await userService.updateUser(editingUser.id, userData);
      
      if (response.success && response.data) {
        // Refrescar la lista
        await fetchUsers(currentPage);
        setEditingUser(null);
        showNotification('success', 'Usuario actualizado exitosamente');
      } else {
        showNotification('error', response.error || 'Error al actualizar usuario');
      }
    } catch (error) {
      showNotification('error', 'Error al actualizar usuario');
    } finally {
      setFormLoading(false);
    }
  };

  const handleDeleteUser = async (userId: number) => {
    if (!window.confirm('¿Estás seguro de que quieres eliminar este usuario?')) {
      return;
    }

    try {
      const response = await userService.deleteUser(userId);
      
      if (response.success) {
        // Refrescar la lista
        await fetchUsers(currentPage);
        showNotification('success', 'Usuario eliminado exitosamente');
      } else {
        showNotification('error', response.error || 'Error al eliminar usuario');
      }
    } catch (error) {
      showNotification('error', 'Error al eliminar usuario');
    }
  };

  const handleEditUser = (user: User) => {
    setEditingUser(user);
    setShowForm(true);
  };

  const handleCancelForm = () => {
    setShowForm(false);
    setEditingUser(null);
  };

  const showNotification = (type: 'success' | 'error', message: string) => {
    setNotification({ type, message });
    setTimeout(() => setNotification(null), 5000);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <h1 className="text-3xl font-bold text-gray-900">
              Gestión de Usuarios
            </h1>
            <button
              onClick={() => setShowForm(true)}
              className="btn-primary flex items-center space-x-2"
            >
              <Plus className="h-5 w-5" />
              <span>Nuevo Usuario</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {/* Notification */}
        {notification && (
          <div className="mb-6">
            <div className={`rounded-md p-4 ${
              notification.type === 'success' 
                ? 'bg-green-50 border border-green-200' 
                : 'bg-red-50 border border-red-200'
            }`}>
              <div className="flex">
                <div className="flex-shrink-0">
                  {notification.type === 'success' ? (
                    <CheckCircle className="h-5 w-5 text-green-400" />
                  ) : (
                    <AlertCircle className="h-5 w-5 text-red-400" />
                  )}
                </div>
                <div className="ml-3">
                  <p className={`text-sm font-medium ${
                    notification.type === 'success' ? 'text-green-800' : 'text-red-800'
                  }`}>
                    {notification.message}
                  </p>
                </div>
                <div className="ml-auto pl-3">
                  <button
                    onClick={() => setNotification(null)}
                    className="inline-flex rounded-md p-1.5 focus:outline-none focus:ring-2 focus:ring-offset-2"
                  >
                    <X className="h-5 w-5" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Form Modal */}
        {showForm && (
          <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
            <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-medium text-gray-900">
                  {editingUser ? 'Editar Usuario' : 'Nuevo Usuario'}
                </h3>
                <button
                  onClick={handleCancelForm}
                  className="text-gray-400 hover:text-gray-600"
                >
                  <X className="h-6 w-6" />
                </button>
              </div>
              
              <UserForm
                user={editingUser}
                onSubmit={editingUser ? handleUpdateUser : handleCreateUser}
                onCancel={handleCancelForm}
                isLoading={formLoading}
              />
            </div>
          </div>
        )}

        {/* User List */}
        <div className="px-4 py-6 sm:px-0">
          <UserList
            users={users}
            onEdit={handleEditUser}
            onDelete={handleDeleteUser}
            isLoading={loading}
            pagination={pagination}
            onPageChange={handlePageChange}
          />
        </div>
      </main>
    </div>
  );
}

export default App;
