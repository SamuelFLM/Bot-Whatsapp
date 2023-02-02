import PySimpleGUI as sg
from Page.Log_contatos import Interface_log_contatos
from Data.Contatos import Contatos
janela_log = Interface_log_contatos()

contatos = Contatos()

class Interface_dados_contato:
    
    def __init__(self) -> None:
        self.background = "White"
    
    def page(self):
        
        cabecalho = [[sg.Image(filename="Src//Page//Img//Icon//esquerda.png", background_color=self.background, pad=(20,(50,0)), enable_events=True, key="voltar"), sg.Image(filename="Src//Page//Img//Logo//logo.png", background_color=self.background, pad=(35,(50,0)))],
                     [sg.Image(filename="Src//Page//Img//Icon//Automacao//Personalizar contato.png", background_color=self.background, pad=(90,(50,0)))]
                    ]
        nome = [  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Nome (2).png", background_color=self.background, pad=(35,(50,0)), key="nome", visible=True)],
                  [sg.Input("", size=(15,0), font="Inter 12 bold",text_color="#6D6D6D", justification='l', background_color=self.background, border_width=0, key="nome_contato", pad=(35,(20,0)))],
                  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Line 2.png", background_color=self.background, pad=(35,(0,0)))],
                 ]
        numero = [[sg.Image(filename="Src//Page//Img//Icon//Automacao//Número.png", background_color=self.background, pad=(35,(30,0)), key="img_numero", visible=True)],
                  [sg.Input("", size=(15,0), font="Inter 12 bold",text_color="#6D6D6D", justification='l', background_color=self.background, border_width=0, key="numero", pad=(35,(20,0)))],
                  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Line 2.png", background_color=self.background, pad=(35,(0,0)))],
                 ]
        mensagem = [
                  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Mensagem.png", background_color=self.background, pad=(35,(50,0)), key="img_numero", visible=True)],
                  [sg.Multiline("", font="Inter 10 bold",text_color="#6D6D6D",s=(50,10), background_color=self.background, key="mensagem", pad=(35,(20,0)),border_width=0,horizontal_scroll=False,autoscroll=True,expand_x=True,sbar_arrow_width=0,sbar_width=0,sbar_background_color="white")],
                  [sg.Image(filename="Src//Page//Img//Icon//Automacao//Line 2.png", background_color=self.background, pad=(35,(0,0)))],
                  [sg.Text("0 caracteres", text_color="#6D6D6D",background_color=self.background, pad=(35,(0,40)),k="tamanho_mensagem")],
        ]
        rodape =  [
            [sg.Image(filename="Src//Page//Img//Icon//Automacao//Group 19 (2).png", background_color=self.background, pad=(0,(0,0)), enable_events=True, key="enviar")],
            ]
        
        layout = [cabecalho, nome,numero,mensagem, rodape]
        
        window = sg.Window("Bot Whatsapp", layout=layout,size=(374, 718), grab_anywhere=True, margins=(0,0), background_color=self.background,icon="Src//Page//Img//Logo//icon.ico", finalize=True)
        
        while True:
            event, values = window.read(timeout=1)
            
            if event == "voltar":
                window.close()
                janela_log.page()
                break
            
            tamanho_mensagem = len(values["mensagem"])
            window["tamanho_mensagem"].update(f"{tamanho_mensagem} caracteres")
           
            if bool(values["nome_contato"]) and bool(values["numero"] and values["mensagem"]):
                window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//Group 20.png")
                if event == "enviar":
                    nome = str(values["nome_contato"])
                    numero = str(values["numero"])
                    mensagem = str(values["mensagem"])
                    contatos.adicionar_contato(nome,numero,mensagem)
                    window.close()
                    janela_log.page(contatos.visualizar_contatos())
                    break
            else:
                window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//Group 19 (2).png")