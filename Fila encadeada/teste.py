# Fila de encadeamento simples

class No:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

class Fila:
    def __init__(self):
        self.inicio = None  # Início da fila
        self.fim = None     # Fim da fila
        self.tamanho = self.get_tamanho()

    # Getters padrões
    def get_inicio(self):
        if self.inicio == None:
            return "Fila vazia"
        return self.inicio.value

    def get_fim(self):
        if self.fim == None:
            return "Fila vazia"
        return self.fim.value

    def get_tamanho(self):
        count = 0
        n = self.inicio
        while n != None:
            count += 1
            n = n.next
        return count

    # Retorna os valores contidos na fila
    def get_values(self):
        retorno = ""
        n = self.inicio
        while n != None:
            retorno += str(n.value) + " "
            n = n.next
        return retorno

    # Mostra na tela dados gerais da fila
    def dados(self):
        print(f"""
            Início: {self.get_inicio()}
            Fim:    {self.get_fim()}
            Tam.:   {self.get_tamanho()}
            Fila:   {self.get_values()}
""")

    # Método para enfileirar (adicionar)
    def enqueue(self, value):
        no = No(value)
        if self.inicio == None:
            self.inicio = self.fim = no
        else:
            self.fim.next = no
            self.fim = no
        return True

    # Método para desenfileirar (remover)
    def dequeue(self):
        if self.inicio == None:
            return False  # Fila vazia

        self.inicio = self.inicio.next

        if self.inicio == None:
            self.fim = None  # Se a fila ficou vazia, atualiza o fim também

        return True

# Função para testar a fila
def testar():
    fila = Fila()

    fila.dados()

    for i in range(1, 5):
        if fila.enqueue(i):
            print("Elemento enfileirado.")

    fila.dados()

    while fila.dequeue():
        print("Elemento desenfileirado.")

    fila.dados()

testar()
