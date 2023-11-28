from app import create_app, socketio
from test import suite

app = create_app()

socketio.run(app)