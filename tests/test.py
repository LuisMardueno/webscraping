import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = '''100,$290.00,Multicolor,Bohemio,floral de margarita,cuello en 'v' o pico,sin mangas,A línea,100% Poliéster
"17,000",$145.53,Multicolor,Bohemio,"Floral, retazo",sin mangas,Smock,Talle alto,lavadora o limpieza en seco profesional
"15,000",$155.54,Negro,Fiesta,Liso,Cuello Alzado,sin mangas,Apretado,"95% Poliéster, 5% Elastano"
1000,$209.44,Multicolor,Bohemio,floral de margarita,escote cuadrado,manga corta,A línea,Tela
"12,000",$133.59,Azul,Bohemio,"Plantas, todo estampado",sin mangas,Túnica,Natural,lavadora o limpieza en seco profesional
600,$308.06,Multicolor,Bohemio,Floral,escote cuadrado,manga corta,A línea,Tela'''

# Convert data to a list of rows
rows = data.split('\n')

# Parse data and remove commas from numeric values
ventas = []
precios = []
for row in rows:
    items = row.split(',')
    ventas.append(float(items[0].replace('"', '').replace(',', '')))  # Removing commas and converting to float
    precios.append(float(items[1].replace('"', '').replace('$', '')))  # Removing dollar sign and converting to float

# Create DataFrame
df = pd.DataFrame({'Ventas': ventas, 'Precios': precios})

# Plotting a pie chart comparing the first column with the second one
plt.figure(figsize=(8, 8))
plt.pie(df['Ventas'], labels=df['Precios'], autopct='%1.1f%%', startangle=140)
plt.title('Comparison of Ventas and Precios')
plt.axis('equal')
plt.show()
