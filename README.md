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
k	  a		  fa		  b		  fb		  x		    fx		    intervX
0	0.000000e+00	3.000000e+00	1.000000e+00	-5.000000e+00	3.750000e-01	-3.222656e-01	1.000000e+00
1	0.000000e+00	3.000000e+00	3.750000e-01	-3.222656e-01	3.386243e-01	-8.790199e-03	3.750000e-01
2	0.000000e+00	3.000000e+00	3.386243e-01	-8.790199e-03	3.376350e-01	-2.258842e-04	3.386243e-01
Raiz encontrada: 0.33763504551140067
```

## 04/11/2015 - Comparando os resultados dos métodos
### Objetivo
O objetivo da aula é aplicar os métodos implementados nas duas aulas acima para achar as raízes de equações não lineares e comparar os resultados.

### Inicialização
Tenha certeza de que você já sincronizou o seu fork com o repositório original e que na sua máquina local você já tenha um clone do seu repositório sincronizado com o bitbucket. O teste assume que você já implementou os métodos da bisseção e da posição falsa.

Abra um terminal, dê um cd na pasta do seu repositório e liste o conteúdo da pasta:
```
$ cd lab_metodos
$ ls
```

Você pode ver que foi acrescentada uma pasta nova, chamada testes:
```
README.md raiz      testes
```

Entre na pasta testes e abra o arquivo **teste01.py**:
```
$ cd testes
$ gedit teste01.py &

```

Resolva as questões abaixo:

### Q1
Compare os resultados dos métodos da Bisseção e da Posição Falsa para a função f(x) = x^3 -9x+3, a=0, b=1 e epsilon = 0.001. Defina uma função para responder esta questão e crie um comentário ao final da função dizendo quantas iterações cada método utilizou e a raiz encontrada. Veja o exemplo nas linhas 43-45 do arquivo teste01.py

Para testar as funções, execute o comando abaixo no terminal:
```
$ python3 teste01.py
```
E você deve ver a saída abaixo:

```
========================================================================
Questão 1: f(x)= x^3-9x+3, a=0, b=1 e epsilon=0.001.
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
Método da Posição Falsa
k	  a		  fa		  b		  fb		  x		  fx		intervX
1	0.000000e+00	3.000000e+00	1.000000e+00	-5.000000e+00	3.750000e-01	-3.222656e-01	1.000000e+00
2	0.000000e+00	3.000000e+00	3.750000e-01	-3.222656e-01	3.386243e-01	-8.790199e-03	3.750000e-01
3	0.000000e+00	3.000000e+00	3.386243e-01	-8.790199e-03	3.376350e-01	-2.258842e-04	3.386243e-01
Raiz encontrada: 0.33763504551140067
=========================================================================
```

### Q2
Utilize o Octave para achar os intervalos para as raízes da equação 2^x-3x=0. Quantas raízes existem para essa equação? Encontre, para cada uma das raízes, um subintervalo que contenha apenas uma raiz e depois utilize os dois métodos estudados cada uma delas e compare os resultados. Você deve implementar uma função para cada raiz. Use nomes como q2_1, q2_2, etc. Use epsilon = 0.00001. Crie um comentário ao final de cada função dizendo quantas iterações cada método utilizou e a raiz encontrada.

### Q3
Utilize o Octave para localizar os subintervalos para as raízes da equação 4cos(x) - e^(2x)=0 no domínio de [-5.5, 3]. Quantas raízes existem nesse intervalo? Encontre, para cada uma das raízes, um subintervalo que contenha apenas uma raiz e depois utilize o método da posição falsa achar cada uma delas com epsilon = 0.00001. Você deve implementar uma função para cada raiz. Use nomes como q3_1, q3_2, etc. Crie um comentário ao final de cada função dizendo quantas iterações cada método utilizou e a raiz encontrada.

```
Dicas: No Octave, a função cosseno é cos() e a e^2 = exp(2).
       No Python você precisa importá-las da biblioteca math:

	   from math import exp, cos
	   #depois pode usá-las normalmente cos(x), exp(x)
```
### No final da aula
Faça um commit e depois um push do seu arquivo:
```
git add teste01.py
git commit -m "Questão 2 implementada."
git push origin master
```

## 11/11/2015 - Método de Newton-Raphson
### Objetivo
O objetivo da aula é implementar o método de Newton-Raphson em Python (ou em outra linguagem de sua preferência) e aplicá-lo para achar as raízes de equações não lineares.

### Parte 1: Configurações
#### Sincronize o fork
Visite o seu fork de lab_metodos e sincronize-o, se necessário.

#### Verifique as configurações da máquina local
Tenha certeza de que a máquina local esteja confugurada com o seu usuário. Num terminal, digite os seguintes comandos:
```
$ git config --get user.name
$ git config --get user.email

```
Você deve ver o seu nome e o seu e-mail. Caso contrário, configure novamente a máquina:

```
$ git config --global user.name "Seu nome"
$ git config --global user.email seu_email@email.com

```

Verifique também se o gedit está configurado como editor padrão:

```
$ git config --get core.editor
gedit -w -s

```
Se for mostrado algo diferente, execute o seguinte comando:

```
$ git config --global core.editor "gedit -w -s"

```

#### Clone ou atualize o seu repositório na máquina local

```
$ git clone url_do_repositório

```

Ou se você já tiver uma cópia do seu repositório, apenas atualize-o:

```
$ cd lab_metodos
$ git pull

```
### Parte 2: Implementação do método de Newton-Raphson

#### 1. Crie um arquivo chamado newton.py na pasta raiz:
```

$ gedit raiz/newton.py &

```
#### 2. Implemente o método de Newton-Raphson de acordo com o algoritmo visto em sala
```
def newton(f, flin, x0, epsilon, iterMax=50):
    # ...
```
#### 3. Teste o método de Newton-Raphson com o mesmo exemplo do método da Bisseção
Ao final do arquivo, dentro do bloco criado com a linha abaixo, faça:

```
if __name__ == "__main__":

```
1. Defina a função f(x) = x^3-9x+3
2. Defina a função flin(x) = 3x^2-9
3. Defina x0 = 0.5 e epsilon = 0.0001
4. Chame a função do método de newton, como abaixo:

```
print("Método de Newton-Raphson")
(houveErro, raiz) = newton(f,flin,x0,epsilon)
if houveErro:
    print("O Método de Newton-Raphson retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s"%raiz)
```

Execute o seu código através do comando abaixo:
```
$ python3 newton.py

```

Confira a saída do seu programa com a saída abaixo:
```
Método de Newton-Raphson
k	  x		  f(x)
1	3.333333e-01	3.703704e-02
2	3.376068e-01	1.834089e-05
Raiz encontrada: 0.33760683760683763
```
### Parte 3: Resolva as seguintes questões
1. Use a sua implementação do Método de Newton para encontrar a raiz da equação 4cos(x) - e^(2x)=0, com x0 = -2.5 e epsilon = 0.00001. O método convergiu? Qual a raiz encontrada e quantas iterações foram executadas?

```
Dicas: Não se esqueça de importar as funções  da biblioteca math:
	   from math import exp, cos, sin
	   #depois pode usá-las normalmente cos(x), exp(x), sin(x)
```
2. E o que acontece quando você executa o método com x0 = -0.5? Explique da maneira mais detalhada possível em um comentário no seu arquivo.

## 18/11/2015 - Método da Secante e método de Newton para polinômios
### Objetivos
Os objetivos da aula são três:
1. Implementar o método da secante e testá-lo
2. Implementar o método de Newton para polinômios e testá-lo
3. Comparar o tempo de execução dos métodos de Newton para polinômios e Newton geral

### Configurações
#### Sincronize o fork
Visite o seu fork de lab_metodos e sincronize-o, se necessário.

#### Verifique as configurações da máquina local
Tenha certeza de que a máquina local esteja confugurada com o seu usuário. Num terminal, digite os seguintes comandos:
```
$ git config --get user.name
$ git config --get user.email

```
Você deve ver o seu nome e o seu e-mail. Caso contrário, configure novamente a máquina:

```
$ git config --global user.name "Seu nome"
$ git config --global user.email seu_email@email.com

```

Verifique também se o gedit está configurado como editor padrão:

```
$ git config --get core.editor
gedit -w -s

```
Se for mostrado algo diferente, execute o seguinte comando:

```
$ git config --global core.editor "gedit -w -s"

```

#### Clone ou atualize o seu repositório na máquina local

```
$ git clone url_do_repositório

```

Ou se você já tiver uma cópia do seu repositório, apenas atualize-o:

```
$ cd lab_metodos
$ git pull

```
### Parte 1: Implementação do método da Secante

#### 1. Copie o arquivo newton.py na pasta raiz e salve-o com o nome secante.py:
```
$ cd raiz
$ cp newton.py secante.py
$ gedit secante.py &

```
#### 2. Implemente o método da Secante, modificando o método de Newton
A primeira modificação é alterar o nome da função e os parâmetros de entrada:
```
def secante(f, x0, x1, epsilon, iterMax=50):

```
Depois acrescente o teste para saber se x1 é raiz, e dentro das iterações, modifique o cálculo de x1 (agora é x2 e use a fórmula da secante) e atualize os valores de x0 e x1 ao final do loop

#### 3. Teste o método da Secante com o exemplo visto em sala
Ao final do arquivo, dentro do bloco definido com a linha abaixo, faça:

```
if __name__ == "__main__":

```
2. Remova a função flin(x) pois ela não é mais necessária
3. Defina x0 = 0, x1 = 1 e epsilon = 0.0005.
4. Altere a chamada da função como abaixo:

```
print("Método da Secante")
(houveErro, raiz) = secante(f,x0,x1,epsilon)
if houveErro:
    print("O Método da Secante retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s"%raiz)
```

Execute o seu código através do comando abaixo:
```
$ python3 secante.py

```

Confira a saída do seu programa com a saída abaixo:
```
Método da Secante
k	  x		  f(x)
-	0.000000e+00	3.000000e+00
-	1.000000e+00	-5.000000e+00
1	3.750000e-01	-3.222656e-01
2	3.319415e-01	4.910114e-02
3	3.376346e-01	-2.222064e-04
Raiz encontrada: 0.33763462072303707
```
Se deu tudo certo, faça o commit do seu arquivo e depois faça o push para o seu repositório:
```
git add secante.py
git commit -m "Método da secante"
git push origin master
```
### Parte 2: Implementação do método de Newton para polinômios
#### 1. Copie o arquivo secante.py na pasta raiz e salve-o com o nome newton_poli.py:
```
$ cp secante.py newton_poly.py
$ gedit newton_poli.py &

```

#### 2. Implemente o método de Newton para polinômios, modificando o método de Newton
A primeira modificação é alterar o nome da função e os parâmetros de entrada:
```
def newton_poli(n, a, x, epsilon, iterMax=50):

```
Modifique o corpo da função com o algoritmo visto em sala.

#### 3. Teste o método de Newton para polinômios com o exemplo visto em sala
Ao final do arquivo, dentro do bloco definido com a linha abaixo, faça:

```
if __name__ == "__main__":

```
2. Remova todas as definições de funções, pois elas não são mais necessárias
3. Defina os parâmetros de entrada como mostrado abaixo:
4. Altere a chamada da função como abaixo:

```

n = 3
a = [-2,-1,2,1]
x = 2
epsilon = 0.001
print("Método de Newton-Raphson para Polinômios")
(houveErro, raiz) = newton_poli(n,a,x,epsilon)
if houveErro:
    print("O Método de Newton-Raphson para polinômios retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s"%raiz)
```

Execute o seu código através do comando abaixo:
```
$ python3 newton_poli.py

```

Confira a saída do seu programa com a saída abaixo:
```
Método de Newton-Raphson para Polinômios
k	  x		  p(x)
0	2.000000000	1.200000e+01
1	1.368421053	2.939204e+00
2	1.077163125	4.932089e-01
3	1.004520163	2.722323e-02
4	1.000016930	1.015792e-04
Raiz encontrada: 1.0000169296346983

```
Se deu tudo certo, faça o commit do seu arquivo e depois faça o push para o seu repositório:
```
git add newton_poli.py
git commit -m "Método de Newton para polinômios"
git push origin master
```
### Parte 3: Comparação de tempo de execução

Dentro da pasta testes existe um arquivo chamado teste_tempo.py. Nesse arquivo é medido o tempo de execução de trechos de código em python, usando o clock da máquina:
```
import time

...

tni = time.perf_counter()
(houveErro1, raiz1) = newton(p,plin,x,epsilon, maxIter)
tnf = time.perf_counter()
print("Tempo de execução do Método de Newton-Raphson: %s ms"%((tnf-tni)*1000))

```
O resultado é em fração de segundos. Nós multiplicamos a diferença por 1000 para obtermos o resultado em milissegundos.

#### 1. Execute o arquivo teste_tempo.py:
```
$ cd ../testes
$ python3 teste_tempo.py

```
Se tudo deu certo até agora, você deve ver algo parecido com a saída abaixo:

```
p(x) = 3*x^5-2*x^4+5*x^3+7*x^2-3*x+1
k	  x		  f(x)		 f'(x)
1	-1.970626e+00	-1.234832e+02	3.150910e+02
2	-1.578729e+00	-3.833619e+01	1.369417e+02
3	-1.298784e+00	-1.102759e+01	6.432769e+01
4	-1.127355e+00	-2.578819e+00	3.597222e+01
5	-1.055666e+00	-3.315022e-01	2.697820e+01
6	-1.043378e+00	-8.595656e-03	2.558616e+01
7	-1.043042e+00	-6.294848e-06	2.554869e+01
8	-1.043042e+00	-3.383960e-12	2.554866e+01
9	-1.043042e+00	3.996803e-15	2.554866e+01
Tempo de execução do Método de Newton-Raphson: 0.4844830255024135 ms
Raiz encontrada: -1.043041987980764



k	  x		  p(x)
0	-0.750000000	3.733398e+00
1	-1.970625798	-1.234832e+02
2	-1.578728896	-3.833619e+01
3	-1.298783552	-1.102759e+01
4	-1.127355155	-2.578819e+00
5	-1.055665965	-3.315022e-01
6	-1.043378184	-8.595656e-03
7	-1.043042234	-6.294848e-06
8	-1.043041988	-3.381961e-12
9	-1.043041988	-2.442491e-15
Tempo de execução do Método de Newton-Raphson para Polinômios: 0.27852700441144407 ms
```

Note que os tempos de execução podem variar, mas em geral o tempo do método de Newton para polinômios deve ser menor.

#### 1. Comparar os tempos de execução de outro polinômio

Copie o arquivo teste_tempo.py para teste_tempo2.py:
```
$ cp teste_tempo.py teste_tempo2.py
$ gedit teste_tempo2.py &

```

Modifique o arquivo para achar as raízes de p(x) = -3*x^6 + 2*x^5-5*x^4+6*x^3+7*x^2-4*x+3, com aproximação inicial x = 1.1 e epsilon = 1.000000e-13

#### 2. Execute o arquivo teste_tempo2.py:
```
$ python3 teste_tempo2.py

```

Escreva num comentário no final do arquivo a raiz encontrada por cada método e o número de iterações. Salve o arquivo.

Se deu tudo certo, faça o commit do seu arquivo e depois faça o push para o seu repositório:
```
git add teste_tempo2.py
git commit -m "Comparação do tempo de execução"
git push origin master
```

