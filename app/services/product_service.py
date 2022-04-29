from app import Log
from app.constants import Messages
from app.models.product_model import Product
from app.models import save_data
from app.services.scripts.script_populate_db import Script

LOG = Log(__name__)


class ProductService:
    def __init__(self):
        ...

    def populate_db(self):
        try:
            script = Script()
            script.populate_db()
        except Exception as e:
            LOG.error("Erro ao tentar popular o banco")
            raise e

    def get_carbo(self):
        try:
            products_list = Product.query.filter(Product.carbohydrate > Product.protein, Product.carbohydrate > Product.fat).all()
            return [product.as_dict() for product in products_list]
        except Exception as e:
            msg = Messages.FAILED_SEARCH.value + "carboidrato"
            LOG.error(msg)
            raise e

    def get_protein(self):
        try:
            products_list = Product.query.filter(Product.protein > Product.carbohydrate, Product.protein > Product.carbohydrate).all()
            return [product.as_dict() for product in products_list]
        except Exception as e:
            msg = Messages.FAILED_SEARCH.value + "gordura"
            LOG.error(msg)
            raise e

    def get_fat(self):
        try:
            products_list = Product.query.filter(Product.fat > Product.protein, Product.fat > Product.carbohydrate).all()
            return [product.as_dict() for product in products_list]
        except Exception as e:
            msg = Messages.FAILED_SEARCH.value + "gordura"
            LOG.error(msg)
            raise e

    def get_all_products(self):
        try:
            products_list = Product.query.all()
            return [product.as_dict() for product in products_list]
        except Exception as e:
            msg = Messages.FAILED_SEARCH.value + "todos"
            LOG.error(msg)
            raise e
