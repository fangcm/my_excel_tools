import xlwings as xw


def main():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


if __name__ == "__main__":
    xw.books.active.set_mock_caller()
    main()
