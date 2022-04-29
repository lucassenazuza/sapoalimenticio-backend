from flask_restful import Resource

from app import Log
from app.services.product_service import ProductService

product_service = ProductService()
LOG = Log(__name__)

from app import Log
from app.constants import Messages
from app.models.product_model import Product
from app.services.scripts.script_populate_db import Script

LOG = Log(__name__)


class PopulateDB(Resource):
    def get(self):
        try:
            LOG.info("Populando banco com dados na pasta alimentos")
            product_list = product_service.populate_db()
            return {"msg": "Banco populado com sucesso"}, 201
        except:
            return {"msg": "Problema ao Popular Banco"}, 500

class AllProductsController(Resource):
    def get(self):
        LOG.info("Buscano todos produtos")
        product_list = []
        try:
            product_list = product_service.get_all_products()
            return {"msg": Messages.SUCCESSFUL_SEARCH.value, "products": product_list}, 200
        except:
            msg = Messages.FAILED_SEARCH.value + "todos"
            LOG.error(msg)
            return {"msg": msg}, 500


class CarbohydrateController(Resource):
    def get(self):
        LOG.info("Buscano Produtos com mais Carboidratos")
        product_list = []
        try:
            product_list = product_service.get_carbo()
            return {"msg": Messages.SUCCESSFUL_SEARCH.value, "products": product_list}, 200
        except:
            msg = Messages.FAILED_SEARCH.value + "carboidrato"
            LOG.error(msg)
            return {"msg": msg}, 500

class ProteinController(Resource):
    def get(self):
        LOG.info("Buscano Produtos com mais Proteinas")
        product_list = []
        try:
            product_list = product_service.get_protein()
            return {"msg": Messages.SUCCESSFUL_SEARCH.value, "products": product_list}, 200
        except:
            msg = Messages.FAILED_SEARCH.value + "proteina"
            LOG.error(msg)
            return {"msg": msg}, 500

class FatController(Resource):
    def get(self):
        LOG.info("Buscano Produtos com mais Gordura")
        product_list = []
        try:
            product_list = product_service.get_fat()
            return {"msg": Messages.SUCCESSFUL_SEARCH.value, "products": product_list}, 200
        except:
            msg = Messages.FAILED_SEARCH.value + "gordura"
            LOG.error(msg)
            return {"msg": msg }, 500
