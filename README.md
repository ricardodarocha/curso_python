# curso de python 

## Introdução ao Python para análise de dados

Instale o uv por exemplo com pip

```py
pip install uv
```

Inicie um novo repositório com uv e  adicione as bibliotecas

```py
uv init
uv add pandas numpy matplotlib

import pandas as pd
dados = pd.read_csv("dados.csv")
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

dados["idade"].hist(bins=5)

dados: DataFrame com os dados lidos do CSV.

["idade"]: seleciona a coluna idade.

.hist(): cria um histograma.

bins=5: divide os valores em 5 intervalos (bins).

Para personalizar o histograma:

dados["idade"].hist(bins=5)
plt.show()

Importante: a coluna idade deve conter valores numéricos. Cada barra representa a frequência de valores em um intervalo de idades.

dados["idade"].hist(bins=5, cumulative=True)
plt.show()

O eixo Y mostrará a frequência acumulada: a quantidade de observações menores ou iguais ao limite superior de cada intervalo.

Para mostrar a proporção acumulada entre 0 e 1:

dados["idade"].hist(bins=5, cumulative=True, density=True)
plt.show()

## Instalação de python no ubuntu

```py
sudo apt update
sudo apt upgrade -y

sudo apt install -y python3 python3-pip python3-venv
```
