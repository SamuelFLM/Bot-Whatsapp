import PySimpleGUI as sg


class Interface_automacao:
    
    def __init__(self) -> None:
        self.background = "White"
    
    def page(self):
        
        cabecalho = [[sg.Image(filename="Src//Page//Img//Icon//esquerda.png", background_color=self.background, pad=(20,(50,0)), enable_events=True, key="voltar"), sg.Image(filename="Src//Page//Img//Logo//logo.png", background_color=self.background, pad=(35,(50,0)))],
                     [sg.Image(filename="Src//Page//Img//Icon//Automacao//Informe os dados.png", background_color=self.background, pad=(108,(50,0)))]
                    ]
        numero = [[sg.Image(filename="Src//Page//Img//Icon//Automacao//Número.png", background_color=self.background, pad=(35,(50,0)), key="img_numero", visible=True)],
                  [sg.Input("", size=(15,0), font="Inter 12 bold",text_color="#6D6D6D", justification='l', background_color=self.background, border_width=0, key="numero", pad=(35,(20,0)))],
                  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Line 2.png", background_color=self.background, pad=(35,(0,0)))],
                 ]
        mensagem = [
                  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Mensagem.png", background_color=self.background, pad=(35,(50,0)), key="img_numero", visible=True)],
                  [sg.Multiline("", font="Inter 10 bold",text_color="#6D6D6D",s=(50,10), background_color=self.background, key="mensagem", pad=(35,(20,0)),border_width=0,horizontal_scroll=False,autoscroll=True,expand_x=True,)],
                  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Line 2.png", background_color=self.background, pad=(35,(0,0)))],
                  [sg.Text("0 caracteres", text_color="#6D6D6D",background_color=self.background, pad=(35,(0,40)),k="tamanho_mensagem")],
        ]
        rodape =  [
            [sg.Image(filename="Src//Page//Img//Icon//Automacao//addoff.png", background_color=self.background, pad=(100,(0,50)), enable_events=True, key="add"),sg.Image(filename="Src//Page//Img//Icon//Automacao//file.png", background_color=self.background, pad=(0,(0,50)), enable_events=True, k="file")],
            [sg.Image(filename="Src//Page//Img//Icon//Automacao//enviaroff.png", background_color=self.background, pad=(0,(0,0)), enable_events=True, key="enviar")],
            ]
        
        layout = [cabecalho, numero,mensagem, rodape]
        
        window = sg.Window("Bot Whatsapp", layout=layout,size=(374, 718), grab_anywhere=True, margins=(0,0), background_color=self.background,icon="Src//Page//Img//Logo//icon.ico", finalize=True)
        return window