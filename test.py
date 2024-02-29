import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()


expenses = (
    ['Rent', 1000,'ana'],
    ['Gas',   100,'juan'],
    ['Food',  300,'xavier'],
    ['Gym',    50,'tomas'],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item in (expenses):
    for i in range(len(item)):
        worksheet.write(row, col + i, item[i])
    row += 1



workbook.close()