from bs4 import BeautifulSoup
import os
directory = 'htmls'
indice = 1
contador = 1
for filename in os.scandir(directory):
    if filename.is_file():

        with open(f"htmls/vestidosShein{indice}.html", 'r',encoding='utf-8') as html_file:
            content = html_file.read()

            soup = BeautifulSoup(content, 'lxml')
            products = soup.find_all('section', class_='product-card multiple-row-card j-expose__product-item hover-effect product-list__item product-list__item-new')
            for index, product in enumerate(products):
                nombre_producto = product.find('div',class_='product-card__goods-title-container').text.replace('SHEIN', '')
                ventas_tag = product.find('p', class_='product-card__selling-proposition-text font-golden')
                ventas = ventas_tag.text.replace('k+ vendidos recientemente', ',000').replace('+ vendidos recientemente','').replace('.','') if ventas_tag else '1000'
                precio = product.find('p', class_='product-item__camecase-wrap').text.replace('$MXN','$')
                img_tag = product.find('img')
                data_src_value = img_tag['data-src']
                link = product.find('a')
                link_tag = link['href']

                with open(f'posts/{contador}.txt','w') as f:

                    f.writelines(f"{nombre_producto.strip()}\n")
                    f.write(f"{ventas.strip()}\n")
                    f.write(f"{precio.strip()}\n")
                    f.write(f"{data_src_value}\n")
                    f.write(f"https://www.shein.com.mx{link_tag} \n")
                contador += 1
            
            indice += 1
            