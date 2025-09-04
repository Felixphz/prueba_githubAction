import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_user():
    return {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User'
    }

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['status'] == 'healthy'

def test_create_user(client, sample_user):
    """Test creating a new user"""
    response = client.post('/api/users', json=sample_user)
    assert response.status_code == 201
    data = response.get_json()
    assert data['success'] == True
    assert data['data']['username'] == sample_user['username']
    assert data['data']['email'] == sample_user['email']

def test_get_users(client, sample_user):
    """Test getting all users"""
    # Create a user first
    client.post('/api/users', json=sample_user)
    
    # Get all users
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert len(data['data']) == 1
    assert data['data'][0]['username'] == sample_user['username']

def test_get_user_by_id(client, sample_user):
    """Test getting a user by ID"""
    # Create a user first
    create_response = client.post('/api/users', json=sample_user)
    user_id = create_response.get_json()['data']['id']
    
    # Get user by ID
    response = client.get(f'/api/users/{user_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['data']['id'] == user_id

def test_update_user(client, sample_user):
    """Test updating a user"""
    # Create a user first
    create_response = client.post('/api/users', json=sample_user)
    user_id = create_response.get_json()['data']['id']
    
    # Update user
    update_data = {'first_name': 'Updated'}
    response = client.put(f'/api/users/{user_id}', json=update_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['data']['first_name'] == 'Updated'

def test_delete_user(client, sample_user):
    """Test deleting a user"""
    # Create a user first
    create_response = client.post('/api/users', json=sample_user)
    user_id = create_response.get_json()['data']['id']
    
    # Delete user
    response = client.delete(f'/api/users/{user_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    
    # Verify user is deleted
    get_response = client.get(f'/api/users/{user_id}')
    assert get_response.status_code == 404

def test_create_user_validation(client):
    """Test user creation validation"""
    # Missing required fields
    response = client.post('/api/users', json={'username': 'test'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] == False
    assert 'error' in data

def test_duplicate_username(client, sample_user):
    """Test duplicate username validation"""
    # Create first user
    client.post('/api/users', json=sample_user)
    
    # Try to create second user with same username
    duplicate_user = sample_user.copy()
    duplicate_user['email'] = 'different@example.com'
    response = client.post('/api/users', json=duplicate_user)
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] == False
    assert 'username ya existe' in data['error']
