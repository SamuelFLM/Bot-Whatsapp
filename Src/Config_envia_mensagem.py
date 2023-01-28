import re
from Page.Envia_mensagem import Interface_automacao
import PySimpleGUI as sg
import pyautogui as bot
import webbrowser

janela_automacao = Interface_automacao()


class Config_automacao:
    
    def __init__(self, home) -> None:
        self.window = janela_automacao.page()
        self.window.home = home
        
    def executar(self):
        
        while True:
            event,values = self.window.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                break
            
            tamanho_mensagem = len(values["mensagem"])
            self.window["tamanho_mensagem"].update(f"{tamanho_mensagem} caracteres")

            if event == "voltar":
                self.window.close()
                self.window.home.executar()
                break
            
            numero = str(values["numero"])
            mensagem = str(values["mensagem"])
            if event == "enviar":
                webbrowser.open_new_tab(f"https://api.whatsapp.com/send?phone={numero}&text={mensagem}")
                
                while bot.locateCenterOnScreen("Src//Page//Img//Icon//Automacao//iniciar_conversa.png"):
                    bot.sleep(1)
                iniciar = bot.locateCenterOnScreen("Src//Page//Img//Icon//Automacao//iniciar_conversa.png")
                bot.click(iniciar[0],iniciar[1])
                    
                
                
        
            
            if bool(values["numero"] and values["mensagem"]):
                self.window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//enviaron.png")
            else:
                self.window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//enviaroff.png")
                
            if bool(values["numero"] and values["mensagem"]):
                self.window["add"].update(filename="Src//Page//Img//Icon//Automacao//addon.png")
            else:
                self.window["add"].update(filename="Src//Page//Img//Icon//Automacao//addoff.png")
            
                        
if __name__ == "__main__":
    t = Config_automacao()
    t.executar()