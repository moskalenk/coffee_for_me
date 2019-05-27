"""
Usage:
    start_script.py <role> <name>
    start_script.py salesman (Alex | Bob | Liza)
    start_script.py manager (Jeff | Scott | Garry)
    start_script.py -h|--help
Options:
    <role>  (salesman | manager)
    <name>  Name argument(name from DB for necessary role).
    -h --help  Show this screen.
"""

from __future__ import print_function, unicode_literals

import click
from docopt import docopt

from db.cafe_db import CafeDB
from menu import Menu
from roles import Salesman, Manager
import questions

import constants as const
from smart_coffee_machine import SmartCoffeeMachine
from services.processing_service import ProcessingService
from services.reporting_service import ReportingService


@click.group()
def main():
    pass


@main.command()
@click.argument("name")
def salesman(name):
    processing_service.check_belonging_name_to_role(name, "salesman")

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
    manager_obj = Manager(name)
    processing_service.check_belonging_name_to_role(name, "manager")

    show_report_func = reporting_service.show_report(manager_obj)
    show_report_func()


if __name__ == '__main__':
    arguments = docopt(__doc__)

    cafe_db = CafeDB("db_coffee_for_me.db")
    menu = Menu(cafe_db)
    processing_service = ProcessingService(cafe_db)
    reporting_service = ReportingService(cafe_db)
    cafe_obj = SmartCoffeeMachine(cafe_db=cafe_db,
                                  menu=menu,
                                  processing_service=processing_service,
                                  reporting_service=reporting_service)
    main()
