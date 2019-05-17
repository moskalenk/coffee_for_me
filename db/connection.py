import sqlite3
from pathlib import Path


class DBConnection:
    """Also we can use that class as context manager"""
    db_path_dir = Path(__file__).parent

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
        return str(Path.joinpath(cls.db_path_dir, db_name))#is it usefull to use classmethod?

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

    def select_as_list(self, sql_statement):
        """Works only with strings(think about it)"""
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            execute_results = cursor.fetchall()
        return list(map(" ".join, execute_results))

    def execute_and_commit(self, sql_statement):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            self.connection.commit()
        # return self #do we need self in return
