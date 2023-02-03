class Contatos:
    def __init__(self) -> None:
        self.contatos = [["Nome contato", "5531999999999", "sua mensagem"]]
        
    def visualizar_contatos(self):
        return self.contatos
    
    def visualizar_contato(self, indice):
        return self.contatos[indice]
    
    def adicionar_contato(self,nome,numero, mensagem):
        
        return self.contatos.append([nome,numero,mensagem])
    
    def excluir_contato(self,indice):
        if indice >= 1:
            return self.contatos.pop(indice)
    
    def pesquisar_contato(self,nome):
        for i in range(len(self.contatos)):
            for j in range(len(self.contatos[i])):
                if self.contatos[i][j] == nome:
                    lista = []
                    lista.append(self.contatos[i])
                    return lista
        else:
            return False
        
    def alteracao_lista_original(self,nome):
        for i in range(len(self.contatos)):
            for j in range(len(self.contatos[i])):
                if self.contatos[i][j] == nome:
                    return self.contatos[i]
        else:
            return False
        
    def editar_contato(self, indice):
       return self.contatos[indice]