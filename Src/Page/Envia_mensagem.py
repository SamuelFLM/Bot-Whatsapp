import PySimpleGUI as sg


class Interface_automacao:
    
    def __init__(self) -> None:
        self.background = "White"
    
    def page(self):
        
        cabecalho = [[sg.Image("", background_color=self.background)]]
        numero = []
        mensagem = []
        rodape =  []
        
        layout = [cabecalho, numero,mensagem, rodape]
        
        window = sg.Window("Bot Whatsapp", layout=layout,size=(374, 718), grab_anywhere=True, margins=(0,0),element_justification='c', background_color=self.background,icon="Src//Page//Img//Logo//icon.ico")
        return window