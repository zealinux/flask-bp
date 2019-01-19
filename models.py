
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

db = SQLAlchemy()

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
