# Atividade 7 — Treinamento de um Perceptron

**Disciplina:** Inteligência Artificial  
**Professor:** Anderson Cavalcanti  
**Universidade:** Universidade Federal Rural de Pernambuco — UABJ

Autores: **Yann K. J. Leão** e **Maria Clara da Silva Ferreira**  
Curso: Engenharia da Computação

## Conteúdo da Pasta

- `main.ipynb` → Notebook principal com implementação, treinamento e explicações.
- `atualizacoes.txt` → Registro completo das atualizações de pesos durante as duas épocas de treinamento.
- `perceptron.py` → Arquivo contendo a classe Perceptron caso seja usada separadamente.

## Objetivo da Atividade

Implementar o funcionamento do **Perceptron clássico** e treinar o modelo utilizando:

- Pesos **iniciais iguais a 0**
- Taxa de aprendizado **α = 0,1**
- **Duas épocas de treinamento**
- Dataset com quatro exemplos contendo duas features e um rótulo (passou/não passou)

Além disso, registrar **todas as atualizações de pesos** ao longo do treinamento em um arquivo `.txt`.

## Descrição do Problema

O professor forneceu uma tabela com quatro alunos:

| Aluno      | Estudou | Fez Trabalho | Passou |
|------------|---------|--------------|--------|
| Joãozinho  | Não     | Não          | Não    |
| Huguinho   | Não     | Sim          | Não    |
| Zezinho    | Sim     | Não          | Sim    |
| Luizinho   | Sim     | Sim          | Sim    |

Codificação utilizada:

- **Estudou:** Não = 0, Sim = 1
- **Fez Trabalho:** Não = 0, Sim = 1
- **Passou (alvo):** Não = −1, Sim = +1

## Como executar

### Abrir o notebook

```bash
jupyter notebook main.ipynb
````

## Geração automática do arquivo de log

O próprio notebook gera o arquivo de log. 
Dinsponível em: [atualizacoes.txt](../perceptron/atualizacoes.txt)
