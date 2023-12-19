#from .Menu import Menu
from .Menu_Item import MenuItem
#from ..extensions import menu_item_model

class MenuController:
    def __init__(self):
        #self.menu_database = Menu()
        
        self.menu_item_database = MenuItem()
        #self.menu_item_database = menu_item_model
        self.menu = {
            'id_menu': '',
            'name': '',
            'description':'',
            'items': {},
            'active': False
            }
        self.items = {}
        self.active = False
    
    #def get_complete_menu(self):
    def get_current_menu_and_items(self):
        print("Menu controller: get_complete_menu")
        return self.menu
    
    #esta funcion sera reemplazada por una ruta en la API
    #def get_menus(self):
    #    print("Menu controller: get_menus")
    #    return self.menu_database.get_all_menu() #devuelve un array de objetos menu
    
    def set_current_menu(self, menu):
        print("Menu controller: set_current_menu")
        print("menu", menu)
        self.menu = menu
        self.menu['items'] = {}
        items = self.menu_item_database.get_all_item_from_menu(menu['id_menu'])
        print("controller items", items)
        for item in items:
            self.menu['items'][item['id_item']] = item
            self.menu['items'][item['id_item']]['amount'] = 0
            self.menu['items'][item['id_item']]['enabled'] = False
        #self.active = True
        self.menu['active'] = True
        return self.menu

    def enable_item(self, id_item, amount):
        print("Menu controller: enable_item")
        self.menu['items'][id_item]['amount'] = amount
        self.menu['items'][id_item]['enabled'] = True
    
    def disable_item(self, id_item):
        print("Menu controller: disable_item")
        self.menu['items'][id_item]['enabled'] = False


    
    #Cliente
    def get_ready_menu(self):
        print("Menu controller: get_ready_menu")
        ready_menu_items = {}
        for item in self.menu['items'].values():
            if(item['amount'] > 0 and item['enabled'] == True):
                ready_menu_items[item['id_item']] = item.copy()
                ready_menu_items[item['id_item']]['amount'] = 0
        return ready_menu_items

    def check_order(self, order):
        cero_item = []
        for order_item in order['items'].values():
            if(order_item['amount'] > 0):
                if(self.menu['items'][order_item['id_item']]['amount'] < order_item['amount']):
                    return False
            else:
                cero_item.append(order_item['id_item'])
                #order['items'].pop(order_item['id_item'], True)
        for id_item in cero_item:
            order['items'].pop(id_item, True)

        #print("Menu controller: check_order entre for", order)
        for order_item in order['items'].values():
            if(order_item['amount'] > 0):
                self.menu['items'][order_item['id_item']]['amount'] = self.menu['items'][order_item['id_item']]['amount'] - order_item['amount']

        #print("self.menu.items", self.menu['items'])
        return True
    
    
    def check_enable_menu(self):
        for item in self.menu['items'].values():
            if(item['enabled'] == True):
                return True
        self.menu['active'] = False
        return False


    





    


    
    #esta no esta siendo usada
    def get_all_items_from_menu(self, id_menu):
        print("Menu controller: get_all_items_from_menu")
        return self.menu_item_database.get_all_item_from_menu(id_menu) #devuelve un array de objetos item
    