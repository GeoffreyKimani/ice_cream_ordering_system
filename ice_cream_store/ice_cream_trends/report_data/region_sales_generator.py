"""here we compare sales from 5 different regions.
assume that each region has 5 stores, then we approach the problem by collating the weekly sales of each of the store """

from random import *
import xlsxwriter

workbook = xlsxwriter.Workbook('/home/jeffkim/Desktop/projects/applications/below_zero_company/ice_cream_store'
                               '/ice_cream_trends/report_data/RegionSales.xlsx')
worksheet = workbook.add_worksheet()

# weeks in an year
weeks = 52

"""generate sales for region one. remember it has 5 stores, therefore the collated weekly sales of the region range 
between 350 and 1750 ice creams"""
row = 0
col = 0
for n in range(weeks):
    weekly_sales = randint(350, 1751)
    print(weekly_sales)
    worksheet.write(row, col, weekly_sales)
    row += 1


"""generate sales for region two. remember it has 5 stores, therefore the collated weekly sales of the region range 
between 350 and 1750 ice creams"""
row = 0
col = 1
for n in range(weeks):
    weekly_sales = randint(350, 1751)
    print(weekly_sales)
    worksheet.write(row, col, weekly_sales)
    row += 1


"""generate sales for region three. remember it has 5 stores, therefore the collated weekly sales of the region range 
between 350 and 1750 ice creams"""
row = 0
col = 2
for n in range(weeks):
    weekly_sales = randint(350, 1751)
    print(weekly_sales)
    worksheet.write(row, col, weekly_sales)
    row += 1


"""generate sales for region four. remember it has 5 stores, therefore the collated weekly sales of the region range 
between 350 and 1750 ice creams"""
row = 0
col = 3
for n in range(weeks):
    weekly_sales = randint(350, 1751)
    print(weekly_sales)
    worksheet.write(row, col, weekly_sales)
    row += 1


"""generate sales for region five. remember it has 5 stores, therefore the collated weekly sales of the region range 
between 350 and 1750 ice creams"""
row = 0
col = 4
for n in range(weeks):
    weekly_sales = randint(350, 1751)
    print(weekly_sales)
    worksheet.write(row, col, weekly_sales)
    row += 1

workbook.close()

