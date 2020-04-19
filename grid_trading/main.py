import xlwings as xw

from grid_trading.action import Action


def main():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"

    action = Action(wb.sheets[0])
    action.calculate()


if __name__ == "__main__":
    xw.books.active.set_mock_caller()
    main()
