from app import db
import uuid


class LoanReview(db.Model):
    __tablename__ = 'loan_reviews'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    loan_id = db.Column(db.String(36), db.ForeignKey('loans.id'), nullable=False)
    lender_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    borrower_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)  
    comments = db.Column(db.Text)
    

    def __repr__(self):
        return f'<LoanReview ID: {self.id}, Rating: {self.rating}>'