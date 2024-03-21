import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

received_list = []
index = 1
while index < 10:
    nombre_producto = f"('Product Name' {index})"
    ventas = f"('venta' {index})"
    precio = f"('precio' {index*100})"
    data_src_value = f"('Imagen numero: ' {index})"
    link_tag = f"('Link' {index})"
    product_info = [nombre_producto, ventas, precio, data_src_value, link_tag]
    index +=1
    received_list.append(product_info)

print(received_list)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item in (received_list):
    for i in range(len(item)):
        worksheet.write(row, col + i, item[i])
    row += 1



workbook.close()