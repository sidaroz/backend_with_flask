import json


class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status =='200 OK'
        assert res.json['message'] == 'Welcome Jax'
    
    def test_get_users(self, api):
        res = api.get('api/users')
        assert res.status == '200 OK'
        assert len(res.json) == 3

    def test_get_users_error(self, api):
        res = api.get('api/users/Test4')
        assert res.status == '400 BAD REQUEST'
        assert "We don't have the user Test4" in res.json['message']

    def test_get_user(self, api):
        res = api.get('api/users/Test1')
        assert res.status == '200 OK'
        assert res.json['username'] == 'Test1'
    
