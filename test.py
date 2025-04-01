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
            print("Add")
            return True
        
        x = self.cab
        for i in range(self.lenght+1):
            if x.next == None:
                x.next = no
                self.topo += 1
                print("Add")
                return True
            else:
                x = x.next
    
    def __str__(self):
        if self.topo == -1:
            return "Pilha vazia"
        
        else:
            x = self.cab
            retorno = str(x.value)

            for i in range(self.lenght):
                print("AQU!")
                if x.next == None:
                    break
                
                x = x.next
                print('valor',x.value)

                retorno = retorno+" "+str(x.next)
        return retorno

#n1 = No(10)
#n2 = No(15)
#n3 = No(20)

pilha = Pilha()

pilha.add(10)
print(pilha)

pilha.add(15)
print(pilha)