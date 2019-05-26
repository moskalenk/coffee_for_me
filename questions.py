from PyInquirer import Validator, ValidationError
from PyInquirer import prompt
from examples import custom_style_1
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


def ask_questions(role, coffee_with_price_list, additional_ingredients):
    salesman_questions = get_questions(role)
    answers = prompt(questions=salesman_questions(coffee_with_price_list, additional_ingredients),
                     style=custom_style_1)
    return answers


def get_questions(role):
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
        },
        {
            'type': 'input',
            'name': const.QUANTITY,
            'message': 'Count of servings do you need?',
            'validate': NumberValidator,
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
        },
    ]
    return my_coffee_questions
