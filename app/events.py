from flask import request
from flask_socketio import emit

from .extensions import socketio
##from .models.Menu_Controller import MenuController
#from .models.Order_Controller import OrderController
#from .models.Order_Controller import Order
#from .models.Frequency_Controller import FrequencyController
##from .controllers import menu_controller
##from .controllers import order_controller
##from .controllers import frequency_controller

#administrador
#MenuView
#from extensions import menu_model
@socketio.on("get-complete-menu")
def get_current_menu_and_items():
    #print("Evento: get-complete-menu", menu_controller.get_complete_menu())
    #emit('get-complete-menu', menu_controller.get_complete_menu(), broadcast=True)
    emit('get-complete-menu', menu_controller.get_current_menu_and_items(), broadcast=True)

@socketio.on("get-menus")
def get_menus():
    print("Evento: get-menus")
    emit('get-menus', menu_controller.get_menus(), broadcast=True)
    #emit('get-menus', menu_model.get_all_menu(), broadcast=True)

@socketio.on("set-menu")
def set_menu(menu):
    current_menu = menu_controller.set_current_menu(menu)
    print("Evento: set-menu", current_menu)
    frequency_controller.set_items(current_menu['items'])
    print("Frequency controller",frequency_controller.get_list_of_frequency())
    emit('get-complete-menu',menu_controller.get_current_menu_and_items() , broadcast=True)
    emit('set-frequency', frequency_controller.get_list_of_frequency(), broadcast=True)

@socketio.on("enable-item")
def enable_item(item):
    print("Evento: enable-item")
    menu_controller.enable_item(item['id_item'], item['amount'])
    item['amount'] = 0
    emit('add-item-to-ready-menu', item , broadcast=True)
    emit('set-active', True , broadcast=True)

@socketio.on("disable-item")
def disable_item(item):
    print("Evento: disable-item")
    menu_controller.disable_item(item['id_item'])
    active = menu_controller.check_enable_menu()
    print("active",active)
    if(not active):
        emit('set-active', False , broadcast=True)