
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def save_data(model_object):
    try:
        db.session.add(model_object)
        db.session.commit()
    except Exception as e:
        raise e