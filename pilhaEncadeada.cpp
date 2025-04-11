#include <iostream>
#include <string>

using namespace std;

// Pilha de encadeamento simples

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

class Pilha {
private:
    int topo;
    No* cab; // Cabeçalho, que será o primeiro valor da pilha

public:
    Pilha() {
        topo = -1;
        cab = nullptr;
    }

    // Getters padrões
    int get_topo() {
        return topo;
    }

    string get_cab() {
        if (cab == nullptr) {
            return "Sem cabeçalho";
        }
        return to_string(cab->value);
    }

    int get_lenght() {
        return topo + 1;
    }

    // Retorna os valores contidos na pilha (usei durante o desenvolvimento do programa)
    string get_values() {
        string retorno = "";
        No* n = cab;
        while (n != nullptr) {
            retorno = retorno+to_string(n->value) + " ";
            n = n->next;
        }
        return retorno;
    }

    // Mostra na tela dados gerais da pilha (usei durante o desenvolvimento do programa)
    void dados() {
        cout << "\n"
             << "Topo: " << get_topo() << "\n"
             << "Cab.: " << get_cab() << "\n"
             << "Len.: " << get_lenght() << "\n"
             << "Pilha: " << get_values() << "\n"
             << endl;
    }

    // Método de adição de valores à pilha
    bool add(int value) {
        No* no = new No(value);

        if (topo == -1) {
            cab = no;
            topo++;
            return true;
        } else {
            No* n = cab;
            while (n->next != nullptr) {
                n = n->next;
            }
            n->next = no;
            topo++;
            return true;
        }
    }

    // Método de remoção de valores da pilha, que segue o padrão Last-In First-Out
    bool drop() {
        if (topo == -1) {
            return false; // Pilha vazia
        } else if (topo == 0) {
            delete cab;
            cab = nullptr;
            topo--;
            return true;
        } else {
            No* n = cab;
            while (n->next->next != nullptr) {
                n = n->next;
            }
            delete n->next;
            n->next = nullptr;
            topo--;
            return true;
        }
    }
};

// Função usada para testar o código
void testar() {
    Pilha pilha;

    pilha.dados();

    for (int i = 1; i < 5; i++) {
        if (pilha.add(i)) {
            cout << "Nó adicionado." << endl;
        }
    }

    pilha.dados();

    while (pilha.drop()) {
        cout << "Nó removido" << endl;
    }

    pilha.dados();
}

int main() {
    testar();
    return 0;
}
