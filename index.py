class No: #Classe Nó
    def __init__(self,value):
        self.value = value #Valor do Nó
        self.prev = None #Nó anterior
        self.next = None #Próximo nó

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
        self.topo = None #Topo da pilha



    def add(self,No): #Método de adição
        if self.topo == None:
            self.array.append(No)
            self.topo = self.array.index(No)
        else:
            self.array.append(No)
            No.prev = self.array[self.topo]
            self.topo = self.array.index(No)
            self.array[self.topo-1].next = No
    
    def drop(self):
        if self.topo == -1:
            return False #Empty pile
        else:
            self.array.remove(self.array[self.topo])
            self.topo -= 1
            return True #Success!

    def __str__(self):
        retorno = ""
        for i in self.array:
            retorno = retorno+str(i.value)+" "
        return retorno
    
    def get_topo(self):
        print(self.topo)
        return self.topo
    
pilha = Pilha()



n1 = No(5)
n2 = No(10)
n3 = No(15)

pilha.add(n1)

print(n1.get_near())

pilha.add(n2)
pilha.add(n3)
print(pilha, pilha.topo)

print("NEAR:")
print(n1.get_near())
print("NEAR:")
print(n2.get_near())
print("NEAR:")
print(n3.get_near())


pilha.drop()
print(pilha, pilha.topo)


pilha.drop()
print(pilha, pilha.topo)

pilha.add(n3)
print(pilha, pilha.topo)

pilha.add(n2)
print(pilha, pilha.topo)

pilha.drop()
print(pilha, pilha.topo)
pilha.drop()
print(pilha, pilha.topo)
pilha.drop()
print(pilha, pilha.topo)
pilha.drop()
print(pilha, pilha.topo)


n4 = No(20)