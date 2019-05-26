from pathlib import Path
from definitions import project_path_dir
import processing_user_answer

import constants as const


class ProcessingService:
    def __init__(self, cafe_db):
        self.cafe_db = cafe_db
        self.user_answer_processed_data = processing_user_answer

    def update_summary_table_by_username(self, column_name, name, answer):
        if column_name == "total":
            current_total_value = self.user_answer_processed_data.calculate_price_for_order(answer)
            new_total_value = self._get_el_from_summary_table_by_username(column_name, name) + current_total_value
            self.cafe_db.update_data_in_summary_table(column_name, name, new_total_value)

        elif column_name == "number_of_sales":
            current_quantity = self.user_answer_processed_data.get_value_by_key_from_answer(answer, const.QUANTITY)
            new_number_of_sales_value = self._get_el_from_summary_table_by_username(column_name, name) + current_quantity
            self.cafe_db.update_data_in_summary_table(column_name, name, new_number_of_sales_value)

    def _get_el_from_summary_table_by_username(self, column_name, name):
        res = self.cafe_db.get_element_from_total_table_for_salesman(
            column_name, name)
        return 0 if not res else res

    @staticmethod
    def save_in_file(data, file_name, mode="w"):
        path_to_file = Path(project_path_dir, file_name)
        with path_to_file.open(mode=mode) as f:
            f.write(data)

    def check_belonging_name_to_role(self, name, role_name):
        names_list = self.cafe_db.get_names_by_role(role_name)
        if name not in names_list:
            raise NameError(f"There is no {name} in list of {role_name}s")
