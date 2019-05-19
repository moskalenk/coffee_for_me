from tabulate import tabulate


def create_table(rows, columns):
    table_rows, table_column_names = rows, columns
    return tabulate(table_rows, headers=table_column_names, tablefmt="presto",
                    numalign="left")
