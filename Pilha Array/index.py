#Pilha com "array" (como Python não tem array, usarei lista)

class No:
    def __init__(self,value):
        self.value = value

class Pilha:            
    def __init__(self, lim):
        self.topo = -1
        self.array = []
        self.lim = lim
        self.lenght = self.get_lenght()
        self.cab = self.get_cab() #Cabeçalho, que será o primeiro valor da pilha

    #Getters padrões
    def get_topo(self):
        return self.topo
    
    def get_cab(self):
        if self.get_lenght() == 0:
            return None
        return self.array[0].value
    
    def get_lenght(self):
        return self.topo + 1

    #Retorna os valores contidos na pilha (usei durante o desenvolvimento do programa)
    def get_values(self):
        retorno = ""
        for no in self.array:
            retorno = retorno+str(no.value)+" "
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
        if self.get_lenght() == self.lim:
            return False
        
        no = No(value)
        self.array += [no]
        self.topo += 1
        return True
        
        
    #Método de remoção de valores da pilha, que segue o padrão Last-In First-Out
    def drop(self):
        if self.get_lenght() == 0:
            return False #Pilha vazia
        
        elif self.get_lenght() == 1:
            self.cab = None
            self.topo -= 1
            self.array = [x for x in self.array if x != self.array[-1]]
            return True
        
        else:
            arrayLenght = self.get_lenght()
            newArray = []
            for i in range(arrayLenght-1):
                newArray = newArray + [self.array[i]]#VERIFICAR!
            self.topo -= 1
            self.array = newArray
            return True    
    
#Função usada para testar o código
def testar():
    pilha = Pilha(5)


    pilha.get_lenght()
    pilha.dados()

    pilha.add(1)
    pilha.dados()

    pilha.add(2)
    pilha.dados()

    pilha.add(3)
    pilha.dados()

    pilha.add(4)
    pilha.dados()

    pilha.drop()
    pilha.dados()

    pilha.drop()
    pilha.dados()

    pilha.drop()
    pilha.dados()

    pilha.drop()
    pilha.dados()

testar()