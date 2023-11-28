from app.extensions import mysql_pool
class Receipt:
    def __init__(self):
        self.mysql_pool = mysql_pool

    def add_receipt(self, _date, _time, _total_amount):
        params = {
                '_date ' : _date,
                '_time': _time,
                '_total_amount': _total_amount,
        }
        query = 'insert into receipt(date_time, _total_amount) values ( %(date_time)s, %(_total_amount)s)'   
        self.mysql_pool.execute(query, params, commit=True)
        data = {'_date ': _date, '_time': _time, '_total_amount': _total_amount}
        return data
    
    def get_receipt(self, id_receipt):
        params = {'id_receipt' : id_receipt}
        cursor = self.mysql_pool.execute('select id_receipt, _date, _time, _total_amount from receipt where id_receipt=%(id_receipt)s', params)
        rv = cursor[0]
        data = {'id_receipt': rv[0], '_date': rv[1], '_time': rv[2],'_total_amount': rv[3]}
        return data
    
    def get_all_receipt(self):
        cursor = self.mysql_pool.execute('select * from receipt')
        data = []
        for rv in cursor:
                content = {'id_receipt': rv[0], '_date': rv[1], '_time': rv[2], '_total_amount': rv[2]}
                data.append(content)
        return data
    
    def get_receipt_by_amount(self, max_amount):
        params = {'max_amount' : max_amount}
        cursor = self.mysql_pool.execute('select id_receipt, _date, _time, _total_amount from receipt where _total_amount < %(amount)s', params)
        data = []
        for rv in cursor:
                content = {'id_receipt': rv[0], '_date': rv[1], '_time': rv[2], '_total_amount': rv[2]}
                data.append(content)
        return data
    
    def get_receipt_by_date(self):
         pass

    def delete_receipt(self, id_receipt):
        params = {'id_receipt' : id_receipt}
        query = 'delete from receipt where id_receipt = %(id_cliente)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data