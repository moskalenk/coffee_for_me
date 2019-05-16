from action.common_type import Common
from lib.db.db_helper import DBHelper

from action.positions_helper import PositionsHelper

# from lib.reporting import create_table


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

    def get_bill(self):
        pass




# text = f"Winners are:{nl}{nl.join(names)}"
#
# print(Salesman("lkd")._get_total_price({'additional ingredients': ['sugar 1 USD', 'cream 2 RYB'], 'coffee': ['Espresso 3 USD']}))
# print(Salesman("lkd").get_all_salesmans())
# print(Salesman("lkd").get_all_additional_ingredients())
# print(Salesman("lkd").get_all_coffee_with_price())
# print(Salesman("lkd").num_of_sales())


# # all_coffee = Salesman("lkd").get_beverage_type()
# # print("espresso" in list(map(",".join, all_coffee)))
# # print(Salesman("lkd").get_additional_ingredients())
#
# # l = [('latte',), ('espresso',), ('cappuccino',)]
# # print(list(map(",".join, l)))
