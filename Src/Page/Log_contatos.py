import PySimpleGUI as sg

class Interface_log_contatos:
    
    def __init__(self) -> None:
        self.background = "white"
        
    def page(self, dados):
        cabecalho = [[sg.Image(filename="Src//Page//Img//Logo//logo.png", background_color=self.background, pad=(100,(50,0)))],
                     [sg.Image(filename="Src//Page//Img//Icon//Contatos//Contatos.png", background_color=self.background, pad=(130,(50,30)))],]
        
        contatos = [
                 [sg.Input("", border_width=0, background_color="white", font="Inter 10 bold", k="nome_contato", s=(35,10),pad=(30,(0,0))), sg.Image(filename="Src//Page//Img//Icon//Contatos//search-24.png", background_color="white", enable_events=True, key="pesquisar")],
                 [sg.Image(filename="Src//Page//Img//Icon//Contatos//Line 6.png", background_color=self.background, pad=(30,(0,40)))],
                 [sg.Table(values=dados,headings=["NOME","NUMERO", "MENSAGEM"], key="table", bind_return_key=True,auto_size_columns=True, background_color="white", expand_x=True, border_width=0,justification='c', font="Jaldi 10 bold", text_color="#6D6D6D",header_border_width=0, max_col_width=15,header_background_color="white", k="table", display_row_numbers=True,sbar_background_color="white", sbar_width=0, sbar_arrow_width=0)],
                 [sg.Image(filename="Src//Page//Img//Icon//Contatos//Line 6.png", background_color=self.background, pad=(30,(50,0)))],
                 ]
        edit_contatos = [
            [sg.Text("", pad=(30,(50, 0)), background_color="white"),sg.Image(filename="Src//Page//Img//Icon//Contatos//note-24.png", background_color=self.background, pad=(30,(50,0)), key="editar", enable_events=True), sg.Image(filename="Src//Page//Img//Icon//Contatos//x-circle-24.png", background_color=self.background, pad=(30,(50,0)), key="excluir", enable_events=True), sg.Image(filename="Src//Page//Img//Icon//Contatos//circle-plus-24 (4).png", key="add",background_color=self.background, pad=(30,(50,0)), enable_events=True)]
        ]
        rodape = [sg.Image(filename="Src//Page//Img//Icon//Automacao//enviaroff.png", background_color="white", pad=(0,(105,0)), k="enviar")]
        
        layout = [cabecalho, contatos, edit_contatos, rodape]
        window = sg.Window("Bot Whatsapp", layout=layout,size=(374, 718), grab_anywhere=True, margins=(0,0), background_color=self.background,icon="Src//Page//Img//Logo//icon.ico", finalize=True)
        
        while True:
                event,values = window.read(timeout=1)
                
                if event == sg.WIN_CLOSED:
                    break
                
                if bool(values["nome_contato"]) and (event == "pesquisar"):
                    window["table"].update(values=dados)
                    
                if event == "add":
                    window.close()
                    break
                    # window.close()
                    # window = janela_automacao.page()
                
                            
            
                # if event == "enviar":
                        #     webbrowser.open_new_tab(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")
                            
                        #     bot.sleep(15)
                        #     bot.press('enter')   
                    
                # window["table"].update(values=contato.visualizar_contato(1))
                    
                # if bool(values["nome_contato"]) == False:
                #     window["table"].update(values=contato.visualizar_contatos())
                    
                
                # if event == "excluir":   
                #     contato.excluir_contato(values["table"][0])
                #     window["table"].update(values=[])
                    
                # if event == "table":
                #     print(values["table"][0])
                #     window["table"].update(values=contato.visualizar_contatos())