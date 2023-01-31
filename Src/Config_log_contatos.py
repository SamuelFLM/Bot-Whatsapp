from Page.Log_contatos import Interface_log_contatos
import PySimpleGUI as sg
from Data.Contatos import Contatos
from Config_dados_contato import Config_dados_contato


janela_contatos = Interface_log_contatos()
contato = Contatos()

class Config_contatos:
    def __init__(self,home) -> None:
       self.window = janela_contatos.page()
       self.window.home = home

    def executar(self, dados):
       
        while True:
            event,values = self.window.read(timeout=1)
            
            if event == "voltar":
                self.window.close()
                self.window.home.executar()
                break
            
            if event == "add":
                self.window.close()
                janela = Config_dados_contato(contato)
                janela.executar()
                break
                        
            if bool(values["nome_contato"]) and (event == "pesquisar"):
                self.window["table"].update(values=[])
                
                
            # self.window["table"].update(values=contato.visualizar_contato(1))
                   
            # if bool(values["nome_contato"]) == False:
            #     self.window["table"].update(values=contato.visualizar_contatos())
                
            
            if event == "excluir":   
                contato.excluir_contato(values["table"][0])
                self.window["table"].update(values=dados)
                
            # if event == "table":
            #     print(values["table"][0])
            #     self.window["table"].update(values=contato.visualizar_contatos())
            
            if event == sg.WIN_CLOSED:
                break
            
if __name__ == "__main__":
    t = Config_contatos()
    t.executar()
        