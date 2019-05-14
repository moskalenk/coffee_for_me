from action.common_type import Common
from lib.db.db_helper import DBHelper


class Salesman(Common):
    def __init__(self, name, position="salesman"):
        super().__init__(name, position)
        self.db_helper = DBHelper("db_coffee_for_me.db")
        # self.db_helper = DBHelper("test_db_cofee.db")

    def get_all_coffee(self):
        return self.db_helper.all_coffee()

    def get_all_coffee_with_price(self):
        all_coffee_with_price = self.db_helper.all_coffee_with_price()
        return list(map(" ".join, all_coffee_with_price))

    def get_one_coffee_with_price(self, coffee_name):
        coffee_with_price = self.db_helper.one_coffee_with_price(coffee_name)
        return list(map(" ".join, coffee_with_price))

    def get_all_additional_ingredients(self):
        return self.db_helper.all_additional_ingredients()

    def get_all_additional_ingredients_with_price(self):
        all_additional_ingredients_with_price = self.db_helper.all_additional_ingredients_with_price()
        return list(map(" ".join, all_additional_ingredients_with_price))

    def save_to_bill(self, sale_info_dict):
        nl = '\n'
        total_price = self._get_total_price(sale_info_dict)
        with open("bill.txt", "w") as f:
            for key in sale_info_dict:
                f.write(f"{key}: {', '.join(sale_info_dict[key])}{nl}")
            f.write(f"Total price: {total_price}")

    @staticmethod
    def _get_total_price(sale_info_dict):
        vals = sale_info_dict.values()
        prices_list = [int(e.split()[1]) for el in vals for e in el]
        return sum(prices_list)#think about summ of diff currency


    # def add_to_db(self, name, coffee_count, answers):
    def add_to_db(self, name):
        id_by_name = self.db_helper.get_id_by_name(name)

    def num_of_sales(self):
        res = self.db_helper.number_of_sales_for_salesman("Bob")
        return 0 if res is None else res


# text = f"Winners are:{nl}{nl.join(names)}"
#
# print(Salesman("lkd")._get_total_price({'additional ingredients': ['sugar 1 USD', 'cream 2 RYB'], 'coffee': ['Espresso 3 USD']}))
# print(Salesman("lkd").get_all_coffee())
# print(Salesman("lkd").get_all_additional_ingredients())
# print(Salesman("lkd").get_all_coffee_with_price())
print(Salesman("lkd").num_of_sales())


# # all_coffee = Salesman("lkd").get_beverage_type()
# # print("espresso" in list(map(",".join, all_coffee)))
# # print(Salesman("lkd").get_additional_ingredients())
#
# # l = [('latte',), ('espresso',), ('cappuccino',)]
# # print(list(map(",".join, l)))
