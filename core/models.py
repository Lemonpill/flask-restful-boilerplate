from core import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=None)
    updated_at = db.Column(db.DateTime, default=None)
    deleted_at = db.Column(db.DateTime, default=None)
