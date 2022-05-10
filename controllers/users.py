from flask import Flask
from Models import usersModel




# users = [
#     {'id': 1, 'username': 'rubhan', 'email': "rubhan24@gmail.com"},
#     {'id': 2, 'username': 'melissa', 'email': "melissa@gmail.com"},
#     {'id': 3, 'username': 'jaxsan', 'email': "jax@gmail.com"}
# ]


def index(req):
    fetchAll = usersModel.Users.getAll()
    return fetchAll, 200

def show(req, username):
    fetchUser = usersModel.Users.show(username)
    return fetchUser, 200


def create(req):
    new_user = req.get_json()
    createUser = usersModel.Users.create(new_user)
    return createUser, 201

def update(req, username):
    fetchUser = usersModel.Users.show(username)
    updatedUser = fetchUser.update(fetchUser[0])

    data = req.get_json()
    for key, val in data.items():
        foundUser[key] = val
    return foundUser, 200

def destroy(req, username):
    fetchUser = usersModel.Users.show(username)
    deleteUser = fetchUser.delete(fetchUser[0]['id']) #This will not work until we use the OOP to make our objects.(i think...)
    print(fetchUser)
    return fetchUser, 204

def find_by_username(username):
    return next(user for user in users if user['username'] == username) #Doesnt make sense 