import constants as const


def get_value_by_key_from_answer(answer, key):
    return answer[key]


def split_chosen_coffee_with_price(answer):
    chosen_coffee = get_value_by_key_from_answer(answer, const.COFFEE_TYPE)
    spl = chosen_coffee.split()

    coffee_type = spl[0]
    price_for_one_coffee = int(spl[1])
    currency_type = spl[-1]
    return coffee_type, price_for_one_coffee, currency_type


def calculate_price_for_order(answer):
    quantity = get_value_by_key_from_answer(answer, const.QUANTITY)
    _, price_for_one_coffee, _ = split_chosen_coffee_with_price(answer)
    return price_for_one_coffee * quantity


def preparing_data_for_creating_table(answer):
    """
    Creating columns and rows for creating table with bill
    :param answer:
    :return:
    """
    set_of_correct_columns = (const.COFFEE_TYPE, const.QUANTITY, const.ADDITIONAL_INGREDIENTS)
    rows, columns = [], []
    for key in answer:
        if key not in set_of_correct_columns:
            continue
        elif type(answer.get(key)) is list:
            rows.append(f"{', '.join(answer[key])}")
            columns.append(key)
        else:
            rows.append(answer[key])
            columns.append(key)

    total_price_for_current_order = calculate_price_for_order(answer)
    columns.append("Total in USD")
    rows.append(f"{total_price_for_current_order}")
    rows_list = (rows,)  # need do to it for creating correct table
    return rows_list, columns
