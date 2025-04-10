#Pilha com "array" (como Python não tem array, usarei lista)

class No:
    def __init__(self,value):
        self.__value = value

    def get_value(self):
        return self.__value

class Pilha:            
    def __init__(self, lim):
        self.__top = -1
        self.__array = []
        self.__lim = lim
        self.__head = self.get_cab()

    #Getters padrões:
    def get_topo(self):
        return self.__top
    
    def get_cab(self):
        if self.get_lenght() == 0:
            return None
        return self.__array[0].get_value()
    
    def get_lenght(self):
        return self.__top + 1

    #Retorna os valores contidos na pilha (usei durante o desenvolvimento do programa):
    def get_values(self):
        retorno = ""
        for no in self.__array:
            retorno = retorno+str(no.get_value())+" "
        return retorno
    
    #Mostra na tela dados gerais da pilha (usei durante o desenvolvimento do programa):
    def dados(self):
        print(f"""
            Topo: {self.get_topo()}
            Cab.: {self.get_cab()}
            Len.: {self.get_lenght()}
            Pilha: {self.get_values()}
""")

    #Método de adição de valores à pilha:
    def add(self,value):
        if self.get_lenght() == self.__lim:
            return False
        
        elif self.get_lenght() == 0:
            no = No(value)
            self.__array = [no]
            self.__top += 1
            return True

        else:
            no = No(value)
            newArray = [None] * (self.get_lenght()+1)
            for i in range(self.get_lenght()):
                newArray[i] = self.__array[i]
            newArray[self.get_lenght()] = no
            self.__array = newArray
            self.__top = self.__top+1
            return True

    #Método de remoção de valores da pilha, que segue o padrão Last-In First-Out:
    def drop(self):
        if self.get_lenght() == 0:
            return False #Pilha vazia
        
        else:
            newArray = [None] * (self.get_lenght()-1)
            for i in range(self.get_lenght()-1):
                newArray[i] = self.__array[i]
            self.__array = newArray
            self.__top = self.__top-1
            return True
    
#Função usada para testar o código (como um main()):
def testar():
    pilha = Pilha(5)

    pilha.dados()
    

    for i in range(1,7):
        
        if not pilha.add(i):
            print("PILHA CHEIA!")
        pilha.dados()

    for i in range(pilha.get_lenght()+1):
        if not pilha.drop():
            print("PILHA VAZIA!")
        pilha.dados()

testar()