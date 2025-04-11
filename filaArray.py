#Fila com "array" (como Python não tem array, usarei lista)

class No:
    def __init__(self,value):
        self.__value = value

    def get_value(self):
        return self.__value

class Fila:            
    def __init__(self, lim):
        self.__lim = lim
        self.__array = [None] * self.__lim
        self.__start = self.get_start()
        self.__end = None
        self.__lenght = 0
        

    #Getters padrões:
    def get_start(self):
        if self.__array[0] == None:
            return self.__array[0]
        return self.__array[0].get_value()
    
    def get_end(self):
        if self.__end == None:
            return self.__end
        return self.__end.get_value()
    
    def get_lenght(self):
        return self.__lenght
    
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
            Start: {self.get_start()}
            End: {self.get_end()}
            Len.: {self.get_lenght()}
            Fila: {self.get_values()}
""")

    #Método de adição de valores à pilha:
    def enqueue(self,value):
        if self.get_lenght() == self.get_lim(): #Se a lista estiver cheia:
            self.__set_lim() #Use o setter para aumentar o limite
        
        no = No(value)
        if self.__lenght == 0:
            self.__start = no
            self.__end = no
            
        self.__array[self.__lenght] = no
        self.__end = no
        self.__lenght = self.__lenght + 1
        return True

    #Método de remoção de valores da pilha, que segue o padrão Last-In First-Out:
    def dequeue(self):
        if self.get_lenght() == 0:
            return False #Pilha vazia
        
        else:
            if self.__lenght == 1:
                self.__end = None
            newArray = [None] * self.__lim
            for i in range(self.__lenght-1):
                newArray[i] = self.__array[i+1]

            self.__array = newArray
            self.__lenght = self.__lenght-1
            return True
    
#Função usada para testar o código (como um main()):
def testar():
    fila = Fila(5)

    fila.dados()

    for i in range(1,7):
        if(fila.enqueue(i)):
            print("Nó adicionado.")
        fila.dados()

    while fila.dequeue():
        print("Nó removido")
        fila.dados()
    
    fila.dados()


testar()