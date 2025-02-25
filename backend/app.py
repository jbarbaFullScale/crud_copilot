from typing import Any
from backend.routes.contact_routes import contact_routes, create_contact, delete_contact, get_contacts
from config import Config
from extensions import db, migrate
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(contact_routes, url_prefix="/api/contact")


# Enable CORS for all routes
CORS(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
