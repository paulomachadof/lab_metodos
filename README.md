# lab_metodos
**Repositório para as aulas de laboratório de Métodos Numéricos**

## Instruções

Clone este repositório no seu diretório home usando o git no terminal:

```
$ cd ~ # ir ao diretório home do usuário
$ git clone https://github.com/emanueles/lab_metodos.git

```
Foi criada uma pasta chamada *lab_metodos* com todos os arquivos incluídos neste repositório.

## Aula sobre o método da Bisseção
### Objetivo
O objetivo da aula é implementar o método da Bisseção em Python (ou em outra linguagem de sua preferência) e aplicá-lo para achar as raízes de equações não lineares.

### Parte 1: Implementar o método da Bisseção
Inicie com o arquivo fornecido localizado em **raiz/bisect.py**. Esse arquivo já possui um esqueleto iniciado e você só precisa editar os comentários indicados. Para abrir o arquivo, use o comando abaixo em um terminal:

```
$ cd lab_metodos/raiz
$ gedit bisect.py &

```

O arquivo já inclui código para testar o método com o exemplo visto em sala. Observe se você consegue reproduzir a tabela de execução para f(x) = x^3-9x+3, com a = 0, b = 1 e epsilon = 0.001. Seu método deve retornar a mesma raiz e executar até k = 10 iterações.
Para testar o método execute o seguinte comando no terminal:
```
$ python3 bisect.py
```

Se você implementar o método corretamente, você deverá ver a seguinte saída:

```
Método da Bisseção
k	  a		  fa		  b		  fb		  x		  fx		intervX
-	0.000000e+00	3.000000e+00	1.000000e+00	-5.000000e+00	5.000000e-01	-1.375000e+00	1.000000e+00
1	0.000000e+00	3.000000e+00	5.000000e-01	-1.375000e+00	2.500000e-01	7.656250e-01	5.000000e-01
2	2.500000e-01	7.656250e-01	5.000000e-01	-1.375000e+00	3.750000e-01	-3.222656e-01	2.500000e-01
3	2.500000e-01	7.656250e-01	3.750000e-01	-3.222656e-01	3.125000e-01	2.180176e-01	1.250000e-01
4	3.125000e-01	2.180176e-01	3.750000e-01	-3.222656e-01	3.437500e-01	-5.313110e-02	6.250000e-02
5	3.125000e-01	2.180176e-01	3.437500e-01	-5.313110e-02	3.281250e-01	8.220291e-02	3.125000e-02
6	3.281250e-01	8.220291e-02	3.437500e-01	-5.313110e-02	3.359375e-01	1.447439e-02	1.562500e-02
7	3.359375e-01	1.447439e-02	3.437500e-01	-5.313110e-02	3.398438e-01	-1.934391e-02	7.812500e-03
8	3.359375e-01	1.447439e-02	3.398438e-01	-1.934391e-02	3.378906e-01	-2.438627e-03	3.906250e-03
9	3.359375e-01	1.447439e-02	3.378906e-01	-2.438627e-03	3.369141e-01	6.016918e-03	1.953125e-03
10	3.369141e-01	6.016918e-03	3.378906e-01	-2.438627e-03	3.374023e-01	1.788904e-03	9.765625e-04
Raiz encontrada: 0.33740234375

```

## Aula sobre o método da Posição Falsa
### Objetivo
O objetivo da aula é implementar o método da Posição Falsa em Python (ou em outra linguagem de sua preferência) e aplicá-lo para achar as raízes de equações não lineares.

### Parte 1: Implementar o método da Posição Falsa
Inicie com o arquivo fornecido localizado em **raiz/false_pos_.py**. Esse arquivo já possui um esqueleto iniciado e você só precisa editar os comentários indicados. Para abrir o arquivo, use o comando abaixo em um terminal:

```
$ cd lab_metodos/raiz
$ gedit false_pos.py &

```

O arquivo já inclui código para testar o método com o exemplo visto em sala. Observe se você consegue reproduzir a tabela de execução para f(x) = x^3-9x+3, com a = 0, b = 1 e epsilon = 0.001. Seu método deve retornar a mesma raiz e executar até k = 2 iterações.
Para testar o método execute o seguinte comando no terminal:
```
$ python3 false_pos.py
```

Se você implementar o método corretamente, você deverá ver a seguinte saída:

```
Método da Posição Falsa
0	0.000000e+00	3.000000e+00	1.000000e+00	-5.000000e+00	3.750000e-01	-3.222656e-01	1.000000e+00
1	0.000000e+00	3.000000e+00	3.750000e-01	-3.222656e-01	3.386243e-01	-8.790199e-03	3.750000e-01
2	0.000000e+00	3.000000e+00	3.386243e-01	-8.790199e-03	3.376350e-01	-2.258842e-04	3.386243e-01
Raiz encontrada: 0.33763504551140067
```