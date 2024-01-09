from flask import request
from flask_socketio import emit

from .extensions import socketio
##from .models.Menu_Controller import MenuController
#from .models.Order_Controller import OrderController
#from .models.Order_Controller import Order
#from .models.Frequency_Controller import FrequencyController
from .controllers import menu_controller
from .controllers import order_controller
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
    #frequency_controller.set_items(current_menu['items'])
    #print("Frequency controller",frequency_controller.get_list_of_frequency())
    emit('get-complete-menu',menu_controller.get_current_menu_and_items() , broadcast=True)
    #emit('set-frequency', frequency_controller.get_list_of_frequency(), broadcast=True)

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


#Cliente
@socketio.on("get-ready-menu")
def get_ready_menu():
    print("Evento: get-ready-menu")
    emit('get-ready-menu', menu_controller.get_ready_menu(), broadcast=True)

@socketio.on("handle-order")
def handle_order(order):
    print("Evento: handle-order")
    if(menu_controller.check_order(order)):
        #print("Antes de emit menu", menu_controller.menu)
        #print("Antes de emit menu solo items", menu_controller.menu['items'])
        new_order = order_controller.add_order(order)
        #frequency_controller.add_order(order)
        #emit('get-complete-menu',menu_controller.get_complete_menu() , broadcast=True)
        emit('get-complete-menu', menu_controller.menu , broadcast=True)
        emit('get-summary-order', order_controller.get_summary_order(new_order), broadcast=True)
        emit('get-waiting-order', new_order, broadcast = True)
        #emit('set-frequency', frequency_controller.get_list_of_frequency(), broadcast=True)
        #tambien se deberia enviar a ordenes en espera
        #este state a continuacion es de la respuesta, se deberia cambiar el state de respues para no
        #confundirlo con el state de en q cola se encuetra
        answer = {}
        answer['state'] = 1
        emit('answer-order', answer)
        print("Evento: handle-order Accept")
    else:
        answer = {}
        answer['state'] = 2
        emit('answer-order', answer)
        print("Evento: handle-order Denied")

#dashboard
@socketio.on("get-summary")
def get_summary():
    print("Evento: get-summary")
    emit('get-summary', order_controller.get_summary(), broadcast=True)



#orders
@socketio.on("get-all-waiting-order")
def get_all_waiting_order():
    print("Evento: get-all-waiting-order")
    emit('get-all-waiting-order', order_controller.get_all_waiting_order(), broadcast=True)

@socketio.on("order-waiting-to-preparating")
def order_waiting_to_preparating(order):
    print("Evento: order-waiting-to-preparating")
    order_controller.order_waiting_to_preparating(order)

@socketio.on("get-all-preparating-order")
def get_all_preparating_order():
    print("Evento: get-all-preparating-order")
    emit('get-all-preparating-order', order_controller.get_all_preparating_order(), broadcast=True)

@socketio.on("order-preparating-to-ready")
def order_preparating_to_ready(change_order):
    print("Evento: order-preparating-to-ready")
    order = order_controller.order_preparating_to_ready(change_order)
    emit('get-ready-order', order, broadcast = True)

#finished orders
@socketio.on("get-all-ready-order")
def get_all_ready_order():
    print("Evento: get-all-ready-order")
    emit('get-all-ready-order', order_controller.get_all_ready_order(), broadcast=True)

@socketio.on("order-ready-to-commited")
def order_ready_to_commited(order):
    print("Evento: order-ready-to-commited")
    order_controller.order_ready_to_commited(order)

@socketio.on("get-all-commited-order")
def get_all_commited_order():
    print("Evento: get-all-commited-order")
    emit('get-all-commited-order', order_controller.get_all_commited_order(), broadcast=True)
