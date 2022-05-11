from flask import Flask
from Models import usersModel

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
    # print(fetchUser)
    newData = req.get_json()
    updatedUser = usersModel.Users.update(fetchUser[0], newData)

    # data = req.get_json()
    # for key, val in data.items():
    #     foundUser[key] = val
    # return foundUser, 200
    return

def destroy(req, username):
    fetchUser = usersModel.Users.show(username)
    deletedUser = usersModel.Users.delete(fetchUser[0]['id']) #This will not work until we use the OOP to make our objects.(i think...)
    print(fetchUser)
    return fetchUser, 204

