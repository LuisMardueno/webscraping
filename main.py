import tkinter as tk
import customtkinter as ctk

app = ctk.CTk()
app.geometry('600x400')
app.title('Pruebas')
ctk.set_appearance_mode('dark')

app.resizable(width=True, height=True)

frame1 = ctk.CTkFrame(master=app,corner_radius= 33)
label = ctk.CTkLabel(frame1, text='Hola')
label.pack(side = 'right')
frame1.pack()


app.mainloop()