from flask import Blueprint, request, jsonify
from models import db, Nota

notas_bp = Blueprint('notas', __name__)

# Criar nota
@notas_bp.route('/', methods=['POST'])
def criar_nota():
    dados = request.get_json()
    nota = Nota(
        titulo=dados['titulo'],
        conteudo=dados['conteudo'],
        privada=dados.get('privada', True)
    )
    db.session.add(nota)
    db.session.commit()
    return jsonify({'mensagem': 'Nota criada', 'id': nota.id}), 201

# Listar todas as notas
@notas_bp.route('/', methods=['GET'])
def listar_notas():
    notas = Nota.query.all()
    resultado = []
    for nota in notas:
        resultado.append({
            'id': nota.id,
            'titulo': nota.titulo,
            'conteudo': nota.conteudo,
            'privada': nota.privada
        })
    return jsonify(resultado)

# Buscar nota por palavra-chave
@notas_bp.route('/buscar', methods=['GET'])
def buscar_nota():
    termo = request.args.get('q', '')
    notas = Nota.query.filter(
        (Nota.titulo.ilike(f'%{termo}%')) | (Nota.conteudo.ilike(f'%{termo}%'))
    ).all()
    
    resultado = []
    for nota in notas:
        resultado.append({
            'id': nota.id,
            'titulo': nota.titulo,
            'conteudo': nota.conteudo,
            'privada': nota.privada
        })
    return jsonify(resultado)

# Editar/Atualizar nota
@notas_bp.route('/<int:id>', methods=['PUT'])
def atualizar_nota(id):
    dados = request.get_json()
    nota = Nota.query.get_or_404(id)
    nota.titulo = dados.get('titulo', nota.titulo)
    nota.conteudo = dados.get('conteudo', nota.conteudo)
    nota.privada = dados.get('privada', nota.privada)
    db.session.commit()
    return jsonify({'mensagem': 'Nota atualizada'})

# Deletar nota
@notas_bp.route('/<int:id>', methods=['DELETE'])
def deletar_nota(id):
    nota = Nota.query.get_or_404(id)
    db.session.delete(nota)
    db.session.commit()
    return jsonify({'mensagem': 'Nota deletada'})
