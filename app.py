
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

db = SQLAlchemy()

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

class BaseMixin(object):
    id =            db.Column(db.Integer, primary_key=True)
    created_at =    db.Column(db.DateTime, default=datetime.now)
    updated_at =    db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        cols = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for k, v in cols.items():
            if isinstance(v, datetime):
                cols[k] = v.strftime("%Y-%m-%d %H:%M:%S")
        return cols

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        pass

class User(db.Model, BaseMixin):
    # __tablename__ = 'users'
    name = db.Column(db.String(128))
    gender = db.Column(db.String(8))

# if __name__ == '__main__':
#     app.run()
