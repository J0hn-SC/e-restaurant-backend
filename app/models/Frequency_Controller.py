class FrequencyController:
    def __init__(self):
        self.items = {}
        self.max_order = 1

    def set_items(self, items):
        #self.items = items.copy()
        for item in items.values():
            self.items[item['id_item']] = item.copy()
            self.items[item['id_item']]['amount'] = 0
            self.items[item['id_item']]['percentage'] = 0

    def add_order(self, order):
        #print("desde add order frequency self.items", self.items)
        for item in order['items']:
            self.items[item['id_item']]['amount'] += item['amount']
            if(self.items[item['id_item']]['amount'] > self.max_order):
                self.max_order = self.items[item['id_item']]['amount']
    
    def set_percentage(self):
        for item in self.items.values():
            item['percentage'] =  round((item['amount'] / self.max_order) * 100)
    
    def get_list_of_frequency(self):
        self.set_percentage()
        list_keys = list(self.items.values())
        return sorted(list_keys, key=lambda x: x['amount'], reverse=True)