from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db

# Import routes (we’ll create them next)
from routes.contract_routes import contract_bp
from routes.validation_routes import validation_bp
from routes.diff_routes import diff_bp
from routes.ai_routes import ai_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS (for React later)
    CORS(app)

    # Initialize DB
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(contract_bp, url_prefix="/contracts")
    app.register_blueprint(validation_bp, url_prefix="/validate")
    app.register_blueprint(diff_bp, url_prefix="/diff")
    app.register_blueprint(ai_bp, url_prefix="/ai")
    
    @app.route("/test")
    def test():
        return "Working!"
    # Create DB tables
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)