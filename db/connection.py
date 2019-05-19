import sqlite3
from pathlib import PurePath
from definitions import db_path_dir


class DBConnection:
    """Also we can use that class as context manager"""

    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name
        self.db_path = self._get_abs_path_for_db(self.db_name)#is need here(may be better in a class(not instanse)?)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        # return self.connection
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.connection.close()

    @classmethod
    def _get_abs_path_for_db(cls, db_name):
        return str(PurePath(db_path_dir, db_name))#is it usefull to use classmethod?

    def select_one(self, sql_statement):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            select_results = cursor.fetchone()[0]
        return select_results

    def select(self, sql_statement):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            select_results = cursor.fetchall()
        return select_results

    def select_as_dict(self, sql_statement):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            column_names = [col[0] for col in cursor.description]
            name_value_iters = [zip(column_names, row) for row in cursor.fetchall()]
            name_to_values_dicts = [dict(name_value_iter) for name_value_iter in name_value_iters]

            print(name_to_values_dicts)

        return name_to_values_dicts

    def select_as_list(self, sql_statement):
        """Works only with strings(think about it)"""
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            execute_results = cursor.fetchall() # as a result wil be list of tuples
        return list(map(lambda tup: " ".join([str(el) for el in tup]), execute_results))

    def execute_and_commit(self, sql_statement):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            self.connection.commit()
        # return self #do we need self in return
