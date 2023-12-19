from flask import Flask 
from flask_cors import CORS
#from .events import socketio
#from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    #app.register_blueprint(main)
    CORS(app, origins=['*','http://localhost:8080/', 'http://localhost:8081/'])
    CORS(app)
    #app.register_blueprint(bp)
    #socketio.init_app(app)

    return app