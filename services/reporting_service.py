import processing_user_answer
from tabulate import tabulate
from roles import Salesman, Manager


class ReportingService:
    def __init__(self, cafe_db):
        self.cafe_db = cafe_db
        self.user_answer_processed_data = processing_user_answer

    def show_report(self, role):
        if isinstance(role, Salesman):
            return self.show_bill
        elif isinstance(role, Manager):
            return self.show_common_report
        else:
            raise NotImplementedError("There is no report for your role")

    def show_common_report(self):
        table = self._create_summary_table()
        print(table)

    @staticmethod
    def show_bill(bill):
        print(bill)

    def get_bill_table(self, answer):
        return self._create_bill_table(answer)

    @staticmethod
    def create_table(rows, columns):
        table_rows, table_column_names = rows, columns
        return tabulate(table_rows, headers=table_column_names, tablefmt="presto",
                        numalign="left")

    def _create_summary_table(self):
        data = self.cafe_db.get_total()
        res = list(map(lambda lst: ["-" if el is None else el for el in lst], data))
        return self.create_table(res, ["Seller name", "Count of coffee", "Total in USD"])

    def _create_bill_table(self, answer):
        rows, columns = processing_user_answer.preparing_data_for_creating_table(answer)
        table = self.create_table(rows, columns)
        return table
