from action.common_type import Common
from lib.db.db_helper import DBHelper


class Salesman(Common):
    def __init__(self, name, position="salesman"):
        super().__init__(name, position)
        self.db_helper = DBHelper("db_coffee_for_me.db")
        # self.db_helper = DBHelper("test_db_cofee.db")

    def get_all_salesmans(self):
        return self.db_helper.all_salesmans()

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

    def save_to_bill(self, sale_info_dict):
        columns = []
        rows = []
        nl = '\n'
        total_price = self._get_total_price_for_coffee(sale_info_dict)

        for key in sale_info_dict:
            if type(sale_info_dict.get(key)) is list:
                columns.append(key)
                rows.append(f"{', '.join(sale_info_dict[key])}")
            else:
                columns.append(key)
                rows.append(sale_info_dict[key])
        print()
        # with open("bill.txt", "w") as f:
        #     for key in sale_info_dict:
        #         if type(sale_info_dict.get(key)) is list:
        #             f.write(f"{key}: {', '.join(sale_info_dict[key])}{nl}")
        #         else:
        #             f.write(f"{key}: {sale_info_dict[key]}{nl}")
        #     f.write(f"Total price: {total_price}")

    @staticmethod
    def _get_total_price_for_coffee(sale_info_dict):
        coffee_with_price = sale_info_dict["coffee type"]
        quantity = sale_info_dict["quantity"]
        split_coffee_with_price = coffee_with_price.split()
        price_for_coffee = int(split_coffee_with_price[1])
        currency_type = split_coffee_with_price[-1]
        return f"{price_for_coffee * quantity} {currency_type}" #think about summ of diff currency


    # def add_to_db(self, name, coffee_count, answers):
    def add_to_db(self, name):
        id_by_name = self.db_helper.get_id_by_name(name)

    def num_of_sales(self):
        res = self.db_helper.number_of_sales_for_salesman("Bob")
        return 0 if res is None else res


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
