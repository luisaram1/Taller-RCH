from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default="mechanic")
    def set_password(self, pwd): self.password_hash = generate_password_hash(pwd)
    def check_password(self, pwd): return check_password_hash(self.password_hash, pwd)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    vehicles = db.relationship("Vehicle", backref="client", lazy=True)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(16), unique=True, nullable=False)
    brand = db.Column(db.String(64))
    model = db.Column(db.String(64))
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    repairs = db.relationship("Repair", backref="vehicle", lazy=True)

class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(32), default="Pendiente")
    cost = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)
