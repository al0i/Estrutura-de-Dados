#include <iostream>
#include <string>

using namespace std;

// Pilha com "array" (como Python não tem array, usarei lista)

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

class Pilha {
private:
    int top;
    int lim;
    No** array;
    int cabecalho;

    // Setter para dobrar o limite da lista
    void set_lim() {
        lim *= 2;
        No** newArray = new No*[lim];
        for (int i = 0; i < get_lenght(); i++) {
            newArray[i] = array[i];
        }
        for (int i = get_lenght(); i < lim; i++) {
            newArray[i] = nullptr;
        }
        delete[] array;
        array = newArray;
    }

public:
    Pilha(int lim) {
        this->lim = lim;
        top = -1;
        array = new No*[lim];
        for (int i = 0; i < lim; i++) {
            array[i] = nullptr;
        }
        cabecalho = get_cab(); // só inicializa, não é usado diretamente
    }

    ~Pilha() {
        for (int i = 0; i <= top; i++) {
            delete array[i];
        }
        delete[] array;
    }

    // Getters padrões:
    int get_top() {
        return top;
    }

    int get_cab() {
        if (array[0] == nullptr) {
            return -1;
        }
        return array[0]->get_value();
    }

    int get_lenght() {
        return top + 1;
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
             << "Topo: " << get_top() << "\n"
             << "Cab.: " << get_cab() << "\n"
             << "Len.: " << get_lenght() << "\n"
             << "Pilha: " << get_values() << "\n"
             << endl;
    }

    // Método de adição de valores à pilha:
    bool add(int value) {
        if (get_lenght() == get_lim()) { // Se a lista estiver cheia:
            set_lim(); // Use o setter para aumentar o limite
        }

        No* no = new No(value);
        top += 1;
        array[top] = no;
        return true;
    }

    // Método de remoção de valores da pilha, que segue o padrão Last-In First-Out:
    bool drop() {
        if (get_lenght() == 0) {
            return false; // Pilha vazia
        } else {
            delete array[top];
            array[top] = nullptr;
            top -= 1;
            return true;
        }
    }
};

// Função usada para testar o código (como um main()):
void testar() {
    Pilha pilha(5);

    pilha.dados();

    for (int i = 1; i <= 6; i++) {
        if (!pilha.add(i)) {
            cout << "PILHA CHEIA!" << endl; // Essa mensagem nunca irá aparecer, pois a lista aumenta conforme a demanda
        }
        pilha.dados();
    }

    for (int i = 0; i <= pilha.get_lenght(); i++) {
        if (!pilha.drop()) {
            cout << "PILHA VAZIA!" << endl;
        }
        pilha.dados();
    }
}

int main() {
    testar();
    return 0;
}
