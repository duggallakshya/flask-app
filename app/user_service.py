from flask import Blueprint, jsonify, request
import json

user_bp = Blueprint('user_bp', __name__)



# Logic to fetch all users
def get_all_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

# Logic to add a new user
def add_user(user_data):
    with open('users.json', 'r') as file:
        users = json.load(file)
    
    users.append(user_data)
    
    with open('users.json', 'w') as file:
        json.dump(users, file)

@user_bp.route('/all-users', methods=['GET'])
def all_users():
    users = get_all_users()
    return jsonify(users)

@user_bp.route('/add-user', methods=['POST'])
def add_new_user():
    user_data = request.get_json()
    add_user(user_data)
    return jsonify({"message": "User added successfully"})
