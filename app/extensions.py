from .models.connection_pool import MySQLPool
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins='*')
mysql_pool = MySQLPool()


from .models.Menu import Menu

menu_model = Menu()