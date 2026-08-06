import matplotlib.pyplot as plt


def expense_chart(summary):

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        summary["Amount"],
        labels=summary["Category"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Expense by Category")

    return fig