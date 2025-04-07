#Fila de encadeamento simples

class No:
    def __init__(self,value):
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

class Fila:
    def __init__(self):
        self.start = None
        self.end = None
        #self.cab = None
        #self.lenght = self.get_lenght()

    #Getters padrões
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end

    '''def get_cab(self):
        if self.cab == None:
            return "Sem cabeçalho"
        return self.cab.value

    def get_lenght(self):
        return self.topo + 1'''
    
    def get_values(self):
        retorno = ""
        n = self.start
        while n != None:
            retorno = retorno+str(n.value)+" "
            n = n.next
        return retorno
    
    def dados(self):
        print(f"""
            Start: {self.get_start()}
            End: {self.get_end()}
            Fila: {self.get_values()}
""")
    
#Função usada para testar o código
def testar():
    fila = Fila()

    fila.dados()

testar()