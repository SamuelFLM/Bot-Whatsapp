
from Page.Envia_mensagem import Interface_automacao
import PySimpleGUI as sg
import webbrowser
janela_automacao = Interface_automacao()

class Config_automacao:
    
    def __init__(self) -> None:
        self.window = janela_automacao.page()
        
    def executar(self):
        
        while True:
            event,values = self.window.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                break
            

if __name__ == "__main__":
    t = Config_automacao()
    t.executar()