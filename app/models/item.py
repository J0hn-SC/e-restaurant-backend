#from ..extensions import mysql_pool
from ..extensions import mysql_pool
class Item:
    def __init__(self):
        self.mysql_pool = mysql_pool

    def add_item(self, _name, _type, _description, _price, _image):
        params = {
                '_name': _name,
                '_type': _type,
                '_description': _description,
                '_price': _price,
                '_image': _image,
        }
        query = 'insert into item(_name, _type, _description, _price, _image) values ( %(_name)s, %(_type)s, %(_description)s, %(_price)s, %(_image)s)'
        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'_name': _name, '_type': _type, '_description': _description, '_price': _price, '_image': _image}    
        return data
    def get_item(self, id_item):
        params = {'id_item' : id_item}
        cursor = self.mysql_pool.execute('select id_item, _name, _type, _description, _price, _image from item where id_item=%(id_item)s', params)
        rv = cursor[0]
        data = {'id_item': rv[0], '_name': rv[1], '_type': rv[2], '_description': rv[3], '_price': rv[4], '_image': rv[5]}
        return data
    def get_all_item(self):
        cursor = self.mysql_pool.execute('select * from item')
        data = []
        for rv in cursor:
                content = {'id_item': rv[0], '_name': rv[1], '_type': rv[2], '_description': rv[3], '_price': rv[4], '_image': rv[5]}
                data.append(content)
        return data
    def delete_item(self, id_item):
        params = {'id_item' : id_item}
        query = 'delete from item where id_item = %(id_cliente)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data