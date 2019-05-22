from __future__ import print_function, unicode_literals
# from PyInquirer import prompt
# from examples import custom_style_1

import click

from db.cafe_db import CafeDB
from menu import Menu
from roles import Salesman, Manager
import questions

import constants as const
from cafe import Cafe
from services.processing_service import ProcessingService
from services.reporting_service import ReportingService


@click.group()
def main():
    pass


@main.command()
@click.argument("name")
def salesman(name):
    sellers_list = cafe_obj.list_of_names_by_role("salesman")
    if name not in sellers_list:
        raise Exception(f"There is no {name} in list of sellers")
    salesman_obj = Salesman(name)

    coffee_with_price_list = menu.coffee_with_price()
    additional_ingredients = menu.additional_ingredients()

    answers = questions.ask_questions(role=salesman_obj,
                                      coffee_with_price_list=coffee_with_price_list,
                                      additional_ingredients=additional_ingredients)
    processing_service.update_summary_table_by_username("total", name, answers)
    processing_service.update_summary_table_by_username("number_of_sales", name, answers)

    if answers[const.BILL] == const.YES:
        bill = reporting_service.get_bill_table(answers)
        processing_service.save_in_file(bill, const.BILL_FILE_NAME)
        show_report_func = reporting_service.show_report(salesman_obj)
        show_report_func(bill)


@main.command()
@click.argument("name")
def manager(name):
    managers_list = cafe_obj.list_of_names_by_role("manager")
    if name not in managers_list:
        raise Exception(f"There is no {name} in list of managers")
    manager_obj = Manager(name)

    show_report_func = reporting_service.show_report(manager_obj)
    show_report_func()


if __name__ == '__main__':
    cafe_db = CafeDB("test_db_coffee.db")
    menu = Menu(cafe_db)
    processing_service = ProcessingService(cafe_db)
    reporting_service = ReportingService(cafe_db)
    cafe_obj = Cafe(cafe_db=cafe_db,
                    menu=menu,
                    processing_service=processing_service,
                    reporting_service=reporting_service)
    main()
