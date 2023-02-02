from Page.Home import Interface_home
from Page.Dados_contato import Interface_dados_contato

import webbrowser
import PySimpleGUI as sg

janela_home = Interface_home()
janela_dados = Interface_dados_contato()


janela1 = janela_home.page()

while True:
    window, event , values = sg.read_all_windows(timeout=1)
    
    if event == sg.WIN_CLOSED:
        break
    
    if window == janela1:
        if event == "entrar" and window == janela1:
            janela1.close()
            janela2 = janela_dados.page()
            break
            
        if  event == "direita":
            window["imagem"].update(filename="Src//Page//Img//Icon//Home//part1.png")
            window["texto"].update(filename="Src//Page//Img//Icon//Home//texto.png")
                    
        if event == "esquerda":
            window["imagem"].update(filename="Src//Page//Img//Icon//Home//part3.png")
            window["texto"].update(filename="Src//Page//Img//Icon//Home//texto3.png")
                
        if event == "como_utilizar":
            webbrowser.open_new_tab("https://github.com/SamuelFLM/Bot-Whatsapp")  
            