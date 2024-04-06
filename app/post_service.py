from flask import Blueprint, jsonify, request
import json

post_bp = Blueprint('post_bp', __name__)

# Logic to fetch all posts
def get_all_posts():
    with open('posts.json', 'r') as file:
        posts = json.load(file)
    return posts

# Logic to add a new post
def add_post(post_data):
    with open('posts.json', 'r') as file:
        posts = json.load(file)
    
    posts.append(post_data)
    
    with open('posts.json', 'w') as file:
        json.dump(posts, file)

@post_bp.route('/all-posts', methods=['GET'])
def all_posts():
    posts = get_all_posts()
    return jsonify(posts)

@post_bp.route('/add-post', methods=['POST'])
def add_new_post():
    post_data = request.get_json()
    add_post(post_data)
    return jsonify({"message": "Post added successfully"})
