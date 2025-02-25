from typing import Any
from config import Config
from extensions import db, migrate
from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.routes.user_routes import (
    create_update_contact,
    delete_contact,
    user_routes,
    get_contacts,
)

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_routes, url_prefix="/api/users")


# Enable CORS for all routes
CORS(app)


@app.route("/")
def home() -> None:
    return "Hello, Flask with Poetry!"


@app.route("/api/contacts", methods=["GET"])
def get_contacts_entry() -> Any:
    return get_contacts()


@app.route("/api/contact/<int:id>", methods=["DELETE"])
def delete_contact_entry(id:int) -> None:
    import pdb; pdb.set_trace()
    if not id:
        return jsonify({"message": "No id provided"}), 400
    return delete_contact(id)

@app.route("/api/contact", methods=["POST", "PUT"])
def create_contact_entry():
    data = request.json
    if data is None:
        return jsonify({"message": "No data provided"}), 400
    return create_update_contact(data)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
