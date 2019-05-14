# -*- coding: utf-8 -*-
"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
"""


def coffee_questions(coffee_list_from_db, additional_ingridients_from_db):
    coffee_wit_price_list = list(map(lambda el: {"name": el}, coffee_list_from_db))
    additional_ingridients_list = list(map(lambda el: {"name": el}, additional_ingridients_from_db))
    my_coffee_questions = [
        {
            'type': 'checkbox',
            'message': 'Select coffee',
            'name': 'coffee',
            'choices': coffee_wit_price_list,
            'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True
            # check empty answer
        },
        {
            'type': 'checkbox',
            'message': 'Select additional ingredients',
            'name': 'additional ingredients',
            'choices': additional_ingridients_list,
        }
    ] #think about adding ingridients to each of coffee 2. add if no request
    return my_coffee_questions
