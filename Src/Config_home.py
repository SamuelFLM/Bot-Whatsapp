
from Page.Home import Interface_home
import PySimpleGUI as sg
import webbrowser
janela_home = Interface_home()

class Config_home:
    
    def __init__(self) -> None:
        self.window = janela_home.page()
        
    def executar(self):
        
        while True:
            event,values = self.window.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                break
            
            if event == "direita":
                self.window["imagem"].update(filename="Src//Page//Img//Icon//Home//part1.png")
                self.window["texto"].update(filename="Src//Page//Img//Icon//Home//texto.png")
                
            if event == "esquerda":
                self.window["imagem"].update(filename="Src//Page//Img//Icon//Home//part3.png")
                self.window["texto"].update(filename="Src//Page//Img//Icon//Home//texto3.png")
            
            if event == "como_utilizar":
                webbrowser.open_new_tab("https://github.com/SamuelFLM/Bot-Whatsapp")    

if __name__ == "__main__":
    t = Config_home()
    t.executar()