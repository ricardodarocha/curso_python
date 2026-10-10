# curso de python 

## Introdução ao Python para análise de dados

Instale o uv por exemplo com pip
Se ocorrer erro, por exemplo `externally-managed-environment` use um  ambiente virtual:

```py
python3 -m venv .venv
source .venv/bin/activate
pip install uv
```

Outra forma de instalar o uv é usar o comando do powershell ou pwsh em algumas versões

```SHELL
powershell -Command "irm https://astral.sh/uv/install.ps1 | iex"
pwsh -Command "irm https://astral.sh/uv/install.ps1 | iex"
```

Inicie um novo repositório com uv e  adicione as bibliotecas

```py
md projeto
cd projeto/

uv init
uv add pandas numpy matplotlib
```

crie um novo arquivo main.py e adicione o código 
crie um arquivo dados.csv com os dados abaixo

```csv
nome,idade
jose,31
maria,32
```

Veja o arquivo de exemplo na pasta dados/

```py
import pandas as pd
dados = pd.read_csv("dados/dados.csv")
print(dados)


```


<img width="321" height="77" alt="image" src="https://github.com/user-attachments/assets/47ffd900-5f38-4973-976c-c4755256432c" />

abre o terminal e execute 

```shell
uv run main.py
```

1. Criar um histograma com pandas

Para construir um histograma, precisamos selecionar uma coluna numérica. Neste exemplo, vamos analisar a distribuição das idades.

Substitua o conteúdo de main.py por:

```py
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

dados["idade"].hist(bins=5)

plt.title("Distribuição das idades")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.show()
```

<img width="1687" height="1101" alt="image" src="https://github.com/user-attachments/assets/294e5f81-99bd-4123-863b-6da4d0402d7d" />

#### Gráfico de barras
Mostra a quantidade de alunos por idade.

```py
dados["idade"].value_counts().sort_index().plot(kind="bar")
plt.xlabel("Idade")
plt.ylabel("Alunos")
plt.show()
```
<img width="426" height="351" alt="image" src="https://github.com/user-attachments/assets/c8aa98ab-e490-4260-9a0f-ee805985dcc1" />

#### Boxplot

Apresenta mediana, quartis e possíveis valores atípicos.

```py
dados.boxplot(column="idade")
plt.ylabel("Idade")
plt.show()
```
<img width="960" height="672" alt="image" src="https://github.com/user-attachments/assets/bb7df070-7465-4954-8e59-4bdee0e5e0b6" />

## Outras dicas

#### Estatística elementar
```py
# Média
print("Média:", dados["idade"].mean())

# Mediana
print("Mediana:", dados["idade"].median())

# Moda
print("Moda:", dados["idade"].mode().tolist())

# Maior valor
print("Máximo:", dados["idade"].max())

# Menor valor
print("Mínimo:", dados["idade"].min())

# Amplitude
print("Amplitude:", dados["idade"].max() - dados["idade"].min())

# Quantidade de alunos
print("Quantidade:", dados["idade"].count())

# Soma das idades
print("Soma:", dados["idade"].sum())
```

#### Estatística descritiva
```py
# Estatísticas descritivas
print(dados["idade"].describe())

# Quantidade de alunos por idade
print(dados["idade"].value_counts().sort_index())

# Alunos com idade maior ou igual a 25 anos
print(dados[dados["idade"] >= 25])

# Ordenar alunos por idade
print(dados.sort_values("idade"))

# Aluno mais velho
print(dados.loc[dados["idade"].idxmax()])

# Aluno mais novo
print(dados.loc[dados["idade"].idxmin()])
```

##  Resumo das funções

Operação|Função pandas
-|-
Média	|`.mean()`
Mediana|`.median()`
Moda	|`.mode()`
Máximo	|`.max()`
Mínimo	|`.min()`
Amplitude	|`.max() - .min()`
Contagem	|`.count()`
Soma	|`.sum()`
Desvio padrão	|`.std()`
Variância	|`.var()`
Quartis	|`.quantile()`
Estatísticas gerais	|`.describe()`

Observação: count() conta valores não nulos, enquanto len(dados) conta o número de linhas do DataFrame.

## Instalar e executar o jupyter notebooks

Melhora a experiência de desenvolvimento permitindo interagir com o código python

```SHELL
uv add jupyter
uv run jupyter notebook --port 8081

REM quando o arquivo já existir, 
uv run jupyter notebook <programa1.ipynb> --port 8081
```

```py
dados["idade"].hist(bins=5)
plt.show()

idades.

dados["idade"].hist(bins=5, cumulative=True)
plt.show()

# O eixo Y mostrará a frequência acumulada: a quantidade de observações menores ou iguais ao limite superior de cada intervalo.
# Para mostrar a proporção acumulada entre 0 e 1:

dados["idade"].hist(bins=5, cumulative=True, density=True)
plt.show()
```

## Instalação de python no ubuntu

```py
sudo apt update
sudo apt upgrade -y

sudo apt install -y python3 python3-pip python3-venv
```
