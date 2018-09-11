"""Here we generate the weekly reports for at least five stores for 1 year."""

from random import *
import xlsxwriter

workbook = xlsxwriter.Workbook('/home/jeffkim/Desktop/projects/applications/below_zero_company/ice_cream_store'
                               '/ice_cream_trends/report_data/StoreSales.xlsx')
worksheet = workbook.add_worksheet()

# weeks in an year
weeks = 52
col = 0

""" Generate sales for store 1 """
row = 0
for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(weekly_sales)
    worksheet.write(row, col, weekly_sales)
    row += 1

""" Generate sales for store 2 """
row = 0
for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(weekly_sales)
    worksheet.write(row, col + 1, weekly_sales)
    row += 1


""" Generate sales for store 3 """
row = 0
for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(weekly_sales)
    worksheet.write(row, col + 2, weekly_sales)
    row += 1


""" Generate sales for store 4 """
row = 0
for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(weekly_sales)
    worksheet.write(row, col + 3, weekly_sales)
    row += 1


""" Generate sales for store 5 """
row = 0
for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(weekly_sales)
    worksheet.write(row, col + 4, weekly_sales)
    row += 1


workbook.close()
