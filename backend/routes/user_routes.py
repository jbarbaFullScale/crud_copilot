from flask import Blueprint, jsonify

user_routes = Blueprint("users", __name__)

@user_routes.route("/", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})
