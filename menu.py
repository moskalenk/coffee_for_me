class Menu:
    def __init__(self, cafe_db):
        self.cafe_db = cafe_db

    def coffee_with_price(self):
        return self.cafe_db.get_coffee_with_price()

    def additional_ingredients(self):
        return self.cafe_db.get_additional_ingredients_list()


