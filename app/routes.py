from flask import Blueprint, jsonify, request
from .extensions import menu_model

bp = Blueprint('main', __name__)

@bp.route('/api/get_menus', methods=['GET'])
def get_menus():
    #esta funcion retora todos los menus
    #devuelve su nombre, descripcion, cantidad de platos
    #content = user_model.login(request.json['email'], request.json['password_'])
    #return jsonify(content)
    print("aPI get_menus")
    return jsonify(menu_model.get_all_menu())