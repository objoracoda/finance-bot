import pandas as pd

import src.expenses as expenses


def parse_expense(string_expense):
    expense_arr = string_expense.split()
    title = expense_arr[1]
    amount = int(expense_arr[0])

    for expense in expenses.exp:
        if (title in expenses.exp[expense]):
            title = expense
            return (amount,title)

    title = "прочее"

    return (amount,title)
    
    
def show_category(rows):
    msg = ""
    for row in rows:
        msg += f"{row[0].capitalize()} - {row[1]}р \n"
    
    return msg


def add_excel(row):
    df = pd.DataFrame({'Дорога': [row[0][1]],
                   'Кафе': [row[1][1]],
                   'Личное': [row[2][1]],
                   'Прочее':[row[3][1]]})

    return df.to_excel('./fin.xlsx', sheet_name='Budgets', index=False)

    