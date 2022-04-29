from app.models import db
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(db.Model):
    __tablename__ = 'produtos_alimenticios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    protein = db.Column(db.Integer, unique=False, nullable=False)
    carbohydrate = db.Column(db.Integer, unique=False, nullable=False)
    fat = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, quantity, protein, carbohydrate, fat):
        self.name = name
        self.quantity = quantity
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
        # return {"id": self.id, "quantity": self.quantity, "protein": self.protein, "carbohydrate": self.carbohydrate,
        #         "fat": self.fat}

    def __repr__(self):
        return '<Product %r>' % self.name
