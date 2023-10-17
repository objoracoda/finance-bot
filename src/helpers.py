import src.dataBase as db


def db_add_expense(expense,name):
    try:
        if name.lower() in db.expense_data:
            db.expense_data[name.lower()] += int(expense)
        else:
            db.expense_data[name.lower()] = int(expense)
        print(db.expense_data)
    except ValueError:
        print("Wrong Input!")
