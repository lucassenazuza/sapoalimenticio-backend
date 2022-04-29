import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DB_NAME = os.environ.get("DB_NAME")
ROOT_PATH = os.getcwd()
