class Tarefa():
    #Função construtora
    def __init__(self,descricao,prioridade,concluida, prazo):
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = concluida
        self.prazo = prazo
    
    def exibirDetalhes(self):
        print(f'descricao: {self.descricao}')
        print(f'prioridade: {self.prioridade}')
        print(f'concluida: {self.concluida}')
        print(f'prazo: {self.prazo}')
    def marcarConcluida(self):
        self.concluida = True
        print(f"A tarefa {self.descricao} foi concluída")
    def mudarPrazo(self, novoPrazo):
        self.prazo = novoPrazo


#Criar objeto
t = Tarefa("teste", "baixa",False,"Até amanhã")
t.exibirDetalhes()
#t.marcarConcluida()
t.mudarPrazo("Até próxima semana")
t.exibirDetalhes()