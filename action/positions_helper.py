from db.db_helper import DBHelper
from reporting import create_table
import constants as const


class PositionsHelper:
    def __init__(self):
        self.db_helper = DBHelper("test_db_cofee.db")

    def get_all_salesmans(self):
        return self.db_helper.all_salesmans()

    def give_a_bill(self, sale_info_dict):
        columns, rows = [], []
        total_price, quantity, currency_type = self._get_total_price_and_currency_type_for_coffee(
            sale_info_dict)

        for key in sale_info_dict:
            if key == const.BILL:
                continue
            if type(sale_info_dict.get(key)) is list:
                columns.append(key)
                rows.append(f"{', '.join(sale_info_dict[key])}")
            else:
                columns.append(key)
                rows.append(sale_info_dict[key])
        columns.append("Total")
        rows.append(f"{total_price} {currency_type}")
        res = create_table(rows, columns)
        print(res)
        self._save_last_order_in_file(res)
        #     # what about empty additional ingredients(in bill)

    @staticmethod
    def _save_last_order_in_file(table):
        with open("bill.txt", "w") as f:
            f.write(table)

    @staticmethod
    def _get_total_price_and_currency_type_for_coffee(sale_info_dict):
        coffee_with_price = sale_info_dict[
            "coffee type"]  # what if dont have ingredients
        quantity = sale_info_dict["quantity"]
        split_coffee_with_price = coffee_with_price.split()
        price_for_coffee = int(split_coffee_with_price[1])
        currency_type = split_coffee_with_price[-1]
        total_value_for_coffee = price_for_coffee * quantity
        return total_value_for_coffee, quantity, currency_type  # think about summ of diff currency

    def get_el_from_summary_table_by_username(self, column_name, name):
        res = self.db_helper.get_element_from_total_table_for_salesman(
            column_name, name)
        return 0 if not res else res

    def update_summary_table_by_name(self, column_name, name, sale_info_dict):
        curr_total, quantity, *rest = self._get_total_price_and_currency_type_for_coffee(
            sale_info_dict)
        if column_name == "total":
            new_total_value = self.get_el_from_summary_table_by_username(
                column_name, name) + curr_total
            self.db_helper.update_data_in_summary_table(column_name, name,
                                                        new_total_value)
        elif column_name == "number_of_sales":
            new_number_of_sales_value = self.get_el_from_summary_table_by_username(
                column_name, name) + quantity
            self.db_helper.update_data_in_summary_table(column_name, name,
                                                        new_number_of_sales_value)

