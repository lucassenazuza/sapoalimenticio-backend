# Script criado para popular base de dados pelos arquivos txt fornecidos na pasta alimentos
import os
import re

from flask_sqlalchemy import SQLAlchemy

from app.models import save_data
from app.models.product_model import Product
from settings import ROOT_PATH


class Script:
    def __init__(self):
        # ler arquivos pasta alimentos
        self.path_txt_folder = os.path.join(ROOT_PATH, "alimentos")
        # Só adicionamos fazemos a leitura dos arquivos com formato arquivo[0-9]*
        self.list_dir = [file for file in os.listdir(self.path_txt_folder) if
                         bool(re.match(r"arquivo_[0-9]*.txt", file))]
        ...

    def populate_db(self):
        for file_txt in self.list_dir:
            file_txt_path = os.path.join(self.path_txt_folder, file_txt)
            # df = pd.read_csv(file_txt_path, sep='\n', header=[0,1]).columns
            with open(file_txt_path) as file:
                lines = file.readlines()
                for i in range(2, len(lines)):
                    product = lines[i].split()
                    #Coloca Palavras maiúsculas primeiro
                    product_name = " ".join(product[:-4])
                    product_quantity = int(product[-4])
                    product_proteins = int(product[-3])
                    product_carbohydrate = int(product[-2])
                    product_fat = int(product[-1])
                    product = Product(product_name, product_quantity, product_proteins, product_carbohydrate, product_fat)
                    save_data(product)

# script = Script()
# script.populate_db()
