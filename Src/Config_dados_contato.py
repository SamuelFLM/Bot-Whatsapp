import re
from Page.Dados_contato import Interface_dados_contato
import PySimpleGUI as sg

janela_automacao = Interface_dados_contato()

class Config_dados_contato:
    
    def __init__(self, manipulicao_contatos) -> None:
        self.window = janela_automacao.page()
        self.window.contatos = manipulicao_contatos
       
    def executar(self):
        
        while True:
            event,values = self.window.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                break
            
            tamanho_mensagem = len(values["mensagem"])
            self.window["tamanho_mensagem"].update(f"{tamanho_mensagem} caracteres")

            if event == "voltar":
                self.window.close()
                self.window.log_contatos.executar()
                break
            
            # if event == "enviar":
            #     webbrowser.open_new_tab(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")
                
            #     bot.sleep(15)
            #     bot.press('enter')
            
            if bool(values["nome_contato"]) and bool(values["numero"] and values["mensagem"]):
                self.window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//Group 20.png")
                if event == "enviar":
                    nome = str(values["nome_contato"])
                    numero = str(values["numero"])
                    mensagem = str(values["mensagem"])
            else:
                self.window["enviar"].update(filename="Src//Page//Img//Icon//Automacao//Group 19 (2).png")

            
                        
if __name__ == "__main__":
    t = Config_dados_contato(contatos=None)
    t.executar()
        
   