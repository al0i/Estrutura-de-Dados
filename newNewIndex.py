class No:
    def __init__(self,value):
        self.value = value
        self.next = None

    def next(self):
        return self.next

    def get_value(self):
        return self.value
    
    def ver_prox(self):
        if self.next == None:
            return False
        else:
            self.ver_prox(self.next)



class Pilha:
    def __init__(self):
        self.topo = -1
        self.cab = None
        self.lenght = self.topo+1


    def add(self,value): #Método de adição
        no = No(value)

        if self.topo == -1:
            self.cab = no
            self.topo += 1
            return True
        
        for i in range(self.lenght):
            if i.next == None:
                i.next = no
                self.topo += 1

    def drop(self):
        if self.topo == -1:
            return False #Empty pile
        else:
            if self.topo == 0:
                self.cab.next = None
                self.cab = None
                self.topo -= 1
                return True
            for i in self.array:
                if i.next == None:
                    i.prev.next = None
                    i.prev = None
                    self.topo -= 1
                    return True

    def __str__(self):
        if self.topo == -1:
            return "Pilha vazia"
        elif self.topo == 0:
            return str(self.cab.value)
        else:
            retorno = str(self.cab.value)
            
            for i in range(self.lenght):
                if i.next == None:
                    pass
                else:
                    retorno+" "+str(i.next)
        return retorno
    
    def get_topo(self):
        print(self.topo)
        return self.topo
    
    def get_values(self, No, retorno):
        if self.topo == -1:
            return "Pilha vazia"
        if No.next == None:
            retorno = retorno+str(No.value)
            return retorno
        else:
            retorno = retorno+str(No.value)+" "
            return self.get_values(No.next, retorno)
        
    def isEmpty(self):
        if self.topo == -1:
            return True
        else:
            return False
        
    def lenght(self):
        return self.topo+1
    
pilha = Pilha()

n1 = No(5)
n2 = No(10)
n3 = No(15)

print(pilha.get_values(pilha.cab, ""))

pilha.add(n1)
print(pilha.get_values(pilha.cab, ""))
pilha.add(n2)
print(pilha.get_values(pilha.cab, ""))
pilha.add(n3)
print(pilha.get_values(pilha.cab, ""))
pilha.drop()
print(pilha.get_values(pilha.cab, ""))
pilha.drop()
print(pilha.get_values(pilha.cab, ""))
pilha.drop()
print(pilha.get_values(pilha.cab, ""))
print(pilha.get_values(pilha.cab, ""))
print(pilha.lenght())