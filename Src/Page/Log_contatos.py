import PySimpleGUI as sg
import webbrowser
import pyautogui as bot
class Interface_log_contatos:
    
    def __init__(self, janela) -> None:
        self.background = "white"
        self.janela = janela
        
    def page(self, dados, contatos_a):
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
        rodape = [sg.Image(filename="Src//Page//Img//Icon//Automacao//enviaroff.png", background_color="white", pad=(0,(105,0)), k="enviar", enable_events=True)]
        
        layout = [cabecalho, contatos, edit_contatos, rodape]
        window = sg.Window("Bot Whatsapp", layout=layout,size=(374, 718), grab_anywhere=True, margins=(0,0), background_color=self.background,icon="Src//Page//Img//Logo//icon.ico", finalize=True)
        
        window["table"].update(values=dados)
        while True:
                event,values = window.read(timeout=1)
                
                if event == sg.WIN_CLOSED:
                    break
                try:
                    nome_pesquisa = values["nome_contato"]
                    if bool(values["nome_contato"]) and (event == "pesquisar"):
                        window["table"].update(values=dados)
                        contato = contatos_a.pesquisar_contato(nome_pesquisa)
                        if contato:
                            window["table"].update(contato)
                            window["excluir"].update(enable_events=False)
                            window["add"].update(enable_events=False)
                            window["editar"].update(enable_events=False)
                            
                        
           
                    
                    if bool(values["nome_contato"]) == False and (event == "pesquisar"):
                           window["table"].update(values=dados)
                        
                            
                    if event == "add":
                        window.close()
                        self.janela.page()
                        break
                        
                    indice_contato = values["table"][0]
                    
                    
                    if bool(indice_contato):
                        window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//enviaron.png")
                        if event == "enviar":
                            numero = contatos_a.visualizar_contato(indice_contato)[1]
                            mensagem = contatos_a.visualizar_contato(indice_contato)[2]
                            webbrowser.open_new_tab(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")
                            bot.sleep(15)
                            bot.press('enter')
                    else:   
                        window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//enviaroff.png")
                    
                    if event == "editar":
                        window.close()
                        nome = contatos_a.visualizar_contato(indice_contato)[0]
                        numero = contatos_a.visualizar_contato(indice_contato)[1]
                        mensagem = contatos_a.visualizar_contato(indice_contato)[2]
                        self.janela.page_att_contato(indice_contato, nome, numero, mensagem)  
                        break
                           
                    
                    if event == "excluir":   
                        contatos_a.excluir_contato(values["table"][0])
                        window["table"].update(values=dados)
                except:
                    pass        
                    