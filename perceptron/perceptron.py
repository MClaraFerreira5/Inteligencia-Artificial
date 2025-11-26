"""
Implementação simples do Perceptron.
- weights: vetor com bias + pesos [w0 (bias), w1, w2, ...]
- learning_rate: alpha
- n_epochs: número de épocas (iterações sobre todo o dataset)
- log: lista de strings registrando cada passo (para salvar em txt)
"""

import numpy as np


class Perceptron:
    def __init__(self, input_dim, learning_rate=0.1, n_epochs=2):
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs
        self.weights = np.zeros(input_dim + 1)  # bias + pesos
        self.log = []

    def predict(self, xi):
        return 1 if np.dot(xi, self.weights) > 0 else -1

    def fit(self, X, y):
        X_bias = np.c_[np.ones(X.shape[0]), X]

        self.log.append("Pesos iniciais: " + str(self.weights.tolist()))

        for epoch in range(1, self.n_epochs + 1):
            self.log.append(f"\n=== ÉPOCA {epoch} ===")

            for i, (xi, yi) in enumerate(zip(X_bias, y), start=1):
                y_pred = self.predict(xi)
                update = self.learning_rate * (yi - y_pred)

                self.log.append(f"Exemplo {i}: x={xi.tolist()}, y={yi}, y_pred={y_pred}, update={update}")
                self.log.append(f"  Pesos antes: {self.weights.tolist()}")

                if update != 0:
                    self.weights += update * xi
                    self.log.append(f"  Pesos depois: {self.weights.tolist()}")
                else:
                    self.log.append("  Nenhuma atualização (update=0)")

        self.log.append("\nPesos finais: " + str(self.weights.tolist()))

    def save_log(self, filename="atualizacoes.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for line in self.log:
                f.write(line + "\n")
