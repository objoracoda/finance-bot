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
    
    
def show_category():
    categorys = []
    for row in expenses.exp:
        categorys.append(row)

    return categorys