from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    from app.models.admin import Admin  
    from app.models.interaction_log import InteractionLog
    from app.models.loan import Loan
    from app.models.loan_review import LoanReview
    from app.models.payment import Payment
    from app.models.user import User


    return app