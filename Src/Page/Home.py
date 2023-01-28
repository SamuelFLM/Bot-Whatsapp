import PySimpleGUI as sg

class Interface_home:
    
    def __init__(self) -> None:
        self.background = "#0A1B1E"
    
    def page(self):
        
        cabecalho = [[sg.Image(filename="Src//Page//Img//Logo//logo.png", background_color=self.background, pad=(100,(20,20)))],
                     [sg.Image(filename="Src//Page//Img//Icon//Home//texto.png", background_color=self.background, pad=(0,(0,60)),k="texto", visible=True)], 
                    ]
        carrocel = [
            [sg.Image(filename="Src//Page//Img//Icon//esquerda_branca.png", background_color=self.background, pad=(10,(0,0)),k="esquerda", enable_events=True, visible=True),
             sg.Image(filename="Src//Page//Img//Icon//Home//part1.png", background_color=self.background, pad=(0,(0,80)),k="imagem", visible=True),
             sg.Image(filename="Src//Page//Img//Icon//Home//part3.png", background_color=self.background, pad=(0,(0,0)),k="imagem2", visible=False),
             sg.Image(filename="Src//Page//Img//Icon//direita_branca.png", background_color=self.background, pad=(10,(0,0)),k="direita", enable_events=True, visible=True),
            ],
        ]
        rodape = [[sg.Image(filename="Src//Page//Img//Icon//Home//rodape1.png", background_color=self.background, pad=(0,(0,0)),k="entrar", enable_events=True)],
                  [sg.Image(filename="Src//Page//Img//Icon//Home//rodape2.png", background_color=self.background, pad=(0,(0,0)),k="como_utilizar", enable_events=True)],
                 ]
        
        layout = [cabecalho,carrocel,rodape]
        window = sg.Window("Bot Whatsapp", layout=layout,size=(374, 718), grab_anywhere=True, margins=(0,0),element_justification='c', background_color=self.background,icon="Src//Page//Img//Logo//icon.ico")
        return window