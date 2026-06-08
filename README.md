# Laboratório de Testes Unitários com Python e PyUnit

Este repositório contém a atividade prática de introdução a testes automatizados utilizando o módulo nativo `unittest` (PyUnit) do Python. O objetivo principal foi compreender os conceitos de asserções, testes de exceções e o ciclo de feedback de testes que passam (OK), falham (FAIL) ou geram erros (ERROR).

## Tecnologias Utilizadas

* **Python 3.x**
* **Módulo nativo `unittest`**
* **Visual Studio Code**

## Estrutura do Projeto

```text
teste-unitario-python/
│
├── calculadora.py       # Contém as funções de operações matemáticas
├── test_calculadora.py  # Contém os testes unitários automatizados
└── README.md            # Documentação do projeto
```
## Funcionalidades Implementadas

Além das operações básicas fornecidas no roteiro inicial (Soma, Subtração, Multiplicação e Divisão), foram desenvolvidos:

* **Função de Potenciação (potencia):** Operação que eleva uma base a um determinado expoente.

## Como Executar os Testes

1. Abra o terminal na raiz do projeto.
2. Execute o comando para rodar a suíte de testes específica:
```text
python -m unittest test_calucladora.py
```
Ou use o descobrimento automático de testes unittest:
```text
python -m unittest discover
```

Exemplo de saída esperada
```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```