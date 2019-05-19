from db.connection import DBConnection


class CafeDB(DBConnection):

    def get_names_by_role(self, role):
        d = {"salesman": self.select_as_list(f"SELECT name FROM sellers"),
             "manager": self.select_as_list("SELECT name FROM managers")}
        return d[role]

    def get_coffee_with_price(self):
        """
        :return: string with 'coffee name', price value' and currency type'. Ex "Latte 4 USD"
        """
        return self.select_as_list("SELECT coffee.name, coffee.price, currency.name\
                                          FROM\
                                          coffee JOIN currency ON coffee.currency_id=currency.id")

    def get_additional_ingredients_list(self):
        return self.select_as_list("SELECT name FROM ingredients")

    def get_element_from_total_table_for_salesman(self, column_name, name):
        """
        Try to get result by using salesman name and name of necessary column
        :param column_name: 'total' or 'number_of_sales'
        :param name:
        :return:
        """
        id_by_name = self._get_id_by_name(name)
        return self.select_one(f"SELECT {column_name}\
                                FROM summary\
                                WHERE id={id_by_name}")

    def _get_id_by_name(self, name):
        return self.select_one(f"SELECT seller_name_id\
                                FROM sellers\
                                JOIN summary ON sellers.id=summary.seller_name_id\
                                WHERE name='{name}'")

    def update_data_in_summary_table(self, column_name, name, new_value):
        id_by_name = self._get_id_by_name(name)
        return self.execute_and_commit(f"UPDATE summary\
                                        SET '{column_name}'={new_value}\
                                        WHERE id={id_by_name}")

    def get_total(self):
        return self.select("SELECT name, number_of_sales, total\
                                    FROM\
                                    sellers join summary on sellers.id=summary.seller_name_id")