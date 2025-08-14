from flask import Flask
from config import Config
from models import db
from routes import notas_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Registrar as rotas
app.register_blueprint(notas_bp, url_prefix='/notas')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria o banco de dados
    app.run(debug=True)