class Contatos:
    def __init__(self) -> None:
        self.contatos = []
        
    def visualizar_contatos(self):
        return self.contatos
    
    def visualizar_contato(self, indice):
        return self.contatos[indice]
    
    def adicionar_contato(self,nome,numero, mensagem):
        return self.contatos.append([nome,numero,mensagem])
    
    def excluir_contato(self,indice):
        return self.contatos.pop(indice)
    
    def pesquisar_contato(self):
        pass
    
    def editar_contato(self):
        pass