from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['BABEL_DEFAULT_LOCALE'] = 'de'
    
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(['en', 'de'])

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        from .routes.faehigkeit_routes import faehigkeit_bp
        app.register_blueprint(faehigkeit_bp, url_prefix='/faehigkeit')
        db.create_all()

    return app