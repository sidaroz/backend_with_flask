users = [
    {'id': 1, 'username': 'rubhan', 'email': "rubhan24@gmail.com"},
    {'id': 2, 'username': 'melissa', 'email': "melissa@gmail.com"},
    {'id': 3, 'username': 'jaxsan', 'email': "jax@gmail.com"}
]

def index(req):
    return [user for user in users], 200

def show(req, username):
    username = username.lower()
    return find_by_username(username), 200

def create(req):
    new_user = req.get_json()
    new_user['id'] = sorted([user['id'] for user in users])[-1] + 1  #Doesnt make sense 
    users.append(new_user)
    return new_user, 201

def update(req, username):
    foundUser = find_by_username(username)
    data = req.get_json()
    for key, val in data.items():
        foundUser[key] = val
    return foundUser, 200

def destroy(req, username):
    foundUser = find_by_username(username)
    users.remove(foundUser)
    print(foundUser)
    return {"message": "Deleted"}, 204 #ask some bredda

def find_by_username(username):
    return next(user for user in users if user['username'] == username) #Doesnt make sense 