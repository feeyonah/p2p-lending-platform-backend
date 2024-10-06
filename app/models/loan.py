from app import db
from datetime import datetime
import enum
class LoanStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    FUNDED = "funded"
    REPAID = "repaid"
    DEFAULTED = "defaulted"

class Loan(db.Model):
    __tablename__ = 'loans'
    
    id = db.Column(db.Integer, primary_key=True)
    borrower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(LoanStatus), default=LoanStatus.PENDING, nullable=False)
    requested_at = db.Column(db.DateTime, default=datetime.utcnow)
    approved_at = db.Column(db.DateTime, nullable=True)
    repaid_at = db.Column(db.DateTime, nullable=True)

    borrower = db.relationship('User', foreign_keys=[borrower_id], backref='loans_as_borrower')
    lender = db.relationship('User', foreign_keys=[lender_id], backref='loans_as_lender')


    
    def __repr__(self):
        return f'<Loan ID: {self.id}, Amount: {self.amount}, Status: {self.status}>'