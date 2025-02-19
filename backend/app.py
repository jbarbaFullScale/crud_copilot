from flask import Flask
from routes.user_routes import get_users
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask with Poetry!"

@app.route("/users")
def users():
    return get_users()

if __name__ == "__main__":
    app.run(debug=True)
