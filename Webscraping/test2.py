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

print(received_list[2])
