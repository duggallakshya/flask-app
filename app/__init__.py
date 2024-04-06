from flask import Flask
from .user_service import user_bp
from .post_service import post_bp
from .product_service import product_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(post_bp, url_prefix='/post')
app.register_blueprint(product_bp, url_prefix='/product')



# Function to initialize JSON files
def initialize_json_files():
    import json
    for filename in ['users.json', 'posts.json', 'products.json']:
        try:
            with open(filename, 'r') as file:
                data = file.read().strip()
                if not data:
                    with open(filename, 'w') as new_file:
                        new_file.write("[]")  # Write an empty list if file is empty
                else:
                    json.loads(data)  # Validate JSON data
        except (FileNotFoundError, json.JSONDecodeError):
            with open(filename, 'w') as file:
                file.write("[]")  # Write an empty list if file is empty or contains invalid JSON



initialize_json_files()
