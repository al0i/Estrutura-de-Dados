#Pilha com "array" (como Python não tem array, usarei lista)

class No:
    def __init__(self,value):
        self.__value = value

    def get_value(self):
        return self.__value

class Pilha:            
    def __init__(self, lim):
        self.__top = -1
        self.__lim = lim
        self.__array = [None] * self.__lim
        self.__head = self.get_cab()

    #Getters padrões:
    def get_top(self):
        return self.__top
    
    def get_cab(self):
        if self.__array[0] == None:
            return None
        return self.__array[0].get_value()
    
    def get_lenght(self):
        return self.__top + 1
    
    def get_lim(self):
        return self.__lim

    #Setter para dobrar o limite da lista
    def __set_lim(self):
        self.__lim = self.__lim * 2
        newArray = [None] * self.__lim
        for i in range(self.get_lenght()):
            newArray[i] = self.__array[i]
        self.__array = newArray
        return True

    #Retorna os valores contidos na pilha (usei durante o desenvolvimento do programa):
    def get_values(self):
        retorno = ""
        for no in self.__array:
            if no != None:
                retorno = retorno+str(no.get_value())+" "
            else:
                retorno = retorno+str(no)+" "
        return retorno
    
    #Mostra na tela dados gerais da pilha (usei durante o desenvolvimento do programa):
    def dados(self):
        print(f"""
            Topo: {self.get_top()}
            Cab.: {self.get_cab()}
            Len.: {self.get_lenght()}
            Pilha: {self.get_values()}
""")

    #Método de adição de valores à pilha:
    def add(self,value):
        if self.get_lenght() == self.get_lim(): #Se a lista estiver cheia:
            self.__set_lim() #Use o setter para aumentar o limite
        
        no = No(value)
        self.__top = self.__top+1
        self.__array[self.__top] = no
        return True

    #Método de remoção de valores da pilha, que segue o padrão Last-In First-Out:
    def drop(self):
        if self.get_lenght() == 0:
            return False #Pilha vazia
        
        else:
            self.__array[self.__top] = None
            self.__top = self.__top-1
            return True
    
#Função usada para testar o código (como um main()):
def testar():
    pilha = Pilha(5)

    pilha.dados()
    

    for i in range(1,7):
        
        if not pilha.add(i):
            print("PILHA CHEIA!") #Essa mensagem nunca irá aparecer, pois a lista aumenta conforme a demanda
            #print(pilha.get_lenght(), pilha.get_top(), pilha.get_lim())
        pilha.dados()

    for i in range(pilha.get_lenght()+1):
        if not pilha.drop():
            print("PILHA VAZIA!")
        pilha.dados()

testar()