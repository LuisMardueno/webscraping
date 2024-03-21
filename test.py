import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
import pandas as pd

i = 0

df = pd.read_csv('datos_todos.csv')
root = tk.Tk()
root.geometry('700x650')
root.title("Catalago")
root.configure(background= '#F2F0CE')

left_frame = ctk.CTkFrame(master=root, fg_color='#F2F0CE')
left_frame.pack(side = 'left', fill = 'both', expand = True)
right_frame = ctk.CTkFrame(master=root, fg_color='#F2F0CE')
right_frame.pack(side = 'right', fill = 'both', expand = True)


frame = ctk.CTkFrame(master=left_frame, width=200, height=200, fg_color= 'transparent')
img_url = df.iloc[i]['Imagenes']
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
marco_imagen = ctk.CTkFrame(master=frame, border_width=10,border_color='#F25C78',corner_radius=33)
panel = tk.Label(marco_imagen, image=img)
panel.pack(fill="both", expand="no", )
frame.pack(side = 'left', fill="y", expand=True)
marco_imagen.pack()

frame2 = ctk.CTkFrame(master=right_frame, width=200, height=200, fg_color='transparent',border_width=10,border_color='#F25C78',corner_radius=33)
frame2.pack(side = 'right',fill="both", expand=True)

# Create labels dynamically
label_data = [
    {"label_text": "Temporada", "column": "Temporada"},
    {"label_text": "Color", "column": "Color"},
    {"label_text": "Estilo", "column": "Estilo"},
    {"label_text": "Estampado", "column": "Estampado"},
    {"label_text": "Escote", "column": "Escote"},
    {"label_text": "Longitud manga", "column": "Longitud_manga"},
    {"label_text": "Corte", "column": "Corte"},
    {"label_text": "Material", "column": "Material"},
    {"label_text": "Precio", "column": "Precio"},
    {"label_text": "Ventas", "column": "Ventas"}
]

label_list = []
for label_info in label_data:
    label = ctk.CTkLabel(frame2, text="", text_color='black',pady = 20, justify= 'center')
    label.pack(side='top')
    label_list.append((label, label_info["column"]))  # Storing both label and column name

def update_labels():
    global i
    for label, column in label_list:
        label.configure(text=f"{column}: {df.iloc[i][column]}")

def button_event():
    global i
    i += 1
    
    # Get the new image URL based on the updated value of i
    img_url = df.iloc[i]['Imagenes']
    response = requests.get(img_url)
    img_data = response.content
    
    # Update the image displayed in the label
    new_img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    panel.configure(image=new_img)
    panel.image = new_img  # update image reference

    # Update labels with new data
    update_labels()

def button2_event():
    global i
    i -= 1
    
    # Get the new image URL based on the updated value of i
    img_url = df.iloc[i]['Imagenes']
    response = requests.get(img_url)
    img_data = response.content
    
    # Update the image displayed in the label
    new_img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    panel.configure(image=new_img)
    panel.image = new_img  # update image reference

    # Update labels with new data
    update_labels()

button = ctk.CTkButton(frame,
                       text="Siguiente",
                       command=button_event,
                       width=150,height=50,
                       corner_radius=30,
                       fg_color='#03A688',
                       text_color=['black','white'],
                       hover_color='#036b58')
button.pack(side="right")

button2 = ctk.CTkButton(frame, text="Anterior",
                        command=button2_event,
                       width=150,height=50,
                       corner_radius=30,
                       fg_color='#03A688',
                       text_color='black',
                       hover_color='#036b58')
button2.pack(side='left')

# Initial update of labels
update_labels()

root.mainloop()
