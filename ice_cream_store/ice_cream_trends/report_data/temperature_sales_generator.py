"""we need to generate average weekly temperature of a given region for 1 year. """

# let our temperature range from 0 degrees celsius to 35 degrees celsius, this will ensure temp. is distributed
# evenly over the extremes

from random import *
import xlsxwriter

workbook = xlsxwriter.Workbook('/home/jeffkim/Desktop/projects/applications/below_zero_company/ice_cream_store'
                               '/ice_cream_trends/report_data/Temperature.xlsx')
worksheet = workbook.add_worksheet()


def weekly_temp_average():
    days = 7

    weekly_temp = 0
    average_temp = 0
    for n in range(days):
        daily_temp = randint(0, 36)
        weekly_temp = weekly_temp + daily_temp
        average_temp = (weekly_temp / 7)
    return average_temp


weeks = 52
row = 0
col = 0
for period in range(weeks):
    temp = weekly_temp_average()
    print(temp)
    worksheet.write(row, col, temp)

# let's generate the sales from this data
    if 0 <= int(temp) <= 15:
        # generate sales that are low
        a = randint(0, 11)
        worksheet.write(row, col + 1, a)
    elif 16 <= int(temp) <= 23:
        # generate sales that are higher
        b = randint(11, 21)
        worksheet.write(row, col + 1, b)
    elif 24 <= int(temp) <= 30:
        # generate sales that are moderately high
        c = randint(21, 41)
        worksheet.write(row, col + 1, c)
    elif 31 <= int(temp) <= 36:
        # generate sales that are very high
        d = randint(50, 71)
        worksheet.write(row, col + 1, d)
    else:
        print('out of range')

    row += 1

workbook.close()

