from typing import Any, Dict
from models.user import Contact
from flask import Blueprint, request, jsonify, Response
from extensions import db


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/", methods=["GET"])
def get_contacts() -> Response:
    contacts = Contact.query.all()
    return jsonify({"contacts": [contact.to_dict() for contact in contacts]})


@user_routes.route("/", methods=["POST", "PUT"])
def create_update_contact(data: Dict[str, Any]) -> Response:
    data = request.json
    if not data.get("id"):
        new_user = Contact(
            name=data["name"],
            email=data["email"],
            address=data["address"],
            contact_number=data["contact_number"],
        )
    else:
        new_user = Contact.query.get(data["id"])
        new_user.name = data["name"]
        new_user.email = data["email"]
        new_user.address = data["address"]
        new_user.contact_number = data["contact_number"]

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


def delete_contact(id: int) -> None:
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted"}), 200
