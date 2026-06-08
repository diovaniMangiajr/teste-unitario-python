# Laboratório de Testes Unitários com Python e PyUnit

Este repositório contém a atividade prática de introdução a testes automatizados utilizando o módulo nativo `unittest` (PyUnit) do Python. O objetivo principal foi compreender os conceitos de asserções, testes de exceções e o ciclo de feedback de testes que passam (OK), falham (FAIL) ou geram erros (ERROR).

## Tecnologias Utilizadas

* **Python 3.12.3**
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
* **Desafio Extra(calcular_meda):** Função que recebe uma lista de números, calcula a média aritmétca e trata o cenário de listas vazias lançando uma exceção.

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
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

## Uso de IA para Geração de Cenários de Teste (Atividade Prática 2)

### 1. Função Escolhida
`calcular_media(lista)`

### 2. Prompt Utilizado
* **Prompt para gerar os cenários.**
```text
"Atue como um professor de Teste de Software.

  

Tenho a seguinte função Python:

  

def calcular_media(lista: list) -> float:
    """Retorna a média de uma lista de números
    Se a lista vier vazia levanta um ValueError
    """

    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    
    return sum(lista) / len(lista)"

  

Quero criar testes unitários usando unittest.

  

Liste pelo menos 6 cenários de teste para essa função.

  

Para cada cenário, informe:

- nome do cenário;

- entrada;

- resultado esperado;

- tipo do cenário: caso normal, caso de borda ou caso de erro.

  

Não gere código ainda.
```

* **Prompt para gerar os códigos dos testes.**
```text

Agora transforme os cenários aprovados em testes unitários usando Python e unittest.


Considere que a função já foi importada no arquivo test_calculadora.py.


Gere apenas o método de teste que deve ser colocado dentro da classe TestCalculadora.

Use nomes de métodos iniciando com test_.
```
### 3. Tabela de Cenários Planejados/Sugeridos

| ID  | Cenário                    | Entrada            | Resultado Esperado | Tipo de caso|
| :-- | :-------------------       | :----------------- | :----------------- | :---------- |
| T01 | Lista de inteiros positvos | `[10, 20, 30, 40]` | `25`               | normal      |
| T02 | Lista com elemento únco    | `[7.5]`            | `7.5`              | de borda    |
| T03 | Lista com números negativos| `[-5, -15, -10]`   | `-10`              | normal      |
| T04 | Lista vazia                | `[]`               | `ValueError`       | de erro     |
| T05 | Lista com números decimais | `[1.5, 2.5, 3.5]`  | `2.5`              | normal      |
| T06 | Média resultante em zero   | `[-10, 10]`        | `0.0`              | borda       |

### 4. Análise dos Cenários
* **Aceitos:** Todos os cenários normais e de borda sugeridos foram incorporados utilizando a estrutura `with self.subTest(...)`.
* **Alterados/Removidos:** (Refatorei todos os testes da função de cálculo de média para usar subtest e o código ficar mais limpo).

### 5. Código final dos testes

```python
def test_calcular_media_com_varios_casos(self):
    """Testa a média aritmética com listas de números variados."""
    casos = [
        ([10, 20, 30, 40], 25),
        ([7.5], 7.5),
        ([-5, -15, -10], -10),
        ([1.5, 2.5, 3.5], 2.5),
        ([-10, 10], 0),
    ]

    for lista, esperado in casos:
        with self.subTest(lista=lista):
            self.assertEqual(calcular_media(lista), esperado)

def test_calcular_media_lista_vazia(self):
    """Garante que calcular_media lança ValueError ao receber lista vazia."""
    with self.assertRaises(ValueError):
        calcular_media([])
```

### 6. Resultado da Execução no Terminal
```bash
python -m unittest discover
```

![Print do Terminal](/docs/print_terminal.png)