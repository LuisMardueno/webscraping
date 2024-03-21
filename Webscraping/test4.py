from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
import xlsxwriter
from selenium.common.exceptions import TimeoutException
workbook = xlsxwriter.Workbook('test2.xlsx')
worksheet = workbook.add_worksheet()
lista = []
row = 0
col = 0
indice = 0
browser = webdriver.Firefox()


with open('links.txt') as file:
        try:
            for index, line in enumerate(file):
                browser.get(line.rstrip())
                html = browser.page_source
                soup = BeautifulSoup(html,'lxml')
                val_divs = soup.find_all('div', class_='product-intro__description-table-item')
                product_info = []
                for val_div in val_divs:
                    key = val_div.find('div', class_='key').text.strip()  # Extract the key
                    val = val_div.find('div', class_='val').text.strip()  # Extract the value
                    #print(f"{key}: {val}")
                    product_info.append(val)
                #print(product_info)
                lista.append(product_info)
                indice+=1
                print(indice)
        except Exception as e:
            print(f"Error : {line.rstrip()}")
            for item in (lista):
                for i in range(len(item)):
                    worksheet.write(row, col + i, item[i])
                row += 1
            #workbook.close()
            print(lista)
for item in (lista):
    for i in range(len(item)):
        worksheet.write(row, col + i, item[i])
    row += 1
workbook.close()



    
