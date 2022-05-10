import pytest
import app
from controllers import users

@pytest.fixture
def api(monkeypatch):
    test_users = [
        {'id': 1, 'name': 'Test1', 'email': 'email@1'},
        {'id': 2, 'name': 'Test2', 'email': 'email@2'},
        {'id': 3, 'name': 'Test3', 'email': 'email3'}
    ]
    monkeypatch.setattr(users, "users", test_users)
    api = app.app.test_client()
    return api