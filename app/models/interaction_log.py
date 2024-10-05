from app import db
import uuid
from datetime import datetime


class Interaction_log(db.Model):
    __tablename__= 'interaction_log'
    id = db.Column(db.String(36), primary_key = True, default= lambda:
                   str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    interaction_type = db.Column(db.String(255), nullable=False)
    flag_reason = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref='interaction_logs')

    def __repr__(self):
        return f'<InteractionLog ID: {self.id}, User ID: {self.user_id}, Type: {self.interaction_type}>'