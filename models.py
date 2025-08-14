from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    privada = db.Column(db.Boolean, default=True)