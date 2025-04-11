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
        self.lenght = 0

    #Getters padrões
    def get_start(self):
        if self.start == None:
            return self.start
        return self.start.value
    
    def get_end(self):
        if self.end == None:
            return self.end
        return self.end.value

    def get_lenght(self):
        return self.lenght

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
            Lenght: {self.lenght}
            Fila: {self.get_values()}
""")
        
    def enqueue(self, value):
        no = No(value)
        if self.lenght == 0:
            self.start = no
            self.end = no
            self.lenght += 1
        elif self.lenght == 1:
            self.end = no
            self.lenght += 1
            self.start.next = no
        else:
            n = self.start
            while n.next != None:
                n = n.next
            n.next = no
            self.end = no
            self.lenght += 1
        return True
        
    def dequeue(self):
        if self.lenght == 0:
            return False #Lista vazia
        if self.lenght == 1:
            self.end = self.start.next
        self.start = self.start.next
        self.lenght -= 1
        return True

            
    
#Função usada para testar o código
def testar():
    fila = Fila()

    fila.dados()

    for i in range(1,5):
        if(fila.enqueue(i)):
            print("Nó adicionado.")

    fila.dados()

    while fila.dequeue():
        print("Nó removido")
    
    fila.dados()

testar()