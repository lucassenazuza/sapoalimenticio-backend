from app.controllers.product_controller import PopulateDB, CarbohydrateController, ProteinController, FatController, \
    AllProductsController


def initialize_routes(app, api):
    api.add_resource(PopulateDB, '/populate')
    api.add_resource(AllProductsController, '/allproducts')
    api.add_resource(CarbohydrateController, '/listcarbo')
    api.add_resource(ProteinController, '/listprotein')
    api.add_resource(FatController, '/listfat')
    api.init_app(app)
