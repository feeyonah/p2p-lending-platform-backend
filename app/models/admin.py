from app import db
import uuid
from datetime import datetime

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.String(36), primary_key = True, default = lambda:
                   str(uuid.uuid4()))
    name = db.Column(db.string(36), nullable = False)
    email = db.Column(db.String(36), unique = True, nullable = False)
    password_hash = db.Column(db.string(245), nullable = False)
    created_at = db.column(db.DateTime, default = datetime.utcnow)
    
