import flet as ft
import pandas as pd
df = pd.read_csv('datos_todos.csv')

def columna(indice):
     images = ft.Column(expand=1, wrap=False, scroll="always")
     for i in range(0, 100):
        images.controls.append(ft.Image(src=df.iloc[i+indice]['Imagenes'],
                                        width=300,height=300,
                                        fit=ft.ImageFit.FILL,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                        border_radius=ft.border_radius.all(10),))
        return images




def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

 
    
    page.add(ft.Row(
         [
            columna(0),
            columna(2),
         ],
         wrap=False,
         scroll='allways',

    ))
         




ft.app(target=main, view=ft.AppView.WEB_BROWSER)
