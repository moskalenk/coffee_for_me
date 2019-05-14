from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt
from examples import custom_style_1

import click

from action.manager import Manager
from action.salesman import Salesman
from action.questions import coffee_questions


@click.group()
def main():
    # actual_name = get_name(name)
    # actual_position = get_position(position)
    # if actual_position == "salesman":
    #     salesman = Salesman(actual_name)
    #     res = input("type of coffee(espresso)")
    #     print(res)
    # elif actual_position == "manager":
    #     manager = Manager(actual_name)
    print("main")


@main.command()
@click.argument("name")
def salesman(name):
    #add check our user
    salesman = Salesman(name)
    coffee_with_price_list = salesman.get_all_coffee_with_price()
    additional_ingridients = salesman.get_all_additional_ingredients_with_price()

    answers = prompt(questions=coffee_questions(coffee_with_price_list, additional_ingridients),
                     style=custom_style_1)#how to add some(2) latte?
    pprint(answers)
    salesman.save_to_bill(answers)
    coffee_count = len(answers["cofee"])
    salesman.add_to_db(name, coffee_count, answers)

@main.command()
@click.argument("name")
def manager(name):
    print("manager")
    return name


if __name__ == '__main__':
    main()
