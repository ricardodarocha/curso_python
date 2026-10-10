import pandas as pd 
import matplotlib.pyplot as plt

def main():
    # print("Hello from aula-py!")
    # nome_f(["Aluno 1", "Aluno 2"])
    analise()

def analise():
    dados = pd.read_csv("dados/alunos.csv")
    # print(dados)
    idades = dados["idade"].sort_values()

    # estatísticas básicas
    media = idades.mean()
    mediana = idades.median()
    moda = idades.mode().tolist()

    #amplitude
    max = idades.max()
    min = idades.min()
    amplitude = max - min
    print(f"Amplitude da amostra ", amplitude)

    print(f"média={media}, mediana={mediana}, moda={moda}")

    #estatística descritiva
    print(idades.describe())

    # print(idades)

    # Desenho do histograma
    # raiz quadrada do tamanho da amostra
    # raiz²(40) = 6 .. 7
    dados["idade"].hist(bins=20)

    plt.title("Idades")
    plt.xlabel("Idade")
    plt.ylabel("Freq")
    plt.show()


if __name__ == "__main__":
    main()

def nome_f(nomes):
    for nome in nomes:
        print("Ola ", nome)
     

