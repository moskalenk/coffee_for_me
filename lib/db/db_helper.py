from lib.db.connection import DBConnection


class DBHelper(DBConnection):
    def all_salesmans(self):
        return self.select_as_list("SELECT name FROM salesman")

    def all_coffee(self):
        coffee = self.select("SELECT name FROM coffee")
        return list(map(",".join, coffee))

    def all_coffee_with_price(self):
        return self.select("SELECT coffee.name, CAST(coffee.price AS TEXT), currency.name\
                                    FROM coffee\
                                    JOIN currency ON coffee.currency_id=currency.id")

    def one_coffee_with_price(self, coffee_name):
        return self.select(f"SELECT coffee.name, CAST(coffee.price AS TEXT), currency.name\
                                    FROM coffee\
                                    JOIN currency ON coffee.currency_id=currency.id\
                                    WHERE coffee.name='{coffee_name}'")

    def all_additional_ingredients(self):
        additional_ingredients = self.select("SELECT name FROM ingredients")
        return list(map(",".join, additional_ingredients))

    def all_additional_ingredients_with_price(self):
        return self.select("SELECT ingredients.name, CAST(ingredients.price AS TEXT), currency.name\
                                    FROM ingredients\
                                    JOIN currency ON ingredients.currency_id=currency.id")

    def get_id_by_name(self, name):
        self.select(f"SELECT seller_name_id\
                                FROM salesman\
                                JOIN summary ON salesman.id=summary.seller_name_id\
                                WHERE name='{name}'")

    def number_of_sales_for_salesman(self, name):
        id = self.get_id_by_name(name)
        self.select(f"SELECT number_of_sales\
                                FROM summary\
                                WHERE id='{id}'")


    # def get_coffee_with_price(self):
    #     coffee__price = self.db_helper.execute_command(f"SELECT name, CAST(price as TEXT) FROM coffee") #think about exaeption
    #     return list(map(" - ".join, coffee__price))
    #
    # def get_additional_ingridients_and_price(self):
    #     ingridients__price = self.db_helper.execute_command(f"SELECT name, CAST(price as TEXT) FROM additional_beverage") #think about exaeption
    #     return list(map(" - ".join, ingridients__price))