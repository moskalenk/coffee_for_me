from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from examples import custom_style_1

import click

from roles.salesman import Salesman
from action.questions import coffee_questions

from action.positions_helper import PositionsHelper
import constants as const


@click.group()
def main():
    print("main")


@main.command()
@click.argument("name")
def salesman(name):
    salesman = Salesman(name)
    position_helper = PositionsHelper()
    salesmans_list = position_helper.get_all_salesmans()
    if name not in salesmans_list:
        raise Exception(f"There is no {name} in list of salesmans")
    coffee_with_price_list = salesman.get_all_coffee_with_price()
    additional_ingridients = salesman.get_all_additional_ingredients()

    answers = prompt(questions=coffee_questions(coffee_with_price_list, additional_ingridients),
                     style=custom_style_1)#how to add some(2) latte?
    # pprint(answers)
    position_helper.update_summary_table_by_name("total", name, answers)
    position_helper.update_summary_table_by_name("number_of_sales", name, answers)

    if answers[const.BILL] == const.YES:
        salesman.get_bill(answers)


@main.command()
@click.argument("name")
def manager(name):
    print("manager")
    return name


if __name__ == '__main__':
    main()
