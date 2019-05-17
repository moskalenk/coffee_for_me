from roles.common_type import Common
from action.positions_helper import PositionsHelper


class Salesman(Common):
    def __init__(self, name, position="salesman"):
        super().__init__(name, position)
        self.position_helper = PositionsHelper()

    def get_all_coffee_with_price(self):
        return self.position_helper.db_helper.all_coffee_with_price()

    def get_all_additional_ingredients(self):
        return self.position_helper.db_helper.all_additional_ingredients()

    def get_bill(self, sale_ifo_dict):
        self.position_helper.create_and_print_bill(sale_ifo_dict)
