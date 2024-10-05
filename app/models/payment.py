from app import db
import uuid
from datetime import datetime

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.String(36), primary_key = True, default = lambda:
                   str(uuid.uuid4()))
    loan_id = db.column(db.String(36), db.ForeignKey('loans.id'), nullable = False)
    amount = db.column(db.Float, nullable = False)
    Payment_data = db.Column(db.DateTime, default = datetime.utcnow)
    status = db.Column(db.Enum('pending', 'completed', 'failed'), default='pending')
    loan = db.relationship('Loan', backref='payments')

    def __repr__(self):
        return f'<Payment ID: {self.id}, Amount: {self.amount}, Status: {self.status}>'