#include <iostream>
#include <vector>
#include <cmath>
#define N 8
using namespace std;

void mostrarSolucao(const vector<vector<int>> & tabuleiro) {
    static int contador = 1;
    cout << "Solucao " << contador++ << ":"  << endl;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (tabuleiro[i][j] == 1) {
                cout << " Q ";
            }
            else {
                cout << " . ";
            }
        }
        cout << endl;
    }
    cout << endl;
}

bool ehSeguro(const vector<vector<int>> & tabuleiro, int linha, int coluna) {
    int i , j;

    for (i = 0; i < coluna; i++) {
        if (tabuleiro[linha][i]) {
            return false;
        }

    }

    for (i = linha, j = coluna; i >= 0 && j >= 0; i--, --j) {
        if (tabuleiro[i][j]) {
            return false;
        }
    }

    for (i = linha, j = coluna; j >= 0 && i < N; i++, --j) {
        if (tabuleiro[i][j]) {
            return false;
        }
    }
    return true;
}

bool solucao(vector<vector<int>> & tabuleiro, int coluna) {
    if (coluna >= N) {
        mostrarSolucao(tabuleiro);
        return true;
    }

    bool res = false;
        for (int i = 0; i < N; i++) {
            if (ehSeguro(tabuleiro, i, coluna)) {
                tabuleiro[i][coluna] = 1;

                res = solucao(tabuleiro, coluna+1) || res;

                tabuleiro[i][coluna] = 0;
            }
        }
    return res;
}

void resolveNRainhas() {
    vector<vector<int>> tabuleiro(N, vector<int>(N, 0));

    if (!solucao(tabuleiro, 0)) {
        cout << "Não existe solução" << endl;
    }
}



bool ehSolucao(const vector<int>& estado) {

    for (int i = 0; i < estado.size(); ++i) {

        for (int j = i + 1; j < estado.size(); ++j) {


            if (estado[i] == estado[j]) {
                cout << "Falso"<< endl;
                return false;

            }

            if (std::abs(estado[i] - estado[j]) == std::abs(i - j)) {
                cout << "Falso"<< endl;
                return false;
            }
        }
    }
    cout << "Verdade"<< endl;
    return true;
}



int main() {
    vector estado(N, 0);
    estado = {7, 3, 0, 2, 5, 1, 6, 4};
    resolveNRainhas();
    ehSolucao(estado);
    return 0;
    // TIP See CLion help at <a href="https://www.jetbrains.com/help/clion/">jetbrains.com/help/clion/</a>. Also, you can try interactive lessons for CLion by selecting 'Help | Learn IDE Features' from the main menu.
}