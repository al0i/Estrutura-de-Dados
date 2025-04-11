#Pilha de encadeamento simples

class No:
    def __init__(self,value):
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

class Pilha:
    def __init__(self):
        self.topo = -1
        self.cab = None #Cabeçalho, que será o primeiro valor da pilha
        self.lenght = self.get_lenght()

    #Getters padrões
    def get_topo(self):
        return self.topo
    
    def get_cab(self):
        if self.cab == None:
            return "Sem cabeçalho"
        return self.cab.value

    def get_lenght(self):
        return self.topo + 1
    
    #Retorna os valores contidos na pilha (usei durante o desenvolvimento do programa)
    def get_values(self):
        retorno = ""
        n = self.cab
        while n != None:
            retorno = retorno+str(n.value)+" "
            n = n.next
        return retorno
    
    #Mostra na tela dados gerais da pilha (usei durante o desenvolvimento do programa)
    def dados(self):
        print(f"""
            Topo: {self.get_topo()}
            Cab.: {self.get_cab()}
            Len.: {self.get_lenght()}
            Pilha: {self.get_values()}
""")

    #Método de adição de valores à pilha
    def add(self,value):
        no = No(value)

        if self.topo == -1:
            self.cab = no
            self.topo += 1
            return True
        
        else:
            n = self.cab
            while n.next != None:
                n = n.next
            n.next = no
            self.topo += 1
            return True
        
    #Método de remoção de valores da pilha, que segue o padrão Last-In First-Out
    def drop(self):
        if self.topo == -1:
            return False #Pilha vazia
        
        elif self.topo == 0:
            self.cab = None
            self.topo -= 1
            return True
        
        else:
            n = self.cab
            while n.next.next != None:
                n = n.next
            n.next = None
            self.topo -= 1
            return True    
    
#Função usada para testar o código
def testar():
    pilha = Pilha()

    pilha.dados()

    for i in range(1,5):
        if(pilha.add(i)):
            print("Nó adicionado.")

    pilha.dados()

    while pilha.drop():
        print("Nó removido")
    
    pilha.dados()

testar()