from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Initialize the Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Include our Routes/Apps
        from .authentication import routes
        from .home import routes

        # Register Blueprints
        app.register_blueprint(authentication.routes.auth_bp)
        app.register_blueprint(home.routes.home_bp)

        return app
