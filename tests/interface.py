import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recomendacion de vestidos")
        self.geometry("800x600")

        # Create left panel frame
        self.left_panel = tk.Frame(self, bg="lightblue", width=200)
        self.left_panel.pack(side="left", fill="y")
        # Load image from URL
        self.image_url = "https://via.placeholder.com/400x400"  # Example image URL
        self.load_image_from_url()
        
        # Create frame for image display
        self.image_frame = tk.Frame(self)
        self.image_frame.pack(expand=True, fill="both")

        

        # Create bottom frame for buttons
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(side="bottom", fill="x")

        # Create buttons
        self.button1 = tk.Button(self.bottom_frame, text="Button 1", command=self.on_button1_click)
        self.button1.pack(side="left", padx=10, pady=10)

        self.button2 = tk.Button(self.bottom_frame, text="Button 2", command=self.on_button2_click)
        self.button2.pack(side="left", padx=10, pady=10)

    def load_image_from_url(self):
        try:
            response = requests.get(self.image_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((400, 400), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(img)
            self.image_label = tk.Label(self.image_frame, image=self.photo)
            self.image_label.pack(expand=True, fill="both", padx=20, pady=20)
        except Exception as e:
            print("Error loading image:", e)

    def on_button1_click(self):
        print("Button 1 clicked.")

    def on_button2_click(self):
        print("Button 2 clicked.")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
