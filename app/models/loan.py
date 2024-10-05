from app import db
import uuid 
from datetime import datetime

class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.String(),primary_key = True, default=lambda:
     str(uuid.uuid4()))
    borrower_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable = False)
    lender_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    amount = db.Column(db.Float, nullable = False)
    interest_rate = db.Column(db.Float, nullable = False)
    duration_month = db.Column(db.Integer, nullable = False)
    status = db.Column(db.Enum('pending', 'approved', 'rejected', 'funded', 'repaid', 'defaulted'), default='pending')
    requested_at = db.Column(db.DateTime ,default = datetime.utcnow)
    approved_at = db.column(db.DateTime)
    repaid_at = db.column(db.DateTime)
    payments = db.relationship('Payment', backref='loan', lazy=True)

    
    def __repr__(self):
        return f'<Loan ID: {self.id}, Amount: {self.amount}, Status: {self.status}>'