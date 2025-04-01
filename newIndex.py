class No:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

    def get_near(self): #Get nós proximos (inclusive a si mesmo)
        #Tratamento de excessões, visto que None não tem atributo value
        if self.prev == None and self.next == None: 
            return str(self.prev)+" "+str(self.value)+" "+str(self.next)
        elif self.prev == None:
            return str(self.prev)+" "+str(self.value)+" "+str(self.next.value)
        elif self.next == None:
            return str(self.prev.value)+" "+str(self.value)+" "+str(self.next)
        else:
            return str(self.prev.value)+" "+str(self.value)+" "+str(self.next.value)



class Pilha: #Classe Pilha
    def __init__(self):
        self.array = []
        self.topo = -1 #Topo da pilha
        self.cab = None



    def add(self,No): #Método de adição
        
        if self.topo == -1:
            self.array.append(No)
            self.cab = No
            self.topo += 1
            #print("NÓ ADDED")
            #print(self.cab.value)
            return True
        else:
            for i in self.array:
                if i.next == None:
                    i.next = No
                    No.prev = i
                    self.array.append(No)
                    self.topo += 1
                    return True

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
            
            for i in self.array:
                if i.next == None and i.prev == None:
                    pass
                else:
                    retorno+" "+str(i.value)
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