# coding: utf-8

import time

from threading import Timer
import multiprocessing

class ArCondicionado(object):
    def __init__(self):
        self.gastos = 0
        self.state = 0
        self.runs = 0
        self.temp_atual = 0
    
    def _reduz_um_grau(self):
        """ Reduz um grau na temperatura do ar condicionado """

        self.temp_atual -= 1
        
        # Se eh a primeira vez que eh chamada o gasto eh de 0.50 e nas
        # proximas vezes, o gasto eh de 0.10
        if self.gastos == 0:
            self.gastos += 0.50
        else:
            self.gastos += 0.10
        
    def refrigera(self, temp_atual, temp_desejada, acionamento=1, execucoes=5):
        """
        Efetua a refrigeracao do ambiente

        Params:

            temp_atual: A temperatura atual do local
            temp_desejada: A temperatura desejada pelo usuario
            acionamento: Qual o tempo em segundos que segundos que devemos
                         agendar o metodo de manter a temperatura, levando em
                         consideracao o crescimento vegetativo da mesma
            execucoes: Quantas vezes o processo de manter a temperatura deve ser
                       acionado
        """

        self.state = 1 # ligando o ar
        self.runs = 0
        self.gastos = 0
        self.temp_atual = temp_atual
        self.temp_desejada = temp_desejada
        
        # Variaveis de controle de execucao - po, eh tem um painel avancado de
        # controle =)
        self._acionamento = acionamento
        self._execucoes = execucoes

        # O primeiro passo ao refrigerar eh chegar a temperatura desejada
        # para depois mante-la. Como nao havia uma determinacao no enunciado do
        # problema sobre isso, nao preparei nenhum rotina para determinar qdo
        # chegamos a temperatura do ambiente e estou usando a ideia de que se o
        # corpo humano nao sente a diferenca de temperatura -2+2, entao se
        # queremos 20graus, podemos ficar em 22 reduzindo duas ativacoes da
        # _reduz_um_grau com uma economia potencial de 0.20 centavos cada vez
        # que o ar for ligado
        while self.temp_atual > (self.temp_desejada+2):
            self._reduz_um_grau()
        
        # Agora precisamos vigiar o crescimento vegetativo de 0.5 grau por
        # minuto, para tanto, vamos preparar um marcar um tarefa para manter a
        # temperatura na condicao requerida
        #
        # Lembrando que estamos utilizando a variavel de controle acionamento
        # para facilitar os testes (a unidade de acionamento eh o segundo)
        #
        # Tambem estou usando a ideia de rodar essas tarefas de forma assincro
        # na pois cheguei a pensar no caso do painel de controle onde o ar deve
        # continuar sendo executado e mantendo a temperatura
        #
        # Tive uma dor de cabeca grande com Threads por ter muito pouco conheci
        # mento sobre o assunto, mas com o multiprocessing ficou sensacional.
        # No entanto, precisei usar Timer para rodar em outra thread, tentei
        # simplificar utilizando um loop mas nao deu certo, entao vai assim
        # mesmo
        self._agendar_acionamentos()
        
    def _agendar_acionamentos(self):
        """
        Metodo responsavel por agendar os acionamentos do ar condicionado
        de forma assincrona, permitindo que possamos inspecionar a execucao
        do ar condicionado no painel
        """

        timer = Timer(self._acionamento, self._manter_temperatura)
        processo = multiprocessing.Process(timer.start())
        processo.start()
    
    def _manter_temperatura(self):
        """
        Controla a temperatura do ambiente, nao permitindo passar da temperatura
        desejada.
        """

        # Nao podemos continuar a execucao e criacao de novas tarefas nas
        # seguintes situacoes:
        #    - o ar foi desligado
        #    - a quantidade de execucoes foi atingida (o ar deve ser desligado)
        if self._execucoes == self.runs:
            self.state = 0

        if self.state == 0:
            return
        else:
            self.temp_atual += 0.5
            self.runs += 1

            if self.temp_atual > (self.temp_desejada+2):
                self._reduz_um_grau()
            
            # Terminado esse ciclo, precisamos agendar outro acionamento a ser
            # feito nos proximos self._acionamento segundos
            self._agendar_acionamentos()
    
    def info(self):
        """ Retorna informacoes sobre o estado atual do ar condicionado """

        return self.temp_atual,self.gastos,self.runs


    def desligar(self):
        """
        Desligar o arcondicionado eh dizer que nao iremos agendar mais nenhuma
        tarefa de resfriamento
        """

        # A partir desse momento nao criamos mais tarefas
        self.state = 0


if __name__ == "__main__":
    ar = ArCondicionado()   

    try:
        ar.refrigera(30,20,1,5)
        time.sleep(15)

        # teste heynemman
        #ar.refrigera(30,20,60,360)
        #time.sleep(60*365) # vamos dar um tempo para o processamento
    except KeyboardInterrupt, error:
        print ar.info()
    
    print ar.info()