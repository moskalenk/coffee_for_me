from action.common_type import Common
from db.db_helper import DBHelper

from action.positions_helper import PositionsHelper


class Salesman(Common):
    def __init__(self, name, position="salesman"):
        super().__init__(name, position)
        self.db_helper = DBHelper("db_coffee_for_me.db")
        # self.db_helper = DBHelper("test_db_cofee.db")
        self.position_helper = PositionsHelper()

    def get_all_coffee_with_price(self):
        return self.db_helper.all_coffee_with_price()

    def get_all_additional_ingredients(self):
        return self.db_helper.all_additional_ingredients()

    def get_bill(self, sale_ifo_dict):
        self.position_helper.give_a_bill(sale_ifo_dict)
