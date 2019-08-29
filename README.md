# Entrevistas Técnicas de Programação

## Atividade sobre buscas em árvores binárias

O objetivo desta atividade é praticar diferentes maneiras de percorrer árvores
binárias. Além disso, vamos exercitar o desenvolvimento de funções recursivas.

Problemas envolvendo árvores binárias são relativamente comuns em entrevistas.
Assim, é importante praticarmos esse tipo de algoritmo para podermos nos preocupar
com a solução do problema em si.

## Descrição da atividade

Você deve implementar as funções definidas em [`search.py`](search.py) de modo
que elas passem nos testes em [`search_test.py`](search_test.py). Você não pode
modificar as assinaturas das funções (ex. adicionar mais argumentos). A função
sempre recebe a raiz da árvore e deve percorrê-la em uma determinada ordem, adicionando
os valores dos nós em uma lista sempre que visitar um novo nó. A lista devolvida
pela sua função será utilizada para verificar a corretude.

Os testes utilizam duas árvores:

### Árvore perfeita

```
               __________0__________
              /                     \
         ____1____               ____2____
        /         \             /         \
      _3_         _4_         _5_         _6_
     /   \       /   \       /   \       /   \
    7     8     9    10    11    12    13    14
```

### Árvore desbalanceada

```
      __________________0___________
     /                              \
    1__________            __________2
               \          /            \
                3__      4____          5
                   \          \           \
                   _6_        _7_          8
                  /   \      /   \        /
                 9    10   11    12     13
```

### Testes

Os testes estão definidos no final do arquivo [`search_test.py`](search_test.py).
A resposta esperada está definida na variável `expected`. Além disso, o nome da
função de teste define se a sua implementação deve ser recursiva ou iterativa.
Por exemplo, no primeiro teste é esperada uma solução recursiva que percorra a
árvore perfeita na seguinte ordem: `[0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 12, 6, 13, 14]`.

## Como entregar

Submeta somente o seu arquivo [`search.py`](search.py) com as soluções na [página da disciplina](http://ensino.kurauchi.com.br/entrevistas/).

## Rubrica

O conceito nesta atividade é definido pela quantidade de testes passando:

| # Testes passando | Conceito |
| :---------------: | :------- |
|       < 4         |    D     |
|         4         |    C     |
|         6         |    C+    |
|         8         |    B     |
|         10        |    B+    |
|         12        |    A     |
|         14        |    A+    |
