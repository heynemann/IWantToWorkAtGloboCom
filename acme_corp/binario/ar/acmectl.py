from core import ArCondicionado

import cmd

class PainelComando(cmd.Cmd):
    """ Painel de controle do ar condicionado """
    
    def preloop(self):
        """ Instanciacao do ar condicionado a ser mantido """

        self.ar = ArCondicionado()

    def do_info(self, line):
        """ info - Retorna a temperatura atual e os gastos e execucoes """

        print "Temperatura: %s / Gastos: %s / Execucoes: %s" % self.ar.info()

    def do_refrigera(self, line):
        """refrigera temp_atual temp_desejada [acionamento] [execucoes]
        Liga o ar condicionado e mantem a temperatura estavel"""

        temps = line.split(" ")

        if len(temps) in [2,4]:
            temps = map(lambda x: int(x), temps)
            self.ar.refrigera(*temps)

        print "Ar condicionado ligado e resfriando !"
    
    def do_desligar(self, line):
        """ Desligar o ar condicionado """
        
        self.ar.desligar()
    
    def do_quit(self, line):
        """ quit - Sair do painel de controle e desligar o ar condicionado """

        self.do_desligar(line)
        return True

if __name__ == "__main__":
    PainelComando().cmdloop()