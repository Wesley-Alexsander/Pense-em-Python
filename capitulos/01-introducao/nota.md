# Capítulo 1: A Jornada do Programa - Notas de Estudo

## 1.1 O que é um Programa?
- **Definição**: Sequência de instruções que especificam tarefas para o computador executar
- **Analogia**: Receita culinária com passos precisos e ordenados

## 1.2 Elementos Básicos de Python
```python
# Exemplo do livro
print("Hello, World!")
```

Componentes:
print() - Função de saída

- "Hello, World!" - String (texto entre aspas)

- Comentário (ignorado pelo interpretador)

## 1.3 Fluxo de Execução

- Ordem linear: Comandos executados de cima para baixo

- Exceções: Estruturas de controle alteram o fluxo (capítulos posteriores)

## 1.4 Erros Comuns:

| Tipo de Erro | Exemplo        | Correção       |
|--------------|----------------|----------------|
| Sintaxe      | `pront("Hello")` | Usar `print()` |
| Semântica    | `print("Hello)`  | Fechar aspas   |

## 1.5 Glossário

- Algoritmo: Processo passo-a-passo para resolver problemas

- Código-fonte: Programa na linguagem original

- Interpretador: Programa que executa código Python diretamente

### 1.6 Operadores aritméticos:
Em Python, as expressões matemáticas seguem a **mesma lógica da aritmética convencional**, tanto na **ordem das operações** quanto na **forma como são interpretadas**. Isso significa que Python respeita a hierarquia de operações, conhecida como **precedência de operadores**, da mesma forma que aprendemos na matemática.

#### **Parênteses `()`**
Parênteses têm a **maior precedência** na ordem de avaliação. Isso significa que qualquer operação dentro de parênteses será realizada antes das demais. Também são úteis para deixar expressões mais fáceis de entender, mesmo que não mudem o resultado final.

- `2 * (3 - 1)` → Primeiro calcula `(3 - 1)`, que dá `2`. Depois: `2 * 2 = 4`
- `(1 + 1) ** (5 - 2)` → Primeiro resolve os parênteses: `2 ** 3 = 8`
- `(minute * 100) / 60` → Mesma coisa que `minute * 100 / 60`, mas os parênteses deixam a intenção mais clara

#### **Exponenciação `**`**
A operação de exponenciação tem a segunda maior precedência. Ela será executada antes de multiplicações, divisões, adições ou subtrações.

- `1 + 2 ** 3` → Primeiro calcula `2 ** 3 = 8`, depois `1 + 8 = 9`
- `2 * 3 ** 2` → Primeiro `3 ** 2 = 9`, depois `2 * 9 = 18`

> ⚠️ A **exponenciação é a única exceção** à regra de avaliação da esquerda para a direita. Ela é avaliada da **direita para a esquerda**.

#### **Multiplicação `*` e Divisão `/`**
Esses dois operadores têm **prioridade maior que a adição e subtração**, mas **menor que os parênteses e a exponenciação**.

- `2 * 3 - 1` → Primeiro `2 * 3 = 6`, depois `6 - 1 = 5`
- `6 + 4 / 2` → Primeiro `4 / 2 = 2`, depois `6 + 2 = 8`

#### **Adição `+` e Subtração `-`**
Têm a **menor precedência** entre os operadores aritméticos. São executados apenas depois que todas as outras operações (parênteses, exponenciação, multiplicação/divisão) forem resolvidas.

#### **Ordem de Avaliação** (Esquerda para Direita)
Quando dois operadores têm a mesma precedência (como `*` e `/`, ou `+` e `-`), a avaliação acontece **da esquerda para a direita**, **exceto na exponenciação**, que é da direita para a esquerda.

- `degrees / 2 * pi` → Primeiro `degrees / 2`, depois multiplica por `pi`
- Para dividir por `2π` diretamente, escreva: `degrees / (2 * pi)` ou `degrees / 2 / pi`



