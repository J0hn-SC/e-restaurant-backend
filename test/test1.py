import unittest
import mysql.connector 
from models.Menu_Item import MenuItem  
from extensions import mysql_pool

class TestMenuItemMethods(unittest.TestCase):

    def setUp(self):
        
        self.menu_item = MenuItem()
        self.mysql_pool = mysql_pool  

    def tearDown(self):
        
        pass
        
    def test_add_menu_item(self):
    
        id_menu = 1
        id_item = 8
        try:
            result = self.menu_item.add_menu_item(id_menu, id_item)
            self.assertEqual(result['id_menu'], id_menu)
            self.assertEqual(result['id_item'], id_item)
        except mysql.connector.errors.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print("Duplicate entry error: Test skipped.")
                return
            else:
                raise e


    def test_get_item_from_menu(self):
        
        id_menu = 1
        id_item = 8
        result = self.menu_item.get_item_from_menu(id_menu, id_item)
        print(result)
        self.assertEqual(result['name'], 'Aji de Gallina')
        

    def test_get_all_item_from_menu(self):
        
        id_menu = 1
        result = self.menu_item.get_all_item_from_menu(id_menu)
        print(result)

    def test_delete_menu_item(self):
        
        id_menu_item = 1
        result = self.menu_item.delete_menu_item(id_menu_item)
        self.assertEqual(result['result'], 1)

       

#if __name__ == '__main__':
#    unittest.main()