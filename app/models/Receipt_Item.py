from app.extensions import mysql_pool
class ReceiptItem:
    def __init__(self):
        self.mysql_pool = mysql_pool

    def add_receipt_item(self, id_receipt, id_item):
        params = {
                'id_receipt': id_receipt,
                'id_item': id_item,
        }
        query = 'insert into receipt_item(id_receipt, id_item) values ( %(id_receipt)s, %(id_item)s)'
        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'id_receipt': id_receipt, 'id_item': id_item}
        return data
    
    def get_item_from_receipt(self, id_receipt, id_item):
        params = {
             'id_receipt' : id_receipt,
             'id_item' : id_item
        }
        cursor = self.mysql_pool.execute('''
            select item.id_item, item._name, item._type, item._description, item._price, item._image
            from receipt_item
            inner join item on receipt_item.id_item = item.id_item 
            where receipt_item.id_receipt =%(id_receipt)s and receipt_item.id_item =%(id_item)s '''
            , params)
        rv = cursor[0]
        data = {'id_item': rv[0], 'name': rv[1], 'type': rv[2], 'description': rv[3], 'price': rv[4], 'image': rv[5]}
        return data
    
    def get_all_item_from_receipt(self, id_receipt):
        params = {
             'id_receipt' : id_receipt,
        }
        cursor = self.mysql_pool.execute('''
            select item.id_item, item._name, item._type, item._description, item._price, item._image
            from receipt_item
            inner join item on receipt_item.id_item = item.id_item 
            where receipt_item.id_receipt =%(id_receipt)s'''
            , params)
        data = []
        for rv in cursor:
                content = {'id_item': str(rv[0]), 'name': rv[1], 'type': rv[2], 'description': rv[3], 'price': rv[4], 'image': rv[5]}
                data.append(content)
        return data
    def delete_receipt_item(self, id_receipt_item):
        params = {'id_receipt_item' : id_receipt_item}
        query = 'delete from receipt_item where id_receipt_item = %(id_cliente)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data