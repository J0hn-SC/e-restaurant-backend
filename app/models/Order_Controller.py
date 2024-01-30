class OrderController:
    def __init__(self):
        self.id_new_order = 1
        self.orders = {} #almacenara todas las ordenes con sus datos
        #el resto de listas solo almacenaran IDs
        self.orders_queue = []
        #este almacenara ids pero por mesa
        self.summary_table = {}
        #los state dentro de orders_queue van de 0 a 3 por donde estan
        #podemos simular el orden de llegada por el id_order, ya q si llega despues sera mayor
        #entonces en lugar de simular un array se puede usar un diccionario
        self.waiting = []
        self.preparating = []
        self.ready = []
        self.commited = []
        self.finished = []

    def add_order(self,order):
        order['id_order'] = self.id_new_order
        self.id_new_order += 1
        order['state'] = 0
        self.orders[order['id_order']] = order.copy()
        self.orders_queue.insert(0, order['id_order'])
        self.waiting.append(order['id_order'])
        table = self.summary_table.get(order['id_table'])
        if table is not None:
            table.append(order)
        else:
            self.summary_table[order['id_table']] = [order]
        
        print("add order orders", self.orders)
        print("add order queue", self.orders_queue)
        print("add order waiting", self.waiting)
        return order
    
    #now it's all the order but is should be only the id_order
    def order_waiting_to_preparating(self, change_order):
        self.orders[change_order['id_order']]['state'] = 1
        self.waiting.remove(change_order['id_order'])
        
        self.preparating.append(change_order['id_order'])

        table = self.summary_table[change_order['id_table']]
        for order in table:
            if(order['id_order'] == change_order['id_order']):
                order['state'] = 1


    def order_preparating_to_ready(self, change_order):
        print("change order preparating", self.preparating)
        print("change order ready", self.ready)
        self.orders[change_order['id_order']]['state'] = 2
        self.preparating.remove(change_order['id_order'])
        self.ready.append(change_order['id_order'])
        #print("add order orders", self.orders)
        print("change preparating", self.preparating)
        print("change order ready", self.ready)

        table = self.summary_table[change_order['id_table']]
        for order in table:
            if(order['id_order'] == change_order['id_order']):
                order['state'] = 2

        return self.orders[change_order['id_order']]

    def order_ready_to_commited(self, change_order):
        self.orders[change_order['id_order']]['state'] = 3
        self.ready.remove(change_order['id_order'])
        self.commited.append(change_order['id_order'])

        table = self.summary_table[change_order['id_table']]
        for order in table:
            if(order['id_order'] == change_order['id_order']):
                order['state'] = 3
    
    def order_ready_to_finished(self, change_order):
        self.orders[change_order['id_order']]['state'] = 4
        self.commited.remove(change_order['id_order'])
        self.finished.append(change_order['id_order'])

        table = self.summary_table[change_order['id_table']]
        for order in table:
            if(order['id_order'] == change_order['id_order']):
                order['state'] = 4

    def get_summary(self):
        summary = []
        for id_order in self.orders_queue:
            summary.append(
                {'id_order': id_order,
                'id_table': self.orders[id_order]['id_table'],
                'n_items': len(self.orders[id_order]['items']),
                'time': self.orders[id_order]['time'],
                'state': self.orders[id_order]['state']
                })
        return summary

    def get_summary_order(self, order):
        return {'id_order': order['id_order'],
                'id_table': order['id_table'],
                'n_items': len(order['items']),
                'time': order['time'],
                'state': 0
                }
    
    def get_summary_all_table(self):
        return self.summary_table
    
    def get_summary_table(self, id_table):
        print(self.summary_table)
        print("por mesa: ", self.summary_table[id_table])
        return self.summary_table[id_table]
    

    def get_all_waiting_order(self):
        waiting_orders = []
        for id_order in self.waiting:
            waiting_orders.append(self.orders[id_order])
        print("all waiting orders", waiting_orders)
        return waiting_orders
    
    def get_all_preparating_order(self):
        preparating_orders = []
        for id_order in self.preparating:
            preparating_orders.append(self.orders[id_order])
        return preparating_orders
    
    def get_all_ready_order(self):
        ready_orders = []
        for id_order in self.ready:
            ready_orders.append(self.orders[id_order])
        print("all ready orders", ready_orders)
        return ready_orders
    
    def get_all_commited_order(self):
        commited_orders = []
        for id_order in self.commited:
            commited_orders.append(self.orders[id_order])
        return commited_orders

