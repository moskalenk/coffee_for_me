from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from examples import custom_style_1

import click

from roles import Salesman, Manager
import questions

import constants as const
from cafe import Cafe


@click.group()
def main():
    pass


@main.command()
@click.argument("name")
def salesman(name):
    cafe_obj = Cafe()
    menu_service = cafe_obj.menu
    processing_service = cafe_obj.processing_service

    sellers_list = cafe_obj.list_of_names_by_role("salesman")
    if name not in sellers_list:
        raise Exception(f"There is no {name} in list of sellers")
    salesman_obj = Salesman(name)

    coffee_with_price_list = menu_service.coffee_with_price()
    additional_ingredients = menu_service.additional_ingredients()

    salesman_questions = questions.ask_questions(salesman_obj)
    answers = prompt(questions=salesman_questions(coffee_with_price_list, additional_ingredients),
                     style=custom_style_1)#how to add some(2) latte?

    processing_service.update_summary_table_by_username("total", name, answers)
    processing_service.update_summary_table_by_username("number_of_sales", name, answers)

    if answers[const.BILL] == const.YES:
        bill = processing_service.bill_table(answers)
        processing_service.save_in_file(bill, const.BILL_FILE_NAME)
        salesman_obj.look_at_bill(bill)


@main.command()
@click.argument("name")
def manager(name):
    cafe_obj = Cafe()
    processing_service = cafe_obj.processing_service

    managers_list = cafe_obj.list_of_names_by_role("manager")
    if name not in managers_list:
        raise Exception(f"There is no {name} in list of managers")
    manager_obj = Manager(name)

    report = processing_service.create_summary_table()
    manager_obj.look_at_report(report)


if __name__ == '__main__':
    main()
