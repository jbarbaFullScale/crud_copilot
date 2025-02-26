from typing import Any, Dict
from models.user import Contact
from flask import Blueprint, request, jsonify, Response
from extensions import db


contact_routes = Blueprint("contact_routes", __name__)

@contact_routes.route("get/<int:id>", methods=["GET"])
def get_contact_by_id(id: int) -> Response:
    contact = Contact.query.filter_by(id=id).first()
    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    return jsonify({"contact": contact.to_dict()})

@contact_routes.route("get", methods=["GET"])
def get_contacts() -> Response:
    contacts = Contact.query.all()
    return jsonify({"contacts": [contact.to_dict() for contact in contacts]})

@contact_routes.route("create", methods=["POST"])
def create_contact() -> Response:
    data = request.json
    email = data.get("email")

    if Contact.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    new_user = Contact(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        contact_number=data["contact_number"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


@contact_routes.route("update/<int:id>", methods=["PUT"])
def update_contact(id: int) -> Response:
    data = request.json
    contact = Contact.query.get(id)

    if (
        contact.email != data["email"]
        and Contact.query.filter_by(email=data["email"]).first()
    ):
        return jsonify({"message": "Email already exists"}), 400

    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    contact.name = data["name"]
    contact.email = data["email"]
    contact.address = data["address"]
    contact.contact_number = data["contact_number"]
    db.session.commit()

    return jsonify(contact.to_dict()), 200


@contact_routes.route("delete/<int:id>", methods=["DELETE"])
def delete_contact(id: int) -> None:
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted"}), 200
