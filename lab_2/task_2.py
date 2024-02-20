import pandas as pd


class ExcelOperations:
    def __init__(self, file_path='pythonexcel.xlsx', sheet_name='sales'):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sales_df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)

    def if_excel_function(self):
        self.sales_df["   >500"] = ["Yes" if x > 500 else "No" for x in self.sales_df["Sales"]]
        print(self.sales_df.head(5), "\n")

    def vlookup_excel_function(self, states_sheet='states'):
        states_df = pd.read_excel(self.file_path, sheet_name=states_sheet)
        sales = self.sales_df.merge(states_df, on="City", how="left")
        print(sales.head(5), "\n")

    def pivot_table_excel_function(self):
        pivot = self.sales_df.pivot_table(values="Sales", index="City", aggfunc="sum")
        print(pivot, "\n")

    def date_range_task(self, start_date="2023-12-12", periods=21, freq="D"):
        dates = pd.date_range(start=start_date, periods=periods, freq=freq)
        print(dates, "\n")

    def find_month_from_date_task(self, dates):
        df = pd.DataFrame({'sales_date': dates, 'total_sales': [675, 500, 575]})
        df['month'] = pd.DatetimeIndex(df['sales_date']).month
        print(df, "\n")

    def convert_timestamps_to_datetime(self, timestamps):
        datetimes = pd.to_datetime(timestamps, unit="s")
        print(datetimes)


if __name__ == '__main__':
    excel_operations = ExcelOperations()

    excel_operations.if_excel_function()
    excel_operations.vlookup_excel_function()
    excel_operations.pivot_table_excel_function()
    excel_operations.date_range_task()
    excel_operations.find_month_from_date_task(['2020-05-18', '2020-08-20', '2020-12-21'])
    excel_operations.convert_timestamps_to_datetime([1577836800, 1581609600, 1583625600, 1585699200, 1588876800])
