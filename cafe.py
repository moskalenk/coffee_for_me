from menu import Menu
from db.cafe_db import CafeDB
from processing_service import ProcessingService


class Cafe:
    def __init__(self):
        self.cafe_db = CafeDB("test_db_coffee.db")
        self.menu = Menu(self.cafe_db)
        self.processing_service = ProcessingService(self.cafe_db)

    def list_of_names_by_role(self, role):
        return self.cafe_db.get_names_by_role(role)
