from app import db
import uuid
from datetime import datetime

class LoanReview(db.Model):
    __tablename__ = 'loan_reviews'
    