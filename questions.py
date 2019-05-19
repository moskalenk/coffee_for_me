"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
"""
from PyInquirer import Validator, ValidationError
import re
import constants as const

from roles import Salesman


class NumberValidator(Validator):
    def validate(self, document):
        ok = re.match('^[1-9]$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a number(from 1 to 9)',
                cursor_position=len(document.text))  # Move cursor to end


def ask_questions(role):
    if isinstance(role, Salesman):
        return salesman_questions
    else:
        raise NotImplementedError(f"There is no implementation for your role")


def salesman_questions(coffee_list_from_db, additional_ingredients_from_db):
    coffee_wit_price_list = list(map(lambda el: {"name": el}, coffee_list_from_db))
    additional_ingridients_list = list(map(lambda el: {"name": el}, additional_ingredients_from_db))
    my_coffee_questions = [
        {
            'type': 'list',
            'message': 'What coffee do you need',
            'name': const.COFFEE_TYPE,
            'choices': coffee_wit_price_list
            # 'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True
            # check empty answer
        },
        {
            'type': 'input',
            'name': const.QUANTITY,
            'message': 'Count of servings do you need?',
            'validate': NumberValidator,
            # 'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True,
            'filter': lambda val: int(val)
        },
        {
            'type': 'checkbox',
            'message': 'Select additional ingredients',
            'name': const.ADDITIONAL_INGREDIENTS,
            'choices': additional_ingridients_list,
            'filter': lambda val: "without any additions" if len(val) == 0 else val
        },
        {
            'type': 'list',
            'message': 'Do you need a bill',
            'name': const.BILL,
            'choices': [const.YES, const.NO]
            # 'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True
            # check empty answer
        },
    ] #think about adding ingridients to each of coffee 2. add if no request
    return my_coffee_questions
