import _mysql_connector
import os
from dotenv import load_dotenv

class Database:

    load_dotenv()

    def conectar(self):

        return _mysql_connector(
            host =      os.detenv("DB_HOST"),
            port =      os.getenv("DB_PORT"),
            database =  os.getenv("DB_NAME"),
            user =      os.getenv("DB_USER"),
            password =  os.getenv("DB_PASSWORD")
        )