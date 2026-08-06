def analyze_data(data):

    income = data[data["Type"] == "Credit"]["Amount"].sum()

    expense = data[data["Type"] == "Debit"]["Amount"].sum()

    savings = income - expense

    return income, expense, savings

def category_summary(data):

    expense = data[data["Type"]== "Debit"]

    summary = (
        expense.groupby("Category")["Amount"]
        .sum()
        .reset_index()
    )

    return summary

def get_insights(data):

    expense = data[data["Type"] == "Debit"]

    highest = expense.loc[expense["Amount"].idxmax()]

    return {
        "highest_expense": highest["Description"],
        "highest_amount": highest["Amount"],
        "category": highest["Category"]
    }