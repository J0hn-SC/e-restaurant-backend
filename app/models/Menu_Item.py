from app.extensions import mysql_pool
class MenuItem:
    def __init__(self):
        self.mysql_pool = mysql_pool

    def add_menu_item(self, id_menu, id_item):
        params = {
                'id_menu': id_menu,
                'id_item': id_item,
        }
        query = 'insert into menu_item(id_menu, id_item) values ( %(id_menu)s, %(id_item)s)'
        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'id_menu': id_menu, 'id_item': id_item}
        return data
    
    def get_item_from_menu(self, id_menu, id_item):
        params = {
             'id_menu' : id_menu,
             'id_item' : id_item
        }
        cursor = self.mysql_pool.execute('''
            select item.id_item, item._name, item._type, item._description, item._price, item._image
            from menu_item
            inner join item on menu_item.id_item = item.id_item 
            where menu_item.id_menu =%(id_menu)s and menu_item.id_item =%(id_item)s '''
            , params)
        rv = cursor[0]
        data = {'id_item': rv[0], 'name': rv[1], 'type': rv[2], 'description': rv[3], 'price': rv[4], 'image': rv[5]}
        return data
    
    def get_all_item_from_menu(self, id_menu):
        params = {
             'id_menu' : id_menu,
        }
        cursor = self.mysql_pool.execute('''
            select item.id_item, item._name, item._type, item._description, item._price, item._image
            from menu_item
            inner join item on menu_item.id_item = item.id_item 
            where menu_item.id_menu =%(id_menu)s'''
            , params)
        data = []
        for rv in cursor:
                content = {'id_item': str(rv[0]), 'name': rv[1], 'type': rv[2], 'description': rv[3], 'price': rv[4], 'image': rv[5]}
                data.append(content)
        return data
    def delete_menu_item(self, id_menu_item):
        params = {'id_menu_item' : id_menu_item}
        query = 'delete from menu_item where id_menu_item = %(id_cliente)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data
    