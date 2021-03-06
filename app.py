
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

from models import db, User

# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = 'localhost'
    PORT = 3306
    DATABASE = 'test1'

    # Note: charset='utf8'|'utf8mb4' not 'utf-8
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    # Issues fixed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    return app

app = create_app()
migrate = Migrate(app, db)

# if __name__ == '__main__':
#     app.run()
