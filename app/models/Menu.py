from app.extensions import mysql_pool
class Menu:
    def __init__(self):
        self.mysql_pool = mysql_pool

    def add_menu(self, _name, _description, _n_items):
        params = {
                '_name': _name,
                '_description': _description,
                '_n_items': _n_items
        }
        query = 'insert into menu(_name, _description, _n_items) values ( %(_name)s, %(_description)s, %(_n_items)s)'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'_name': _name, '_description': _description, '_n_items': 0}
        #data = self.mysql_pool.execute('SELECT LAST_INSERT_ID()')
        #print("data: ", data)
        return data
    
    def get_menu(self, id_menu):
        params = {'id_menu' : id_menu}
        cursor = self.mysql_pool.execute('select id_menu, _name, _description, _n_items from menu where id_menu=%(id_menu)s', params)
        rv = cursor[0]
        data = {'id_menu': rv[0], 'name': rv[1], 'description': rv[2], '_n_items': 0}
        return data
    
    def get_menu_by_name(self, name):
        params = {'name' : name}
        cursor = self.mysql_pool.execute('select id_menu, _name, _description, _n_items from menu where _name=%(name)s', params)
        rv = cursor[0]
        data = {'id_menu': rv[0], 'name': rv[1], 'description': rv[2], '_n_items': 0}
        return data
    
    def get_all_menu(self):
        cursor = self.mysql_pool.execute('select * from menu')
        data = []
        for rv in cursor:
                content = {'id_menu': rv[0], 'name': rv[1], 'description': rv[2], 'n_items': rv[3]}
                data.append(content)
        return data
    
    def delete_menu(self, id_menu):
        params = {'id_menu' : id_menu}
        query = 'delete from menu where id_menu = %(id_menu)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data