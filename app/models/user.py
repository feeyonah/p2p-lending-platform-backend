from app import db
import uuid
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key = True, default = lambda:
                   str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password_hash = db.Column(db.string(255), nullable = False)
    role = db.COlumn(db.Enum('borrower','lender'), nullable = False)
    credit_score = db.Column(db.integer)
    reputation_score = db.Column(db.float)
    created_at = db.column(db.DateTime , default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}, Role: {self.role}>'