#include <iostream>
#include <string>

using namespace std;

// Fila de encadeamento simples

class No {
public:
    int value;
    No* next;

    No(int val) {
        value = val;
        next = nullptr;
    }

    No* get_next() {
        return next;
    }
};

class Fila {
private:
    No* start;
    No* end;
    int lenght;

public:
    Fila() {
        start = nullptr;
        end = nullptr;
        lenght = 0;
    }

    // Getters padrões
    int get_start() {
        if (start == nullptr) {
            return -1;
        }
        return start->value;
    }

    int get_end() {
        if (end == nullptr) {
            return -1;
        }
        return end->value;
    }

    int get_lenght() {
        return lenght;
    }

    string get_values() {
        string retorno = "";
        No* n = start;
        while (n != nullptr) {
            retorno = retorno+to_string(n->value) + " ";
            n = n->next;
        }
        return retorno;
    }

    void dados() {
        cout << "\n"
             << "Start: " << get_start() << "\n"
             << "End: " << get_end() << "\n"
             << "Lenght: " << lenght << "\n"
             << "Fila: " << get_values() << "\n"
             << endl;
    }

    bool enqueue(int value) {
        No* no = new No(value);
        if (lenght == 0) {
            start = no;
            end = no;
            lenght++;
        } else if (lenght == 1) {
            end = no;
            start->next = no;
            lenght++;
        } else {
            No* n = start;
            while (n->next != nullptr) {
                n = n->next;
            }
            n->next = no;
            end = no;
            lenght++;
        }
        return true;
    }

    bool dequeue() {
        if (lenght == 0) {
            return false; // Lista vazia
        }
        if (lenght == 1) {
            end = start->next;
        }
        No* temp = start;
        start = start->next;
        delete temp;
        lenght--;
        return true;
    }
};

// Função usada para testar o código
void testar() {
    Fila fila;

    fila.dados();

    for (int i = 1; i <= 4; i++) {
        if (fila.enqueue(i)) {
            cout << "Nó adicionado." << endl;
        }
    }

    fila.dados();

    while (fila.dequeue()) {
        cout << "Nó removido" << endl;
    }

    fila.dados();
}

int main() {
    testar();
    return 0;
}
