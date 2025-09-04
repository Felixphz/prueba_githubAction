from flask import Blueprint, request, jsonify
from .models import User
from . import db
import logging

logger = logging.getLogger(__name__)
api = Blueprint('api', __name__)

def validate_user_data(data):
    """Validar datos del usuario"""
    required_fields = ['username', 'email', 'first_name', 'last_name']
    errors = []
    
    for field in required_fields:
        if not data.get(field):
            errors.append(f'Campo {field} es requerido')
        elif not isinstance(data[field], str) or len(data[field].strip()) == 0:
            errors.append(f'Campo {field} no puede estar vacío')
    
    # Validar email
    if data.get('email') and '@' not in data['email']:
        errors.append('El email no es válido')
    
    # Validar longitud de campos
    if data.get('username') and len(data['username']) > 80:
        errors.append('El username no puede tener más de 80 caracteres')
    
    if data.get('email') and len(data['email']) > 120:
        errors.append('El email no puede tener más de 120 caracteres')
    
    return errors

@api.route('/users', methods=['GET'])
def get_users():
    """Obtener todos los usuarios"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 50, type=int), 100)  # Máximo 100 por página
        
        users = User.query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        return jsonify({
            'success': True,
            'data': [user.to_dict() for user in users.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': users.total,
                'pages': users.pages,
                'has_next': users.has_next,
                'has_prev': users.has_prev
            }
        }), 200
    except Exception as e:
        logger.error(f"Error al obtener usuarios: {e}")
        return jsonify({
            'success': False,
            'error': 'Error interno del servidor'
        }), 500

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Obtener usuario por ID"""
    try:
        user = User.query.get_or_404(user_id)
        return jsonify({
            'success': True,
            'data': user.to_dict()
        }), 200
    except Exception as e:
        logger.error(f"Error al obtener usuario {user_id}: {e}")
        return jsonify({
            'success': False,
            'error': 'Usuario no encontrado'
        }), 404

@api.route('/users', methods=['POST'])
def create_user():
    """Crear nuevo usuario"""
    try:
        if not request.is_json:
            return jsonify({
                'success': False,
                'error': 'Content-Type debe ser application/json'
            }), 400
        
        data = request.get_json()
        
        # Validar datos
        validation_errors = validate_user_data(data)
        if validation_errors:
            return jsonify({
                'success': False,
                'error': '; '.join(validation_errors)
            }), 400
        
        # Verificar si el usuario ya existe
        if User.query.filter_by(username=data['username']).first():
            return jsonify({
                'success': False,
                'error': 'El username ya existe'
            }), 400
        
        if User.query.filter_by(email=data['email']).first():
            return jsonify({
                'success': False,
                'error': 'El email ya existe'
            }), 400
        
        # Crear nuevo usuario
        new_user = User(
            username=data['username'].strip(),
            email=data['email'].strip().lower(),
            first_name=data['first_name'].strip(),
            last_name=data['last_name'].strip()
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        logger.info(f"Usuario creado: {new_user.username}")
        
        return jsonify({
            'success': True,
            'data': new_user.to_dict(),
            'message': 'Usuario creado exitosamente'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error al crear usuario: {e}")
        return jsonify({
            'success': False,
            'error': 'Error interno del servidor'
        }), 500

@api.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Actualizar usuario existente"""
    try:
        if not request.is_json:
            return jsonify({
                'success': False,
                'error': 'Content-Type debe ser application/json'
            }), 400
        
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        # Validar campos si están presentes
        if 'username' in data:
            if len(data['username'].strip()) == 0:
                return jsonify({
                    'success': False,
                    'error': 'El username no puede estar vacío'
                }), 400
            if data['username'].strip() != user.username:
                if User.query.filter_by(username=data['username'].strip()).first():
                    return jsonify({
                        'success': False,
                        'error': 'El username ya existe'
                    }), 400
                user.username = data['username'].strip()
        
        if 'email' in data:
            if len(data['email'].strip()) == 0 or '@' not in data['email']:
                return jsonify({
                    'success': False,
                    'error': 'El email no es válido'
                }), 400
            if data['email'].strip().lower() != user.email:
                if User.query.filter_by(email=data['email'].strip().lower()).first():
                    return jsonify({
                        'success': False,
                        'error': 'El email ya existe'
                    }), 400
                user.email = data['email'].strip().lower()
        
        if 'first_name' in data:
            if len(data['first_name'].strip()) == 0:
                return jsonify({
                    'success': False,
                    'error': 'El nombre no puede estar vacío'
                }), 400
            user.first_name = data['first_name'].strip()
        
        if 'last_name' in data:
            if len(data['last_name'].strip()) == 0:
                return jsonify({
                    'success': False,
                    'error': 'El apellido no puede estar vacío'
                }), 400
            user.last_name = data['last_name'].strip()
        
        db.session.commit()
        
        logger.info(f"Usuario actualizado: {user.username}")
        
        return jsonify({
            'success': True,
            'data': user.to_dict(),
            'message': 'Usuario actualizado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error al actualizar usuario {user_id}: {e}")
        return jsonify({
            'success': False,
            'error': 'Error interno del servidor'
        }), 500

@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Eliminar usuario"""
    try:
        user = User.query.get_or_404(user_id)
        username = user.username
        
        db.session.delete(user)
        db.session.commit()
        
        logger.info(f"Usuario eliminado: {username}")
        
        return jsonify({
            'success': True,
            'message': 'Usuario eliminado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error al eliminar usuario {user_id}: {e}")
        return jsonify({
            'success': False,
            'error': 'Error interno del servidor'
        }), 500

@api.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        # Verificar conexión a la base de datos
        from sqlalchemy import text
        db.session.execute(text('SELECT 1'))
        return jsonify({
            'success': True,
            'message': 'API funcionando correctamente',
            'status': 'healthy',
            'database': 'connected'
        }), 200
    except Exception as e:
        logger.error(f"Health check falló: {e}")
        return jsonify({
            'success': False,
            'message': 'API con problemas',
            'status': 'unhealthy',
            'database': 'disconnected',
            'error': str(e)
        }), 503
