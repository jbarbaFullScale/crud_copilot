from extensions import db


class Contact(db.Model):
    __tablename__ = "contact"
    # a contact table with fields id, name, email, address, contact_number, created_at, updated_at
    # The psql script for this model is
    # CREATE TABLE contact (
    #     id SERIAL PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     email VARCHAR(255) NOT NULL,
    #     address VARCHAR(255) NOT NULL,
    #     contact_number VARCHAR(255) NOT NULL,
    #     created_at TIMESTAMP DEFAULT NOW(),
    #     updated_at TIMESTAMP DEFAULT NOW() ON UPDATE NOW()
    # );

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "contact_number": self.contact_number,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
