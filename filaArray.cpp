#include <iostream>
#include <string>

using namespace std;

// Fila com "array" (como Python não tem array, usarei lista)

class No {
private:
    int value;

public:
    No(int val) {
        value = val;
    }

    int get_value() {
        return value;
    }
};

class Fila {
private:
    int lim;
    No** array;
    No* start;
    No* end;
    int lenght;

    // Setter para dobrar o limite da lista
    void set_lim() {
        lim *= 2;
        No** newArray = new No*[lim];
        for (int i = 0; i < lenght; i++) {
            newArray[i] = array[i];
        }
        for (int i = lenght; i < lim; i++) {
            newArray[i] = nullptr;
        }
        delete[] array;
        array = newArray;
    }

public:
    Fila(int lim) {
        this->lim = lim;
        array = new No*[lim];
        for (int i = 0; i < lim; i++) {
            array[i] = nullptr;
        }
        start = nullptr;
        end = nullptr;
        lenght = 0;
    }

    ~Fila() {
        for (int i = 0; i < lenght; i++) {
            delete array[i];
        }
        delete[] array;
    }

    // Getters padrões:
    int get_start() {
        if (array[0] == nullptr) return -1;
        return array[0]->get_value();
    }

    int get_end() {
        if (end == nullptr) return -1;
        return end->get_value();
    }

    int get_lenght() {
        return lenght;
    }

    int get_lim() {
        return lim;
    }

    // Retorna os valores contidos na pilha (usei durante o desenvolvimento do programa):
    string get_values() {
        string retorno = "";
        for (int i = 0; i < lim; i++) {
            if (array[i] != nullptr) {
                retorno = retorno+to_string(array[i]->get_value()) + " ";
            } else {
                retorno = retorno+"None ";
            }
        }
        return retorno;
    }

    // Mostra na tela dados gerais da pilha (usei durante o desenvolvimento do programa):
    void dados() {
        cout << "\n"
             << "Start: " << get_start() << "\n"
             << "End: " << get_end() << "\n"
             << "Len.: " << get_lenght() << "\n"
             << "Fila: " << get_values() << "\n"
             << endl;
    }

    // Método de adição de valores à pilha:
    bool enqueue(int value) {
        if (get_lenght() == get_lim()) { // Se a lista estiver cheia:
            set_lim(); // Use o setter para aumentar o limite
        }

        No* no = new No(value);
        if (lenght == 0) {
            start = no;
            end = no;
        }

        array[lenght] = no;
        end = no;
        lenght++;
        return true;
    }

    // Método de remoção de valores da pilha, que segue o padrão Last-In First-Out:
    bool dequeue() {
        if (get_lenght() == 0) {
            return false; // Pilha vazia
        }

        else {
            if (lenght == 1) {
                delete array[0];
                array[0] = nullptr;
                end = nullptr;
            } else {
                delete array[0];
                for (int i = 0; i < lenght - 1; i++) {
                    array[i] = array[i + 1];
                }
                array[lenght - 1] = nullptr;
            }
            lenght--;
            return true;
        }
    }
};

// Função usada para testar o código (como um main()):
void testar() {
    Fila fila(5);

    fila.dados();

    for (int i = 1; i <= 6; i++) {
        if (fila.enqueue(i)) {
            cout << "Nó adicionado." << endl;
        }
        fila.dados();
    }

    while (fila.dequeue()) {
        cout << "Nó removido" << endl;
        fila.dados();
    }

    fila.dados();
}

int main() {
    testar();
    return 0;
}
