from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

DB_URI = 'sqlite:///app.db'
# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf-8'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE) 
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# Issues fixed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
