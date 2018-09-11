"""Assuming that a store sells a minimum of 10 ice creams and a maximum of 50 ice creams in a day, then we can determine
 the weekly sales to range from 70 to 350 pieces of ice cream in a week."""

# let's generate weekly sales for the 52 weeks in an year, we use random values that range from 70 - 350
from random import *
import xlsxwriter

workbook = xlsxwriter.Workbook('/home/jeffkim/Desktop/projects/applications/below_zero_company/ice_cream_store'
                               '/ice_cream_trends/report_data/WeeklySales.xlsx')
worksheet = workbook.add_worksheet()
# start from the first cell
row = 0
col = 0

# weeks in an year
weeks = 52

"""produce results for year 2010, in excel it will appear in column 1"""

for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(n, weekly_sales)
    worksheet.write(row, col, weekly_sales)
    row += 1


""" produce results for year 2011, in excel it will appear in column 2 """

row = 0  # reinitialize row to 0
for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(n, weekly_sales)
    worksheet.write(row, col + 1, weekly_sales)
    row += 1


"""produce results for year 2012, in excel it will appear in column 3"""

row = 0  # reinitialize row to 0
for n in range(weeks):
    weekly_sales = randint(70, 351)
    print(n, weekly_sales)
    worksheet.write(row, col + 2, weekly_sales)
    row += 1

workbook.close()
