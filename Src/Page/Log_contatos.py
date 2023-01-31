import PySimpleGUI as sg


class Interface_log_contatos:
    
    def __init__(self) -> None:
        self.background = "white"
        
    def page(self):
        cabecalho = [[sg.Image(filename="Src//Page//Img//Icon//esquerda.png", background_color=self.background, pad=(20,(50,0)), enable_events=True, key="voltar"), sg.Image(filename="Src//Page//Img//Logo//logo.png", background_color=self.background, pad=(35,(50,0)))],
                     [sg.Image(filename="Src//Page//Img//Icon//Contatos//Contatos.png", background_color=self.background, pad=(130,(50,30)))],]
        
        contatos = [
                 [sg.Input("", border_width=0, background_color="white", font="Inter 10 bold", k="nome_contato", s=(35,10),pad=(30,(0,0))), sg.Image(filename="Src//Page//Img//Icon//Contatos//search-24.png", background_color="white", enable_events=True, key="pesquisar")],
                 [sg.Image(filename="Src//Page//Img//Icon//Contatos//Line 6.png", background_color=self.background, pad=(30,(0,40)))],
                 [sg.Table(values=[],headings=["NOME","NUMERO", "MENSAGEM"], key="table", bind_return_key=True,auto_size_columns=True, background_color="white", expand_x=True, border_width=0,justification='c', font="Jaldi 10 bold", text_color="#6D6D6D",header_border_width=0, max_col_width=15,header_background_color="white", k="table", display_row_numbers=True,sbar_background_color="white", sbar_width=0, sbar_arrow_width=0)],
                 [sg.Image(filename="Src//Page//Img//Icon//Contatos//Line 6.png", background_color=self.background, pad=(30,(50,0)))],
                 ]
        edit_contatos = [
            [sg.Text("", pad=(30,(50, 0)), background_color="white"),sg.Image(filename="Src//Page//Img//Icon//Contatos//note-24.png", background_color=self.background, pad=(30,(50,0)), key="editar", enable_events=True), sg.Image(filename="Src//Page//Img//Icon//Contatos//x-circle-24.png", background_color=self.background, pad=(30,(50,0)), key="excluir", enable_events=True), sg.Image(filename="Src//Page//Img//Icon//Contatos//circle-plus-24 (4).png", key="add",background_color=self.background, pad=(30,(50,0)), enable_events=True)]
        ]
        rodape = [sg.Image(filename="Src//Page//Img//Icon//Automacao//enviaroff.png", background_color="white", pad=(0,(105,0)), k="enviar")]
        
        layout = [cabecalho, contatos, edit_contatos, rodape]
        window = sg.Window("Bot Whatsapp", layout=layout,size=(374, 718), grab_anywhere=True, margins=(0,0), background_color=self.background,icon="Src//Page//Img//Logo//icon.ico", finalize=True)
        return window